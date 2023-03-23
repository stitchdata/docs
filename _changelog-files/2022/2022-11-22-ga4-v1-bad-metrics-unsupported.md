---
title: "Google Analytics 4 update: bad metrics marked unsupported"
content-type: "changelog-entry"
date: 2022-11-22
entry-type: updated-feature
entry-category: integration
connection-id: google-analytics-4
connection-version: 
pull-request: "https://github.com/singer-io/tap-ga4/pull/28"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to filter bad metric names so a connection can successfully complete a check. The bad metrics will be marked unsupported in field selection.