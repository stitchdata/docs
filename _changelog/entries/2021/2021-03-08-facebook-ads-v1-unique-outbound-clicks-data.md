---
title: "Facebook Ads (v1) integrations: New ads_insights.unique_outbound_clicks data"
content-type: "changelog-entry"
date: 2021-03-08
entry-type: updated-feature
entry-category: integration
connection-id: "facebook-ads"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-facebook/pull/138"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added the `unique_outbound_clicks` field to each of the `ads_insights_*` tables in the {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration.