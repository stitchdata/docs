---
title: "Zoom (v1) update: Updated data for report_meetings and report_webinars tables"
content-type: "changelog-entry"
date: 2021-03-15
entry-type: improvement
entry-category: "integration"
connection-id: "zoom"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-zoom/pull/4"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

We've made a few updates to the {{ this-connection.display_name }} `report_meetings` and `report_webinars` tables

1. The `dept` attribute in both tables now correctly returns an `integer` instead of a `string`
2. We've added the `host_id` and `user_id` fields to the `report_webinars` table
