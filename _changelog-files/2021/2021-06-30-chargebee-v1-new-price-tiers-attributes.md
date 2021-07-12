---
title: "Chargebee (v1) improvement: New fields in tables"
content-type: "changelog-entry"
date: 2021-06-30
entry-type: improvement
entry-category: "integration"
connection-id: "chargebee"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-chargebee/pull/53"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added new fields to the `events` and `addons` schema.

New to the `events` schema:
- `show_descriptions_in_invoices`
- `show_description_in_quotes`
- `object` subattribute within the `tiers` attribute

New to the `addons` schema:
- `show_descriptions_in_invoices`
- `show_description_in_quotes`
- `object` subattribute within the `price_in_decimal` attribute

