---
title: Syncing Data
permalink: /replication/syncing-data
keywords: syncing, sync, replicate, replication, select data, sync data, sync table, sync column
tags: [replication]

summary: "After you connect an integration and Stitch performs a structure sync, the next thing you'll do is select tables and columns to sync. In this guide, we'll walk you through how to sync/unsync objects for database and SaaS integrations."
type: "syncing"
toc: true
weight: 1
---
{% include misc/data-files.html %}

After you initially connect an integration, Stitch will perform a structure sync to detect the databases, tables, and columns in the integration.

Once the structure sync is complete, you'll be able to select the individual tables and columns you want to sync. Stitch calls this **whitelisting** and it's **currently available only for certain integrations**, which you can read more about below.

These integrations require tables and columns to be selected before data can begin replicating. Once the setup process is complete, Stitch will begin replicating your data.

---

## Integrations that Support Whitelisting

The following integrations support some level of whitelisting: 

{% include replication/integrations-with-whitelisting.html %}

Keep in mind that:

- **Only these integrations support whitelisting.** If an integration doesn't support whitelisting, **all available data - meaning all the tables and columns that Stitch can access** - will be set to sync.

  For detailed info on the data Stitch syncs from [SaaS integrations]({{ site.baseurl }}/integrations/saas), check out the **Schema** section of any integration's guide.
- **Only the tables and columns you set to sync in these integrations will be replicated.** If nothing is set to sync in these integrations, the integration will have a status of `Not Configured`. Replication won't begin until some objects are synced.

---

## Select Data to Sync

Selecting data to sync is easy. All you need to do is click into the integration from the {{ app.page-names.dashboard }} page and find the object you want to sync. Then, {{ app.menu-paths.sync | replace: "Click","click" }}

**By default, all columns in a table will be set to sync.** For integrations that support whitelisting, you can un-sync columns by clicking on the **table name** and then selecting columns to un-sync.

Additionally, if you're syncing data from a database integration, you'll be prompted to select a [Replication Method]({{ link.replication.rep-methods | prepend: site.baseurl }}) for tables that you set to sync.

{% capture rep-methods %}
**Replication Methods & Row Count Impact**<br>
Replication Methods are extremely important - we can't stress this enough. They'll not only directly impact your row count, but incorrectly defined methods can also cause data discrepancies.<br><br>

If you're unfamiliar with Stitch's Replication Methods, we recommend you check out the [Replication Method guide]({{ link.replication.rep-methods | prepend: site.baseurl }}) before defining methods for your tables.
{% endcapture %}
{% include important.html content=rep-methods %}

### Parent Objects & Syncing
{% capture parent-objects %}
> The table containing these columns is not set to sync. Please sync the parent table to ensure replication of columns selected on this screen.

If you see this message or something similar on the {{ app.page-names.int-details }} page, it means that the object **above** what you're looking at - in this case, a table - isn't set to sync.

**Parent objects must set to sync for the objects under them to successfully replicate.** To be clear: for a column to sync, the table above it must also be set to sync. If applicable, so must the **schema** containing the table, and the **database** containing the schema.
{% endcapture %}

{{ parent-objects }}

### Sync Database Views

While the steps for syncing a database view are almost the same as those for syncing a table, there are some slight differences.

For more info check out the [Syncing Database Views]({{ link.replication.db-views | prepend: site.baseurl }}) guide.

### Sync New & Additional Columns on Already-Syncing Tables

What happens when you've added a brand-new column in the data source or you want to sync additional columns on an already-syncing table?

For more info check out the [Syncing New & Additional Columns]({{ link.replication.syncing-new-columns | prepend: site.baseurl }}) guide.

---

## Unsync Data

There a few ways you can unsync objects:

1. **Unsync All.** To unsync all objects **in the page you're currently on**, click the **grey checkbox** next to the **Table/Column Name** column, then click **Stop Syncing All**.

   Note that if this is a parent object - meaning it contains an object beneath it - Stitch will also stop syncing the child object.
2. **Unsync individual objects.** Locate the object and click the **checkbox** next to the object's name.

Whatever method you choose, the checkbox(es) of the object(s) you unsync will turn grey and the **Method** will change to **Not Synced**.

Additionally, if you want to re-sync a previously unsynced table, you'll need to set the table's Replication Method again.

--- 

## Troubleshooting

### Missing Objects

> Stitch cannot detect any objects (databases, tables, etc.) at or below this level.

If you receive this message or you can't find an object (database, table, column, etc.), [it's typically a permissions issue]({{ link.troubleshooting.missing-objects | prepend: site.baseurl }}).

### Not Supported Table/Column Messages in Database Integrations

If you see a status of `Not Supported` for a table or column in a database integration, there a few potential root causes:

- **Insufficient permissions.** Verify that the Stitch user has all the required permissions as outlined in the **Setup** instructions for the database. Docs for database integrations [can be found here]({{ site.baseurl }}/integrations/databases).

   After you grant the required permissions and a full replication cycle has completed, the table's **Sync Status** should change to `Supported` and be available for syncing.
- **Unsupported column.** If a column is displayed as `Not Supported`, it may be that the column contains an [unsupported data type]({{ link.troubleshooting.unsupported-data-types | prepend: site.baseurl }}).

### Parent Object Isn't Set to Sync
{{ parent-objects }}
