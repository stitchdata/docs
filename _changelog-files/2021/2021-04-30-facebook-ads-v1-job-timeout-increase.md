---
title: "Facebook Ads (v1) update: Increased replication job timeout"
content-type: "changelog-entry"
date: 2021-04-30
entry-type: updated-feature
entry-category: integration
connection-id: "facebook-ads"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-facebook/pull/148"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've increased the timeout from 120 seconds to 300 seconds for {{ this-connection.display_name }} `Ads Insights` replication jobs.