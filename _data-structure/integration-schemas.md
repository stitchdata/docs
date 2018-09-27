---
title: Integration Schemas
permalink: /data-structure/integration-schemas
keywords: integration schemas, stitch schema, _sdc, sdc, stitch creates schemas, data warehouse
tags: [replication]
summary: "Learn how Stitch organizes the data replicated from your sources in your data warehouse."

toc: true
weight: 1
---
{% include misc/data-files.html %}
{% assign sdc-columns = site.data.stitch.sdc-columns %}

For each integration that you add to Stitch, a schema specific to that integration will be created in your data warehouse. The integration's schema is where all the data Stitch replicates from the data source will be stored.

---

## Integration schema names

When you create an integration, you're asked to provide a name for the integration. This name is used to create the integration's schema in your data warehouse.

![Naming an integration]({{ site.baseurl }}/images/integrations/integration-name.png)

If you want the schema name to be different than the display name, click the **Change** link below the **Integration Name** field and enter a new name in the field that displays:

![Using different names for schemas & display names.]({{ site.baseurl }}/images/integrations/change-schema-name.gif)

**Note**: After you save an integration, its schema name can't be changed.

### Changing and re-using schema names

Changing an integration's schema name requires you to create a new integration and fully re-replicate all historical data.

Schema names from deleted integrations can be re-used. However, if a naming collision occurs (two schema names canonicalize to the same name) the destination [may reject the data](#rejected-records-log) - deleting an integration in the Stitch app won't delete that integration's schema or data from your data warehouse.

---

## Integration schema composition

Schemas created by Stitch contain that integration's tables and one additional table called `{{ rejected-records.name }}`, which serves as a log for [data loading issues](#rejected-records-log).

![The Stitch schema structure.]({{ site.baseurl }}/images/stitch-schema-structure.png)

Aside from `{{ rejected-records.name }}`, the tables that Stitch creates in integration schemas depends on the **type** of integration.

### Database integration tables

For database integrations, the schema in your destination will mirror your data source and contain only the [tables and columns you set to replicate]({{ link.replication.syncing | prepend: site.baseurl }}).

There is one exception to this, however: [MongoDB]({{ site.baseurl }}/integrations/databases/mongodb) integrations don't support whitelisting at the field level. All fields contained in a collection are automatically set to replicate when a collection is selected for replication.

### SaaS integration tables

For SaaS integrations, the schema depends on whether the integration supports <a href="#" data-toggle="tooltip" data-original-title="{{ site.data.tooltips.whitelisting-feature }}">whitelisting</a>:

- **If object selection is supported,** the schema will contain only the tables (and columns, for some integrations) you set to replicate. A full list of integrations that support object selection [can be found here]({{ link.replication.syncing | prepend: site.baseurl | append: "#integrations-that-support-whitelisting" }}).
- **If object selection isn't supported,** all available tables and columns in the integration will be replicated to your data warehouse. You can find out more about the available tables and their Replication Methods in the **Schema** section of the [SaaS Integration docs]({{ site.baseurl }}/integrations/saas/).

---

## Integration table schemas

The integration tables in the schema contain the replicated data from tables set to replicate. **Note**: If you de-select a table from replication, doing so won't remove that table's data from your destination.

### Data storage

How your data is stored in the schemas and tables created by Stitch depends on a few things:

- How data is structured in that particular data source (ex: use of nested data structures),
- Any changes you might make to the data source (ex: adding/removing a column),
- Stitch-specific data handling rules (ex: entirely `NULL` columns), and
- How your destination handles data (ex: columns with mixed data types, nested data structures)

Stitch will encounter dozens of scenarios when replicating and loading your data. Familiarizing yourself with these scenarios and the nuances of your destination will enable you to better understand your data's structure and efficiently troubleshoot if issues arise.

To learn more about how handles these scenarios, check out the [Data Loading guide for your destination]({{ link.destinations.storage.loading-data | prepend: site.baseurl }}).

### {{ system-column.prefix }} columns

In addition to the columns set to replicate in these tables, there are also a few columns prepended with `{{ system-column.prefix }}`. Stitch uses these columns to replicate your data.**Don't remove these columns**, as doing so will cause replication issues in Stitch.

Some columns are applicable to all tables and integrations, while others may only be in certain tables:

{% for category in sdc-columns.categories %}
- **{{ category.display-name }}** - {{ category.description | flatify }}
{% endfor %}

Click the tabs below for more info on the columns in each category. 

{% include stitch/stitch-system-table.html table="system" %}

---

## Rejected records log

Occasionally, Stitch will encounter data that it can't load into your destination. For example: a table contains more columns than the destination's supported limit. 

On your end, this will usually look like you're missing data. When Stitch is unable to load data, however, the occurrence will be logged in a table named `{{ rejected-records.name }}`. Every integration schema created by Stitch will include this table as well as the other tables in the integration.

The `{{ rejected-records.name }}` table acts as a log of data rejections and includes the reason, as much of the record that can fit, and the date of the occurrence.

This rejection log can be useful for investigating data discrepancies and troubleshooting errors surfaced during the data loading process.

To learn more about this table, check out the [Rejected Records Log guide]({{ link.destinations.storage.rejected-records | prepend: site.baseurl }}).