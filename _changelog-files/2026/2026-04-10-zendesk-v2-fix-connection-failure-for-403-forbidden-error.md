---
title: "Zendesk Support (v2): Fix connection failure for 403 Forbidden error"
content-type: "changelog-entry"
date: 2026-04-10
entry-type: bug-fix
entry-category: integration
connection-id: zendesk
connection-version: 2
pull-request: "https://github.com/singer-io/tap-zendesk/pull/185"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix connection failure for 403 Forbidden error.