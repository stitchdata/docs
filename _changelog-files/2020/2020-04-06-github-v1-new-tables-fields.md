---
title: "GitHub (v1) update: Team memberships and new fields now available!"
content-type: "changelog-entry"
date: 2020-04-06
entry-type: updated-feature
entry-category: integration
connection-id: "github"
connection-version: 1
pull-request: "https://github.com/singer-io/tap-github/pull/75"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've made some updates to our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration, including some a new table and additional fields!

Here's a look at the changes:

- `team_memberships`: **New table**! Includes membership data for team members in repositories specified for the integration.
- `project_cards`: **New fields**: `_sdc_repository`, `cards_url`, `name`
- `issue_milestones`, `project_columns`, `team_members`: Added the `_sdc_repository` field
- `projects`, `pull_request_reviews`, `teams`: Minor data formatting changes