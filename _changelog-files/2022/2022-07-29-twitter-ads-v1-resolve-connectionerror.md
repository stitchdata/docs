---
title: "Twitter Ads (v1) bug fix: Resolve ConnectionError"
content-type: "changelog-entry"
date: 2022-07-29
entry-type: bug-fix
entry-category: integration
connection-id: twitter-ads
connection-version: 1
pull-request: "https://github.com/singer-io/tap-twitter-ads/pull/32"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed a bug in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration causing an error when replicating streams with a large number of records, such as the `targeting_conversations` and `targeting_location` streams.