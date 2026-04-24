---
title: "GitLab (v1): Updated params to headers"
content-type: "changelog-entry"
date: 2025-10-29
entry-type: improvement
entry-category: integration
connection-id: gitlab
connection-version: 1
pull-request: "https://github.com/singer-io/tap-gitlab/pull/44"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to update `params` to `headers` to prevent errors.