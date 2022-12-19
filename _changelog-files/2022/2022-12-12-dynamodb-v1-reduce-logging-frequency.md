---
title: "Amazon DynamoDB (v1) update: Reduce logging frequency"
content-type: "changelog-entry"
date: 2022-12-12
entry-type: improvement
entry-category: integration
connection-id: amazon-dynamodb
connection-version: 1
pull-request: "https://github.com/singer-io/tap-dynamodb/pull/48"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to reduce the amount of logs produced during replication by logging only at the start of a full-table scan.