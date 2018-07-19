---
title: Replication Keys for Database Integrations
permalink: /replication/replication-keys
keywords: replicate, replication, replication key, keys, stitch replicates data, rp
tags: [replication]

summary: "Replication Keys are columns that Stitch uses to identify new and updated data for replication. These columns are one of the most important components of Stitch, as they enable Stitch to correctly capture new and updated data. In this guide, we'll walk you through what a Replication Key is, what its requirements are, and how to choose the best column for the job."
type: "settings"
toc: true
weight: 3
---
{% include misc/data-files.html %}

{% include note.html type="single-line" content="**While the majority of this guide applies to database integrations**, the info we cover is helpful for understanding Stitch replication as a whole, even if you're only using SaaS integrations." %}

Replication Keys are columns that Stitch uses to identify new and updated data for replication. When you set a table to use [Incremental Replication]({{ link.replication.rep-methods | prepend: site.baseurl | append: "#incremental-replication" }}), you’ll also need to define a Replication Key for that table.

As improperly setting Replication Keys can cause data discrepancies, latency, and high row counts, it’s important to understand how they work, what makes a good key, and the gotchas associated with them.

{% capture mongo-rep-key %}
**Mongo Integrations & Replication Keys**<br>
Before you dive in, **are you working with a Mongo integration**? If so, please refer to the [Selecting Mongo Replication Keys guide]({{ link.replication.mongo-rep-keys | prepend: site.baseurl }}), as Replication Keys work a little differently for Mongo integrations.
{% endcapture %}

{% include important.html content=mongo-rep-key %}

---

{% include replication/rep-keys-vs-primary-keys.html %}

---

{% include replication/rep-key-requirements.html %}

---

## Recommendations & Gotchas

While a column only need be an `integer`, `datetime`, or `timestamp` to be a Replication Key, we have some recommendations (and things you should keep in mind) when selecting a column to be a Replication Key.

{% include replication/rep-key-recommendations.html %}

{% include replication/rep-key-gotchas.html %}

### Data Discrepancies & Row Count Impact

Replication Keys are one of the single most important aspects of data replication. Because they're so important, we felt these two points merited their own section:

- **Incorrectly selecting a Replication Key can cause data discrepancies.** For example: you set the Replication Key for an Append-Only table to an `id` column, which is an auto-incrementing integer. Existing rows in this table are updated, but the `id` column never changes after the record is created. Stitch will not detect the updated values because the `id` column hasn’t changed.

- **Incorrectly selecting a Replication Key can impact your row count.** For example: you set the Replication Key column for a table to a `BIGINT` column that’s used in a boolean fashion, meaning it contains 0s and 1s. Every time the values in this column change, the row will be re-replicated to your data warehouse and count against your monthly limit.

  If you encounter a data discrepancy, we recommend you start by verifying that the Replication Method and Key for the table are properly set. For further assistance, check out the [Data Discrepancy Troubleshooting Guide]({{ link.troubleshooting.discrepancy-guide | prepend: site.baseurl }}).

--- 

{% include replication/define-rep-keys.html %}

---

{% include replication/reset-rep-keys.html %}
