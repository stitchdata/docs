---
title: "Amazon Redshift (v2) destination: Fix boolean precision"
content-type: "changelog-entry"
date: 2016-08-23
entry-type: bug-fix
entry-category: destination
connection-id: redshift
connection-version: 2
---

{{ site.data.changelog.metadata.single-destination | flatify }}

This release ensures precision for boolean data types, specifically that false values are accurately displayed as `false` (instead of `null`) in {{ this-connection.display_name }}.