---
title: "Google Ads (v1) improvement: Implement Automatic Keys"
content-type: "changelog-entry"
date: 2022-05-09
entry-type: improvement
entry-category: integration
connection-id: google-ads
connection-version: 1
pull-request: "https://github.com/singer-io/tap-google-ads/pull/55"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We noticed dupilicate results being written for distinct reporting records across our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration reporting tables. This caused some overwritting on records that should not have been overwritten.

To fix this we've implemented automatic keys to ensure that data can be loaded and identified downstream as distinct records.
