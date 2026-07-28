---
title: "GitHub (v2): Check for wrong credentials"
content-type: "changelog-entry"
date: 2025-09-23
entry-type: improvement
entry-category: integration
connection-id: github
connection-version: 2
pull-request: "https://github.com/singer-io/tap-github/pull/222"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to check for wrong credentials before checking for rate limit.