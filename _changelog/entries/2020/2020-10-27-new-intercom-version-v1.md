---
title: "Intercom integration: New version (v1)"
content-type: "changelog-entry"
date: 2020-10-27
entry-type: new-feature
entry-category: integration
connection-id: "intercom"
connection-version: 1
---
{{ site.data.changelog.metadata.single-integration | flatify }}

A new version (v{{ this-connection.this-version }}) of our {{ this-connection.display_name }} integration is now available! 

We’ve worked hard to ensure this new integration is the best way to extract data from {{ this-connection.display_name }} to your Stitch destination. The new integration, based on the [Singer standard]({{ site.singer }}){:target="new"}, includes many new features such as:

- Use of Intercom API version 2.0
- Updated OAuth flow for easier authentication
- New tables, including:
  - [contacts]({{ this-connection.url | prepend: site.baseurl | append: "#contacts" }}) (formerly (`users`)
  - [contact_attributes]({{ this-connection.url | prepend: site.baseurl | append: "#contact_attributes" }})
  - [company_attributes]({{ this-connection.url | prepend: site.baseurl | append: "#company_attributes" }})
  - [teams]({{ this-connection.url | prepend: site.baseurl | append: "#teams" }})
- Additional field support for the [conversations]({{ this-connection.url | prepend: site.baseurl | append: "#conversations" }}) table, including:
  - `conversation_ratings`
  - `sla_applied`
  - `statistics`
- Enhanced extraction approaches for the `contacts` and `companies` tables
- User-facing [Extraction Logs]({{ site.data.urls.replication.extraction-logs | prepend: site.baseurl }})
- [Table and field selection]({{ site.data.urls.replication.syncing | prepend: site.baseurl }})
- [Enhanced scheduling options]({{ site.data.urls.replication.rep-scheduling | prepend: site.baseurl }})
- [Run and stop Extraction]({{ site.data.urls.replication.start-stop-extraction | prepend: site.baseurl }}) on demand functionality
- Availability via the [Stitch Connect API]({{ site.data.urls.connect.overview | prepend: site.baseurl }})
- Enhanced schema validation

Get started today by creating a new {{ this-connection.display_name }} integration or learn more in the [updated documentation]({{ this-connection.url | prepend: site.baseurl }}).