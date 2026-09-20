# Build Record: PRJ-###

## Control and inputs

- Builder:
- Project Index version loaded:
- Files 01–03 versions loaded:
- Candidate/output version:
- Approved tools and environment:

## Software build standard (define before building; the Builder matches it exactly)

### Stack and environment

| Item | Value |
|---|---|
| Stack class (web, desktop, mobile, terminal, service or library, data model) |  |
| Languages and runtimes (exact versions) |  |
| Frameworks |  |
| Data store |  |
| Package manager and lockfile |  |
| UI automation and capture tool for UAT (browser automation; the platform UI test harness or OS screen capture; terminal capture; scripted calls) |  |
| Image tooling for PNG measurement and contact sheets (where the class produces PNGs) |  |
| Target platform(s) for the packaged artifact |  |

### Commands

Each with its expected success output. The Builder records the actual output beside it in `evidence/REPRODUCE.md`.

| Purpose | Command | Expected success line or count |
|---|---|---|
| Clean build from an empty directory |  |  |
| Run the application (production mode) |  |  |
| Lint and type checks |  |  |
| Unit and integration tests |  |  |
| Package the artifact |  |  |
| Load the exemplar set through the product's own entry path |  |  |

### Structure, naming, and versioning

- Repository structure (defaults: source `work/app/`, artifact `work/dist/`, prior candidates `work/dist-archive/`; nothing at the kit root):
- File and module naming:
- Version scheme and where the visible stamp appears in the UI:
- Commit message convention:
- Evidence layout: `work/evidence/` per the master prompt's Section 11, verbatim

### Forbidden actions and content

- Forbidden actions (network, destructive commands, paths outside the worktree, secrets in source or logs):
- Forbidden content on production paths: `TODO`, `FIXME`, `stub`, `placeholder`, `mock`, `fake`, `lorem`, `sample data`, `driver: null`, `dryRun`, `readOnly: true` defaults, `applied: false` defaults, raw JSON dumps in operator-facing UI
- Permitted stub exceptions by exact path (usually none):
- Banned-word battery for documents the Builder writes: no em-dashes; no `comprehensive`, `ensuring`, `tailored`, `robust`, `leverage`, `delve`, `landscape`, `cutting-edge`, `seamless`, `tapestry`, `unleash`, `empower`, `synergize`, `rigor`, `critically`, `notably`, `meticulous`; no marketing words; American English

## Build contract

- Structure and naming:
- Approved inputs/dependencies:
- Forbidden actions or content:
- Human-owned decisions:
- Error/failure behavior:
- Provenance, logs, or citations:
- Accessibility and experience standard:
- Review and change rule:
- Version, handoff, and rollback:

## Build record (filled by the Builder)

| ID | Built artifact or decision | Traces to REQ / EXP | Location/version | Evidence/check performed | Known deviation | Status |
|---|---|---|---|---|---|---|
| BUILD-001 |  | REQ-001 / EXP-001 |  |  |  | built |

## Build verification (filled by the Builder)

- Clean build/production evidence (command, environment, output):
- Static or automated checks (counts with environment and skip reasons):
- Stub sweep result:
- Census result (built versus implied by 03):
- Human review:
- Known limitations:
- Rollback/recovery rehearsal:
- Upstream change requests raised instead of silently implemented (CHG IDs):
- Known deviations and approved disposition:
- Assumptions made (AS IDs) and where each is visible in the product:

**Builder exit test:** Does a reproducible candidate exist, with every material build choice traced to approved function and interaction decisions and every deviation made visible?
