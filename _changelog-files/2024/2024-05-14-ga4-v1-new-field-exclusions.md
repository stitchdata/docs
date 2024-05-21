---
title: "Google Analytics 4 (v1) update: New field exclusions"
content-type: "changelog-entry"
date: 2024-05-14
entry-type: updated-feature
entry-category: integration
connection-id: google-analytics-4
connection-version: 1
pull-request: "https://github.com/singer-io/tap-ga4/pull/104"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add new field exclusions to avoid the following error:

```
Error: 400 Cannot have filter_partition dimension without specifying filter-partitions in the request.
```