# Audit and Acceptance: PRJ-###

## Control and inputs

- Auditor / acceptance lead:
- Project Index version loaded:
- Files 01–04 versions loaded:
- Candidate version tested:
- Test users, environment, and constraints:
- Independent reviewers/sessions:

## Software profile: how rows are judged

- UAT target: the packaged or served artifact from the clean-build command, started from a clean data directory, exemplar set loaded through the product's own entry path. Never a development server or a test harness.
- Evidence per row with a surface: PNG before and after per profile (captured with the stack class's method; none for a service or library, where the profile is `api`), a state readback (store, API, file, or log), and the console and log excerpt. A PNG without a readback is incomplete; a readback without a PNG is incomplete when the row has a surface.
- PNG rules: native rendering only; stable-render wait; full resolution; unique SHA-256 per file; the Builder opens and looks at every PNG and records one sentence per capture; contact sheets per surface group.
- Input round trip: every input the stack class has (fields and controls; dialogs and file pickers; arguments, flags, stdin, and config values; parameters, headers, and body fields; input cells) is exercised with the exemplar value, the invalid values the kit names, and the empty case; the value is read back from the store and compared within the row's tolerance.
- Error, refusal, recovery, offline, and authority rows trigger the real condition, never a toggle.
- Result vocabulary per row: `PASS`, `PASS(local:<adapter>)`, `FAIL`, `BLOCKED(OPEN-### or CHG-###)`, `NOT-RUN(human-only or environment)`.
- RAG for visual rows: **Red** prevents use or hides required information (FAIL); **Amber** functions but forces a workaround or strain (FAIL unless the row's threshold admits it, then PASS with a recorded limit); **Green** usable at every profile with no blocking defect.
- Restart rule: after the last fix, the full battery reruns from a clean build and a clean data directory. Closure requires two consecutive clean full passes with no fix between them.
- A green automated suite never overrides an observed failure.
- The Builder may add `UAT-NEW-###` rows in this schema. The Builder may not edit, weaken, delete, or rename an existing row.

## UAT and verification cases

| ID | User/actor and scenario | Action or condition | Expected observable result | Traces to BN / REQ / EXP / BUILD | Evidence required (profiles, readback source, tolerance) | Pass threshold | Result |
|---|---|---|---|---|---|---|---|
| UAT-001 |  |  |  | BN-001 / REQ-001 / EXP-001 / BUILD-001 |  |  | not run |

## Exemplar cases

One row per case. Cases live here, in `02`'s proving cases, or in `work/exemplars/cases.json`; expected results come from the Truth Owner, and the Builder records actual results verbatim. Nothing under `shape-refs/` is an exemplar case.

| Case ID | Entry path | Traces to REQ | Expected | Actual | Tolerance | Result |
|---|---|---|---|---|---|---|

## Required audit coverage

- Primary user path and intended outcome:
- Error, refusal, recovery, and unavailability:
- Functional verification:
- Interaction, information order, and visual expectations:
- Accessibility and readability:
- Content/data accuracy and source fidelity:
- Security, privacy, authority, and records boundaries:
- Performance or timing:
- Cross-role handoffs:
- Regression and change impact:
- Project-specific checks requested by the Truth Owner:

## Human-only gates

Rows that require a physical device the Builder does not have, a named human, or a signature. Recorded as `NOT-RUN(human-only)`; never reported as passes. A missing tool or environment is not human-only: it is `NOT-RUN(environment)` with a blocking `OPEN-###`.

| ID | Gate | Who performs it | Environment | Result |
|---|---|---|---|---|

## Findings and trace closure (filled by the Builder, verified by the Auditor)

- BN IDs with no UAT evidence:
- REQ IDs with no verification evidence:
- EXP/BUILD IDs not exercised:
- UAT cases with no upstream authority:
- Defects, severity, owner, and retest state (UAT-DEF IDs):
- Limits accepted by whom and why:
- Loop history: passes run, rows fixed per pass, the two closing full passes with counts:

## Defect records

One file per defect under `work/evidence/uat/<version>/pass-NN/defects/UAT-DEF-###.md`: row, severity, requirement quoted, reproduction from clean state, observed with evidence paths, expected, required exit condition, fix (version, files, pre-fix-failing control, before and after runs), status.

## Result comparison (when a Result 2 exists)

- `RESULT 1:` artifact/version, Project Index version, and exact 01–05 versions used
- `FIRST PRESENTATION:` what was shown, questions, and feedback
- `CONTEXT DIAGNOSIS:` which upstream decisions shaped strengths and defects
- `CONTEXT DELTAS:` file/section/ID, before → after, reason, affected trace links
- `ITERATION WINDOW:` start/end and UAT rerun
- `RESULT 2:` artifact/version, Project Index version, improvements, regressions, unchanged defects, and evidence
- `SECOND PRESENTATION:` comparison defended and questions answered
- `NEXT ITERATION:` next change, expected effect, evidence, and owner

## Authorization (Auditor and owner only; the Builder never fills this)

- Builder verdict received: `CANDIDATE READY FOR INDEPENDENT AUDIT | CANDIDATE BLOCKED`
- Independent audit: `REPRODUCE.md` re-run, manifest recomputed, PNGs reviewed, `05` diffed against the attached original, OPEN list compared with `01`
- Verdict: `AUTHORIZE | AUTHORIZE WITH RECORDED LIMITS | RETURN FOR REPAIR | REJECT`
- Evidence package:
- Open defects and owners:
- Human acceptance authority and date:
