---
title: "Google Search COnsole (v0) bug fix: Handle no data exception for sitemaps stream"
content-type: "changelog-entry"
date: 2023-04-04
entry-type: bug-fix
entry-category: integration
connection-id: google-search-console
connection-version: 0
pull-request: "https://github.com/singer-io/tap-google-search-console/pull/38"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed an issue related to `sitemaps` streams with no data in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration.