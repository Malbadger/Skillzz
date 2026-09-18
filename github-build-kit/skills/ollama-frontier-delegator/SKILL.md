---
name: ollama-frontier-delegator
description: Delegate bounded, low-risk coding and text-transformation tasks to an already-running local Ollama model, then have Codex or Claude Code inspect and validate the result. Use for routine generation, boilerplate, test scaffolding, formatting, summarization, or first-pass code when conserving frontier-model tokens without changing Ollama or evicting its active model.
---

# Ollama Frontier Delegator

Use the resident Ollama model as a junior implementer. Keep the frontier model responsible for specifications, tests, judgment, repository edits, verification, and the final answer.

## Workflow

1. Inspect the request and repository state at the frontier.
2. Delegate only a bounded, independently checkable subtask.
3. Resolve paths relative to this `SKILL.md`, then run `python3 <skill-directory>/scripts/ollama_delegate.py --list` to identify resident models.
4. Write a compact contract containing acceptance criteria, exact dependency signatures, relevant types, language versions, and only necessary source context.
5. Send it through stdin:

   ```bash
   python3 <skill-directory>/scripts/ollama_delegate.py <<'PROMPT'
   Produce a unified diff for this bounded change.
   [contract, exact interfaces, and necessary context]
   PROMPT
   ```

6. Treat the response as an untrusted draft. Apply edits with the frontier agent's normal editing tools.
7. Inspect consumer-visible output shapes, async/thread boundaries, error paths, and dependency calls closely.
8. Run tests, linters, type checks, or focused inspections at the frontier.
9. Prefer a targeted frontier fix when a draft is close; do not regenerate working sections unnecessarily.

## Delegate

- boilerplate and repetitive code
- test-case enumeration and initial scaffolds; the frontier agent writes final tests
- small pure functions with explicit contracts
- docstrings, fixtures, schemas, and mechanical transformations
- summarization of large, non-sensitive local output
- proposed regexes, SQL, shell snippets, or refactors that will be tested

Ask for a diff or structured answer rather than broad discussion. Include exact dependency APIs: local models commonly invent interfaces they cannot see.

## Keep at the Frontier

Do not delegate:

- auditing, validation, approval, or final review
- architecture, security, privacy, authentication, authorization, or cryptography
- destructive operations, deployments, migrations, financial actions, or incident response
- ambiguous changes requiring product judgment
- secrets, credentials, private keys, or unredacted sensitive data
- final tests, interpretation of test results, or the completion decision

For mixed tasks, delegate only the safe subproblem.

## Preserve Ollama State

The helper only calls `/api/ps` and `/api/chat`. It does not start, stop, configure, pull, preload, or unload models. By default it uses only a model reported as resident and refuses to trigger a new load. It prefers `OLLAMA_DELEGATE_MODEL`, then a resident Qwen model, then another resident model.

Do not pass `--allow-load` unless the user explicitly accepts possible VRAM eviction. Do not change `keep_alive`, Ollama environment variables, or service configuration.

The default endpoint is `http://127.0.0.1:11434`. Set `OLLAMA_HOST` or pass `--host` for another loopback address. Remote endpoints are rejected.

## Validation Standard

Never accept code because it looks plausible. Compare it with actual files, check exact API signatures and consumer-required shapes, and execute proportionate checks. Abandon poor local output when direct frontier work is cheaper than repeated prompting.

The frontier agent remains accountable for every change and claim.
