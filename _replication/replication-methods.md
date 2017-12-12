---
title: Replication Methods
permalink: /replication/replication-methods
keywords: replicate, replication, replication method, stitch replicates data
tags: [replication]
category: "settings"

summary: "Replication Methods tell Stitch how to replicate data during a replication job. In this guide, we'll explain the methods Stitch uses, how they work for database and SaaS integrations, and how to define Replication Methods for your database integration tables."
type: "settings"
toc: true
weight: 2
---
{% include misc/data-files.html %}

Replication Methods define **how** Stitch will replicate your data during a replication job. While SaaS integration tables have their Replication Methods defined by Stitch, **you can define how tables in database integrations are replicated.**

Replication Methods are extremely important - we can't stress this enough. They'll not only directly impact your row count, but incorrectly defined methods can also cause data discrepancies.

---

## Replication Method Types

Stitch employs two methods to replicate data from your data sources: Incremental and Full Table.

### Incremental Replication

Incremental Replication means that **Stitch will only replicate new or updated data on every replication attempt**. As this method will greatly reduce latency and data usage, we highly recommend using it where ever possible.

To identify new and updated data for replication, Stitch uses what is called a **Replication Key**. 

#### Replication Keys

When Stitch replicates your data, it will store the last recorded maximum value in the Replication Key column and compare it against the data source - **not what's in your data warehouse** - to identify new/updated data. 

Any row with a Replication Key value greater than or equal to the stored value is where Stitch will begin the next replication attempt.

{% capture replication-key %}
**Incorrectly setting Replication Keys can cause data discrepancies and row count issues**, so we strongly recommend checking out the [Selecting Replication Keys guide]({{ link.replication.rep-keys | prepend: site.baseurl }}) before you define the Replication Methods and Keys for your tables.<br><br>

**If you're working with a MongoDB integration,** note that Replication Keys work a little differently. Refer to the [Selecting Mongo Replication Keys guide]({{ link.replication.mongo-rep-keys | prepend: site.baseurl }}) for more info.
{% endcapture %}

{% include important.html content=replication-key %}

#### Updated At Incremental Replication

The `updated_at` method of Incremental Replication uses a `timestamp` or `datetime` column (set as the Replication Key) that's updated whenever information in a row is changed. Stitch will compare the last recorded MAX value in this column with what's in the data source to identify new and updated data for replication.

This method works for tables that will both add new rows and update existing ones.

For example: the Replication Key for the `customers` table below is the `updated_at` column.

During the initial sync, the following rows are replicated:

{% highlight markdown %}
| id [PK] | name        | age | updated_at          |
|---------+-------------+-----+---------------------|
| 1       | Finn        | 14  | 2017-01-01 14:34:23 |
| 2       | Jake        | 6   | 2017-01-01 14:34:23 |
| 3       | Beamo       | 1   | 2017-01-01 14:34:23 |
| 4       | Bubblegum   | 16  | 2016-12-31 02:45:53 |
{% endhighlight %}

When the sync completes, Stitch will store the MAX value in the `updated_at` column (`2017-01-01 14:34:23`) to identify data for replication.

**After** the completion of the initial sync but **before** the next sync starts, these changes are made in the data source:

{% highlight markdown %}
| id [PK] | name        | age | updated_at          |
|---------+-------------+-----+---------------------|
| 1       | Finn        | 15  | 2017-01-02 15:00:18 |   // age is changed in existing row
| 2       | Jake        | 6   | 2017-01-01 14:34:23 |
| 3       | Beamo       | 1   | 2017-01-01 14:34:23 |
| 4       | Bubblegum   | 16  | 2016-12-31 02:45:53 |
| 5       | King        | 300 | 2017-01-02 15:10:42 |   // new row is added
{% endhighlight %}

When the next sync begins, Stitch will compare the stored `updated_at` value of `2017-01-01 14:34:23` against what's in the data source to select rows to replicate. Anything **greater than or equal to** this value will be selected.

During the next sync, the following rows are replicated:

{% highlight markdown %}
| id [PK] | name  | age | updated_at          |
|---------+-------+-----+---------------------|
| 1       | Finn  | 15  | 2017-01-02 15:00:18 |
| 2       | Jake  | 6   | 2017-01-01 14:34:23 |
| 3       | Beamo | 1   | 2017-01-01 14:34:23 |
| 5       | King  | 300 | 2017-01-02 15:10:42 |
{% endhighlight %}

Instead of replicating the entire table again, only the rows with Replication Key values that were **greater than or equal to** the last value saved by Stitch were replicated. Notice that the record for `Bubblegum` (`4`) was not selected for replication because of its Replication Key value.

While there may be a small amount of duplication when using this method (it's to ensure Stitch doesn't miss any data), it's the most efficient way to use Stitch.

#### Append-Only Incremental Replication

Append-Only Replication is when only new data is added, or appended, to a table. Existing rows are never updated. If a value is changed in an existing record, a new row with the new data will be appended to the end of the table. 

This means that there can be many different rows in a table with the same Primary Key, each representing what that record was at that moment in time. Stitch provides the `{{ system-column.sequence }}` column to help distinguish the age of the records.

{% include replication/append-only-replication-example.html %}

#### Deleted Records & Incremental Replication

Depending on how records are deleted (hard vs. soft), deletes may not be captured when your data is replicated.

##### Hard Deletes

Stitch is unable to capture hard deletes because it looks for values that are greater than or equal to the recorded value in the Replication Key column. If a record is hard deleted, there won't be a value to compare against and the delete won't be detected.

##### Soft Deletes

Soft deletes occur when a record remains in the table but uses a flag to indicate deletion. In some cases this is a boolean column. In others this may be a timestamp or datetime column called `deleted_at` which in turn updates the `updated_at` value, thus allowing Stitch to identify the change.

---  

### Full Table Replication

Full Table Replication means that **Stitch will replicate the entire contents of a table on every replication attempt**. As this Replication Method can cause latency and quickly use up your monthly row limit, it's the most inefficient way to use Stitch.

We recommend using Incremental Replication if the table in question contains any timestamped or datetime columns.

**Note that Stitch does not currently support Full Table Replication for Mongo integrations.**

---

## Define Replication Methods for Database Integration Tables

**Note that Replication Methods can only be defined for tables in database integrations.**

After you set a table to sync, you'll be prompted to select a Replication Method in the Table Settings window.

1. Click the Replication Method you want the table to use.
2. **If using Incremental Replication**, you'll also need to select a Replication Key. Select the appropriate column from the drop-down.
3. When finished, click the **Update Settings** button.

To change these settings, click into the table and then click the **Table Settings** link.

---

## Learn about SaaS Integration Replication Methods

As previously mentioned, Replication Methods can currently only be defined for tables in database integrations.

To learn more about the Replication Methods used by SaaS integration tables, refer to the **Schema** section in the [SaaS integration docs]({{ site.baseurl }}/integrations/saas).
