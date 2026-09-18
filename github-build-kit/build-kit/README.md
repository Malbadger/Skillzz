# Build-to-Acceptance kit (agnostic copy)

A paste-ready prompt that drives a coding agent from a controlled specification
set to a working application, with UAT run on the real artifact and evidence a
stranger can re-run. Plus the six document templates the prompt reads, and the
failure-mode catalog that explains why each rule exists.

Imported 2026-08-27 from `build-to-acceptance.zip`. Not authored here; not
verified here. See the note at `research/build-to-acceptance-kit.md`.

## Files

| File | What it is |
|---|---|
| `BUILD-TO-ACCEPTANCE-MASTER-PROMPT.md` | The whole thing: operator instructions, the paste block, three appendices, changelog |
| `BUILD-PROMPT-ANALYSIS.md` | The 20 observed agent failure modes each rule exists to catch, plus the design decisions |
| `kit-templates/00-PROJECT-INDEX.md` | Configuration control: active versions, change register, execution gate |
| `kit-templates/01-PROJECT-TRUTH.md` | What the project IS: needs (`BN-###`), scope, roles, owner-reserved decisions |
| `kit-templates/02-FUNCTIONAL-CONTRACT.md` | What it must DO: requirements (`REQ-###`), data model, rules, failure behavior |
| `kit-templates/03-INTERACTION-DECISIONS.md` | How it must BEHAVE: ordered experience (`EXP-###`), surfaces, profiles, states |
| `kit-templates/04-BUILD-RECORD.md` | How builds are made: stack, commands, conventions, forbidden content (`BUILD-###`) |
| `kit-templates/05-AUDIT-AND-ACCEPTANCE.md` | How done is judged: UAT rows (`UAT-###`), thresholds, evidence rules |

## Using it

Fill the six templates into a `build-kit/` folder, add a `START-HERE.txt`, run
Appendix A's readiness check, then paste the prompt block into a fresh agent
session connected to that folder:

```bash
sed -n '/^## THE PROMPT/,/^## END OF PROMPT/p' BUILD-TO-ACCEPTANCE-MASTER-PROMPT.md
```

The block is self-contained by design: the evidence contract travels inside it,
so the agent implements a fixed contract instead of inventing release
machinery. The session returns `CANDIDATE READY FOR INDEPENDENT AUDIT` or
`CANDIDATE BLOCKED` and never authorizes its own work.

Two things to size up before committing to it. The prompt is ~5k tokens of
standing instruction, and the evidence it demands (PNG pairs per row per
profile, a readback per row, hashes for all of it) is heavy for a small build.
It is built for a real product with an owner who will audit it, not for a
weekend script.

## Where each downloaded file went

Every file in `build-to-acceptance.zip` is accounted for here. Names differ
from the download; content is otherwise whole except where this table says
otherwise.

| File in the zip | Here | Content |
|---|---|---|
| `BUILD-TO-ACCEPTANCE-MASTER-PROMPT_v1_0.md` | `BUILD-TO-ACCEPTANCE-MASTER-PROMPT.md` | Complete. Operator preamble, paste block, Appendices A/B/C, changelog. Only project-identifying names changed |
| `BUILD-TO-ACCEPTANCE-PROMPT_v1_0.md` | *not kept* | Byte-duplicate of the paste block already inside the master, between the `## THE PROMPT` and `## END OF PROMPT` markers. Dropped so there is only one copy to maintain; the `sed` line above extracts it |
| `BUILD-PROMPT-ANALYSIS_2026-08-27.md` | `BUILD-PROMPT-ANALYSIS.md` | Rewritten, ~40% shorter. Kept: the 20 failure modes, what worked, the design decisions, the open items, the boundary. Dropped: §2 (inventory of the author's own named systems) and §3 (their prompt's six-generation lineage) — both pure org history. Each failure mode's evidence citation was replaced with the shape of the evidence |
| `kit-templates/00` through `05` | `kit-templates/00` through `05` | Complete, names unchanged |
| `.DS_Store`, `__MACOSX/` | *not kept* | macOS filesystem cruft |

## What was changed from the download

Project-specific content was removed so the prompt is reusable. **No rule,
threshold, phase, ID family, or detection was altered.**

| Original | Here |
|---|---|
| `ALIP-AE-Desk-Kit/` at a hardcoded `~/ALIP/...` path | `build-kit/` at whatever local path `START-HERE.txt` names |
| `handouts/` (course handouts) | `shape-refs/` (documents that define shape only) |
| Named operator, named vendor agents | "the operator", "the Builder seat", "any coding agent" |
| "Rule 6" (an in-house standard number) | the **separation rule**, defined where it is first used |
| Classroom/capstone framing on the six files | dropped; "Capstone comparison" is now "Result comparison" |
| `RICE Role / Instruction / Context / Example` gate fields | spelled out as plain field names |
| The analysis memo's org inventory, prompt lineage, and internal file citations | dropped; the failure-mode catalog was kept with the evidence generalized to its shape |

`work/CLAUDE.md` and `AGENTS.md` are still named in the precedence rule. Those
are agent-tooling conventions, not project facts, and they are correct as-is.
