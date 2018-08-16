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

The data types Stitch supports for replication fall into two categories:

- **Common**, which are data types supported for all integrations
- **Integration-specific**, which are data types supported for specific integrations and integration versions, where applicable. **Note**: Common data types also apply to integrations that support integration-specific data types.

**Note**: If a data type isn't present in either the Common or Integration-specific tables, it means that Stitch doesn't currently support replication for that data type. Replicating columns with unsupported data types may lead to issues with replication.

{% include replication/templates/data-types/data-type-formatting.html formatting="tabs" integration_name="postgres" display_name="PostgreSQL" %}

---

## Next steps

To allow Stitch to successfully replicate the table you'll need to de-select any columns with unsupported data types. This will prevent Stitch from attempting to replicate them, thus allowing the table to replicate as it should.