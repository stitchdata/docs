---
title: "Google Analytics (v1) update: Improved parsing of datetimes"
content-type: "changelog-entry"
date: 2020-05-12
entry-type: bug-fix
entry-category: integration
connection-id: "google-analytics" 
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-google-analytics/pull/22"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Previously, fields in the `Time` group could cause errors during Extraction, as they were returned from Google's API using a non-ISO format.

These fields are now parsed as `datetime` and converted to ISO-8601 (UTC) during Extraction.