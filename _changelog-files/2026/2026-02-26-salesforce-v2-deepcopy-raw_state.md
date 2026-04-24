---
title: "Salesforce (v2): Fix previous states being dropped between tap runs"
content-type: "changelog-entry"
date: 2026-02-26
entry-type: bug-fix
entry-category: integration
connection-id: salesforce
connection-version: 2
pull-request: "https://github.com/singer-io/tap-salesforce/pull/207"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix previous states being dropped between tap runs.