---
title: "Amazon Aurora MySQL RDS integration: New version (v2) now in beta"
content-type: "changelog-entry"
date: 2022-01-14
entry-type: beta
entry-category: integration
connection-id: aurora-rds
connection-version: 2
---

{{ site.data.changelog.metadata.single-integration | flatify }}

{% assign all-aurora-rds = site.database-integrations | where:"key","aurora-rds-integration" %}
{% assign aurora-rds-overview = all-aurora-rds | where:"content-type","database-category" | first %}

A new version (v{{ this-connection.this-version }}) of our {{ this-connection.display_name }} integration is now in beta!

This version (v{{ this-connection.this-version }}) of Stitch's {{ this-connection.display_name }} integration optimizes replication by utilizing Avro schemas to write and validate data, thereby reducing the amount of time spent on data extraction and preparation. Compared to previous versions of the {{ this-connection.display_name }} integration, this version boasts increased performance and overall reduced replication time.

Notable improvements and changes in this version also include:

- **New column (field) naming rules.** Avro has specific rules that dictate how columns can be named. As a result, column names will be canonicalized to adhere to Avro rules and persisted to your destination using the Avro-friendly name. Refer to the [Column name transformations section]({{ this-connection.url | prepend: site.baseurl | prepend: site.home | append: "#data-replication--column-name-transformations" }}) in the {{ this-connection.display_name }} docs for more info.
- **Expanded data type support**. This version supports additional {{ this-connection.display_name }} data types. Refer to the [{{ this-connection.display_name }} data types documentation]({{ aurora-rds-overview.url | prepend: site.baseurl | prepend: site.home | append: "#data-types" }}) for more info.

**Note**: The following features aren't currently supported, but will be before the integration leaves beta:

- Custom SSL certificates and certificate authorities

To get a look at how this version compares to the previous version of {{ this-connection.display_name }}, refer to the [{{ this-connection.display_name }} version comparison documentation]({{ aurora-rds-overview.url | prepend: site.baseurl | prepend: site.home | append: "#supported-features" }}).
