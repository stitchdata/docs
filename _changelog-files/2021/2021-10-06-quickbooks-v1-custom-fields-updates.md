---
title: "Quickbooks (v1) update: Custom fields"
content-type: "changelog-entry"
date: 2021-10-06
entry-type: updated-feature
entry-category: integration
connection-id: quickbooks
connection-version: 1
pull-request: "https://github.com/singer-io/tap-quickbooks/pull/45"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our custom fields table in the {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration for the following supported tables:

- `credit_memos`
- `estimates`
- `invoices`
- `purchase_orders`
- `refund_receipts`
- `sales_receipts`


