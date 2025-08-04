---
title: "Chargify (v1) update: New component data!"
content-type: "changelog-entry"
date: 2021-06-01
entry-type: improvement
entry-category: integration
connection-id: chargify
connection-version: 1
pull-request: "https://github.com/singer-io/tap-chargify/pull/39"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

New fields have been added to the `components` table of our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration:

- `default_price_point_name`
- `product_family_name`
- `prices.id`
- `prices.component_id`
- `prices.starting_quantity`
- `prices.ending_quantity`
- `prices.unit_price`
- `prices.price_point_id`
- `prices.formatted_unit_price`

Learn more in [our documentation]({{ this-connection.url | prepend: site.baseurl | prepend: site.home }}).