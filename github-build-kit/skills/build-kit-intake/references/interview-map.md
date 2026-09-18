# Interview map for Build-to-Acceptance

Ask for decisions in the order below, adapting the wording to the project. A supplied repo, design, or prior answer may already settle a question. Ask follow-ups only when the answer changes behavior or acceptance.

| Phase | Questions to resolve | Destination |
|---|---|---|
| Project truth | Who uses it, for what decision or outcome? What is in the first release and explicitly out? What does success look like? Who owns scope, authority, privacy, and external commitments? | `01` purpose, truth model, roles, `BN`, owner-reserved decisions; `00` project map |
| Functional behavior | For each need, what triggers the action, what input is accepted, what result appears, where is it stored, and what happens on bad input or unavailable dependencies? Which system is authoritative for every displayed value? | `02` boundary, data model, integrations, rules, `REQ` |
| Interaction | What are the entry point, ordered steps, user decisions, roles, surfaces, states, and recovery paths? Which devices or environments must work? What accessibility or visual references are required? | `03` actor model, `EXP`, surface and profile tables, states |
| Build standard | Which stack and repository conventions are fixed? What exact commands clean-build, run, check, test, package, and load exemplars? What tools can drive and capture the real artifact? What actions or paths are prohibited? | `04` pre-build standard and contract; `00` software profile |
| Acceptance | What concrete example inputs and owner-supplied expected results prove the rule? What should an independent observer see and read back? What is the threshold or tolerance? Which checks require a human or unavailable environment? | `05` UAT and exemplar rows, coverage, human-only gates |

## Trace and ownership rules

- `BN` expresses a needed outcome; `REQ` implements it; `EXP` places it in an experience; `UAT` checks the stated result. A command-only or service project may have an API or terminal interaction rather than a screen.
- Prefer one observable behavior per `REQ`. Include the failure or recovery case and verification method. Give every `REQ` at least one UAT row. Give every `EXP` a UAT path or an explicit reason it cannot be run yet.
- The owner supplies expected exemplar results or an authoritative way to calculate them. Keep `Actual` and `Result` empty or `not run` during intake.
- `04`'s build record and verification section belong to the Builder. `05`'s observed findings and authorization belong to the Builder and Auditor as labeled. Intake may prepare their structure but may not present predictions as observations.
- `00` controls active versions. A change to an approved `01`–`03` decision needs a `CHG-###` proposal and downstream impact; do not overwrite the prior approved decision.
- A `HOLD` names the missing decision, its owner, affected rows, and branches that can still proceed. Do not convert `HOLD` to `READY` by weakening a UAT threshold or inventing an expected result.
