---
title: "Google Analytics (v1) update: Remove searchKeyword as default Behavior Overview field"
content-type: "changelog-entry"
date: 2020-04-22
entry-type: updated-feature
entry-category: integration
connection-id: "google-analytics" 
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-google-analytics/pull/20"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

As `searchKeyword` isn't data that {{ this-connection.display_name }} collects by default, we've removed it from the default fields selected for replication for the Behavior Overview report. This field will still be available in Stitch, just not selected by default.