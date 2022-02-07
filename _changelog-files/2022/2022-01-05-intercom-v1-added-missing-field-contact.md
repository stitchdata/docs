---
title: "Intercom (v1) bug fix: Added missing fields in the contact stream"
content-type: "changelog-entry"
date: 2022-01-05
entry-type: bug-fix
entry-category: integration
connection-id: intercom
connection-version: 1
pull-request: "https://github.com/singer-io/tap-intercom/pull/43"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed a bug in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration causing missing fields in the `contacts` stream.