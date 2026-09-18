#!/usr/bin/env python3
"""Fail-closed validator and seal writer for Context Gate schema v1."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
from pathlib import Path
from typing import Any

TIERS = {"T0": 0, "T1": 1, "T2": 2, "T3": 3}
SHA256_RE = re.compile(r"[0-9a-f]{64}")


class Invalid(ValueError):
    pass


def exact_keys(value: Any, keys: set[str], label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise Invalid(f"{label} must be an object")
    missing, extra = keys - value.keys(), value.keys() - keys
    if missing or extra:
        raise Invalid(f"{label} keys invalid; missing={sorted(missing)}, extra={sorted(extra)}")
    return value


def nonempty(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise Invalid(f"{label} must be a nonempty string")
    return value


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_ref(root: Path, value: Any, label: str) -> tuple[dict[str, str], Path]:
    ref = exact_keys(value, {"path", "sha256"}, label)
    raw_path = nonempty(ref["path"], f"{label}.path")
    digest = ref["sha256"]
    if not isinstance(digest, str) or SHA256_RE.fullmatch(digest) is None:
        raise Invalid(f"{label}.sha256 must be 64 lowercase hex characters")
    candidate = Path(raw_path)
    if candidate.is_absolute():
        raise Invalid(f"{label}.path must be relative")
    resolved = (root / candidate).resolve(strict=False)
    if resolved == root or root not in resolved.parents:
        raise Invalid(f"{label}.path escapes root")
    if not resolved.is_file():
        raise Invalid(f"{label}.path is not a regular file")
    try:
        actual = sha256_bytes(resolved.read_bytes())
    except OSError as exc:
        raise Invalid(f"{label}.path cannot be read: {exc}") from exc
    if actual != digest:
        raise Invalid(f"{label}.sha256 does not match file")
    return {"path": raw_path, "sha256": digest}, resolved


def identity(value: Any, label: str, auditor: bool = False) -> dict[str, Any]:
    keys = {"run_id", "model", "tier"} | ({"authored_artifacts"} if auditor else set())
    item = exact_keys(value, keys, label)
    nonempty(item["run_id"], f"{label}.run_id")
    nonempty(item["model"], f"{label}.model")
    if item["tier"] not in TIERS:
        raise Invalid(f"{label}.tier must be T0, T1, T2, or T3")
    if auditor and item["authored_artifacts"] is not False:
        raise Invalid("auditor.authored_artifacts must be false")
    return item


def load_json(path: Path, label: str) -> tuple[Any, bytes]:
    try:
        raw = path.read_bytes()
        return json.loads(raw.decode("utf-8")), raw
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise Invalid(f"{label} is not readable UTF-8 JSON: {exc}") from exc


def contract_schema(value: Any) -> dict[str, Any]:
    contract = exact_keys(value, {
        "schema_version", "gate_id", "next_phase", "max_context_bytes",
        "mechanical_checks", "criteria",
    }, "contract")
    if contract["schema_version"] != 1:
        raise Invalid("contract.schema_version must be 1")
    nonempty(contract["gate_id"], "contract.gate_id")
    nonempty(contract["next_phase"], "contract.next_phase")
    if type(contract["max_context_bytes"]) is not int or contract["max_context_bytes"] <= 0:
        raise Invalid("contract.max_context_bytes must be a positive integer")
    for field in ("mechanical_checks", "criteria"):
        values = contract[field]
        if not isinstance(values, list):
            raise Invalid(f"contract.{field} must be an array")
        ids: list[str] = []
        for index, value in enumerate(values):
            row = exact_keys(value, {"id", "description"}, f"contract.{field}[{index}]")
            ids.append(nonempty(row["id"], f"contract.{field}[{index}].id"))
            nonempty(row["description"], f"contract.{field}[{index}].description")
        if len(ids) != len(set(ids)):
            raise Invalid(f"contract.{field} IDs must be unique")
    return contract


def evidence_list(root: Path, value: Any, label: str) -> None:
    if not isinstance(value, list) or not value:
        raise Invalid(f"{label} must be a nonempty array")
    for index, ref in enumerate(value):
        safe_ref(root, ref, f"{label}[{index}]")


def verdict_items(root: Path, values: Any, expected: list[str], label: str,
                  with_finding: bool) -> list[dict[str, Any]]:
    if not isinstance(values, list):
        raise Invalid(f"{label} must be an array")
    keys = {"id", "status", "evidence"} | ({"finding"} if with_finding else set())
    seen: list[str] = []
    for index, value in enumerate(values):
        item = exact_keys(value, keys, f"{label}[{index}]")
        item_id = nonempty(item["id"], f"{label}[{index}].id")
        seen.append(item_id)
        if item["status"] not in {"PASS", "FAIL"}:
            raise Invalid(f"{label}[{index}].status must be PASS or FAIL")
        evidence_list(root, item["evidence"], f"{label}[{index}].evidence")
        if with_finding:
            if not isinstance(item["finding"], str):
                raise Invalid(f"{label}[{index}].finding must be a string")
            if item["status"] == "PASS" and item["finding"] != "":
                raise Invalid(f"{label}[{index}].finding must be empty on PASS")
            if item["status"] == "FAIL" and not item["finding"].strip():
                raise Invalid(f"{label}[{index}].finding must be nonempty on FAIL")
    if len(seen) != len(set(seen)) or set(seen) != set(expected) or len(seen) != len(expected):
        raise Invalid(f"{label} must cover every contract ID exactly once")
    return values


def seal_target(root: Path, raw: str) -> tuple[Path, str]:
    value = Path(nonempty(raw, "seal path"))
    target = value.resolve(strict=False) if value.is_absolute() else (root / value).resolve(strict=False)
    if target == root or root not in target.parents:
        raise Invalid("seal path escapes root")
    if target.exists() and target.is_dir():
        raise Invalid("seal path is a directory")
    parent = target.parent.resolve(strict=False)
    if parent != root and root not in parent.parents:
        raise Invalid("seal parent escapes root")
    try:
        shown = str(target.relative_to(root))
    except ValueError as exc:
        raise Invalid("seal path escapes root") from exc
    return target, shown


def validate(root: Path, verdict_path: Path, seal_arg: str | None) -> tuple[int, dict[str, Any], dict[str, Any] | None, Path | None]:
    verdict, verdict_raw = load_json(verdict_path, "verdict")
    verdict = exact_keys(verdict, {
        "schema_version", "gate_id", "verdict", "contract", "builder", "auditor",
        "mechanical_checks", "criteria", "approved_context",
    }, "verdict")
    if verdict["schema_version"] != 1:
        raise Invalid("verdict.schema_version must be 1")
    gate_id = nonempty(verdict["gate_id"], "verdict.gate_id")
    if verdict["verdict"] not in {"PASS", "FAIL"}:
        raise Invalid("verdict.verdict must be PASS or FAIL")

    contract_ref, contract_path = safe_ref(root, verdict["contract"], "verdict.contract")
    contract_value, _ = load_json(contract_path, "contract")
    contract = contract_schema(contract_value)
    if gate_id != contract["gate_id"]:
        raise Invalid("verdict.gate_id does not match contract")

    builder = identity(verdict["builder"], "builder")
    auditor = identity(verdict["auditor"], "auditor", auditor=True)
    if builder["run_id"] == auditor["run_id"]:
        raise Invalid("auditor.run_id must differ from builder.run_id")
    if builder["model"] == auditor["model"]:
        raise Invalid("auditor.model must differ from builder.model")
    if TIERS[auditor["tier"]] < TIERS[builder["tier"]]:
        raise Invalid("auditor.tier must be at least builder.tier")

    checks = verdict_items(root, verdict["mechanical_checks"],
                           [x["id"] for x in contract["mechanical_checks"]],
                           "mechanical_checks", False)
    criteria = verdict_items(root, verdict["criteria"],
                             [x["id"] for x in contract["criteria"]],
                             "criteria", True)
    failed = [x["id"] for x in checks + criteria if x["status"] == "FAIL"]

    approved = verdict["approved_context"]
    approved_ref: dict[str, Any] | None = None
    if verdict["verdict"] == "PASS":
        if failed:
            raise Invalid("PASS cannot contain failed checks or criteria")
        item = exact_keys(approved, {"path", "sha256", "next_phase"}, "approved_context")
        if item["next_phase"] != contract["next_phase"]:
            raise Invalid("approved_context.next_phase does not match contract")
        ref, approved_path = safe_ref(root, {"path": item["path"], "sha256": item["sha256"]}, "approved_context")
        if approved_path.stat().st_size > contract["max_context_bytes"]:
            raise Invalid("approved context exceeds contract byte budget")
        approved_ref = {**ref, "next_phase": item["next_phase"]}
    else:
        if not failed:
            raise Invalid("FAIL must contain at least one failed check or criterion")
        if approved is not None:
            raise Invalid("approved_context must be null on FAIL")
        if seal_arg is not None:
            raise Invalid("cannot request a seal for FAIL")

    target = shown = None
    if seal_arg is not None:
        target, shown = seal_target(root, seal_arg)
    seal = None
    if verdict["verdict"] == "PASS":
        seal = {
            "schema_version": 1,
            "gate_id": gate_id,
            "verdict_sha256": sha256_bytes(verdict_raw),
            "contract": contract_ref,
            "approved_context": approved_ref,
            "auditor": auditor,
        }
        return 0, {"gate_id": gate_id, "seal": shown, "status": "VALID", "verdict": "PASS"}, seal, target
    return 1, {"failed_ids": failed, "gate_id": gate_id, "status": "VALID", "verdict": "FAIL"}, None, None


def write_seal(target: Path, seal: dict[str, Any]) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary: str | None = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=target.parent, delete=False) as handle:
            temporary = handle.name
            json.dump(seal, handle, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, target)
        temporary = None
    finally:
        if temporary is not None:
            try:
                os.unlink(temporary)
            except FileNotFoundError:
                pass


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--verdict", required=True)
    parser.add_argument("--seal-out")
    args = parser.parse_args()
    gate_id = ""
    try:
        root = Path(args.root).resolve(strict=True)
        if not root.is_dir():
            raise Invalid("root must be a directory")
        verdict_path = Path(args.verdict)
        if not verdict_path.is_absolute():
            verdict_path = root / verdict_path
        code, output, seal, target = validate(root, verdict_path, args.seal_out)
        gate_id = output.get("gate_id", "")
        if seal is not None and target is not None:
            write_seal(target, seal)
        print(json.dumps(output, separators=(",", ":"), sort_keys=True))
        return code
    except (Invalid, OSError, RuntimeError) as exc:
        print(json.dumps({"errors": [str(exc)], "gate_id": gate_id, "status": "INVALID"},
                         separators=(",", ":"), sort_keys=True))
        return 2


if __name__ == "__main__":
    sys.exit(main())
