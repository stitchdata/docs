---
title: Supported Data Types
permalink: /replication/supported-data-types
keywords: supported datatypes data types datatype
tags: [replication]
sidebar: stitchnav

summary: "A full roll-up of the data types Stitch supports for replication."
type: "syncing"
toc: true
weight: 5
---
{% include misc/data-files.html %}

As of {{ stitch.last-updated }}, Stitch supports replicating the data types listed in the table below. 

If a data type is not present in the table, it means that Stitch does not currently support replication for that data type. [Syncing columns with unsupported data types may lead to issues with replication](#sync-unsupported-data-types).

{% include stitch/supported-data-types.html %}

---

## Columns with Mixed Data Types {#mixed-data-types}

Occasionally Stitch will encounter a column that contains more than one data type. As Stitch requires that there be only one data type per column to properly type and store your data, columns containing multiple data types may be "split" to ensure all values are correctly typed.

For example: an `order_confirmed` column is synced and typed as `BOOLEAN`. In a subsequent sync, Stitch detects `VARCHAR` values in this column.

As a result, Stitch will create an additional column to accommodate the `VARCHAR` values. The new column name will be the original name appended with the data type: `order_confirmed__string`

How columns are named depends on the type of destination being used to warehouse data. Refer to the [Mixed Data Types guide for more info]({{ link.destinations.storage.column-splitting | prepend: site.baseurl }}).

---

## Syncing Unsupported Data Types {#sync-unsupported-data-types}

Columns containing data types that aren't supported may prevent an entire table from replicating. 

If you determine a non-replicating column contains an unsupported data type, you'll need to unsync it to allow the table to successfully replicate.

---

## 'Not Supported' Status for Columns

If a column you want to sync has a Status of `Not Supported`, the root cause may be an [unsupported data type or insufficient user permissions]({{ link.troubleshooting.unsupported-data-types | prepend: site.baseurl }}).