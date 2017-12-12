---
title: Choosing a Destination
permalink: /destinations/choosing-a-stitch-destination
tags: [destinations]
keywords: destination, destinations, data warehouse, data warehouses, warehouse, stitch etl, etl, compare destinations, choose destination, select destination
summary: "If you're new to data warehousing or want to see how Stitch's destination offerings compare to each other, look no further. This guide will help you choose the best Stitch destination for your data warehousing needs."

toc: true
type: "all"
destination: false
---
{% include misc/data-files.html %}

When Stitch replicates your data, we'll load it into the destination - or data warehouse - of your choosing. A data warehouse is a central repository of integrated data from disparate sources.

**As we currently only allow you to connect one destination to your account**, we recommend asking yourself the questions below before making your selection. By fully assessing each choice first, you'll decrease the likelihood of needing to switch destinations or re-replicate all of your data at a later date.

 - Does it support all (or most of) your data sources?
 - Will the structure of the data replicated by Stitch work with how you plan to use it?
 - Do you need a fully-managed solution, or can you perform maintenance tasks on your own?
 - Does the provider's pricing fall within your budget?

At the end of this article is a visual rollup of how each of Stitch's destinations stack up against each other. This chart includes some supported limits (ex: length of table names), what task each destination excels at, and so on.

{% capture data-strategy%}
**Not sure where to start?**<br>
If you're feeling overwhelmed or you're unsure of what to look for, don't worry. For a solid primer on data warehouses and setting the data strategy for your organization, check out our [Data Strategy Guide]({{ site.data-strategy }}).
{% endcapture %}

{% include tip.html content=data-strategy %}

---

## Getting Started, Fast

If you simply want to try Stitch or Redshift or if you don't have the ability to spin up a Redshift cluster of your own in AWS, we recommend trying [Panoply]({{ link.destinations.overviews.panoply | prepend: site.baseurl | append: "#setup" }}). With just a few clicks, you create your own fully-managed Redshift data warehouse and start replicating data in minutes.

Keep in mind that switching to a different destination at any point will require a full re-sync of your data.

---

## Integration & Destination Compatibility

Some integrations may be partially or fully incompatible with some of the destinations offered by Stitch. For example: some destinations don't support storing multiple data types in the same column. If a SaaS integration sends over a column with mixed data types, some destinations may "reject" the data.

For integrations that allow you to control how data is structured, you may be able to fix the problem at the source and successfully replicate the data. If this is not possible, however, Stitch may never be able to successfully replicate the incompatible data.

[**Check Integration & Destination Compatibility**]({{ link.destinations.overviews.compatibility | prepend: site.baseurl }})

---

## Data Structure

While the majority of your data will look the same across our destinations, there are some key differences you should be aware of.

### Nested Data Structures

If you decide to use a destination that doesn't natively support nested structures - meaning **Redshift, Panoply,** or **PostgreSQL** - Stitch will de-nest these structures. 

This means that Stitch will create subtables and more rows will count against your quota, depending on the level of nesting.

**Google BigQuery** and **Snowflake**, however, natively support nested structures. This means nested records will be stored intact in these destinations.

Check out the [Handling of Nested Data & Row Count Impact]({{ link.destinations.storage.nested-structures | prepend: site.baseurl }}) for an in-depth look at what we mean by nested records, how Stitch handles nested data, and what those records will look like in your data warehouse.

### BigQuery & Append-Only Replication

The current release of Stitch's BigQuery destination uses **<a href="#" data-toggle="tooltip" data-original-title="{{site.data.tooltips.append-only-rep}}">Append-Only Incremental Replication</a>.**

For SaaS and database tables that use Incremental Replication, Stitch will replicate data into BigQuery in an append-only fashion. Data that updates existing an existing row will NOT overwrite the row. Instead, a new row with the new data will be appended to the end of the table.

This means that there can be many different rows in a BigQuery table with the same Primary Key, each representing what the data was at that moment in time. **These are not duplicate rows** - they're "snapshots" of the record at different points.

For more info, check out [this detailed explanation on Append-Only Replication]({{ link.replication.rep-methods | prepend: site.baseurl | append: "#append-only-incremental-replication" }}) or [our recommendations for querying append-only tables]({{ link.replication.append-only | prepend: site.baseurl }}).

### Redshift vs. PostgreSQL

If you've worked with PostgreSQL in the past and are considering Redshift as your data warehouse, you should note that Redshift [implements some Postgres features differently](http://docs.aws.amazon.com/redshift/latest/dg/c_redshift-sql-implementated-differently.html){:target="_blank"}. In addition, some [features](http://docs.aws.amazon.com/redshift/latest/dg/c_unsupported-postgresql-features.html){:target="_blank"}, [data types](http://docs.aws.amazon.com/redshift/latest/dg/c_unsupported-postgresql-datatypes.html){:target="_blank"}, and [functions](http://docs.aws.amazon.com/redshift/latest/dg/c_unsupported-postgresql-functions.html){:target="_blank"} aren't supported at all.

---

## Setup & Maintenance

With the exception of a self-hosted PostgreSQL instance, all the destinations offered by Stitch are cloud-hosted databases, meaning you won't have to factor in server maintenance when making a decision.

[**BigQuery**](https://cloud.google.com/solutions/bigquery-data-warehouse#maintenance){:target="_blank"}, [**Heroku**](https://devcenter.heroku.com/articles/platform-updates-maintenance-and-notifications){:target="_blank"}, **Panoply**, and **Snowflake** are fully-managed solutions that include routine maintenance and upgrades in their plans. Setting up Snowflake requires more technical know-how than the other aforementioned destinations.

**Redshift, Amazon Postgres-RDS**, and **self-hosted Postgres instances** will require you to perform and schedule maintenance tasks on your own. Spinning up a Redshift and Amazon Postgres-RDS instance will require technical knowledge and familiarity with the Amazon Web Services (AWS) console.

---

## Pricing

Every destination offered by Stitch has its own pricing structure. Some providers charge by overall usage, others by an hourly rate or the amount of stored data. Depending on your needs, some pricing structures may fit better into your budget.

In the next section, you'll find each destination's pricing structure, including a link to detailed price info and whether a free option (trial or plan) is available. Here are a few things to keep in mind:

{% assign destinations = site.destinations | where:"destination",true %}
{% for destination in destinations %}
- **{{ destination.display_name }}**: {{ destination.pricing_notes }}{% if destination.type == "bigquery" %} To learn more about how Stitch may impact your BigQuery costs, [click here]({{ link.destinations.overviews.bigquery-pricing | prepend: site.baseurl }}).{% endif %}
{% endfor %}

---

## Compare Destinations

{% include destinations/destination-rollup.html %}

---

## Additional Resources & Setup Tutorials

Ready to pick a destination and get started? Use the links below to check out a more in-depth look at each destination or move on to the setup and connection process.

{% include destinations/destination-tiles.html %}
