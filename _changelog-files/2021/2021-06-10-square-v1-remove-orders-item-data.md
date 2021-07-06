---
title: "Square (v1) update: item_data object removed from orders table"
content-type: "changelog-entry"
date: 2021-06-10
entry-type: removed
entry-category: integration
connection-id: "square"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-square/pull/104"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

The `item_data` object has been removed from {{ this-connection.display_name }}'s `orders` table. We removed this object due to it being undocumented by {{ this-connection.display_name }} and not being returned by {{ this-connection.display_name }}'s API.