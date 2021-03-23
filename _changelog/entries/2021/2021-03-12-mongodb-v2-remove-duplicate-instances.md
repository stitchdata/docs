---
title: MongoDB (v2) improvement: Duplicate database instances removed
content-type: "changelog-entry"
date: 2021-03-12
entry-type: improvement
entry-category: "integration"
connection-id: "mongodb"
connection-version: "2"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

This improvement removes duplicate instances of databases from the list of discovered databases in the Stitch {{ this-connection.display_name }} inegration. 