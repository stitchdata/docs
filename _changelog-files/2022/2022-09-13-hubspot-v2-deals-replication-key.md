---
title: "HubSpot (v2) update: Replication key automatically included"
content-type: "changelog-entry"
date: 2022-09-13
entry-type: updated-feature
entry-category: integration
connection-id: hubspot
connection-version: 2
pull-request: "https://github.com/singer-io/tap-hubspot/pull/195"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated the `deals` table of our {{ this-connection.display_name }} integration by changing its replication method to `INCREMENTAL` and updating the replication key to `property_hs_lastmodifieddate`.