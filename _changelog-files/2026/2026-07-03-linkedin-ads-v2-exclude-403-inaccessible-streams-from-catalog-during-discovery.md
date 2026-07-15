---
title: "LinkedIn Ads (v2): Exclude 403-inaccessible streams from catalog during discovery"
content-type: "changelog-entry"
date: 2026-07-03
entry-type: improvement
entry-category: integration
connection-id: linkedin-ads
connection-version: 2
pull-request: "https://github.com/singer-io/tap-linkedin-ads/pull/86"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to exclude 403-inaccessible streams from catalog during discovery.