---
title: Querying Append-Only Tables
permalink: /data-structure/querying-append-only-tables
tags: [destinations, bigquery_destination]
keywords: bigquery, google bigquery data warehouse, bigquery data warehouse, bigquery etl, etl to bigquery, append-only, append only, query append only
summary: "In this article, we'll cover how append-only replication works and how to account for it in your queries."
weight: 4.0
toc: true
destination: "BigQuery"
---
{% include misc/data-files.html %}

{% capture note %}
The querying strategy outline here can be applied to any table that is loaded in an <a href="#" data-toggle="tooltip" data-original-title="{{site.data.tooltips.append-only-rep}}">Append-Only</a> manner. This is applicable to **BigQuery** and **Amazon S3 (CSV) destinations**. {% endcapture %}

{% include note.html content=note %}

{{ site.data.tooltips.append-only-rep }}

For tables using Incremental Replication, Stitch currently loads data into Google BigQuery in an append-only fashion. This means that as time goes on, tables will wind up containing many different versions of the same row.

Data stored this way can provide insights and historical details about how those rows have changed over time - creating a timeline of the status changes of an order record, for example - but in some cases, you might just want the latest version of the table.

---

## Grab the Latest Version of Every Row {#latest-version-every-row}

In each Stitch-generated integration table, you'll see a few columns prepended with `{{ system-column.prefix }}`. The column we'll focus on here is the `{{ system-column.sequence }}` column. This column is a Unix epoch (down to the millisecond) attached to the record during replication and can help determine the order of all the versions of a row.

Stitch uses these sequence values in a few places to correctly order rows for loading, but it can be also used to grab the latest version of a record in an append-only table.

Let's take a look at an example. Assume we have an `orders` table that contains:

- A Primary Key of `id`,
- The system `{{ system-column.prefix }}` columns added by Stitch, and
- Other order attribute columns

If you wanted to create a snapshot of the latest version of this table, you could run a query like this:

{% highlight sql %}
SELECT DISTINCT o.*
FROM [stitch-analytics-bigquery-123:ecommerce.orders] o
INNER JOIN (
    SELECT
        MAX({{ system-column.sequence }}) AS seq,
        id
    FROM [stitch-analytics-bigquery-123:ecommerce.orders]
    GROUP BY id ) oo
ON o.id = oo.id
AND o.{{ system-column.sequence }} = oo.seq
{% endhighlight %}

This approach uses a subquery to get a single list of every row's Primary Key and maximum sequence number. Since it's possible to have duplicate records in your warehouse, the query also selects only distinct records of the latest version of the row. It then joins the original table to both the Primary Key and maximum sequence, which makes all other column values available for querying.

---

## Create Views in Your Data Warehouse

To make this easier, you can turn queries like the one above into a view. We recommend this approach because a view will encapsulate all the logic and simplify the process of querying against the latest version of your data.

For more info on creating views in the data warehouses Stitch supports, check out these docs:

- [Creating views in Amazon Redshift](http://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_VIEW.html)
- [Creating views in Google BigQuery](https://cloud.google.com/bigquery/querying-data#views)
- [Creating views in PostgreSQL](https://www.postgresql.org/docs/9.4/static/sql-createview.html)