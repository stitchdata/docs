---
title: "LinkedIn Ads (v2): fix: raise error on inaccessible accounts and gracefully handle 404 during discovery"
content-type: "changelog-entry"
date: 2026-08-03
entry-type: bug-fix
entry-category: integration
connection-id: linkedin-ads
connection-version: 2
pull-request: "https://github.com/singer-io/tap-linkedin-ads/pull/88"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix: raise error on inaccessible accounts and gracefully handle 404 during discovery.