---
title: "Shopify (v1) improvement: Improved data typing for abandoned checkouts"
content-type: "changelog-entry"
date: 2021-05-19
entry-type: improvement
entry-category: integration
connection-id: "shopify"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-shopify/pull/44"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Previously, some users were encountering JSON schema validation errors for the `abandoned_checkouts` table due to how some columns were being typed. This change types the following columns correctly, eliminating the validation errors:

- `note_attributes`
- `line_items.applied_discounts`
- `shipping_lines.applied_discounts`
- `shipping_lines.custom_tax_lines`

Check out the [pull request]({{ entry.pull-request }}){:target="new"} for more info.