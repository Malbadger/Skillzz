# Useful patterns from the local archive

These are condensed from archive index entries and the Build-to-Acceptance research note. They are guidance, not copies of private runbooks. Status reflects the archive at packaging time.

## Build-to-Acceptance kit — research, current

The reusable asset is the `build-kit/` folder. Its failure-mode catalog covers 20 ways an agent can report a result it did not establish. The strongest portable checks are: capture before and after evidence with a state readback; hash evidence when captured; require a failing test before a defect fix; run two clean full passes without source changes; label claims by provenance; and keep the builder's verdict separate from independent authorization. The complete kit is heavy for a small script and has not been run end to end on this machine.

## Context gate — build, current

Use mechanical checks before independent review. Keep the reviewer separate from the author, preserve hashed evidence, and fail closed when required proof is absent. The archived implementation reported 16 adversarial tests passing. This package includes the skill instructions and validator script, but does not claim the full companion implementation is bundled.

## Context engineering methodology — research, current

Provide each agent role a bounded context package with a fixed priority order. A useful workflow separates review, design, build, and audit. The source's statistics were observational for one operator; reuse the framework, not a general performance claim.

## Agent graph versus loop — research, current

Put deterministic transitions, budgets, and checkpoints in code. Use a model for decisions that genuinely require judgment. Give delegated work a narrow contract and explicit return criteria.

## Local agent harness — build, current

A Claude Code style loop against local Ollama used interactive context eviction. The archive reported the core complete and 80 tests passing; GUI and packaging remained. This is a design reference, not a packaged component here.

## Ollama context and VRAM tuning — runbook, current

Local context capacity depends on GPU memory and the loaded model, not only the model's advertised context. Measure GPU residency and concurrency on the target host before setting a production context size. The archive's numeric results are machine-specific and are intentionally omitted.

## Capability placement — research, current

Use the strongest available reasoning tier for orchestration and independent audit. Non-authorship is the key separation property for audit; a weaker reviewer can miss problems. This is a design principle, not a benchmark guarantee.
