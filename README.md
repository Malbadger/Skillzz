# Skillzz

Portable expert prompts for five agent workflows:

- Archive Search
- Build-to-Acceptance Kit Intake
- Context Curator
- Context Gate
- Pi Agentic Workflow Accelerator

The `prompts/build-kit-templates/` directory contains the six canonical Build-to-Acceptance templates used by the intake prompt.

## Pi always-on policy

`pi/APPEND_SYSTEM.md` is the compact, always-on form of the Pi Agentic Workflow Accelerator. Install it globally without replacing Pi's default system prompt:

```bash
mkdir -p "$HOME/.pi/agent"
ln -s "$(pwd)/pi/APPEND_SYSTEM.md" "$HOME/.pi/agent/APPEND_SYSTEM.md"
```

Run the command from the repository root. Restart Pi after installing or updating the file. The longer prompt under `prompts/` remains the standalone reference and kickoff version.

## Safety and portability

The published prompts contain no user-specific home paths, credentials, email addresses, private network locations, or private archive contents. Local integrations are configured with environment variables such as `ARCHIVE_ROOT`, `CONTEXT_CURATOR_HOME`, and `CONTEXT_GATE_VALIDATOR`.

Review and validate every workflow in its target environment before relying on it. Context Gate requires a deterministic validator; a model-generated verdict by itself is not authorization to advance a phase.
