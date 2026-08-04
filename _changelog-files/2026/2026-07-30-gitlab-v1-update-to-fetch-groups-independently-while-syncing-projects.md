---
title: "GitLab (v1): Update to fetch groups independently while syncing projects"
content-type: "changelog-entry"
date: 2026-07-30
entry-type: improvement
entry-category: integration
connection-id: gitlab
connection-version: 1
pull-request: "https://github.com/singer-io/tap-gitlab/pull/55"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to update to fetch groups independently while syncing projects.