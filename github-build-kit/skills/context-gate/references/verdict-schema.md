# Context Gate schema v1

The frozen contract and auditor verdict are strict JSON objects. Unknown keys,
duplicate IDs, missing evidence, unsafe paths, or hash mismatches are invalid.

## Frozen gate contract

```json
{
  "schema_version": 1,
  "gate_id": "phase-1",
  "next_phase": "phase-2",
  "max_context_bytes": 32768,
  "mechanical_checks": [{"id": "tests", "description": "All declared tests pass"}],
  "criteria": [{"id": "contract", "description": "Output satisfies the sealed contract"}]
}
```

IDs must be nonempty and unique within their list. `max_context_bytes` must be
a positive integer.

## Auditor verdict

```json
{
  "schema_version": 1,
  "gate_id": "phase-1",
  "verdict": "PASS",
  "contract": {"path": "gate/contract.json", "sha256": "<64 lowercase hex>"},
  "builder": {"run_id": "builder-run", "model": "builder-model", "tier": "T2"},
  "auditor": {
    "run_id": "auditor-run",
    "model": "different-auditor-model",
    "tier": "T2",
    "authored_artifacts": false
  },
  "mechanical_checks": [
    {"id": "tests", "status": "PASS", "evidence": [{"path": "gate/tests.txt", "sha256": "<64 lowercase hex>"}]}
  ],
  "criteria": [
    {"id": "contract", "status": "PASS", "evidence": [{"path": "gate/audit.txt", "sha256": "<64 lowercase hex>"}], "finding": ""}
  ],
  "approved_context": {"path": "gate/context.json", "sha256": "<64 lowercase hex>", "next_phase": "phase-2"}
}
```

All referenced paths are relative to the project root, remain inside it after
symlink resolution, name regular files, and match their hashes. Tiers are
`T0` through `T3`; the auditor tier cannot be below the builder tier.

A `PASS` requires every check and criterion to pass and a valid approved
context within its byte budget. A `FAIL` requires at least one failed item and
`approved_context: null`. Passing criteria have an empty `finding`; failing
criteria have a nonempty, actionable finding. Mechanical items do not contain
`finding`.

## Validator authority

`validate_gate.py` exits `0` for valid PASS, `1` for valid FAIL, and `2` for
invalid or unsafe input. It writes a deterministic seal only for valid PASS.
Consumers must admit context using the seal, not the auditor verdict alone.
