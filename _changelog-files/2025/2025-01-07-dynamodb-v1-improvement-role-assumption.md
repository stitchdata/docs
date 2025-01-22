---
title: "Amazon DynamoDB (v1) improvement: Security enhancement for role assumption"
content-type: "changelog-entry"
date: 2025-01-07
entry-type: improvement
entry-category: integration
connection-id: amazon-dynamodb
connection-version: v1
pull-request: "https://github.com/singer-io/tap-dynamodb/pull/59"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration by using a proxy AWS account for role assumption by using a two-step role assumption process.