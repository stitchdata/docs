---
title: "Facebook Ads (v1) update: Retry for job polling"
content-type: "changelog-entry"
date: 2021-11-02
entry-type: improvement
entry-category: integration
connection-id: "facebook-ads"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-facebook/pull/174"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to resolve race-condition errors. The integration will now retry when an error is encountered with `AdsInsights` job polling.