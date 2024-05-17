---
title: "Intercom (v2) bug fix: Conversations stream bookmarking"
content-type: "changelog-entry"
date: 2024-05-08
entry-type: bug-fix
entry-category: integration
connection-id: intercom
connection-version: 2
pull-request: "https://github.com/singer-io/tap-intercom/pull/73"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix the following issue during the integration execution.

The `conversations` records have been updated after the previous synchronization start was missed. This issue has been fixed by bookmarking the last synchronization start time.

A long running synchronization was stuck in loop after interruption because the synchronization was resumed from the start. Nested filters have been added in `search_query` to resume the synchronization from the last processed conversations record.
