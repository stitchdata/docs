---
title: "Facebook Ads (v1) integrations: Field deprecation"
content-type: "changelog-entry"
date: 2018-07-26
entry-type: deprecation
entry-category: integration
connection-id: facebook-ads
connection-version: 1
---
{{ site.data.changelog.metadata.single-integration | flatify }}

[Facebook has deprecated the following fields](https://developers.facebook.com/docs/graph-api/changelog/breaking-changes#feb2018){:target="new"}, meaning they are no longer available for selection or retrieval via Facebook's API:

- `call_to_action_clicks`
- `cost_per_total_action`
- `social_reach`
- `social_impressions`
- `social_clicks`
- `unique_social_clicks`
- `today_spend`
- `total_actions`
- `total_unique_actions`

In addition, several types of metrics have been deprecated. **Note**: The fields are still available, but the types listed below are not:

- `actions` field: `mention`, `tab_view`
- `action_values` field: `app_custom_event`
- `cost_per_action_type` field: `mention`, `tab_view`
- `canvas_avg_view_percentage_per_component` field: `canvas_view`