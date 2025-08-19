---
title: "Shopify (v3): Improve query size and more"
content-type: "changelog-entry"
date: 2025-05-26
entry-type: improvement
entry-category: integration
connection-id: shopify
connection-version: 3
pull-request: "https://github.com/singer-io/tap-shopify/pull/214"
---
{ site.data.changelog.metadata.single-integration | flatify }

We've improved our { this-connection.display_name } (v{ this-connection.this-version }) integration to reduce query size and API response payload, to avoid Shopify errors and more improvemens such as including a GraphQL query in the logs for particular stream.