---
title: "Facebook Ads (v1) integrations: API upgrade to v3.2"
content-type: "changelog-entry"
date: 2018-11-13
entry-type: updated-feature
entry-category: integration
connection-id: facebook-ads
connection-version: 1
---

{{ site.data.changelog.metadata.single-integration | flatify }}

We have updated the {{ this-connection.display_name }} integration to use the latest version of the Facebook Marketing API - [version 3.2](https://developers.facebook.com/docs/graph-api/changelog/version3.2#marketing-api){:target="new"}.

As part of this update, Facebook has [deprecated](https://developers.facebook.com/docs/graph-api/changelog/version3.2#marketing-api){:target="new"} many values for `cost_per_action_type` to simplify reporting and support reporting based on their new eight standard events. Additionally, the `total_action_value` field has been deprecated and removed from all `ads_insights` tables.