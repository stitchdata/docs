---
title: "Google BigQuery (v1) destinations: NUMERIC data type support"
content-type: "changelog-entry"
date: 2018-12-04
entry-type: updated-feature
entry-category: destination
connection-id: bigquery
connection-version: 1
---

{{ site.data.changelog.metadata.single-destination | flatify }}

We've added support for the [NUMERIC](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric-type){:target="new"} data type in {{ this-connection.display_name }} destinations. Numeric data will be loaded into `NUMERIC` columns going forward, rather than columns with the floating point data type.