---
title: Amazon Redshift (v2) destination transaction optimization
content-type: "changelog-entry"
date: 2019-03-12
entry-type: improvement
entry-category: destination
connection-id: redshift
connection-version: 2
---

{{ site.data.changelog.metadata.single-destination | flatify }}

We have split DDL statements like `ALTER table` commands into their own transaction in [{{ this-connection.display_name }} destinations]({{ this-connection.url | prepend: site.baseurl }}) to minimize the length of time that tables are locked.