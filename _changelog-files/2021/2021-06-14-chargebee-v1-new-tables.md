---
title: "Chargebee (v1) update: New item tables for Chargebee Product Catalog v2!"
content-type: "changelog-entry"
date: 2021-06-14
entry-type: improvement
entry-category: "integration, documentation"
connection-id: "chargebee"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-chargebee/pull/42"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've made some big changes to how our {{ this-connection.display_name }} integration works, along with adding some new tables.

{{ integration.display_name }} (v{{ this-connection.this-version }}) integrations now use the Product Catalog version for the {{ integration.display_name }} site to determine which tables to display in Stitch. Some tables and fields are only available if your {{ integration.display_name }} site is using v1.0 of the Product Catalog, some only on v2.0. We've added a new section to the [{{ integration.display_name }} documentation]({{ this-connection.url | prepend: site.baseurl | prepend: site.home | append: "#product-catalog-versions" }}) that goes into more detail.

In addition to this change, we've added a few new tables which are available if using {{ integration.display_name }} Product Catalog v2.0:

- [items]({{ this-connection.url | prepend: site.baseurl | prepend: site.home | append: "#items" }})
- [item_families]({{ this-connection.url | prepend: site.baseurl | prepend: site.home | append: "#item_families" }})
- [item_prices]({{ this-connection.url | prepend: site.baseurl | prepend: site.home | append: "#item_prices" }})

**Note**: Stitch's {{ integration.display_name }} (v{{ this-connection.this-version }}) integration supports both Product Catalog v1.0 and v2.0. The version of the integration doesn't refer to support for a specific {{ integration.display_name }} Product Catalog version.