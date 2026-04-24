---
title: "Pendo (v1) bug fix: Set maximum record limit"
content-type: "changelog-entry"
date: 2023-08-02
entry-type: bug-fix
entry-category: integration
connection-id: pendo
connection-version: 1
pull-request: "https://github.com/singer-io/tap-pendo/pull/126"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed an issue in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration by resetting the record limit in case of a race condition.