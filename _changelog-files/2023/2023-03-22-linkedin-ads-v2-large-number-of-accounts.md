---
title: "LinkedIn (v2): Allow processing of large number of accounts"
content-type: "changelog-entry"
date: 2023-03-22
entry-type: improvement
entry-category: integration
connection-id: linkedin-ads
connection-version: 2
pull-request: "https://github.com/singer-io/tap-linkedin-ads/pull/60"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to avoid errors when working with a large number of accounts.