---
title: "Marketo integration: New version (v2)"
content-type: "changelog-entry"
date: 2018-06-26
entry-type: new-feature
entry-category: integration
connection-id: marketo
connection-version: 2
---

{{ site.data.changelog.metadata.single-integration | flatify }}

A new version (v{{ this-connection.this-version }}) of our {{ this-connection.display_name }} integration is now available! Major changes include:

- **Activity selection** – Each {{ this-connection.display_name }} activity type is now its own table, allowing you to replicate just the ones you care about the most.
- **Replication of campaigns and programs** – These objects are now available for replication to your destination.
- **Column selection** – Just as with tables, we’ll only replicate the columns that you want.
- **Improved efficiency** – The integration now uses {{ this-connection.display_name }} Bulk API, which allows us to more efficiently replicate large amounts of data. [Review our documentation](https://www.stitchdata.com/docs/integrations/saas/marketo#activities-leads-replication) for more details.

Learn more about the integration and these features in our [{{ this-connection.display_name }} integration documentation]({{ this-connection.url | prepend: site.baseurl | prepend: site.home }}). 