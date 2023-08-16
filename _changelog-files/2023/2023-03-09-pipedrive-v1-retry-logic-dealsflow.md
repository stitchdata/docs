---
title: "Pipedrive (v1) improvement: Improved retry logic for null requests for DealsFlow stream"
content-type: "changelog-entry"
date: 2023-03-09
entry-type: improvement
entry-category: integration
connection-id: pipedrive
connection-version: 1
pull-request: "https://github.com/singer-io/tap-pipedrive/pull/131"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added retry logic to the {{ this-connection.display_name }} (v{{ this-connection.this-version }}) `dealsflow` stream. This allows the integration to automatically retry API requests when it returns a status of 200 but a null body.