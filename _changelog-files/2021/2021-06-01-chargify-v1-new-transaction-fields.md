---
title: "Chargify (v1) update: New transaction data!"
content-type: "changelog-entry"
date: 2021-06-01
entry-type: updated-feature
entry-category: integration
connection-id: chargify
connection-version: 1
pull-request: "https://github.com/singer-io/tap-chargify/pull/39"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

New fields have been added to the `transactions` table of our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration:

- `period_range_start`
- `period_range_end`
- `price_point_id`
- `price_point_handle`
- `component_handle`
- `component_price_point_id`
- `component_price_point_handle`

Learn more in [our documentation]({{ this-connection.url | prepend: site.baseurl | prepend: site.home }}).