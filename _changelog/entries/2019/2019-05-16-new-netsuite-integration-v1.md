---
title: "NetSuite integration: New version (v1)"
content-type: "changelog-entry"
date: 2019-05-16
entry-type: new-feature
entry-category: integration
connection-id: netsuite
connection-version: 1
---
{{ site.data.changelog.metadata.single-integration | flatify }}

A new version (v{{ this-connection.this-version }}) of our {{ this-connection.display_name }} integration is now available! 

We’ve worked hard to ensure this new integration is the best way to extract data from {{ this-connection.display_name }} to your Stitch destination. The new integration, based on the [Singer standard]({{ site.singer }}){:target="new"}, includes many new features such as:

- Removal of `netsuite_` prefixes from table names
- {{ integration.display_name }} token based authentication
- Optimizations to API concurrency during discovery of tables/fields
- Utilization of an updated {{ integration.display_name }} WSDL for a more complete set of tables/fields
- [Field selection]({{ site.data.urls.replication.syncing | prepend: site.baseurl }})

Get started today by creating a new {{ this-connection.display_name }} integration or learn more in the [updated documentation]({{ this-connection.url | prepend: site.baseurl }}).