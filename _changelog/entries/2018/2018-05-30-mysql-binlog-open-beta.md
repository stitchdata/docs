---
title: "MySQL (v1) integrations: Binlog replication support"
content-type: "changelog-entry"
date: 2018-05-30
entry-type: new-feature
entry-category: replication
connection-id: mysql
connection-version: 1
---

{{ site.data.changelog.metadata.single-integration | flatify }}

{{ this-connection.display_name }} integrations can now use binlog replication to perform incremental replication in Stitch!

If you have binary logging enabled for your MySQL database, Stitch can now use it to help replicate your data. Log-based Incremental Replication allows for incremental replication of a table without a Replication Key and will capture and persist hard deletes.

This feature is now available as a Replication Method on the **Table Settings** of {{ this-connection.display_name }} integrations. Check out the [docs]({{ site.data.urls.replication.log-based-incremental | prepend: site.baseurl | prepend: site.home }}) for more info.