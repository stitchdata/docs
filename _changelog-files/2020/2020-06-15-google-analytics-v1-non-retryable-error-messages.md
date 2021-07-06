---
title: "Google Analytics (v1) integrations: Non-retryable error messages now in Extraction Logs"
content-type: "changelog-entry"
date: 2020-06-15
entry-type: improvement
entry-category: integration
connection-id: "google-analytics" 
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-google-analytics/pull/29"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Error messages from HTTP `4xx` codes that aren't retryable will now include details from {{ this-connection.display_name }} detailing what the issue is. Previously, these messages weren't included in Extraction Logs, leading to confusion about the issue causing the error.