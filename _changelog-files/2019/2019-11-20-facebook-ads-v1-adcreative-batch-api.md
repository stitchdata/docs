---
title: "Facebook Ads (v1) integrations: Use Batch API for adcreative table"
content-type: "changelog-entry"
date: 2019-11-20
entry-type: improvement
entry-category: integration
connection-id: "facebook-ads"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-facebook/pull/73"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated the `adcreative` table in the {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to use Facebook's [Batch API](https://developers.facebook.com/docs/marketing-api/catalog-batch){:target="new"}. This change was made to prevent errors resulting from requesting too much data.  