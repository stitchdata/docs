---
title: "Google Ads (v1) update: Add request timeout to gas.search"
content-type: "changelog-entry"
date: 2022-06-30
entry-type: updated-feature
entry-category: integration
connection-id: google-ads
connection-version: 1
pull-request: "https://github.com/singer-io/tap-google-ads/pull/64"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add a request timeout option to the `search` request with a default value of 900 seconds.