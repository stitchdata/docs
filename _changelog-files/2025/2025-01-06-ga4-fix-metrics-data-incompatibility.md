---
title: "Google Analytics 4: Metrics and data incompatibility"
content-type: "changelog-entry"
date: 2025-01-06
entry-type: bug-fix
entry-category: integration
connection-id: google-analytics-4
connection-version: 1
pull-request: "https://github.com/singer-io/tap-ga4/pull/106"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix metrics and data incompatibility by  implementing `advertiserAdCostPerKeyEvent`.