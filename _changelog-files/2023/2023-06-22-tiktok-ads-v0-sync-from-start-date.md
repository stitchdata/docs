---
title: "TikTok Ads (v0) bug fix: Sync records from start date"
content-type: "changelog-entry"
date: 2023-06-22
entry-type: bug-fix
entry-category: integration
connection-id: tiktok-ads
connection-version: 0
pull-request: "https://github.com/singer-io/tap-tiktok-ads/pull/22"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed an issue in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to ensure that Stitch uses the start date specified in the configuration when syncing records.