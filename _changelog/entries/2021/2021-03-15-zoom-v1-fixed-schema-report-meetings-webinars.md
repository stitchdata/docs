---
title: "Zoom (v1) update: Updated data for `report_meetings` and `report_webinars` tables"
content-type: "changelog-entry"
date: 2021-03-15
entry-type: updated-feature
entry-category: "integration"
connection-id: "zoom"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-zoom/pull/4"
---

{{ site.data.changelog.metadata.single-integration | flatify }}


1. The `dept` attribute was returning a `string` value instead of an `integer`. The update corrects that attribute for the `report_meetings` and `report_webinars` tables. 

2. The following fields were added to the `report_webinars` table: `host_id`, `user_id`.