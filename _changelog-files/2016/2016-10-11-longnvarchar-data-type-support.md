---
title: LONGNVARCHAR data type support
content-type: "changelog-entry"
date: 2016-10-11
entry-type: new-feature
entry-category: replication
---

Up until now, Stitch supported `VARCHAR`, `NVARCHAR`, and `LONGVARCHAR`. Today we’ve added support for the crazy uncle of the `VARCHAR` family, `LONGNVARCHAR`! 

Just a note: If you have existing database integrations that have this data type, you’ll need to go in and specifically track it. Any new integrations will automatically track this data type.