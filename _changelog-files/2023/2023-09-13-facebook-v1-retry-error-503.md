---
title: "Facebook Ads (v1) update: Add retry logic for status code 503"
content-type: "changelog-entry"
date: 2023-09-13
entry-type: improvement
entry-category: integration
connection-id: facebook-ads
connection-version: 1
pull-request: "https://github.com/singer-io/tap-facebook/pull/226"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration by adding a retry logic system when an error with the HTTP status code 503 (Service Unavailable) occurs.