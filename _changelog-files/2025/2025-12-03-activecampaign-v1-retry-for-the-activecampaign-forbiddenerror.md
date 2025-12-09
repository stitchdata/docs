---
title: "ActiveCampaign (v1): Add a retry for the ActiveCampaignForbiddenError"
content-type: "changelog-entry"
date: 2025-12-03
entry-type: improvement
entry-category: integration
connection-id: activecampaign
connection-version: 1
pull-request: "https://github.com/singer-io/tap-activecampaign/pull/52"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add a retry for the `ActiveCampaignForbiddenError`.