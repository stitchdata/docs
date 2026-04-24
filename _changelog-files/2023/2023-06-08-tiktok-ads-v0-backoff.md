---
title: "TikTok Ads (v0) bug fix: Backoff for errors"
content-type: "changelog-entry"
date: 2023-06-08
entry-type: bug-fix
entry-category: integration
connection-id: tiktok-ads
connection-version: 0
pull-request: "https://github.com/singer-io/tap-tiktok-ads/pull/21"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed an issue in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration by adding a backoff in case an error with one of the following codes occurs: `40200`, `40201`, `40202`, `40700`, and `50002`.
