---
title: "Facebook Ads (v1) bug fix: Unexpected data type for replication key"
content-type: "changelog-entry"
date: 2021-11-19
entry-type: bug-fix
entry-category: integration
connection-id: facebook-ads
connection-version: 1
pull-request: "https://github.com/singer-io/tap-facebook/pull/172"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

The `ads_insights_age_gender` and `ads_insights_hourly_advertiser` tables had unexpected data types in the replication key field, `date_start`. The {{ this-connection.display_name }} integration now formats those fields as `date-time`.