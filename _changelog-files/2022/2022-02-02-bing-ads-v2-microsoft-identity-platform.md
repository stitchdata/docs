---
title: "Microsoft Advertising (v2) update: Prefer Microsoft Identity Platform Authentication"
content-type: "changelog-entry"
date: 2022-02-02
entry-type: improvement
entry-category: integration
connection-id: bing-ads
connection-version: 2
pull-request: "https://github.com/singer-io/tap-bing-ads/pull/99"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

To modernize the methods of authentication for our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration, we've updated our feature detection to prefer Microsoft Identity Platform as the default.