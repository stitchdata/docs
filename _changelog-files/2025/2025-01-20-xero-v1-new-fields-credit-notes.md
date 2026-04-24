---
title: "Xero (v1) update: New fields in the schema of credit_notes"
content-type: "changelog-entry"
date: 2025-01-20
entry-type: improvement
entry-category: integration
connection-id: xero
connection-version: 1
pull-request: "https://github.com/singer-io/tap-xero/pull/117"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add new fields to the `credit_notes` table:
- InvoiceAddresses
- Taxability
- TaxBreakdown
- SalesTaxCodeId