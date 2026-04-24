---
title: "Google Analytics (v1) integrations: Reduced retry aggressiveness"
content-type: "changelog-entry"
date: 2020-08-07
entry-type: improvement
entry-category: integration
connection-id: "google-analytics" 
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-google-analytics/pull/31"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved the retry logic for {{ this-connection.display_name }} to make retries less aggressive, ideally reduceing the consumption of daily API quotas.