# Agent handoff

Record one handoff per task in docs/handoffs/<date>-<topic>.md. Keep private paths, media metadata, credentials and client details out of shared/public notes.

- Task and acceptance criteria:
- Repository, base commit, branch and final reviewed commit:
- Owner and current status: planned / implementing / ready for review / changes requested / blocked / accepted
- Files changed and reason:
- Validation commands, actual results, skips and limitations:
- Independent reviewer findings, severity, file/line and disposition:
- Remaining risks and exact next action:
- User approvals needed and evidence of approvals received:

The builder hands the exact commit and diff to a separate review session. The reviewer checks correctness, data safety and test relevance; the builder addresses actionable findings and requests re-review. Stop after two unresolved review rounds or any missing access/approval. A second AI is advisory, not owner approval. Never call your own implementation independently reviewed. No background loop is enabled by this convention.
