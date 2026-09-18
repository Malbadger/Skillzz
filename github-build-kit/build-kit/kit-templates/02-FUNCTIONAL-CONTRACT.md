# Functional Contract: PRJ-###

## Control and inputs

- Functional Designer:
- Project Index version loaded:
- Project Truth version loaded:
- Functional baseline:
- Open authority or interface decisions:

## Functional boundary

- Output/system of interest:
- Actors and external systems:
- Inputs and authoritative sources:
- Required processing or transformation:
- Outputs and destinations:
- Human-owned decisions:
- Interfaces and handoffs:
- Exception path and failure handling:

## Software profile

### Data model

| Entity | Key | Required fields | Validation rules | Retention and deletion | Traces to BN |
|---|---|---|---|---|---|

### Integrations

For each external system. When credentials are not supplied, the Builder builds the real adapter against the interface reference, a labeled local adapter with the same contract, selects by configuration with the real adapter as default, tests both, and records `OPEN-###` for the credential.

| System | Interface reference (doc, version, section) | Credentials supplied? | Permitted local adapter behavior | Traces to REQ |
|---|---|---|---|---|

### Calculations and rules

Every rule the application applies, stated so a test can be written from it, with the exemplar case that proves it.

| Rule ID | Rule text or formula | Inputs | Output | Edge cases | Proving exemplar case | Traces to REQ |
|---|---|---|---|---|---|---|

## Functional requirements

Each requirement is singular, necessary, feasible, unambiguous, and verifiable. Software may "shall accept, calculate, deny, preserve, or report." The verification method is one of `test` (automated test named for the REQ), `demonstration` (a UAT row with evidence), `inspection`, or `analysis`.

| ID | The output shall… | Traces to BN | Trigger/input | Required behavior/output | Failure or recovery behavior | Verification method and evidence | Owner | Status |
|---|---|---|---|---|---|---|---|---|
| REQ-001 |  | BN-001 |  |  |  | test / demonstration / inspection / analysis |  | proposed |

## Quality and boundary requirements

- Accuracy and source fidelity:
- Safety, security, privacy, and records:
- Accessibility:
- Performance or timing:
- AI may / may not:
- Human review and terminal authority:
- Unavailability and recovery:

## Functional audit

- Needs with no functional response:
- Requirements with no upstream need:
- Compound or non-verifiable requirements:
- Missing failure/recovery behavior:
- Conflicts or human decisions:
- Verification method:
- Expected evidence:
- Owner:
- Pass condition:

**Functional Designer exit test:** Can a Builder and Auditor tell exactly what must happen, what must never happen, and what observable evidence would prove each function without guessing about the desired behavior?
