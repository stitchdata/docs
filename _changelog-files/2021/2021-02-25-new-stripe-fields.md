---
title: "Stripe (v1) update: New fields!"
content-type: "changelog-entry"
date: 2021-02-25
entry-type: updated-feature
entry-category: integration
connection-id: stripe
connection-version: 1
full-connection-version: "1.4.5"
pull-request: "https://github.com/singer-io/tap-stripe/pull/77"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

New fields have been added to our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration!

The following tables now have additional fields available for replication:

- [`charges`]({{ this-connection.url | prepend: site.baseurl | append: "#charges"}})
- [`customers`]({{ this-connection.url | prepend: site.baseurl | append: "#customers"}})
- [`invoice_items`]({{ this-connection.url | prepend: site.baseurl | append: "#invoice-items"}})
- [`invoice_line_items`]({{ this-connection.url | prepend: site.baseurl | append: "#invoice-line-items"}})
- [`invoices`]({{ this-connection.url | prepend: site.baseurl | append: "#invoices"}})
- [`payouts`]({{ this-connection.url | prepend: site.baseurl | append: "#"}})
- [`subscription_items`]({{ this-connection.url | prepend: site.baseurl | append: "#subscription-items"}})
- [`subscriptions`]({{ this-connection.url | prepend: site.baseurl | append: "#subscriptions"}})

Learn more in [our documentation]({{ this-connection.url | prepend: site.baseurl }}).