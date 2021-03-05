---
title: PostgreSQL integration: New version (v2) now in beta
content-type: "changelog-entry"
date: 2021-03-05
entry-type: beta
entry-category: integration
connection-id: postgres
connection-version: 2
---

{{ site.data.changelog.metadata.single-integration | flatify }}

{% assign all-postgres = site.database-integrations | where:"key","postgres-integration" %}
{% assign postgres-overview = all-postgres | where:"content-type","database-category" | first %}

A new version (v{{ this-connection.this-version }}) of our {{ this-connection.display_name }} integration is now in beta!

This version (v{{ this-connection.this-version }}) of Stitch's {{ this-connection.display_name }} integration optimizes replication by utilizing Avro schemas to write and validate data, thereby reducing the amount of time spent on data extraction and preparation. Compared to previous versions of the {{ this-connection.display_name }} integration, this version boasts increased performance and overall reduced replication time.

Notable improvements and changes in this version also include:

- **New column (field) naming rules.** Avro has specific rules that dictate how columns can be named. As a result, column names will be canonicalized to adhere to Avro rules and persisted to your destination using the Avro-friendly name. Refer to the [Column name transformations section](#data-replication--column-name-transformations) in the {{ this-connection.display_name }} docs for more info.
- **Expanded data type support**. This version supports additional {{ this-connection.display_name }} data types. Refer to the [{{ this-connection.display_name }} data types documentation]({{ postgres-overview.url | prepend: site.baseurl | append: "#data-types" }}) for more info.
- **Improved handling of `JSON`, `JSONB`, and `HSTORE` data types**. In previous versions, these data types were treated as strings. This version will send them to your destination as JSON objects, which may result in [de-nesting]({{ link.destinations.storage.nested-structures | prepend: site.baseurl }}).

**Note**: The following features aren't currently supported, but will be before the integration leaves beta:

- Key-based Incremental Replication
- `ARRAY` data type

To get a look at how this version compares to the previous version of {{ this-connection.display_name }}, refer to the [{{ this-connection.display_name }} version comparison documentation]({{ postgres-overview.url | prepend: site.baseurl | append: "#supported-features" }}).

Learn more about the integration and these features in our [{{ this-connection.display_name }} integration documentation]({{ this-connection.url | prepend: site.baseurl }}). 
