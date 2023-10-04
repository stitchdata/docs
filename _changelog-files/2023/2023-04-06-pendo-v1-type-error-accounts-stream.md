---
title: "Pendo (v1) bug fix: Type error in the accounts stream"
content-type: "changelog-entry"
date: 2023-04-06
entry-type: bug-fix
entry-category: integration
connection-id: pendo
connection-version: 1
pull-request: "https://github.com/singer-io/tap-pendo/pull/122"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed an issue related to replication keys in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration.