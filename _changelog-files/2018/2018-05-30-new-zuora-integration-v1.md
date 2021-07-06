---
title: "Zuora integration: New version (v1)"
content-type: "changelog-entry"
date: 2018-05-30
entry-type: new-feature
entry-category: integration
connection-id: zuora
connection-version: 1
---
{{ site.data.changelog.metadata.single-integration | flatify }}

A new version (v{{ this-connection.this-version }}) of our {{ this-connection.display_name }} integration is now available! 

We’ve worked hard to ensure this new integration is the best way to extract data from {{ this-connection.display_name }} to your Stitch destination. The new integration, based on the [Singer standard]({{ site.singer }}){:target="new"}, includes many new features such as:

- Removal of `zuora_` prefixes from table names
- Expanded table and field availability 
- Choice of {{ this-connection.display_name }} API, allowing you to choose the API that best fits your needs
- Replication of deleted records when using the AQuA API
- [Table and field selection]({{ site.data.urls.replication.syncing | prepend: site.baseurl | prepend: site.home }})
- Enhanced schema validation

Get started today by creating a new {{ this-connection.display_name }} integration or learn more in the [updated documentation]({{ this-connection.url | prepend: site.baseurl | prepend: site.home }}).