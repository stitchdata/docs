---
title: "Zendesk Support (v2) bug fixes: Rate limit and retry for 5xx errors"
content-type: "changelog-entry"
date: 2024-11-27
entry-type: bug-fix
entry-category: integration
connection-id: zendesk
connection-version: 2
pull-request: "https://github.com/singer-io/tap-zendesk/pull/155"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix rate limit error. We've also added more retries to avoid the 5xx errors.