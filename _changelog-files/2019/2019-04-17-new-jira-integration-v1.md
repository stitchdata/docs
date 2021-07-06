---
title: "JIRA integration: New version (v1)"
content-type: "changelog-entry"
date: 2019-04-17
entry-type: new-feature
entry-category: integration
connection-id: jira
connection-version: 1
---
{{ site.data.changelog.metadata.single-integration | flatify }}

A new version (v{{ this-connection.this-version }}) of our {{ this-connection.display_name }} integration is now available! 

We’ve worked hard to ensure this new integration is the best way to extract data from {{ this-connection.display_name }} to your Stitch destination. The new integration, based on the [Singer standard]({{ site.singer }}){:target="new"}, includes many new features such as:

- Removal of `jira_` prefixes from table names
- New tables, including:
  - [issues]({{ this-connection.url | prepend: site.baseurl | prepend: site.home | append: "#issues" }}), [changelog]({{ this-connection.url | prepend: site.baseurl | prepend: site.home | append: "#changelog" }}), and [transitions]({{ this-connection.url | prepend: site.baseurl | prepend: site.home | append: "#transitions" }}) are now top-level tables
  - [roles]({{ this-connection.url | prepend: site.baseurl | prepend: site.home | append: "#worklogs" }}) (formerly `jira_project_roles`)
  - [worklogs]({{ this-connection.url | prepend: site.baseurl | prepend: site.home | append: "#worklogs" }})
- {{ this-connection.display_name }} Cloud accounts now use an API token instead of user/password authentication
- User-facing [Extraction Logs]({{ site.data.urls.replication.extraction-logs | prepend: site.baseurl | prepend: site.home }})
- [Table and field selection]({{ site.data.urls.replication.syncing | prepend: site.baseurl | prepend: site.home }})
- [Run and stop Extraction]({{ site.data.urls.replication.start-stop-extraction | prepend: site.baseurl | prepend: site.home }}) on demand functionality
- Enhanced schema validation

Get started today by creating a new {{ this-connection.display_name }} integration or learn more in the [updated documentation]({{ this-connection.url | prepend: site.baseurl | prepend: site.home }}).