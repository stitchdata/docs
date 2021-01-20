---
title: New version (v1) of  integration
# content-type: "changelog-entry"
date: 2020-10-28
entry-type: new-feature
entry-category: integration
connection-id: 
connection-version: 1
---
{{ site.data.changelog.metadata.single-integration | flatify }}

A new version (v{{ integration.this-version }}) of our {{ integration.display_name }} integration is now available! 

We’ve worked hard to ensure this new integration is the best way to extract data from {{ integration.display_name }} to your Stitch destination. The new integration, based on the [Singer standard]({{ site.singer }}){:target="new"}, includes many new features such as:

- Removal of `` prefixes from table names
- New tables, including:
  - []({{ integration.url | prepend: site.baseurl | append: "#" }})
- User-facing [Extraction Logs]({{ link.replication.extraction-logs | prepend: site.baseurl }})
- [Table and field selection]({{ link.replication.syncing | prepend: site.baseurl }})
- [Enhanced scheduling options]({{ link.replication.rep-scheduling | prepend: site.baseurl }})
- [Run and stop Extraction]({{ link.replication.start-stop-extraction | prepend: site.baseurl }}) on demand functionality
- Availability via the [Stitch Connect API]({{ link.connect.overview | prepend: site.baseurl }})
- Enhanced schema validation

Get started today by creating a new {{ integration.display_name }} integration or learn more in the [updated documentation]({{ integration.url | prepend: site.baseurl }}).