---
title: "Freshdesk (v2): Reduce SSRF risk"
content-type: "changelog-entry"
date: 2026-10-26
entry-type: improvement
entry-category: integration
connection-id: freshdesk
connection-version: 2
pull-request: "https://github.com/singer-io/tap-freshdesk/pull/73"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to reduce SSRF risk.