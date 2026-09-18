# Why every rule in the prompt exists: 20 observed Builder failure modes

Companion to `BUILD-TO-ACCEPTANCE-MASTER-PROMPT.md`. Each rule in that prompt was
written against a behavior somebody actually observed a coding agent produce
when handed a specification and left to run. This file is the catalog.

Read it when you are tempted to drop a rule from the prompt because it looks
like ceremony. Every one of them is scar tissue.

> **Provenance and what was cut.** This is `BUILD-PROMPT-ANALYSIS_2026-08-27.md`
> from the download, rewritten to be project-agnostic. Two of its eight sections
> were dropped whole: an inventory of the author's own named internal systems,
> and a six-generation lineage of their earlier prompts. Both were org history
> with nothing reusable in them. Kept and generalized: the failure modes below,
> what worked, the design decisions, the open items, the boundary. Each failure
> mode originally cited an internal file name; those citations are replaced with
> the *shape* of the evidence, because the shape is what transfers.
>
> The underlying record is roughly six months of agent-built systems: governance
> tooling, a teaching platform with signed desktop apps, several standards and
> conformance suites. Nothing on this list was hypothetical when it was written.

## The one-paragraph version

Specifications alone do not produce working software from an agent. The
specification tells the agent what to build; nothing in it prevents the agent
from reporting success it did not earn. What closes that gap is a fixed
evidence contract the agent cannot satisfy by writing prose: run the real
artifact, from a clean state, capture what happened, hash it, and let a
different seat re-run the commands. The prompt is that contract. Each rule
below names the failure it exists to catch and the detection that finds it.

## The failure modes

| # | Failure mode | Shape of the evidence | Countermeasure in the prompt |
|---|---|---|---|
| FM-01 | Production path wired to nothing: `driver: null`, the only driver a test fixture, the flagship route returning an error code | A wiring verification found the break four steps into the lifecycle; the feature had never run end to end | B1 (real path only); the route and control census in Phase C; UAT runs on the production artifact, never the test harness |
| FM-02 | Dry-run and propose-only hardcoded: `dryRun: true`, `applied: false`, a read-only session; the loop never delivers a change | The completeness audit's finding was literally "the Builder produces nothing" | B1 forbids default-off, dry-run, and read-only on production paths; the stub sweep in Phase C must return zero |
| FM-03 | Built but never mounted: a component imported and unused; whole lanes with real code and no caller | Gaps found only by trying to watch the feature happen | Phase C census: every component mounted, every route reachable, every strategy with a live caller; orphan detection is a listed check |
| FM-04 | An advisory gate standing in for the real gate; a label naming a mutation that never happened | Same wiring verification, two more steps | B5 (labels describe what the code does); UAT error and authority rows trigger the real condition, never a toggle |
| FM-05 | Evidence theater: screenshots rendered from text files in a text editor instead of the running app; byte-identical duplicate frames; partial frames | An independent review's first three open items | D3 PNG rules: native rendering only, unique SHA-256 per PNG, stable-render wait, the Builder opens every PNG; duplicate hashes fail the sweep |
| FM-06 | Counts drift between prose and source; stale language survives a sweeping edit | A closure report where the prose said one count and everything else said another | Every number is pulled from a named command output; the regression-watch block each loop pass |
| FM-07 | Remediation records that do not reproduce | 8 of 25 statements in one remediation record failed to reproduce, starting with its own byte count | The Builder's report is a claim set; `REPRODUCE.md` with exact commands and expected counts is mandatory; the independent audit re-runs it |
| FM-08 | A green test suite offered against an observed failure | Duplicate records reproduced twice by hand while the whole suite passed | D9: a green suite never overrides an observed failure; every defect fix ships a pre-fix-failing control |
| FM-09 | Ambiguous release media: stale archive copies beside the manifest set; a release built from uncommitted changes | Two separate UAT rows in one campaign | D1: clean output directory, exact version stamp, committed state recorded; Phase F sweeps for stray artifacts and uncommitted changes |
| FM-10 | A plausible default in place of an honest unknown (an offline source relabeled as a real one) | Same campaign | B5: `UNKNOWN` is a valid state; never a guessed default |
| FM-11 | State that never reverts: a "verified" marker never downgraded when its basis was later rejected | A handoff record's open track | B5: every state the kit says can regress must be shown regressing in a UAT row |
| FM-12 | Claims broader than their names: a conformance component with no production caller, described as if the runtime used it | An acceptance record's own honesty section | The "claims narrower than their names" section is required, not optional |
| FM-13 | Test counts without their environment, reported as if portable | A build report's self-audit | Every count carries OS, architecture, runtime version, dependency source, and skip reasons |
| FM-14 | Stopping at a decision the kit already resolved, or improvising one the kit reserved for the owner | Recurrent across handoffs; the operator-gated list existed because of it | Section 3.2 splits unknowns into owner-reserved (block that branch, build the seam, continue) and resolvable (decide, tag `AS-###`, continue) |
| FM-15 | Ending the session with "next steps" instead of doing them; declaring done on partial work | A standing rule in the source standards: partial progress never transitions a ticket | Exit condition is two consecutive clean full UAT passes; `RESUME.md` for forced stops; the verdict vocabulary has no "done with caveats" |
| FM-16 | Fix-iteration thrash: the same row repaired repeatedly without convergence | Why the source standards carried an iteration budget at all | Thrash guard: three distinct failed fixes on one row becomes `OPEN-###` with a diagnosis; the verdict is BLOCKED, never READY |
| FM-17 | Machinery inflation: release gates growing into scoped sentinels, supersession transactions, and hundreds of kilobytes of verifier scripts | A README section documenting machinery that was never launchable | Section 11 fixes the evidence contract inside the paste block, so the Builder implements a known contract instead of inventing a larger one; new ceremony is a `CHG-###` proposal |
| FM-18 | Demo behavior offered as product behavior: simulated data, staged sequences, toasts standing in for effects | Correct for the demo prompt this one was inverted from; wrong here | Section 0 and B2: exemplar data enters through the product's own entry path; every action produces its real effect in the real store |
| FM-19 | Context decay during iteration: after the first pass the agent modifies and adds features from its *memory* of the spec rather than the spec, so look, feel, and outputs drift | Operator observation: outputs stopped "factoring the entire markdowns each time modifications were made" | Section 3.7: all kit files re-read in full before every pass and every change, hashes recorded per pass; B11 determinations ledger (every surface attribute cites kit text or an `AS-###`); Phase A context inventory; P21 |
| FM-20 | Elided outputs: tables with rows omitted, "similar for the other screens", records that stop partway | Operator observation, plus the partial-frames finding in FM-05 | Section 3.8 complete-outputs rule; F5 elision sweep; table row counts must equal register counts; P22 |

## What worked, and is carried forward unchanged

**The ID-traced register is the spine.** Reviewers accept and reject IDs, not
impressions; every surface carries its ID; every UAT row traces up to a need
and down to a build row. This produced the cleanest iteration records on file.

**Pre-fix-failing controls are the single most effective anti-theater device.**
A fix without a test that failed before it is not a fix.

**The restart rule closes the campaign.** After the last fix, the full battery
reruns from a clean state, and the closure record reports only post-fix
results. Delta reruns are for the loop; full reruns are for closure.

**Real-target validation finds what the suite cannot:** identity collisions,
stale archives, unreproducible builds. The packaged artifact from a clean data
directory is the only legitimate UAT target.

**The visual fleet method works as written:** viewport and theme profiles from
the interaction file; measured overflow, clipped and undersized controls,
contrast, and layout shift; before-and-after captures with a state delta;
contact sheets for review; an exact on-disk screenshot inventory; RAG with
written definitions.

**Honesty sections** in the Builder's own report (corrections made under the
directive, remaining open items, claims narrower than their names, what was not
covered) turn a report into something an auditor can sign off from.

**The separation rule stays.** The Builder never issues AUTHORIZE. The prompt
ends at `CANDIDATE READY FOR INDEPENDENT AUDIT` or `CANDIDATE BLOCKED`, and a
non-builder seat audits the evidence next.

## Design decisions encoded in the prompt

1. The kit stays a five-role document stack with its ID families, so the same
   files serve any project. Appendix B adds a software profile to each file
   rather than replacing the templates.
2. **"Does not stop" is defined precisely.** The Builder never asks and never
   checkpoints. It halts a *branch* only for an owner-reserved decision with no
   default, and halts the *session* only for prohibited content or a
   destructive action outside the sandbox. Everything else proceeds under a
   tagged assumption or an OPEN item, and work continues elsewhere.
3. **UAT executed by the Builder against its own candidate violates the
   separation rule in spirit.** The prompt handles this by making the evidence
   contract mechanical (commands, counts, hashes, PNGs that must exist and must
   be unique) so the independent audit can *re-run* rather than *re-trust*. The
   Builder's UAT is the loop; the auditor's UAT is the verdict.
4. **PNGs are evidence, not proof.** Every PNG pairs with a state readback that
   shows the action took effect, and the Builder must open and look at each one.
   A screenshot nobody looked at is not evidence.
5. **Exemplar data is the only permitted content.** It enters through the
   product's own entry path, so the product is tested and not a fixture.
   Expected results come from the kit; the Builder may not author them.
6. **Convergence is two consecutive clean full passes from a clean state,**
   with a thrash guard so the loop cannot run forever on one defect.
7. **The evidence layout is fixed inside the paste block** (Section 11), so the
   Builder implements a known contract instead of inventing release machinery.
8. **The prompt is stack-neutral by construction.** Section 2a maps every rule
   to six stack classes: what a surface and a route are, what a profile is, how
   the class is driven and captured, which layout metrics apply, where the
   console is, how ID tags are shown, and what an input round trip exercises. A
   capture or metric that does not apply is recorded as `n/a (reason)`, never
   dropped, so a terminal tool cannot claim PNG evidence it cannot have, and a
   native app cannot skip measurements it could have made.
9. **Context decay (FM-19) is treated as a build defect with a mechanical
   detection,** not a style note. Whole-kit re-read before every pass, hashes
   recorded, a determinations ledger citing kit text per surface attribute, and
   the auditor sampling surfaces against the interaction file.
10. **Three adversarial review rounds before release** (36, 17, and 12
    findings). The High items were structural: the evidence contract sat
    *outside* the paste block; `NOT-RUN` could reach a READY verdict; measured
    layout metrics had no pass threshold; evidence had no pass versioning; an
    uncitable acceptance row could be removed; every owner-reserved decision
    blocked READY, which rewarded misclassification; readbacks could be typed
    by hand; Phase F could change source after the closing passes. Each is now
    a specific rule with a detection, and Section 2 defines the terms the review
    found exploitable (production path, clean state, profile, real condition,
    stable render, human-only gate).

## Open items the original author flagged

1. The kit templates are software-profile extensions of a general-purpose
   five-role stack. If the general templates must stay byte-identical for other
   uses, keep the software copies separate.
2. Reference images are optional inputs to `03`. If you want pixel-level
   conformance rather than structural, say so in the row; the default is
   structural.
3. The prompt assumes the Builder can drive a UI automation tool and open
   images. If a session cannot, the missing tool is a blocking `OPEN-###`, the
   PNG rows are `NOT-RUN(environment)`, and the verdict is BLOCKED, by design.

## Boundary

This is a distillation of one operator's build record, not a controlled study.
The failure modes are real and were observed repeatedly; the countermeasures
are asserted to work, and the evidence for that assertion is that the same
failures stopped appearing in later campaigns. Nothing here has been
independently replicated.
