---
title: "Mixpanel integration: New version (v1)"
content-type: "changelog-entry"
date: 2020-10-28
entry-type: new-feature
entry-category: integration
connection-id: mixpanel
connection-version: 1
---
{{ site.data.changelog.metadata.single-integration | flatify }}

A new version (v{{ this-connection.this-version }}) of our {{ this-connection.display_name }} integration is now available! 

We’ve worked hard to ensure this new integration is the best way to extract data from {{ this-connection.display_name }} to your Stitch destination. The new integration, based on the [Singer standard]({{ site.singer }}){:target="new"}, includes many new features such as:

- Removal of `mixpanel_` prefixes on table names
- New tables, including:
	- [annotations]({{ this-connection.url | prepend: site.baseurl | prepend: site.home | append: "#annotations" }})
	- [cohort_members]({{ this-connection.url | prepend: site.baseurl | prepend: site.home | append: "#cohort_members" }})
	- [cohorts]({{ this-connection.url | prepend: site.baseurl | prepend: site.home | append: "#cohorts" }})
	- [revenue]({{ this-connection.url | prepend: site.baseurl | prepend: site.home | append: "#revenue" }})
- User-facing [Extraction Logs]({{ site.data.urls.replication.extraction-logs | prepend: site.baseurl | prepend: site.home }})
- Updated API secret authentication
- The `export` table now uses [Append-only loading behavior]({{ this-connection.url | prepend: site.baseurl | prepend: site.home | append: "#export-events-loading-behavior" }})
- [Configurable attribution windows]({{ this-connection.url | prepend: site.baseurl | prepend: site.home | append: "#attribution-windows-extraction" }}) for the `export`, `funnels`, and `revenue` tables
- [Table and field selection]({{ site.data.urls.replication.syncing | prepend: site.baseurl | prepend: site.home }})
- [Enhanced scheduling options]({{ site.data.urls.replication.rep-scheduling | prepend: site.baseurl | prepend: site.home }})
- [Run and stop Extraction]({{ site.data.urls.replication.start-stop-extraction | prepend: site.baseurl | prepend: site.home }}) on demand functionality
- Availability via the [Stitch Connect API]({{ site.data.urls.connect.overview | prepend: site.baseurl | prepend: site.home }})
- Enhanced schema validation

Get started today by creating a new {{ this-connection.display_name }} integration or learn more in the [updated documentation]({{ this-connection.url | prepend: site.baseurl | prepend: site.home }}).