---
title: "ActiveCampaign (v1): Updated the bounce_logs schema"
content-type: "changelog-entry"
date: 2024-09-05
entry-type: updated-feature
entry-category: integration
connection-id: activecampaign
connection-version: 1
pull-request: "https://github.com/singer-io/tap-activecampaign/pull/42"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to allow the `code` field as `string`.