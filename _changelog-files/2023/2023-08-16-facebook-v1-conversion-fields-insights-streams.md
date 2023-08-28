---
title: "Facebook Ads (v1): Add conversions to insights streams"
content-type: "changelog-entry"
date: 2023-08-16
entry-type: updated-feature
entry-category: integration
connection-id: facebook-ads
connection-version: 1
pull-request: "https://github.com/singer-io/tap-facebook/pull/204"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add the `conversions` and `conversion_values` fields to insights streams.