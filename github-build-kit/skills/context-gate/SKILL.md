---
name: context-gate
description: Verify and seal context packages at explicit phase boundaries in agentic project workflows. Use when a builder has produced phase artifacts and a candidate handoff that must receive a binary PASS or FAIL from a separate auditor model before the next phase may begin. Enforces frozen criteria, evidence hashes, auditor independence, capability parity, context budgets, and fail-closed admission.
---

# Context Gate

Run this skill only as an explicit phase-boundary graph node. Never use it for
conversation compaction, during a node, or as an unsolicited interruption.

## Inputs

Accept only:

- a frozen gate-contract JSON file;
- the builder's candidate context package and artifact manifest;
- raw mechanical evidence produced by the declared checks;
- builder run ID, canonical model identity, and capability tier.

Never give the auditor the builder's transcript, reasoning, or message log.

## Gate sequence

1. Run every mechanical check declared by the frozen contract. Persist its raw
   output as immutable evidence and hash it. Do not let a model rewrite it.
2. Dispatch a fresh, isolated auditor model even when a mechanical check fails.
   A mechanical failure irrevocably locks the gate verdict to `FAIL`.
3. Require the auditor to use a different canonical model identity and run ID,
   capability tier greater than or equal to the builder, `authored_artifacts`
   set to `false`, and read-only tools.
4. Give the auditor only the frozen contract, hashed artifacts, raw mechanical
   evidence, and candidate context package. Require one verdict entry for every
   contract check and criterion. The auditor may inspect and judge but never
   repair artifacts.
5. Require the auditor to emit only the JSON defined in
   [references/verdict-schema.md](references/verdict-schema.md).
6. Run the deterministic validator. It is the final authority on admissibility:

   ```bash
   python3 scripts/validate_gate.py \
     --root /absolute/project/root \
     --verdict relative/path/verdict.json \
     --seal-out relative/path/gate-seal.json
   ```

7. Route solely from the validator exit code:
   - `0`: validated `PASS`; release only the sealed approved context package.
   - `1`: validated `FAIL`; release no context to the next phase and return the
     compact failed-criterion packet to the builder.
   - `2`: invalid or unsafe verdict; treat as `FAIL`, release nothing, and fix
     the gate machinery rather than the product artifact.

Never allow model prose, an orchestrator preference, retry pressure, missing
evidence, or ambiguity to override a mechanical failure or validator result.

## Auditor output rules

- Use exactly `PASS` or `FAIL`; never emit a provisional third state.
- Cite existing hashed evidence for every check and criterion.
- Use an empty finding for each passing semantic criterion and a concrete,
  actionable finding for each failing one.
- Set `approved_context` only when every mechanical check and criterion passes.
- On any uncertainty or missing evidence, mark the affected criterion `FAIL`.

Only the seal authorizes the next phase to believe the approved context. A raw
auditor `PASS` without a valid seal has no authority.
