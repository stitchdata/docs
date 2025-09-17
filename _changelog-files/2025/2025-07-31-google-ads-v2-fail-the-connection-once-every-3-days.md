---
title: "Google Ads (v2): Implement connection failure once every 3 days"
content-type: "changelog-entry"
date: 2025-07-31
entry-type: improvement
entry-category: integration
connection-id: google-ads
connection-version: 2
pull-request: "https://github.com/singer-io/tap-google-ads/pull/100"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to implement a connection failure once every 3 days to inform that the version is deprecated.