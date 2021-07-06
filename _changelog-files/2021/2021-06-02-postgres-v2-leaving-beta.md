---
title: "PostgreSQL (v2) update: Leaving beta!"
content-type: "changelog-entry"
date: 2021-06-02
entry-type: new-feature
entry-category: integration
connection-id: "postgres"
connection-version: "2"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

A new version (v{{ this-connection.this-version }}) of our {{ this-connection.display_name }} integration has left beta and is now generally available!

This version (v{{ this-connection.this-version }}) of Stitch's {{ this-connection.display_name }} integration optimizes replication by utilizing Avro schemas to write and validate data, thereby reducing the amount of time spent on data extraction and preparation. Compared to previous versions of the {{ this-connection.display_name }} integration, this version boasts increased performance and overall reduced replication time.

Notable improvements and changes in this version also include:

- **Expanded data type support**. This version supports additional {{ this-connection.display_name }} data types. Refer to the [{{ this-connection.display_name }} data types documentation]({{ postgres-overview.url | prepend: site.baseurl | append: "#data-types" }}) for more info.
- **Improved handling of `JSON`, `JSONB`, and `HSTORE` data types**. In previous versions, these data types were treated as strings. This version will send them to your destination as JSON objects, which may result in [de-nesting]({{ site.data.urls.destinations.storage.nested-structures | prepend: site.baseurl | prepend: site.home }}).
- **Improved handling of schema changes in tables using Log-based Incremental Replication.** Adding and removing columns in these tables will no longer cause extraction errors. **Note**: This limitation still applies to [version 1]({{ site.home | append: site.baseurl | append: site.data.urls.replication.log-based-incremental | append: "#limitation--structural-changes" }}).

**Note**: The following features aren't fully supported, but are being worked on:

- **Arrays of `DECIMAL`, `NUMERIC`, and `TIMESTAMP(TZ)` data types**
- **Support for other flavors of {{ this-connection.display_name }}**. We're in the process of testing this version of our integration with other flavors of {{ this-connection.display_name }}, including Heroku, Google CloudSQL, Amazon Aurora, and Amazon RDS.

To get a look at how this version compares to the previous version of {{ this-connection.display_name }}, refer to the [{{ this-connection.display_name }} version comparison documentation]({{ postgres-overview.url | prepend: site.baseurl | append: "#supported-features" }}).