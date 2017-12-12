---
title: Identifying & Resolving Rejected Record Issues
keywords: troubleshooting, destination, trouble, issue, help, error, errors
permalink: /data-structure/identifying-rejected-records
tags: [troubleshooting_destinations, troubleshooting_errors]

summary: "From time to time, Stitch may run into problems when attempting to load data into your data warehouse. When data is deemed incompatible by the data warehouse, the record will be rejected and Stitch will log it in a rejected records log."
toc: true
weight: 5
---
{% include misc/data-files.html %}

From time to time, Stitch may run into problems when attempting to load data into your destination. When data is deemed incompatible by the destination, the record will be "rejected" and logged in a table named `{{ rejected-records.name }}`.

---

## Reasons for Rejection

Reasons for rejection will depend on the type of data warehouse you’re using, as each has its own data requirements and restrictions.

There are some common causes for rejection, however:

- Column names contain data type suffixes (ex: `__bigint`), which are reserved by Stitch
- Table and/or column names contain `{{ system-column.prefix }}` or `{{ system-column.rjm-prefix }}` prefixes, which are reserved by Stitch
- Table or column names exceed the supported character limit
- Integer data that falls outside the range supported by the data warehouse

For a detailed rollup of how each destination handles data - including what situations will result in rejected records -  refer to the [Data Loading guide]({{ link.destinations.storage.loading-data | prepend: site.baseurl }}) for the destination you’re using.

---

## {{ rejected-records.name }} Table

In every integration schema created by Stitch is a table named `{{ rejected-records.name }}` which acts as a log for a particular integration's rejected records.

This table contains information about why a record was rejected, the date of the rejection, and the name of the table in the integration schema that the data was destined for.

{% include stitch/stitch-system-table.html table="rejected" %}

Take a look at the sample data in the last column. If Stitch was attempting to load this record into a Redshift data warehouse, it would be rejected. Why?

The answer: Redshift is case-insensitive. Because `id` and `Id` canonicalize to the same name - that is, they differ only by case - a collision error surfaced when Stitch attempted to load the data.

---

## Resolving Record Rejection Issues

In some cases, you may be able to pinpoint and resolve the root cause of the rejection.

Consider the `id` and `Id` example from the previous section. If these fields came from a database integration, you could re-name the columns - for example: `customer_id` and `first_order_id` - in the source database and re-sync the data. This would resolve the field collision error and allow Stitch to load the data.

However, it may not be possible to resolve every rejected record issue. While you may be able to resolve the issue in a database integration, the majority of SaaS integrations don’t provide users with the ability to define and control the structure of their data.