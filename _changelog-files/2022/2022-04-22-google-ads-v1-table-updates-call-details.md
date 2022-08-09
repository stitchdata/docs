---
title: "Google Ads (v1) update: Table updates"
content-type: "changelog-entry"
date: 2022-04-22
entry-type: updated-feature
entry-category: integration
connection-id: google-ads
connection-version: 1
pull-request: "https://github.com/singer-io/tap-google-ads/pull/49"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated some of our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) tables:

- Removed `campaign_id` from `campaign_budgets`
- Added `call_details` tables