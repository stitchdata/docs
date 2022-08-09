---
title: "Yotpo (v1) update: Products table endpoint changes"
content-type: "changelog-entry"
date: 2022-06-25
entry-type: updated-feature
entry-category: integration
connection-id: yotpo
connection-version: 1
pull-request: "https://github.com/singer-io/tap-yotpo/pull/33"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

{{ this-connection.display_name }} recently change the endpoint for the `products` schema and the `category` attribute has been deprecated. Since it cannot be deleted, we've updated our `category.name` and `category.id` attributes to accept `null` values.