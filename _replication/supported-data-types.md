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

The data types Stitch supports for replication fall into two categories:

- **Common**, which are data types supported for all integrations
- **Integration-specific**, which are data types supported for specific integrations and integration versions, where applicable. **Note**: Common data types also apply to integrations that support integration-specific data types.

**Note**: If a data type isn't present in either the Common or Integration-specific tables, it means that Stitch doesn't currently support replication for that data type. [Replicating columns with unsupported data types may lead to issues with replication](#sync-unsupported-data-types).

{% include replication/templates/data-types/data-type-formatting.html formatting="tabs" integration_name="postgres" display_name="PostgreSQL" %}

---

## Columns with mixed data types {#mixed-data-types}

Occasionally Stitch will encounter a column that contains more than one data type. As Stitch requires that there be only one data type per column to properly type and store your data, columns containing multiple data types may be "split" to ensure all values are correctly typed.

For example: an `order_confirmed` column is synced and typed as `BOOLEAN`. In a subsequent sync, Stitch detects `VARCHAR` values in this column.

As a result, Stitch will create an additional column to accommodate the `VARCHAR` values. The new column name will be the original name appended with the data type: `order_confirmed__string`

How columns are named depends on the type of destination being used to warehouse data. Refer to the [Mixed Data Types guide for more info]({{ link.destinations.storage.column-splitting | prepend: site.baseurl }}).

---

## Replicating unsupported data types {#sync-unsupported-data-types}

Columns containing data types that aren't supported may prevent an entire table from replicating. 

If you determine a non-replicating column contains an unsupported data type, you'll need to de-select it to allow the table to successfully replicate.

---

## 'Not Supported' status for columns

If a column you want to sync has a Status of `Not Supported`, the root cause may be an [unsupported data type or insufficient user permissions]({{ link.troubleshooting.unsupported-data-types | prepend: site.baseurl }}).