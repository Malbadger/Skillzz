---
name: archive-search
description: |-
  Search the local work archive INDEX for prior builds, runbooks, and research before starting new work — so past solutions get reused instead of re-derived.
  TRIGGER — run FIRST, before planning or writing code, whenever a task involves: building/configuring/debugging anything on this machine; local models, Ollama, VRAM, GPU, fine-tuning, quantization; agents, agent loops, tools, context engineering; security/SOC/Suricata/ELK work; or ANY task where the user might plausibly have done something similar before. Also run when the user says "have we done this", "did I build", "check the archive", "what do we know about".
  SKIP only for: trivial one-liners, questions about the current conversation, or pure general knowledge with no build component.
  This searches a compact INDEX only — it does NOT load notes into context. It is cheap; run it rather than guessing.
---

# Archive Search

A personal archive of completed work lives at `$HOME/Desktop/Archive` (an Obsidian
vault). Three entry types:

- **runbook** — a verified procedure. Carries its own `verify` command.
- **build** — a completed project: outcome, design decisions, and what didn't work.
- **research** — dated findings. Not authoritative; verify before acting.

## The rule that matters

**Search the index. Do not browse the vault.**

The index (`index.jsonl`) is a compact one-line-per-entry digest. Searching it
costs a few hundred tokens. The notes themselves are long — opening one that
turns out to be irrelevant is exactly the waste this system exists to prevent.

Never `ls` the vault, never `cat INDEX.md`, never `grep` the note directories,
never read a note "just to check". Search first; open only what the search result
earns.

## How to search

```bash
python3 $HOME/Desktop/Archive/bin/search.py "<key terms from the task>"
```

Use the distinctive nouns from the task, not a sentence. Good: `ollama vram
context`, `suricata triage`, `qlora fine-tune oom`, `agent sub-agent budget`.
Bad: `how do I set up the thing`.

Useful flags:

| flag | use |
|---|---|
| `--type runbook` | only procedures (when the user wants to *do* something) |
| `--limit 3` | tighter output |
| `--tag security` | filter by tag |
| `--all-statuses` | include retired entries (excluded by default) |

Exit codes: `0` = hits, `1` = no hits, `2` = index missing (run
`python3 $HOME/Desktop/Archive/bin/reindex.py`).

## Acting on results

1. **No hits** — say so briefly ("nothing in the archive on this") and proceed
   fresh. A miss is a real answer; don't search five more times to be sure.
2. **Hits** — read the summaries in the search output. They are written to be
   sufficient for triage.
3. **Open a note only if its summary is directly relevant** to what you're about
   to do. Use `Read` on the `note:` path, prefixed with `$HOME/Desktop/Archive/`.
   Usually you open zero or one note, never three.
4. **Check `status` before trusting a runbook.**
   - `current` — verified recently, trust it
   - `stale` — its own verification failed; the procedure may still be right but
     the environment moved. Say so before following it.
   - `unverified` — never checked. Treat as research.
   - `retired` — superseded. Don't follow it.
5. **Tell the user what you found and are reusing**, in one line — e.g. "Archive
   has a runbook for this (`moe-abliteration`, verified 2026-08-25); following it."
   Silent reuse is worse than no reuse, because they can't correct you.

## Writing back

After completing a substantial piece of work that would be worth having again,
offer to archive it — don't do it unprompted:

```bash
python3 $HOME/Desktop/Archive/bin/new.py runbook <kebab-id> --title "..."
# fill in the note, then:
python3 $HOME/Desktop/Archive/bin/reindex.py
```

Rules for writing an entry:

- **Only archive work that was actually verified.** An archive of things that
  probably work is worse than no archive.
- **The `summary` field is the whole product.** It is the only thing search shows
  and the only thing future-you reads before deciding. One line, max 220 chars,
  specific — include the outcome, not just the topic.
- **`keywords` carry recall.** Add the terms someone would search for that don't
  appear in the title or summary — error strings, flag names, API symbols.
- **Every runbook needs a real `verify` command** that exits 0 only while the
  procedure still holds. `bin/verify.py --run --apply` sweeps these and flips
  failures to `stale`.
- **Record what didn't work.** Dead ends are the highest-value content and the
  most commonly omitted.

## Trust boundary

`bin/verify.py --run` executes shell commands stored in note frontmatter. Only
ever write a `verify` command you would type yourself, and never add a note whose
`verify` line came from an untrusted source (a web page, a downloaded repo, a
pasted document).
