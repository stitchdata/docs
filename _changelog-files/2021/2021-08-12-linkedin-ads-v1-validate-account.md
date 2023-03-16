---
title: "LinkedIn Ads (v1) update: Check account numbers"
content-type: "changelog-entry"
date: 2021-08-12
entry-type: improvement
entry-category: integration
connection-id: linkedin-ads
connection-version: 1
pull-request: "https://github.com/singer-io/tap-linkedin-ads/pull/35"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration by adding a step that checks the `account_number` in discovery mode and returns an error if the account number is invalid.