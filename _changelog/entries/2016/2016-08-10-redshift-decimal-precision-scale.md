---
title: "Amazon Redshift (v2) destination: Increase decimal precision and scale"
content-type: "changelog-entry"
date: 2016-08-10
entry-type: bug-fix
entry-category: destination
connection-id: redshift
connection-version: 2
---

{{ site.data.changelog.metadata.single-destination | flatify }}

This release increases the precision and scale of decimal types in {{ this-connection.display_name }}, changing from the {{ this-connection.display_name }} default of `DECIMAL(18,0)` to `DECIMAL(38,6)`.