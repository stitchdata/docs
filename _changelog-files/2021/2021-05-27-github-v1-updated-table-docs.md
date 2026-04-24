---
title: "GitHub (v1) update: New table documentation now available"
content-type: "changelog-entry"
date: 2021-05-27
entry-type: improvement
entry-category: "integration, documentation"
connection-id: "github"
connection-version: 1
pull-request: "https://github.com/stitchdata/docs/pull/646"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated the {{ this-connection.display_name }} (v{{ this-connection.this-version }}) docs with info about the following tables:

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
- `team_memberships`
- `teams`

Check out the [updated docs]({{ site.home | append: site.baseurl | append: this-connection.url | append: "#schema" }}) for more info.