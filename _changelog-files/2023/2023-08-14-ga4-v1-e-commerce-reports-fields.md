---
title: "Google Analytics 4 (v1) bug fix: Field updates for e-commerce reports"
content-type: "changelog-entry"
date: 2023-08-14
entry-type: bug-fix
entry-category: integration
connection-id: google-analytics-4
connection-version: 1
pull-request: "https://github.com/singer-io/tap-ga4/pull/71"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed broken e-commerce reports in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration by updating incompatible fields.