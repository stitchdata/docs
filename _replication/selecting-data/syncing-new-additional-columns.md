---
title: Syncing New & Additional Columns on Already-Syncing Tables
permalink: /replication/syncing-new-additional-columns
keywords: syncing, sync, replicate, replication, select data, sync data, sync table, sync column, add new columns, sync new column, add additional columns
tags: [replication]

content-type: "select-data"
toc: true
weight: 3

summary: "What happens when you add a brand-new column in a data source or you want to sync additional columns on an already-syncing table? How will your row count be impacted? In this guide, we cover how Stitch handles new columns, what you can expect for existing rows, and how to backfill data."
---
{% include misc/data-files.html %}

When you add a new column to a table in your data source, what happens in Stitch? What about syncing additional columns on already-syncing tables? Depending on the type of integration and the [Replication Method]({{ link.replication.rep-methods | prepend: site.baseurl }}) the table uses, there are a few possible outcomes.

---

## New Columns in the Data Source & Stitch

When a new column is added in a data source, Stitch will first need to perform a **structure sync** to detect it.

Note that:

- It may take some time for Stitch to detect the new column and display it in the {{ app.page-names.int-details }} page.
- The following applies to both database and non-webhook SaaS integrations.

### Already-Syncing Tables
After the structure sync completes, the column will **be automatically synced** and, **if the [integration supports whitelisting columns]({{ link.replication.syncing | prepend: site.baseurl | append: "#integrations-that-support-whitelisting" }})**, display in the {{ app.page-names.int-details }} page. Data for the column will then replicate based on the table's Replication Method.

**Keep in mind that for Incremental tables**, you may need to [backfill existing rows](#backfilling-existing-rows) if the addition of new data hasn't updated the table's [Replication Key]({{ link.replication.rep-keys | prepend: site.baseurl }}).

### Non-Syncing Tables
If the table isn't currently selected to sync, the new column will display inside Stitch (if the [integration supports whitelisting columns]({{ link.replication.syncing | prepend: site.baseurl | append: "#integrations-that-support-whitelisting" }})) **but will have to be manually set to sync**.

---

## Syncing Additional Columns on Already-Syncing Tables

In this case, we aren't talking about brand new columns in the data source, **but previously existing columns that have never been set to sync in Stitch**. How Stitch handles the syncing of additional rows depends on the table's Replication Method.

### Full Table Replication

For tables using Full Table Replication, data in the newly-synced column will be available for **all rows** - including new and existing - the next time the table is successfully replicated.

### Incremental Replication

For tables using Incremental Replication, data in the newly-synced column will be available **only for rows added AFTER the column is synced. Existing rows must be backfilled to make the data available.**

Getting newly-synced column data into existing rows requires a full re-ync of the table. Because this can significantly impact your row count and we don't want to re-replicate data without your say-so, we leave inserting newly-synced column data into existing rows up to you.

---

{% include replication/reset-rep-keys.html %}