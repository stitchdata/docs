---
title: "Snapchat Ads (v1) bug fix: Datetime conversion issue "
content-type: "changelog-entry"
date: 2023-11-15
entry-type: bug-fix
entry-category: integration
connection-id: snapchat-ads
connection-version: 1
pull-request: "https://github.com/singer-io/tap-snapchat-ads/pull/28"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix issues related to Daylight Savings Time when converting a datetime to midnight in the local time.