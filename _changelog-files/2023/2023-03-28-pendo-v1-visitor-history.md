---
title: "Pendo (v1) bug fix: Visitor history issue"
content-type: "changelog-entry"
date: 2023-03-28
entry-type: bug-fix
entry-category: integration
connection-id: pendo
connection-version: 1
pull-request: "https://github.com/singer-io/tap-pendo/pull/119"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed an issue with the `visitor_history` stream in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration. Records older than the bookmark are no longer synchronized.