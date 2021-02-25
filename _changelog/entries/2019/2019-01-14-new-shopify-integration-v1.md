---
title: "Shopify integration: New version (v1)"
content-type: "changelog-entry"
date: 2019-01-14
entry-type: new-feature
entry-category: integration
connection-id: shopify
connection-version: 1
---
{{ site.data.changelog.metadata.single-integration | flatify }}

A new version (v{{ this-connection.this-version }}) of our {{ this-connection.display_name }} integration is now available! 

We’ve worked hard to ensure this new integration is the best way to extract data from {{ this-connection.display_name }} to your Stitch destination. The new integration, based on the [Singer standard]({{ site.singer }}){:target="new"}, includes many new features such as:

- A few table changes and improvements:
  - The [collects]({{ this-connection.url | prepend: site.baseurl | prepend: site.home | append: "#collects" }}) and [order_refunds]({{ this-connection.url | prepend: site.baseurl | prepend: site.home | append: "#order_refunds" }}) tables now use [Key-based Incremental Replication]({{ site.data.urls.replication.key-based-incremental | prepend: site.baseurl | prepend: site.home }})
  - We've renamed `checkouts` to [abandoned_checkouts]({{ this-connection.url | prepend: site.baseurl | prepend: site.home | append: "#abandoned_checkouts" }}) to clarify the table's available data
  - Product and customer metadata is now available! Track the [products]({{ this-connection.url | prepend: site.baseurl | prepend: site.home | append: "#products" }}), [customers]({{ this-connection.url | prepend: site.baseurl | prepend: site.home | append: "#customers" }}), and [metafields]({{ this-connection.url | prepend: site.baseurl | prepend: site.home | append: "#metafields" }}) tables to replicate this data
- Optimized methods for retrieving {{ this-connection.display_name }} data
- Optimized use of {{ this-connection.display_name }} API quota for extraction
- User-facing [Extraction Logs]({{ site.data.urls.replication.extraction-logs | prepend: site.baseurl | prepend: site.home }})
- [Table and field selection]({{ site.data.urls.replication.syncing | prepend: site.baseurl | prepend: site.home }})
- Availability via the [Stitch Connect API]({{ site.data.urls.connect.overview | prepend: site.baseurl | prepend: site.home }})

Get started today by creating a new {{ this-connection.display_name }} integration or learn more in the [updated documentation]({{ this-connection.url | prepend: site.baseurl | prepend: site.home }}).