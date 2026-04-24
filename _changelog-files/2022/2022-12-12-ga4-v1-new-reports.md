---
title: "Google Analytics 4 (v1): new reports"
content-type: "changelog-entry"
date: 2022-12-12
entry-type: new-feature
entry-category: integration
connection-id: google-analytics-4
connection-version: 1
pull-request: "https://github.com/singer-io/tap-ga4/pull/31"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added two new premade reports with dimension filters to our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration: `conversions_report` and `in_app_purchases`.