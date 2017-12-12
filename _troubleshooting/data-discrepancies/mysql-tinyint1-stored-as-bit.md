---
title: MySQL TINYINT(1)/boolean Columns Stored as BIT
keywords: troubleshooting, integration, database integration, trouble, issue, help, mysql
permalink: /troubleshooting/mysql-tinyint1-stored-as-bit
tags: [data_discrepancy, database_integrations]

summary: "If you've noticed that some MySQL `TINYINT(1)` columns are displaying as `BIT` in Stitch, it's usually due to how the MySQL driver converts this data type."
type: "discrepancy, database-integration, replication"
---

In MySQL, `TINYINT(1)` and boolean are synonymous. Because of this, the MySQL driver implicitly converts the `TINYINT(1)` fields to boolean if the the Java `tinyInt1isBit` configuration property is set to `true` (which is the default) and the storage size is 1. Stitch then interprets these columns as `BIT(1)/boolean`.

For more info, refer to [MySQL's Java and MySQL Types documentation](https://dev.mysql.com/doc/connector-j/5.1/en/connector-j-reference-type-conversions.html).

To work around this, you have a few options:

- In the source, you can change the data type for the affected column to something that isn't synonymous with boolean, such as `TINYINT(4)`.
- If you'd prefer not to change the data type, you can create a view on top of the table and then define the data type for the affected column in that view to be `TINYINT(4)` or the data type you choose. The view can then be set up to be replicated through Stitch.