---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Identifying & Resolving Rejected Record Issues
keywords: troubleshooting, destination, trouble, issue, help, error, errors
permalink: /data-structure/identifying-rejected-records
layout: general
tags: [troubleshooting_destinations, troubleshooting_errors]

summary: "From time to time, Stitch may run into problems when attempting to load data into your destination. When data is deemed incompatible by the destination, the record will be rejected and Stitch will log it in a rejected records log."
toc: true
weight: 5


# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  From time to time, Stitch may run into problems when attempting to load data into your destination. For example: A table contains more columns than the destination's supported limit. 

  On your end, this will usually look like you're missing data. When Stitch is unable to load data, however, the occurrence will be logged in a table named `{{ rejected-records.name }}`. Every integration schema created by Stitch will include this table as well as the other tables in the integration.

  This rejection log can be useful for investigating data discrepancies and troubleshooting errors surfaced during the data loading process.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary | flatify }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#      CONTENT SECTIONS      #
# -------------------------- #

sections:
  - title: "Reasons for data rejection"
    anchor: "reasons-for-rejection"
    summary: "Some reasons why data can be rejected"
    content: |
      Reasons for rejection will depend on the type of destination you’re using, as each has its own data requirements and restrictions.

      There are some common causes for rejection, however:

      - Column names contain data type suffixes (ex: `__bigint`), which are reserved by Stitch
      - Table and/or column names contain `{{ system-column.prefix }}` or `{{ system-column.rjm-prefix }}` prefixes, which are reserved by Stitch
      - Table or column names exceed the supported character limit
      - Integer data that falls outside the range supported by the data warehouse

      For a detailed rollup of how each destination handles data - including what situations will result in rejected records -  refer to the [Data Loading guide]({{ link.destinations.storage.loading-data | prepend: site.baseurl }}) for the destination you’re using.

  - title: "{{ rejected-records.name }} table schema"
    anchor: "rejected-records-table"
    summary: "The schema of the rejected records log table"
    content: |
      In every integration schema created by Stitch is a table named `{{ rejected-records.name }}` which acts as a log for a particular integration's rejected records.

      This table contains information about when and why a data rejection occurred. The `{{ rejected-records.name }}` table contains the following columns: 

      {% assign attribute-list=site.data.stitch.system-tables.sdc-rejected.attributes %}

      {% include stitch/stitch-system-table.html attribute-list=attribute-list %}

      Take a look at the sample data in the last column. If Stitch was attempting to load this record into a Redshift destination, it would be rejected. Why?

      In this case, it's because Redshift is case-insensitive. Because `id` and `Id` canonicalize to the same name - that is, they differ only by case - a collision error surfaced when Stitch attempted to load the data.

  - title: "Resolving data rejection issues"
    anchor: "resolving-record-rejection-issues"
    summary: "How to resolve data rejection issues"
    content: |
      In some cases, you may be able to pinpoint and resolve the root cause of the rejection.

      Consider the `id` and `Id` example from the previous section. If these fields came from a database integration, you could re-name the columns - for example: `customer_id` and `first_order_id` - in the source database and re-replicate the data. This would resolve the field collision error and allow Stitch to load the data.

      However, it may not be possible to resolve every rejected record issue. While you may be able to resolve the issue in a database integration, the majority of SaaS integrations don’t provide users with the ability to define and control the structure of their data.
---
{% include misc/data-files.html %}