---
title: "Amazon DynamoDB (v1) update: Increased precision for decimals"
content-type: "changelog-entry"
date: 2021-11-02
entry-type: improvement
entry-category: integration
connection-id: amazon-dynamodb
connection-version: 1
pull-request: "https://github.com/singer-io/tap-dynamodb/pull/33"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to expand the decimal precision to match the max width of a `singer.decimal`.