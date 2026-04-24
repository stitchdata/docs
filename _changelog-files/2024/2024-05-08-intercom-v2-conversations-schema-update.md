---
title: "Intercom (v2) bug fix: Conversations schema update"
content-type: "changelog-entry"
date: 2024-05-08
entry-type: bug-fix
entry-category: integration
connection-id: intercom
connection-version: 2
pull-request: "https://github.com/singer-io/tap-intercom/pull/71"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix the following error during the integration execution.

The `assignee` object was not getting populated as a response using the API version 2.5. The `conversations` schema has been updated.

