---
title: "Mambu (v2) update: Changes in the gl_journal_entries stream"
content-type: "changelog-entry"
date: 2021-11-03
entry-type: improvement
entry-category: integration
connection-id: "mambu"
connection-version: "2"
pull-request: "https://github.com/singer-io/tap-mambu/pull/56"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to change the `replication_keys` and `bookmark_field` for the `gl_journal_entries` stream from `booking_date` to `creation_date`.

This change solves the issue where journal entries were missing when transactions were reversed.