---
title: "Amazon DynamoDB (v1) bug fix: Fix error handling for incorrectly set-up log based streams"
content-type: "changelog-entry"
date: 2023-04-03
entry-type: bug-fix
entry-category: integration
connection-id: amazon-dynamodb
connection-version: 1
pull-request: "https://github.com/singer-io/tap-dynamodb/pull/50"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed an issue in the set up for log-based streams in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration.