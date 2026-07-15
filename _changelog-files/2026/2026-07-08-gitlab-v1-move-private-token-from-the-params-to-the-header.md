---
title: "GitLab (v1): Move private token from the params to the header"
content-type: "changelog-entry"
date: 2026-07-08
entry-type: improvement
entry-category: integration
connection-id: gitlab
connection-version: 1
pull-request: "https://github.com/singer-io/tap-gitlab/pull/54"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to move private token from the params to the header.