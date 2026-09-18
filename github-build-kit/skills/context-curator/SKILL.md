---
name: context-curator
description: User-directed context-window compaction for Claude Code and Codex transcripts or tasks. Use when the user explicitly asks to curate, preserve, trim, or compact current context, or when the client reports imminent compaction at an idle human turn boundary. Recommend semantic KEEP/EXTRACT/DROP choices, interview the user about ambiguous material, and produce a confirmed digest. Never interrupt an active automated, background, or unattended workflow; allow native automatic compaction to proceed normally.
---

# Context Curator

Make the user the authority over what survives compaction. Treat model choices
as recommendations until the user approves a final preview.

Once this skill is loaded, do not invoke `context-curator` or any other skill
again to perform its steps. Use the available filesystem/command tools directly.
If a required tool is unavailable, state the limitation after one attempt and
ask the user how to proceed; never loop on skill loading.

## Gate: decide whether to run

First check for active automation. If a plan, tool loop, background task,
unattended run, or "continue until complete" workflow is in progress, do not
interview—even if context pressure is high. Continue the workflow and let native
automatic compaction run. If the user requested curation mid-run, defer it until the
next idle human boundary unless the user explicitly pauses the automation.

When no automation is active, enter the interactive workflow only when either
condition holds:

1. The user explicitly invoked this skill or asked to curate/compact context.
2. The client explicitly reports imminent compaction, execution is idle at a
   human turn boundary, and a user is available to answer.

Otherwise do nothing: do not ask questions or create artifacts.

If uncertain whether a run is interactive, default to no interruption.

## Privacy and client selection

- Keep Claude Code transcripts on-box. Use the transcript CLI only from local
  Claude Code/Ollama or when the user explicitly supplies a safe local file.
- In Codex, curate only the context already present in the current Codex task.
  Do not open or upload `~/.claude/projects` transcripts.
- Never claim that a skill can rewrite a client's hidden live message array.
  The deliverable is a canonical, user-approved compact brief for native
  compaction or re-seeding.

## Interactive workflow

1. Inventory the current work into semantic groups such as current objective,
   constraints, user preferences, accepted decisions, verified results,
   important artifacts, open tasks, rejected approaches, and stale tool output.
2. Recommend `KEEP`, `EXTRACT`, or `DROP` for each group. Give a short reason
   and approximate token savings. Recommendations are advisory.
3. Ask one to three focused questions per turn about ambiguous groups. Ask in
   user language ("keep the failed deployment history?") rather than raw entry
   IDs. Always offer a way to protect exact wording.
4. Apply the answers and show a final preview containing:
   - protected instructions/facts;
   - retained compact summaries;
   - open tasks and next action;
   - dropped groups and estimated savings.
5. Ask for explicit approval. Revision is not approval. Do not materialize a
   final brief until the user clearly approves the displayed preview.
6. Materialize the approved brief, place its contents at the conversation
   frontier, and describe the client-specific handoff below.

Never silently convert an ambiguous recommendation into a final decision.

## Claude Code/Ollama transcript workflow

Resolve exactly one current transcript; never pass a directory or scan siblings:

```bash
project_key="$(pwd | sed 's#/#-#g')"
project_dir="$HOME/.claude/projects/$project_key"
transcript="$(find "$project_dir" -maxdepth 1 -type f -name '*.jsonl' \
  -printf '%T@ %p\n' | sort -nr | head -1 | cut -d' ' -f2-)"
test -n "$transcript" && test -f "$transcript"
work_dir="$(mktemp -d)"
```

Run the read-only audit if the user requests context-pressure details:

```bash
$HOME/Desktop/Python/context-curator/.venv/bin/python \
  -m context_curator.cli audit --transcript "$transcript"
```

Create the candidate inventory before interviewing:

```bash
$HOME/Desktop/Python/context-curator/.venv/bin/python \
  -m context_curator.cli propose \
  --transcript "$transcript" --out "$work_dir/proposal.json"
```

Read [references/decision-schema.md](references/decision-schema.md) before
writing the decision document. Keep `confirmed` false while drafting. Render
the exact preview and show it with its approval SHA-256:

```bash
$HOME/Desktop/Python/context-curator/.venv/bin/python \
  -m context_curator.cli preview \
  --transcript "$transcript" \
  --proposal "$work_dir/proposal.json" \
  --decisions "$work_dir/decisions.json" \
  --out "$work_dir/preview.md"
```

After the user approves that exact preview, set `confirmed` to true, copy the
printed hash into `approved_preview_sha256`, and finalize:

```bash
$HOME/Desktop/Python/context-curator/.venv/bin/python \
  -m context_curator.cli finalize \
  --transcript "$transcript" \
  --proposal "$work_dir/proposal.json" \
  --decisions "$work_dir/decisions.json" \
  --out "$work_dir/approved-context.md" \
  --receipt "$work_dir/receipt.json"
```

Present the approved brief in the conversation. For immediate replacement,
the user may pass it to Claude Code's native `/compact` instructions or use it
to re-seed after `/clear`. Do not invoke either destructive transition without
the user.

Do not use the legacy `curate` CLI command for an interactive session; it is an
evaluation compatibility path and does not contain the approval gate.

## Codex workflow

Use the same interview and approval sequence, but build semantic groups from
the current task context instead of a Claude transcript. After approval, emit
the compact brief as the newest canonical task state. Codex's native automatic
compactor can then preserve that state when needed. If Codex exposes no manual
compaction control, say so plainly rather than claiming the window changed.

## Final response contract

State which client path ran, what the user protected, counts of retained and
dropped groups, estimated size/savings, and whether native compaction still
requires a user action. Do not reproduce dropped sensitive content.
