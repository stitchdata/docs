---
title: "ActiveCampaign (v1): New field"
content-type: "changelog-entry"
date: 2023-03-21
entry-type: updated-feature
entry-category: integration
connection-id: activecampaign
connection-version: 1
pull-request: "https://github.com/singer-io/tap-activecampaign/pull/26"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add a `phone` field in he `contacts` stream.