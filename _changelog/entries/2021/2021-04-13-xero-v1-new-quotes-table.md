---
title: "Xero (v1) update: New table!"
content-type: "changelog-entry"
date: 2021-04-13
entry-type: updated-feature
entry-category: integration
connection-id: xero
connection-version: 1
pull-request: "https://github.com/singer-io/tap-xero/pull/86"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

A new table has been added to our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration!

The following table is now available for replication:

- `quotes`

Learn more in [our documentation]({{ this-connection.url | prepend: site.baseurl }})