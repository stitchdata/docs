---
title: "Salesforce integration: New version (v1)"
content-type: "changelog-entry"
date: 2017-11-16
entry-type: new-feature
entry-category: integration
connection-id: salesforce
connection-version: 1
---

{{ site.data.changelog.metadata.single-integration | flatify }}

A new version (v{{ this-connection.this-version }}) of our {{ this-connection.display_name }} integration is now available! Major changes include:

- Choose between {{ this-connection.display_name }} Bulk or REST API
- Configure how much of your {{ this-connection.display_name }} API quota Stitch can use
- Connect to {{ this-connection.display_name }} Sandbox accounts
- Choose whether Stitch automatically replicates new fields
- Reset the [Replication Key]({{ site.data.urls.replication.rep-keys | prepend: site.baseurl }}) for individual {{ this-connection.display_name }} tables in Stitch
- Toggle between [Incremental]({{ site.data.urls.replication.key-based-incremental | prepend: site.baseurl }}) or [ull Table Replication]({{ site.data.urls.replication.full-table | prepend: site.baseurl }}) for tables
- Access the latest objects and fields from the newest version of the {{ this-connection.display_name }} API
- Removed `sf_` prefix for tables for all newly created integrations

Learn more about the integration and these features in our [{{ this-connection.display_name }} integration documentation]({{ this-connection.url | prepend: site.baseurl }}). 