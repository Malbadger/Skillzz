# Skillzz

Portable expert prompts for five agent workflows:

- Archive Search
- Build-to-Acceptance Kit Intake
- Context Curator
- Context Gate
- Pi Agentic Workflow Accelerator

The `prompts/build-kit-templates/` directory contains the six canonical Build-to-Acceptance templates used by the intake prompt.

## Safety and portability

The published prompts contain no user-specific home paths, credentials, email addresses, private network locations, or private archive contents. Local integrations are configured with environment variables such as `ARCHIVE_ROOT`, `CONTEXT_CURATOR_HOME`, and `CONTEXT_GATE_VALIDATOR`.

Review and validate every workflow in its target environment before relying on it. Context Gate requires a deterministic validator; a model-generated verdict by itself is not authorization to advance a phase.
