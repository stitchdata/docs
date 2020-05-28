---
title: Missing Columns & NULL Values
keywords: troubleshooting, trouble, issue, help, data discrepancy, discrepancies, not replicating, no replication, nulls, null
permalink: /troubleshooting/missing-columns-and-null-values
tags: [data_discrepancy, replication, nonreplicating_data]

summary: "If you've noticed some missing columns or data from your data warehouse, the root cause may be `NULL` values."
type: "discrepancy, replication-all"
toc: false
promote: "false"
---

If you've noticed some missing columns or data from your data warehouse, the root cause may be `NULL` values.

---

## Stitch Replication

When Stitch loads your data, it uses the column's data type to determine how to correctly store the data in your data warehouse. If a column only contains `NULLs`, Stitch's loading processes won't be able to infer the correct data type to store the data properly.

In short: when a column only contains `NULLs`, it won't be replicated to your data warehouse.

---

## Next Steps

If you notice some missing columns, we recommend checking to see if they contain only `NULLs`. If this is the case, should that column at any point contain non-`NULL` values in the future, the column will immediately be created in your data warehouse and populated with the non-`NULL` values.

---

## Contacting Support

If you check the columns and find they contain values that are non-null, please reach out to support.
