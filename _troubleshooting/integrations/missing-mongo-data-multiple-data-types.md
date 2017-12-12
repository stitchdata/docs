---
title: Missing Mongo Data & Fields with Multiple Data Types
keywords: troubleshooting, integration, database integration, trouble, issue, help, mongo, mongodb, data discrepancy, data types
permalink: /troubleshooting/missing-mongo-data-multiple-data-types
tags: [data_discrepancy, database_integrations]

summary: "Missing some Mongo data? The root cause may be multiple data types in the Replication Key field and how Mongo sorts data based on data type."
toc: true
type: "discrepancy, database-integration, replication"
---

Missing some Mongo data in your data warehouse? [Due to how Mongo sorts data based on data type](https://docs.mongodb.com/manual/reference/bson-types/#comparison-sort-order), Stitch may be unable to correctly identify new and updated data. If you don’t see data that you’d expect to, the root cause may be multiple data types in the table’s Replication Key field.

---

## 

Here’s an example of multiple data types in the Replication Key field can cause data discrepancies:

1. You sync a table, using a field called `table_id` as the Replication Key. This field contains both `ObjectId` and `String` data types.
2. A historical sync of the table completes.
3. Because Mongo considers `ObjectId` data types to be greater than `Strings`, Stitch will record the `MAX` value as the last replicated record containing an `ObjectId` data type in the Replication Key field.
4. New records are added to the table.
5. During the next sync, Stitch uses the last recorded `MAX` value - in this case, an `ObjectId` - to identify new/updated data. **Remember: only records with Replication Key values greater than or equal to this value will be selected for replication.**
6. Because `ObjectIds > Strings`, all records with `Strings` are considered to be less than the last recorded `MAX` value. This means Stitch won’t be able to detect these records and replicate them to your data warehouse.

---

## Check for Multiple Data Types

To determine if a field has more than one data type, we recommend running the following queries. **We’re using Mongo version 3.0+, so keep in mind that these queries may be different for your version.**

Run this query to count how many of a single data type there are in the table’s Replication Key field, replacing:

- `nameOfCollection` with the table name,
- `replicationKeyField` with the field name, and
- `knownDataTypeId` with the Mongo BSON data type ID. You can find the data type IDs [here in Mongo’s docs](https://docs.mongodb.com/manual/reference/bson-types/#bson-types).

{% highlight sql %}
   db.nameOfCollection.count({replicationKeyField: {$type: knownDataTypeId}});
{% endhighlight %}

Next, run this query to get a count of **all** records in the table:

{% highlight sql %}
db.nameOfCollection.count();
{% endhighlight %}

Compare the results. If the counts are equal, then the Replication Key field contains only one data type.

Additionally, the following query will return the `MAX` value for the table’s Replication Key field. This can be helpful when comparing your source database to what’s in your data warehouse:

{% highlight sql %}
db.nameOfCollection.find().sort({replicationKeyField:-1}).limit(1);
{% endhighlight %}

---

## Next Steps

### If Collection Count ≠ Data Type Count
If the results of the data type and total record counts **aren’t** equal, multiple data types in the Replication Key field may be interfering with Stitch’s replication process. Resolving this issue may require a full re-sync of the problem table.

### If Collection Count = Data Type Count
If the results of the data type and total record counts queries **are** equal, then the root cause may not be multiple data types and further investigation is needed.

---

## Before Contacting Support
Before reaching out to support, we recommend using the Data Discrepancy Troubleshooting Guide to further investigate the problem if you haven’t already. Providing us with the information from the queries in this article as well as the guide will help us pinpoint the issue more quickly.