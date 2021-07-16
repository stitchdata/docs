---
title: "Chargebee (v1) update: New fields!"
content-type: "changelog-entry"
date: 2021-06-30
entry-type: updated-feature
entry-category: "integration"
connection-id: "chargebee"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-chargebee/pull/53"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added new fields to the `events` and `addons` tables.

New to the `events` table:
- `show_descriptions_in_invoices`
- `show_description_in_quotes`
- `object` subattribute within the `tiers` attribute

New to the `addons` table:
- `show_descriptions_in_invoices`
- `show_description_in_quotes`
- `object` subattribute within the `price_in_decimal` attribute

