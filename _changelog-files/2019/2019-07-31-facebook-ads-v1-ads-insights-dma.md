---
title: "Facebook Ads (v1) integrations: New ads_insights data"
content-type: "changelog-entry"
date: 2019-07-31
entry-type: updated-feature
entry-category: integration
connection-id: "facebook-ads"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-facebook/pull/64"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added a new table to our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration: `ads_insights_dma`

This table contains entries for each campaign/set/ad combination for each day, along with detailed statistics, segmented by DMA (Designated Market Area).

Learn more in [our documentation]({{ this-connection.url | prepend: site.baseurl | append: "#ads-insights-dma" }}).