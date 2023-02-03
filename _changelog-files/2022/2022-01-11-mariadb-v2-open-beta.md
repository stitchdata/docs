---
title: "MariaDB integration: New version (v2) now in beta"
content-type: "changelog-entry"
date: 2022-01-11
entry-type: beta
entry-category: integration
connection-id: mariadb
connection-version: 2
---

{{ site.data.changelog.metadata.single-integration | flatify }}

{% assign all-mariadb = site.database-integrations | where:"key","mariadb-integration" %}
{% assign mariadb-overview = all-mariadb | where:"content-type","database-category" | first %}

A new version (v{{ this-connection.this-version }}) of our {{ this-connection.display_name }} integration is now in beta!

To get a look at how this version compares to the previous version of {{ this-connection.display_name }}, refer to the [{{ this-connection.display_name }} version comparison documentation]({{ mariadb-overview.url | prepend: site.baseurl | prepend: site.home | append: "#supported-features" }}).
