---
title: Database Integration Table Name Collisons
keywords: troubleshooting, trouble, issue, help, data discrepancy, discrepancies,
permalink: /troubleshooting/data-discrepancies/database-integration-table-name-collisions
tags: [data_discrepancy]

summary: "In database integrations, if the names of multiple tables canonicalize to the same name - even if they're from different source databses or schemas - name collisions and data discrepancies can occur. This applies to any database integration available in Stitch."
type: "discrepancy, database-integration, replication"
promote: "false"
---

{{ page.summary }}

---

## Object naming and loading

When Stitch replicates data from a database integration, all selected tables are loaded into a single schema in your destination. Because Stitch doesn't re-create databases and schemas in your destination, if two tables with the same name are replicated, naming collisions and data discrepancies can occur.

### Example 1: Two tables with different names

On the left there are the source tables, prepended by the schema they're contained in. On the right is how the tables are expected to look in the destination schema, named `database_integration`.

| In the source       | In the destination             |
|---------------------|--------------------------------|
| customers.orders    | database_integration.orders    |
| companies.projects  | database_integration.projects  |

### Example 2: Two tables with the same name

Let's say that the source `customers` and `companies` schemas both contain an `addresses` table. In this situation, the table names would canonicalize to the same name in the destination:

| In the source       | In the destination             |
|---------------------|--------------------------------|
| customers.addresses | database_integration.addresses |
| companies.addresses | database_integration.addresses |

When this occurs, you may receive a table name collision error or data for both tables may be incorrectly loaded into one table.

---

## Workarounds

- **Ensure table names are unique across schemas and databases**.
- **Create multiple database integrations** if it isn't feasible to ensure table name uniqueness between your source databases and schemas. Using this method, you can replicate each table separately and have Stitch load them into different destination schemas, ensuring name uniqueness.
- **For PostgreSQL-backed database integrations:** Check the **Include PostgreSQL schema names in destination tables** setting during the initial setup of the integration.

   When this setting is checked, Stitch will include the name of the source schema in the destination table name, ensuring table names are unique. For example: `customers.addresses` would result in a destination table named `customers__addresses`.

   **Note**: This setting cannot be changed once the integration is saved. Additionally, including schema names in destination table names may result in tables with names that exceed your destination's object name limits.