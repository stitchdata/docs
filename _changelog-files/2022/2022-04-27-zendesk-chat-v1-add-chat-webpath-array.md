---
title: "Zendesk Chat (v1) update: New table"
content-type: "changelog-entry"
date: 2022-04-27
entry-type: updated-feature
entry-category: integration
connection-id: zendesk-chat
connection-version: 1
pull-request: "https://github.com/singer-io/tap-zendesk-chat/pull/41"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added the `chat_webpath_array` table to our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to validate the `array` type attributes in our tables. 