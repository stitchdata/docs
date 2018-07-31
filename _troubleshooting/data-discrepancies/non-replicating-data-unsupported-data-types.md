---
title: Non-Replicating Data & Unsupported Data Types
keywords: troubleshooting, trouble, issue, help, data discrepancy, discrepancies, not replicating, no replication
permalink: /troubleshooting/non-replicating-data-unsupported-data-types
tags: [data_discrepancy, replication, nonreplicating_data]

summary: "If a table isn't replicating into your data warehouse, it may be because one or more of the columns in the table contains an unsupported data type."
toc: true
type: "replication-all, discrepancy"
---

{% include misc/data-files.html %}

If a table isn't replicating into your destination, it may be because one or more of the columns in the table contains an unsupported data type. An unsupported data type may keep an entire table from replicating successfully.

---

## Supported data types

As of {{ stitch.last-updated }}, Stitch supports replicating the data types listed in the table below.

{% include replication/templates/data-types/data-type-formatting.html formatting="tabs" %}

---

## Next steps

To allow Stitch to successfully replicate the table you'll need to unsync any columns with unsupported data types. This will prevent Stitch from attempting to sync them, thus allowing the table to replicate as it should.