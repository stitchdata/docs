---
title: "Google BigQuery (v1) destination: Data type incompatibilities fix"
content-type: "changelog-entry"
date: 2017-04-26
entry-type: bug-fix
entry-category: destination
connection-id: bigquery
connection-version: 1
---

{{ site.data.changelog.metadata.single-destination | flatify }}

We've improved the way Stitch loads data into {{ this-connection.display_name }} destinations. This update, already in production, fixes data type incompatibilities that were preventing certain tables from loading data into {{ this-connection.display_name }} datasets.