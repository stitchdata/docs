---
title: "Google Ads update: New  labels table"
content-type: "changelog-entry"
date: 2022-04-25
entry-type: updated-feature
entry-category: integration
connection-id: google-ads
connection-version: 1
pull-request: "https://github.com/singer-io/tap-google-ads/pull/53"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added the `labels` table to our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration. Additionally, we've added the `campaign.labels` attribute to all reports that contain the `campaigns` resource.