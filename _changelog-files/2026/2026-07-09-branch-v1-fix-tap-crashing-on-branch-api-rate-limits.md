---
title: "Branch (v1): Fix tap crashing on API rate limits"
content-type: "changelog-entry"
date: 2026-07-09
entry-type: bug-fix
entry-category: integration
connection-id: branch
connection-version: 1
pull-request: "https://github.com/singer-io/tap-branch/pull/7"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix tap crashing on API rate limits.