# Project Truth: PRJ-###

## Control

- Project/output:
- Truth Owner:
- Project Index version loaded:
- Version/date:
- Status: `DRAFT | BASELINED | SUPERSEDED`
- Approved by:

## Idea, purpose, and decision

- Idea in one sentence:
- Why this should exist:
- Intended recipient/operator/beneficiary:
- Decision or behavior it should enable:
- Final output and medium:

## Complete truth model

- Current state and workflow:
- Desired end state:
- In scope:
- Out of scope:
- Constraints and non-negotiables:
- Known facts with evidence locators:
- Assumptions requiring validation:
- Contradictions requiring a human decision:
- Unknowns, owner, and impact for each:
- Risks and affected people:
- Definition of success:

## Software profile

### Roles

Actors whose identity changes what the application shows or permits. The Builder builds a role switcher from this table and runs role-dependent UAT rows once per named role.

| Role | Who | What they can see | What they can do | What they must never do |
|---|---|---|---|---|

### Owner-reserved decisions

Decisions the Builder may not make. For each, the Builder builds the configuration seam that lets the owner decide later, records `OPEN-###`, and continues with everything the decision does not touch.

| Decision | Options | Default the Builder may seam | Owner | Branches blocked until decided |
|---|---|---|---|---|

### Exemplar set

- Location: the exemplar cases table in `05-AUDIT-AND-ACCEPTANCE.md`, the proving cases in `02`, or `work/exemplars/cases.json` (never `shape-refs/`)
- Case count:
- Source of each expected result (who computed it, from what, when):
- Cases the Builder may not run without a human present (if any):

## Needs

Write needs as outcomes, not solutions.

| ID | Needed outcome | Stakeholder | Evidence/source | Success measure | Priority | Not claimed | Status |
|---|---|---|---|---|---|---|---|
| BN-001 |  |  |  |  |  |  | proposed |

## Truth verification and change log

- Sources actually reopened:
- Claims changed after retrieval or review:
- Missing or disputed evidence:
- Human decisions still required:

| Version/date | What changed | Evidence or decision | Downstream roles requiring review |
|---|---|---|---|

**Truth Owner exit test:** Could a different professional explain what is wanted, why, for whom, against what evidence, inside what boundary, and what remains unknown without asking AI to invent anything?

AI must not infer missing project facts. Mark the gap `OPEN`, name its owner and impact, and stop that branch until evidence or a human decision closes it.
