---
title: "Salesforce (v2) bug fix: Pk chunking condition fix"
content-type: "changelog-entry"
date: 2024-03-12
entry-type: bug-fix
entry-category: integration
connection-id: tap-salesforce
connection-version: 2
pull-request: "https://github.com/singer-io/tap-salesforce/pull/176"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix the following error during the integration execution:

```
CRITICAL One or more batches failed during PK chunked job.
```
