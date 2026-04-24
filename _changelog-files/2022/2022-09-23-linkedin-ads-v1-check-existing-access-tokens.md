---
title: "LinkedIn Ads (v1) update: Check existing access tokens"
content-type: "changelog-entry"
date: 2022-09-23
entry-type: improvement
entry-category: integration
connection-id: linkedin-ads
connection-version: 1
pull-request: "https://github.com/singer-io/tap-linkedin-ads/pull/50"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to avoid generating a new access token when a valid one already exists. The integration now checks the expiration date of an existing token and uses it if it is valid, instead of creating a new one.