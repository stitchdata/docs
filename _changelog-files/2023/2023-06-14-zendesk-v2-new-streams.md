---
title: "Zendesk Support (v2) update: New streams"
content-type: "changelog-entry"
date: 2023-06-14
entry-type: new-feature
entry-category: integration
connection-id: zendesk
connection-version: 2
pull-request: "https://github.com/singer-io/tap-zendesk/pull/111"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add two new streams: `talk_phone_numbers` and `ticket_metrics_event`.