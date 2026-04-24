---
title: "Zendesk (v1) update: Retry for 5xx errors"
content-type: "changelog-entry"
date: 2021-11-30
entry-type: improvement
entry-category: integration
connection-id: zendesk
connection-version: 1
pull-request: "https://github.com/singer-io/tap-zendesk/pull/93"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved how our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration handles errors by adding a retry mechanism to all `5xx` errors.