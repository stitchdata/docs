---
title: "Google Ads (v1) update: Add limit clause to core table queries"
content-type: "changelog-entry"
date: 2022-07-05
entry-type: updated-feature
entry-category: integration
connection-id: google-ads
connection-version: 1
pull-request: "https://github.com/singer-io/tap-google-ads/pull/68"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added support for configurable page limits for all core tables except: `call_details`, `campaign_labels`, `ad_group_criterion`, and `campaign_criterion`.