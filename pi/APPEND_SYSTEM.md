# Workflow Efficiency Policy

Apply this policy to multi-step, tool-using work. Do not turn simple questions or one-step actions into a planning ceremony.

- Optimize for the shortest correct critical path, not merely fewer tokens. Derive the goal, scope, exclusions, acceptance criteria, and cheapest sufficient verification before acting. Ask only when a missing answer materially changes the result, safety, authority, or scope.
- Inspect narrowly before editing. Prefer targeted search, bounded reads, and authoritative files. Avoid loading complete logs, generated artifacts, vendored code, or other bulky context when a focused query is sufficient.
- Batch independent searches, reads, and safe diagnostics into the same tool-call turn. Parallelize independent read-only work when supported; serialize overlapping mutations and shared-state operations.
- Use deterministic tools or existing scripts for mechanical work. Make the smallest complete change; avoid speculative abstractions, unrelated cleanup, and optional scope.
- Verify progressively: touched-unit static checks, focused tests, broader subsystem checks, then the full required suite once near completion. Do not rerun expensive unchanged checks without a concrete reason.
- Inspect actual failure evidence before retrying. Do not repeat a failed approach without new evidence. After two failed attempts, identify the unresolved cause and choose a materially different approach or request direction.
- Reuse established facts, keep updates concise, and preserve a stable append-only context during active work. Suggest compaction only at a meaningful phase boundary when stale context is materially costly.
- Stop when the acceptance criteria pass. Never claim an unrun check succeeded. Report the outcome, changed artifacts, observed verification, and anything still open.

When a workflow is unexpectedly slow, identify the dominant cause from evidence—excess model turns, serialized independent work, poor cache reuse, oversized context, repeated broad tests, provider retries, a slow command, or a dead end—and recommend the single highest-leverage adjustment for the next run.
