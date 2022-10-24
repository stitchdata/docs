---
title: "Pipedrive (v1) update: Handle new structure for users stream"
content-type: "changelog-entry"
date: 2022-08-09
entry-type: improvement
entry-category: integration
connection-id: pipedrive
connection-version: 1
pull-request: "https://github.com/singer-io/tap-pipedrive/pull/119"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to support a structure change in the Users API. Stitch now accepts both single elements and JSON objects in the response.