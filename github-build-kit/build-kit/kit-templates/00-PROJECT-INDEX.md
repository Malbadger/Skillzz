# Project Index: PRJ-###

- Project:
- Configuration owner:
- Index version/date:
- Status: `DRAFT | BASELINED | SUPERSEDED`
- Final output:
- Medium: software
- Intended recipient/operator:
- Purpose or decision enabled:
- Current authorized baseline:

## Project map

State the whole project in one paragraph: what you are producing, for whom, why it matters, what evidence governs it, and what observable result counts as success. This is the map above the five professional files; it does not replace their detail.

## Software profile (read by the Build-to-Acceptance master prompt)

- Execution mode: `BUILD` (a working application; the demo prompt uses `DEMO`; the Builder refuses a mixed mode)
- Exit condition: two consecutive clean full UAT passes from a clean state, no fix applied between them
- Kit location: the local path `START-HERE.txt` names (a local folder, not a cloud-synced one); the Builder never creates files at the kit root
- Work folder: `work/` (application source `work/app/`, artifact `work/dist/`, prior candidates `work/dist-archive/`, evidence `work/evidence/`, optional `work/exemplars/` and `work/reference/`; override in `04`)
- Resume rule: `work/evidence/RESUME.md` is read first on any restart
- Evidence root: `work/evidence/` in the layout the master prompt's Section 11 fixes
- Context rule: the Builder re-reads all seven kit files in full before every pass and every change, and records their hashes; `shape-refs/` supplies shape only, never project facts
- Stack class (master prompt Section 2a): web | desktop | mobile | terminal | service or library | data model
- Builder session must have: shell, the UI automation and capture tool for that stack class, image viewer, the runtimes `04` names

## Controlled-file register

| Controlled item | Professional owner | Current version/status | Authoritative inputs | Produces/controls | Downstream review required? |
|---|---|---|---|---|---|
| `01-PROJECT-TRUTH.md` | Truth Owner |  | source evidence and human decisions | BN-### truth baseline |  |
| `02-FUNCTIONAL-CONTRACT.md` | Functional Designer |  | baselined Project Truth | REQ-### functional baseline |  |
| `03-INTERACTION-DECISIONS.md` | Interaction Designer |  | baselined Project Truth + Functional Contract | EXP-### interaction baseline |  |
| `04-BUILD-RECORD.md` | Builder |  | approved BN/REQ/EXP baseline | BUILD-### candidate record |  |
| `05-AUDIT-AND-ACCEPTANCE.md` | Auditor |  | exact controlled files + candidate | UAT-### evidence and verdict |  |
| `START-HERE.txt` | Kit maintainer |  | folder logistics | folder rules and the submission rule |  |
| exemplar cases (`05` table, `02` proving cases, or `work/exemplars/cases.json`) | Truth Owner |  | source evidence | expected results per case |  |
| `work/reference/` (optional) | Interaction Designer |  | approved EXP rows | reference images by EXP or screen ID |  |
| final output (the application) | Builder / human output owner |  | exact authorized input set | Result 1 or Result 2 |  |

## Configuration rules

- A **controlled item** is a file or output whose exact version can change the result.
- A **baseline** is the approved set of versions used for a build, test, or decision. Baselined does not mean permanently frozen; it means changes are deliberate and recorded.
- Never overwrite an approved upstream decision silently. Record the proposed delta in the owning file, approve it through the owning role, update this register, and mark every affected downstream file `REVIEW REQUIRED` until it is reconciled and retested.
- Preserve superseded versions when they are needed to explain Result 1, a defect, a rollback, or an authorization decision.
- File names alone are not configuration control. The index must identify the active version and status of every controlled item.

## Decision and change register

The Builder appends rows here in state `proposed` only. Approval belongs to the owning role.

| Change ID | Owning file/section/ID | Before → after | Evidence or human decision | Affected files/trace IDs | Approval | State |
|---|---|---|---|---|---|---|
| CHG-001 |  |  |  |  |  | proposed |

## One-shot execution gate

Complete this before handing the kit to the Builder.

- Execution ID:
- Exact `01`–`05` versions loaded:
- Exemplar set version and case count:
- Source/evidence set loaded:
- Role the Builder is given:
- Instruction (the task in one sentence):
- Context supplied (the exact file set):
- Example of the output shape expected:
- Expected output and format:
- Human-owned decisions and prohibited actions:
- Open items: `NONE` or list owner, impact, and blocked branch:
- Expected UAT cases and acceptance threshold:
- Rollback/recovery point:
- Gate verdict: `READY FOR RESULT 1 | READY FOR RESULT 2 | HOLD`

The gate is `HOLD` when a controlled file is missing, two files claim different active versions, an upstream change has not reached affected downstream files, an open decision lacks an owner, an exemplar case lacks an expected result, or a UAT row has no predeclared expected result. A HOLD kit still goes to the Builder if you choose; the Builder builds everything the HOLD does not block and returns `CANDIDATE BLOCKED`.

## Result baselines

- `RESULT 1 CONFIGURATION:` index version, exact `01`–`05` versions, exemplar set version, build/output version, source commit, date/time
- `RESULT 2 CONFIGURATION:` index version, exact `01`–`05` versions after approved context deltas, exemplar set version, build/output version, source commit, date/time
- Comparison location: `05-AUDIT-AND-ACCEPTANCE.md`

AI must not infer missing project facts or silently select between conflicting versions. Mark the conflict or gap `OPEN`, name its owner and impact, and stop the affected branch until evidence or a human decision closes it. The rest of the build continues.
