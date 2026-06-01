---
title: "Google Analytics 4 (v1): Handle 400 InvalidArgument during checkCompatibility"
content-type: "changelog-entry"
date: 2026-05-27
entry-type: improvement
entry-category: integration
connection-id: google-analytics-4
connection-version: 1
pull-request: "https://github.com/singer-io/tap-ga4/pull/126"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to handle 400 InvalidArgument during checkCompatibility.