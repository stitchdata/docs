---
title: "MongoDB integration: New version (v1)"
content-type: "changelog-entry"
date: 2019-11-04
entry-type: new-feature
entry-category: integration
connection-id: mongodb
connection-version: 1
---
{{ site.data.changelog.metadata.single-integration | flatify }}

A new version (v{{ this-connection.this-version }}) of our {{ this-connection.display_name }} integration is now available! 

We’ve worked hard to ensure this new integration is the best way to extract data from {{ this-connection.display_name }} to your Stitch destination. The new integration, based on the [Singer standard]({{ site.singer }}){:target="new"}, includes many new features such as:

- User-facing [Extraction Logs]({{ site.data.urls.replication.extraction-logs | prepend: site.baseurl | prepend: site.home }})
- Field selection/exclusion using [Projection Queries]({{ site.data.urls.integrations.mongodb-projection-queries | prepend: site.baseurl | prepend: site.home }})
- Support for [logical replication via OpLog]({{ site.data.urls.replication.log-based-incremental | prepend: site.baseurl | prepend: site.home }}) and [Full Table Replication]({{ site.data.urls.replication.full-table | prepend: site.baseurl | prepend: site.home }})
- [Enhanced scheduling options]({{ site.data.urls.replication.rep-scheduling | prepend: site.baseurl | prepend: site.home }})
- [Run and stop Extraction]({{ site.data.urls.replication.start-stop-extraction | prepend: site.baseurl | prepend: site.home }}) on demand functionality
- Availability via the [Stitch Connect API]({{ site.data.urls.connect.overview | prepend: site.baseurl | prepend: site.home }})

Get started today by creating a new {{ this-connection.display_name }} integration or learn more in the [updated documentation]({{ this-connection.url | prepend: site.baseurl | prepend: site.home }}).