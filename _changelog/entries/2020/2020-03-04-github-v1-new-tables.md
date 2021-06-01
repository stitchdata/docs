---
title: "GitHub (v1) update: New tables!"
content-type: "changelog-entry"
date: 2020-03-04
entry-type: updated-feature
entry-category: integration
connection-id: "github"
connection-version: 1
pull-request: "https://github.com/singer-io/tap-github/pull/70"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

New tables have been added to our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration!

The following tables are now available for replication:

- `commit_comments`
- `commits`
- `events`
- `issue_labels`
- `issue_milestones`
- `project_cards`
- `project_columns`
- `projects`
- `pull_request_reviews`
- `team_members`
- `teams`