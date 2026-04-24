---
title: "ReCharge (v1) update: New rate limit handling"
content-type: "changelog-entry"
date: 2021-06-03
entry-type: improvement
entry-category: integration
connection-id: recharge
connection-version: 1
pull-request: "https://github.com/singer-io/tap-recharge/pull/8"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated how our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration makes requests to the {{ this-connection.display_name }} API to ensure Stitch doesn't exceed {{ this-connection.display_name }}'s rate limit.