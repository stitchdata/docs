---
title: "Google Analytics (v1) update: Improved handling of retryable errors"
content-type: "changelog-entry"
date: 2020-05-21
entry-type: improvement
entry-category: integration
connection-id: "google-analytics" 
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-google-analytics/pull/24"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated the retry logic for our {{ this-connection.display_name }} integration to include HTTP codes `403` and `429`. In the event that Stitch receives these responses from {{ this-connection.display_name }}, the integration will exponentially back off and retry.