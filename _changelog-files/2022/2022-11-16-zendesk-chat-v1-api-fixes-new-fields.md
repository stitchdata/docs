---
title: "Zendesk Chat (v1) update: API fixes and new fields"
content-type: "changelog-entry"
date: 2022-11-16
entry-type: improvement
entry-category: integration
connection-id: zendesk-chat
connection-version: 1
pull-request: "https://github.com/singer-io/tap-zendesk-chat/pull/45"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration by adding fields in the `shortcuts` and `bans` streams and fixing some API issues.