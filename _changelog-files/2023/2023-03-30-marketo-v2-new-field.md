---
title: "Marketo (v2): New field available"
content-type: "changelog-entry"
date: 2023-03-30
entry-type: improvement
entry-category: integration
connection-id: marketo
connection-version: 2
pull-request: "https://github.com/singer-io/tap-marketo/pull/82"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

The `campaignId` field is now available for the `activities` stream in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration.