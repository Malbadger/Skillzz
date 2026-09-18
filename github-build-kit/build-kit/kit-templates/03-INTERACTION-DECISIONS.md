# Interaction Decisions: PRJ-###

## Control and inputs

- Interaction Designer:
- Project Index version loaded:
- Project Truth version loaded:
- Functional Contract version loaded:
- Intended environments and access needs:

## Actor and information model

| Actor | Goal or decision | Information needed | Where/when it appears | Action available | Authority limit |
|---|---|---|---|---|---|

## Ordered experience

| ID | Actor/state | What must happen first | Information shown or supplied | Action/decision | Next state | Traces to REQ |
|---|---|---|---|---|---|---|
| EXP-001 |  |  |  |  |  | REQ-001 |

## Software profile

### Surface inventory

One row per surface in the stack class's terms (page or screen, window or view, command, endpoint, sheet or report); the route is how a user reaches it (URL, menu path, command line, operation, tab). The Builder's census is compared against this table.

| Surface ID | Route | Actors | Primary EXP rows | Controls or inputs (count) | States present |
|---|---|---|---|---|---|

### Profiles

Every UAT row with a surface runs once per profile. Name at least the devices the Truth file implies. For a desktop application the viewport is the window size; for a terminal application it is columns by rows plus color mode; for a service or library the single profile is `api`.

| Profile ID | Viewport, window, or terminal size | Theme or color mode | Text scale | Reduced motion | Notes |
|---|---|---|---|---|---|

- Interactive target minimum size (px):
- Text contrast floor: 4.5:1 body, 3:1 large text (or stricter)
- Stable-render quiet window for captures (ms):

### Reference images

Optional. Structural conformance (same regions, order, controls, states) is the default bar; state `pixel` only where pixel identity is required.

| EXP or Screen ID | File in `work/reference/` | Conformance bar (structural / pixel) | Notes |
|---|---|---|---|

### State table

One row per surface. Every state named here must be produced by a real condition in UAT, never by a toggle.

| Surface ID | Empty | Loading | Error | Offline | Refused (authority) | Completed |
|---|---|---|---|---|---|---|

## Interaction and presentation decisions

- Entry point and first decision:
- Information hierarchy: what is primary, supporting, optional, or hidden until needed:
- Required sequence and dependencies:
- Human-to-AI and AI-to-human handoffs:
- Confirmation, refusal, escalation, and recovery states:
- Visual expectations: layout, emphasis, density, charts/figures, status, and feedback:
- Accessibility: keyboard, focus order, text size, contrast, non-color cues, captions/alternatives:
- Empty, loading, error, offline, and completed states:
- What the experience must not do:

## Decision record

| Decision | Alternatives considered | Choice and reason | Evidence/user need | Affected EXP/REQ | Human owner |
|---|---|---|---|---|---|

## Open decisions

Decisions nobody has made. The Builder shows these as open at the surface they affect and never resolves them.

| Open decision | Options | Surfaces affected | Owner |
|---|---|---|---|

## Interaction audit

- Actors with no supported path:
- Information required but not placed:
- Actions with no feedback or recovery:
- Steps in the wrong order or missing prerequisites:
- Visual/accessibility decisions not testable:

**Interaction Designer exit test:** Can a Builder place every required piece of information, action, decision, state, and visual expectation in the correct order without inventing an experience?
