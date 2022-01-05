---
title: "Adroll (v1) feature: Added lookback window"
content-type: "changelog-entry"
date: 2021-10-20
entry-type: new-feature
entry-category: integration
connection-id: stripe
connection-version: 1
pull-request: "https://github.com/singer-io/tap-adroll/pull/26"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added a lookback window to the `ad_reports` table in our {{ this-connection.display_name }} integration to account for attribution over time.