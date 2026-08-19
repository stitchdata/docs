# DDR-001: DITA Variables Skill Scope and Repository Location

**Date Detected:** 2026-06-29
**Detected by:** AI agent (skill bootstrap and migration)
**Status:** Approved

## Decision Summary

| Decision | Value |
|---|---|
| Skill scope | DITA variables means only `<keyword conref>` references to `common/taxonomy/metadata-variables.dita` |
| Explicitly out of scope | Ditamap keydef/keyref and reuse-topic conref patterns |
| Canonical location | `docs-core/.github/skills/dita-variables/` |
| Portability policy | Skill content uses repo-relative paths in guidance text |
| Local orchestrator compatibility | Local `INDEX.yaml` may reference the repo skill via absolute path on each machine |

## Context

The initial draft of the skill included additional DITA mechanisms (keydef/keyref and reuse-topic conref).
Team clarification narrowed the meaning of "DITA variables" to taxonomy variables from
`metadata-variables.dita` only.

In addition, the skill needed to be committed in `docs-core` and `docs-components` so other users can consume it.

## Rationale

1. Team vocabulary consistency: keeping "DITA variables" tied to one source of truth avoids ambiguity.
2. Governance clarity: a focused scope makes validation and onboarding simpler for AI agents.
3. Collaboration: placing the skill in the repository enables shared review, versioning, and reuse.

## Actions Taken

1. Moved canonical skill files into `docs-core/.github/skills/dita-variables/`.
2. Updated skill text to use relative repo paths in examples and gate instructions.
3. Added Draft-doc agent instruction to invoke `dita-variables` for DITA docs-core or docs-components work.
4. Repointed local `INDEX.yaml` to the repo-hosted skill paths.

## Impact Assessment

**Scope:** AI agent behavior for DITA drafting/review in docs-core.

**Affected areas:**
- `.github/agents/Draft-doc.agent.md`
- `.github/skills/dita-variables/`
- local orchestrator index (`C:\Users\ychen\.copilot\skills\INDEX.yaml`)

## Follow-Up

- Future decisions in this folder should be contentful DDR files
- Any future scope expansion (for example, including keyref) requires a new DDR that supersedes this one.
