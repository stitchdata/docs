---
title: "Mambu (v2) bug fix: Duplicated record in the audit_trails stream"
content-type: "changelog-entry"
date: 2021-11-29
entry-type: bug-fix
entry-category: integration
connection-id: "mambu"
connection-version: "2"
pull-request: "https://github.com/singer-io/tap-mambu/pull/59"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add a `number_last_occurrence` value for bookmarks in the `audit_trails` stream. This solves the issue of duplicated records.