---
title: "Harvest Forecast (v1) bug fix: Correct sync_endpoints method"
content-type: "changelog-entry"
date: 2021-06-08
entry-type: bug-fix
entry-category: integration
connection-id: "harvest-forecast"
connection-version: 1
pull-request: "https://github.com/singer-io/tap-harvest-forecast/pull/21"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

This update fixes an issue in {{ this-connection.display_name }} integrations where data replication would fail due to incorrectly ordered objects in the integration's code. Additionally, this change also removes duplicate items from the integration's output.