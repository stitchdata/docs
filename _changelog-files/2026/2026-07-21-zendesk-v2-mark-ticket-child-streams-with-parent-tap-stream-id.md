---
title: "Zendesk Support (v2): mark ticket child streams with parent-tap-stream-id"
content-type: "changelog-entry"
date: 2026-07-21
entry-type: improvement
entry-category: integration
connection-id: zendesk
connection-version: 2
pull-request: "https://github.com/singer-io/tap-zendesk/pull/190"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to mark ticket child streams with parent-tap-stream-id.