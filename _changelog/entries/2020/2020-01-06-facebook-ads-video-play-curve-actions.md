---
title: "Facebook Ads (v1) integrations: New ads_insights.video_play_curve_actions data"
content-type: "changelog-entry"
date: 2020-01-06
entry-type: updated-feature
entry-category: integration
connection-id: "facebook-ads"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-facebook/pull/80"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added the `video_play_curve_actions` field to each of the `ads_insights_*` tables in the {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration.