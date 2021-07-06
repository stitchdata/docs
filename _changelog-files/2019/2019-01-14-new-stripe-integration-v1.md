---
title: "Stripe integration: New version (v1)"
content-type: "changelog-entry"
date: 2019-01-14
entry-type: new-feature
entry-category: integration
connection-id: stripe
connection-version: 1
---
{{ site.data.changelog.metadata.single-integration | flatify }}

A new version (v{{ this-connectionthis-connection.this-version }}) of our {{ this-connection.display_name }} integration is now available! 

We’ve worked hard to ensure this new integration is the best way to extract data from {{ this-connection.display_name }} to your Stitch destination. The new integration, based on the [Singer standard]({{ site.singer }}){:target="new"}, includes many new features such as:

- Removal of `stripe_` prefixes from table names
- New and improved tables, including:
  - [invoice_line_items]({{ this-connection.url | prepend: site.baseurl | prepend: site.home | append: "#invoice_line_items" }})
  - [subscription_items]({{ this-connection.url | prepend: site.baseurl | prepend: site.home | append: "#subscription_items" }})
  - [subscription_line_items]({{ this-connection.url | prepend: site.baseurl | prepend: site.home | append: "#subscription_line_items" }})
  - The `transfer_transactions` table has been replaced by [payouts]({{ this-connection.url | prepend: site.baseurl | prepend: site.home | append: "#payouts" }})
- User-facing [Extraction Logs]({{ site.data.urls.replication.extraction-logs | prepend: site.baseurl | prepend: site.home }})
- [Table and field selection]({{ site.data.urls.replication.syncing | prepend: site.baseurl | prepend: site.home }})
- Availability via the [Stitch Connect API]({{ site.data.urls.connect.overview | prepend: site.baseurl | prepend: site.home }})

Get started today by creating a new {{ this-connection.display_name }} integration or learn more in the [updated documentation]({{ this-connection.url | prepend: site.baseurl | prepend: site.home }}).