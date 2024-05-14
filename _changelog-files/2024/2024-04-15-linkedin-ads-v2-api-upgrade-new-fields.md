---
title: "LinkedIn Ads (v2) update: API upgrade and new fields"
content-type: "changelog-entry"
date: 2024-04-15
entry-type: updated-feature
entry-category: integration
connection-id: linkedin-ads
connection-version: 2
pull-request: "https://github.com/singer-io/tap-linkedin-ads/pull/69"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated the {{ this-connection.display_name }} integration's API version from 2023-04 to 2024-03.

We've updated API endpoints for the following streams: `campaign_groups`, `campaigns`, `creatives`.

A cursor-based pagination has been implemented for the following streams: `accounts`, `campaign_groups`, `campaigns`, `creatives`.

Unsupported `pivot` and `pivotValue` have been removed from the `fields` query parameters in Analytics API requests.

New fields have been added to the `video_ads` stream. It now requires the scope `r_organization_social` to synchronize the records.
Data is not available for `change_audit_stamps` in the new endpoint.
