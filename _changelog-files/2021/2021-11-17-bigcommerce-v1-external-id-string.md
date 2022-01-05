---
title: "BigCommerce (v1) update: External ID is now a string value"
content-type: "changelog-entry"
date: 2021-11-17
entry-type: updated-feature
entry-category: integration
connection-id: bigcommerce
connection-version: 1
pull-request: "https://github.com/singer-io/tap-bigcommerce/pull/13"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

`product.external_id` is now defined as a string in the BigCommerce v2 API documentation. We've updated this in our {{ this-connection.display_name }} integration.