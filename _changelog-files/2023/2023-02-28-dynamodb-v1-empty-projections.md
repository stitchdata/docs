---
title: "Amazon DynamoDB (v1) update: Handle empty projections"
content-type: "changelog-entry"
date: 2023-02-28
entry-type: bug-fix
entry-category: integration
connection-id: amazon-dynamodb
connection-version: 1
pull-request: "https://github.com/singer-io/tap-dynamodb/pull/49"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to properly handle empty projections.