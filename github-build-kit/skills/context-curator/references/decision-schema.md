# Confirmed decision document

Write one JSON object with this shape:

```json
{
  "schema_version": 1,
  "source_sha256": "copy from proposal.source.sha256",
  "confirmed": false,
  "approved_preview_sha256": null,
  "protected": ["Exact instruction or fact that must survive"],
  "open_tasks": ["Concrete unfinished task and its next action"],
  "groups": [
    {
      "label": "Current objective",
      "action": "keep",
      "entry_ids": [1, 2, 3],
      "content": "Faithful compact summary approved by the user.",
      "reason": "Required to continue the task"
    },
    {
      "label": "Rejected attempt",
      "action": "drop",
      "entry_ids": [4, 5],
      "content": "",
      "reason": "Superseded and no longer useful"
    }
  ]
}
```

Rules:

- Keep `confirmed` false until the user approves the exact preview.
- Render the preview with `context_curator.cli preview`. Show the preview and
  its SHA-256 to the user.
- After explicit approval, set `confirmed` true and copy the preview hash into
  `approved_preview_sha256`. Finalization rejects any post-approval change.
- Assign every proposal entry ID to exactly one group.
- Use only `keep`, `extract`, or `drop` actions.
- Supply faithful compact `content` for `keep` and `extract` groups.
- Leave `content` empty for `drop` groups.
- Put wording that must survive unchanged in `protected`.
- Do not infer approval from silence, continued automation, or a prior general
  authorization to work autonomously.
