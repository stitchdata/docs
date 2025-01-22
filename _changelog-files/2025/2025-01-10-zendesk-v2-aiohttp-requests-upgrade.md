---
title: "Zendesk Support (v2) update: aiohttp and requests library version upgrade"
content-type: "changelog-entry"
date: 2025-01-10
entry-type: improvement
entry-category: integration
connection-id: zendesk
connection-version: v2
pull-request: "https://github.com/singer-io/tap-zendesk/pull/157"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration by upgrading `aiohttp` version to 3.11.11 and requests library version to 2.32.3. 