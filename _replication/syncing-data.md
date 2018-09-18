---
title: Selecting data to replicate
permalink: /replication/syncing-data
keywords: syncing, sync, replicate, replication, select data, sync data, sync table, sync column
tags: [replication]

summary: "After you connect an integration and Stitch performs a structure sync, the next thing you'll do is select tables and columns to replicate. In this guide, we'll walk you through how to set objects for database and SaaS integrations to replicate."
type: "syncing"
toc: true
weight: 1
---
{% include misc/data-files.html %}

After you initially connect an integration, Stitch will perform a structure sync to detect the databases, tables, and columns in the integration.

Once the structure sync is complete, you'll be able to select the individual tables and columns you want to replicate. Stitch calls this **table** or **column selection** and it's **currently available only for certain integrations**, which you can read more about below.

These integrations require tables and columns to be selected before data can begin replicating. Once the setup process is complete, Stitch will begin replicating your data.

---

## Integrations that support table or column selection

The following integrations support some level of object selection: 

{% include replication/integrations-with-whitelisting.html %}

Keep in mind that:

- **Only these integrations support object selection.** If an integration doesn't support object selection, all available data - meaning all the tables and columns that Stitch can access - will be set to replicate.

  For detailed info on the data Stitch replicates from [SaaS integrations]({{ site.baseurl }}/integrations/saas), check out the **Schema** section of any integration's guide.
- **Only the tables and columns you set to replicate in these integrations will be replicated.** If nothing is set to replicate in these integrations, the integration will have a status of `Not Configured`. Replication won't begin until some objects are selected.

---

## Set tables and columns to replicate

Setting data to replicate is easy. All you need to do is click into the integration from the {{ app.page-names.dashboard }} page and find the object you want to replicate. Then, {{ app.menu-paths.sync | replace: "Click","click" }} Keep in mind that:

- **For database integration tables**, all columns will be set to replicate automatically.

   Additionally, you'll be prompted to select a [Replication Method]({{ link.replication.rep-methods | prepend: site.baseurl }}) for tables that you set to replicate.
- **For SaaS integration tables that support column selection**, you can select columns by clicking on the **table name** and then tracking columns to replicate.

{% capture rep-methods %}
Replication Methods are extremely important - we can't stress this enough. They'll not only directly impact your row count, but incorrectly defined methods can also cause data discrepancies.

If you're unfamiliar with Stitch's Replication Methods, we recommend you check out the [Replication Method guide]({{ link.replication.rep-methods | prepend: site.baseurl }}) before defining methods for your tables.
{% endcapture %}
{% include important.html first-line="**Replication Methods and row count impact**" content=rep-methods %}

### Parent objects and replication
{% capture parent-objects %}
> The table containing these columns is not set to sync. Please sync the parent table to ensure replication of columns selected on this screen.

If you see this message or something similar on the {{ app.page-names.int-details }} page, it means that the object **above** what you're looking at - in this case, a table - isn't set to replicate.

Parent objects must be set to replicate for the objects under them to successfully replicate. To be clear: For a column to replicate, the table above it must also be set to replicate. If applicable, so must the **schema** containing the table, and the **database** containing the schema.
{% endcapture %}

{{ parent-objects }}

### Replicate database views

While the steps for replicating a database view are almost the same as those for replicating a table, there are some slight differences.

For more info check out the [ing Database Views]({{ link.replication.db-views | prepend: site.baseurl }}) guide.

### Replicate new and additional columns on already-replicating Tables

What happens when you've added a brand-new column in the data source or you want to replicate additional columns on an already-replicating table?

For more info check out the [Syncing New & Additional Columns]({{ link.replication.syncing-new-columns | prepend: site.baseurl }}) guide.

---

## De-select tables and columns

There a few ways you can de-select objects:

1. **De-select all objects.** To de-select all objects **in the page you're currently on**, click the **grey checkbox** next to the **Table/Column Name** column, then click **Stop Syncing All**.

   **Note**: If this is a parent object - meaning it contains an object beneath it - Stitch will also stop replicating the child object.
2. **De-select individual objects.** Locate the object and click the **checkbox** next to the object's name.

Whatever method you choose, the checkbox(es) of the object(s) you de-select will turn grey and the **Method** will change to **Not Synced**.

Additionally, if you want to track a previously de-selected table, you'll need to set the table's Replication Method again.

--- 

## Troubleshooting

### Missing objects

> Stitch cannot detect any objects (databases, tables, etc.) at or below this level.

If you receive this message or you can't find an object (database, table, column, etc.), [it's typically a permissions issue]({{ link.troubleshooting.missing-objects | prepend: site.baseurl }}).

### Not supported table/column messages in database integrations

If you see a status of `Not Supported` for a table or column in a database integration, there a few potential root causes:

- **Insufficient permissions.** Verify that the Stitch user has all the required permissions as outlined in the **Setup** instructions for the database. Docs for database integrations [can be found here]({{ site.baseurl }}/integrations/databases).

   After you grant the required permissions and a full replication cycle has completed, the table's **Sync Status** should change to `Supported` and be available for syncing.
- **Unsupported column.** If a column is displayed as `Not Supported`, it may be that the column contains an [unsupported data type]({{ link.troubleshooting.unsupported-data-types | prepend: site.baseurl }}).

### Parent object isn't set to replicate
{{ parent-objects }}
