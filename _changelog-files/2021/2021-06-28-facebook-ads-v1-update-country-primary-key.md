---
title: "Facebook Ads (v1) update: Fixed composite primary key"
content-type: "changelog-entry"
date: 2021-06-28
entry-type: updated-feature
entry-category: integration
connection-id: "facebook-ads"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-facebook/pull/154"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've completed the `ads_insights_country` composite primary key to now include `country`. The composite primary key is now: `campaign_id", "adset_id", "ad_id", "date_start", "country"`.