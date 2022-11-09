---
title: "Github (v1) update: Fix team_members stream primary key"
content-type: "changelog-entry"
date: 2022-02-23
entry-type: updated-feature
entry-category: integration
connection-id: github
connection-version: 1
pull-request: "https://github.com/singer-io/tap-github/pull/157"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated the `team_members` stream's primary keys to: `id`, `team_slug`.