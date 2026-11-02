# Review and release convention

1. Confirm origin, privacy, clean/dirty state and base commit. Preserve unrelated work.
2. Work on a task branch; stage only intended paths. Never force-push or use broad staging for this setup.
3. Run relevant source checks and meaningful behavioural checks. Record missing environments; syntax checks are not app acceptance.
4. Request independent review of the exact commit. Resolve findings and record evidence using docs/HANDOFF.md.
5. Ask Nacho before merging, deploying, installing, changing visibility/settings, or importing local/private data. Open a draft PR only within the authorised scope.
6. Merge only the reviewed revision with passing required checks and owner approval. Recheck after later changes.

These files describe a process; they do not enforce GitHub permissions or start agents. GitHub reported HTTP 403 for private-repository branch protection/rulesets on 2026-11-02, requesting an account upgrade. Keep sources private. Until enforcement is available, the owner must follow this manual gate; CI alone cannot prevent a direct push. If protection becomes available, require PRs, passing checks, resolved conversations, disallow force pushes/deletions, and minimise bypass. A sole owner cannot provide a second person's GitHub approval; AI comments do not satisfy that requirement.

Never give untrusted pull requests write tokens or secrets. Use pull_request rather than pull_request_target for source checks. Do not run installers, collectors, app builds or deployments as routine documentation checks.
