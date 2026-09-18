---
name: build-kit-intake
description: Interview a project owner and draft or revise the six Build-to-Acceptance kit files before a Builder session. Use when asked to set up, fill, or repair a build kit; do not use for implementing the application or auditing a finished candidate.
---

# Build-kit intake

Turn a product idea, existing repository, and the owner's answers into a reviewable Build-to-Acceptance kit. This is an intake and specification skill. The Builder and independent Auditor retain their separate roles.

## Source of truth

The kit on this machine is at `../../build-kit/`. Read its `README.md`, `kit-templates/00-PROJECT-INDEX.md` through `05-AUDIT-AND-ACCEPTANCE.md`, and `BUILD-TO-ACCEPTANCE-MASTER-PROMPT.md` Appendix A when preparing a kit. Use the templates as the output skeleton; preserve their required fields, tables, ID families, and evidence contract. Do not edit the archived source. If these files are unavailable, tell the owner and request the kit rather than inventing a replacement schema.

For the interview's question map and file ownership, read [references/interview-map.md](references/interview-map.md). Read existing project documentation and code when the owner points to a repository; distinguish observed repository facts from the owner's intended behavior. Search the archive first when the work includes build, configuration, or debugging under this machine's `AGENTS.md`.

## Intake loop

1. Establish the project name, whether this is a new or existing build, the target repository or destination, the decision maker, and the intended users. If a kit already exists, inspect and revise it in place; preserve approved versions and record proposed changes in `00` instead of replacing them silently.
2. Ask small, coherent batches of questions, normally 2–4 at a time. Start with purpose, actors, success, and version-one boundaries. Continue into behavior, data, integrations, interface, stack, and acceptance. Offer a recommendation and its reason when an engineering choice is genuinely open. Do not make the owner answer questions that the existing code or documentation resolves.
3. Record answers in the owning file as the interview progresses. Give each need `BN-###`, each functional requirement `REQ-###`, each ordered interaction `EXP-###`, and each acceptance case `UAT-###`. Maintain trace links among them. Write singular requirements with observable outputs, failure behavior, and a verification method. For each UAT row, predeclare expected behavior and a pass threshold; never let the Builder define its own expected result after seeing the implementation.
4. For every value the product shows or computes, identify its authoritative source, calculation, or owner decision. Ask about an unsourced value before treating its behavior as settled. Classify unresolved choices as owner-reserved (scope, authority, privacy, money, external commitments, safety) or resolvable implementation choices. Put owner-reserved items and affected branches in `01`; record other assumptions visibly with alternatives and impact. Unknown is a valid entry; a plausible guess is not evidence.
5. Fill `04`'s pre-build standard and `05`'s predeclared acceptance cases. Do not fill Builder-observed `BUILD` rows, actual test results, defect records, or Auditor authorization. Determine exact build/run/test/package commands from the repo when possible; otherwise leave an explicit open item with owner and impact. Never claim a command works until it has been run.
6. Create `START-HERE.txt` with the kit's absolute local path, file set, working directories, and handoff instructions. Keep generated source, artifacts, and evidence in `work/`, not at the kit root. Use the kit's own folder convention unless the owner chooses another location.
7. Run the master prompt's Appendix A readiness check and trace census. Report `READY FOR RESULT 1`, `READY FOR RESULT 2`, or `HOLD` in `00` with the exact unresolved items and blocked branches. A draft may remain `HOLD`; still finish every unaffected section. Mark files `DRAFT` until the designated owner approves a baseline. Do not self-approve, mark `BASELINED`, or change an approved baseline on the owner's behalf.

## Handoff

Give the owner a concise map of what is filled, what decisions still require them, and whether the kit is ready for the Builder. When ready, identify the Builder prompt location and extraction boundary; do not launch a Builder session as part of intake unless separately requested. Keep the distinction between specified, observed in the repository, assumed, and not yet verified clear in the kit and in the handoff.
