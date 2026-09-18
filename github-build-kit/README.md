# Build kit and reusable skills

This folder packages a reusable Build-to-Acceptance kit, five locally customized agent skills, and a short guide to useful archived patterns.

## Contents

- `build-kit/`: the master prompt, failure-mode analysis, and six specification templates. This is an imported, project-agnostic copy. It was marked `current` in the local archive but has **not** been verified end to end on this machine. The source package did not include a license; check redistribution rights before placing it in a public repository.
- `skills/build-kit-intake/`: prepares a project-specific kit from owner answers and repository facts.
- `skills/archive-search/`: searches an indexed local archive before opening full notes.
- `skills/context-curator/`: selects and compresses context for an agent task.
- `skills/context-gate/`: validates evidence and independent audit decisions.
- `skills/ollama-frontier-delegator/`: delegates bounded work to a local Ollama model.
- `archive-guide/USEFUL-PATTERNS.md`: distilled archive findings, with status and limits.

Paths in skill files were generalized for portability. Some skills require their companion code or local services; see each `SKILL.md` before using it.

No credentials, private keys, local transcripts, or archive vault contents are intended to be included. Run a fresh secret scan before publishing after any edits.
