---
title: "Recharge (v2) update: Cleanup customer table"
content-type: "changelog-entry"
date: 2022-09-26
entry-type: updated-feature
entry-category: integration
connection-id: recharge
connection-version: 2
pull-request: "https://github.com/singer-io/tap-recharge/pull/39"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've removed the `shopify_customer_id` field which was removed by {{ this-connection.display_name }} in favor of the `external_customer_id` object.