---
title: Full Table Replication
permalink: /replication/replication-methods/full-table
keywords: replicate, replication, replication method, stitch replicates data
tags: [replication]
layout: general

content-type: "replication-methods"
toc: true
weight: 2

summary: "Full Table Replication is a replication method in which all rows in a table - including new, updated, and existing - are replicated during every replication job. his guide contains an overview of how Full Table Replication works, when it should be used, its limitations, and how to enable it for an integration."


# --------------------------- #
#  REPLICATION METHOD DETAILS #
# --------------------------- #

## For info about this Replication Method, see:
## _data/taps/extraction/replication-methods/full-table-replication.yml


row-usage-example:
  - name: "Job 1"
    time: "00:00"
    this-job: "10,000"
    running-total: "10,000"

  - name: "Job 2"
    time: "00:30"
    this-job: "10,000"
    running-total: "20,000"

  - name: "Job 3"
    time: "01:00"
    this-job: "10,000"
    running-total: "30,000"

  - name: "Job 4"
    time: "01:30"
    this-job: "10,000"
    running-total: "40,000"

  - name: "Job 5"
    time: "02:00"
    this-job: "10,000"
    running-total: "50,000"


# --------------------------- #
#       CONTENT SECTIONS      #
# --------------------------- #

sections:
  - content: |
      {{ site.data.tooltips.full-table-rep }} In this guide, we'll cover:

      1. [How it works (with examples)](#hhow-full-table-replication-works),
      2. [When it should be used](#when-full-table-replication), and
      3. [Limitations of this Replication Method](#limitations)

  - title: "How {{ page.title }} works"
    anchor: "how-full-table-replication-works"
    content: |
      Tables that use {{ page.title }} are replicated in full during each replication job. Regardless of whether a record is new or simply modified, all records in the table will be selected for extraction.

      If {{ page.title }} were a SQL query, it would look like this:

      {% capture code %}
      SELECT column_you_selected_1,
             column_you_selected_2,
             [...]
        FROM schema.table
      {% endcapture %}

      {% include layout/code-snippet.html code=code language="sql" %}

# During loading, the destination table will be overwritten with the newly extracted data. **Note**: This doesn't apply to append-only destinations like [BigQuery]({{ link.destinations.overviews.bigquery | prepend: site.baseurl }}) or [Amazon S3 CSV]({{ link.destinations.overviews.amazon-s3 | prepend: site.baseurl }}).

  - title: "When {{ page.title }} should be used"
    anchor: "when-full-table-replication"
    content: |
      {{ page.title }} may be a good fit if:

      1. Records are hard deleted from the source.
      2. The table doesn't contain a suitable column for [Key-based Incremental Replication]({{ link.replication.key-based-rep | prepend: site.baseurl }}).
      3. [Log-based Incremental Replication]({{ link.replication.log-based-rep | prepend: site.baseurl }}) is unavailable for the source.
      4. **For MongoDB-backed database integrations**: The `_id` field contains only one data type. Refer to the [Limitations section](#limitation--mongo-multiple-data-types-discrepancies) for more info.

  - title: "Limitations of {{ page.title }}"
    anchor: "limitations"
    content: |
      Before you select {{ page.title }} as the Replication Method for a table, you should be aware of the limitations this method can have. Being aware of these limitations can help prevent data discrepancies and ensure your data is replicated in the most efficient manner possible.

      The limitations of {{ page.title }} are:

      {% for subsection in section.subsections %}
      {% assign limitation-title = "Limitation " | append: forloop.index | append: ": " %}
      - [{{ subsection.title | flatify | remove: limitation-title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Limitation {{ forloop.index }}: Can cause latency"
        anchor: "limitation--latency"
        content: |
          How large a source table is - that is, how many records the table contains - can affect how quickly Stitch is able to extract data from a source.

          In the case of large tables using {{ page.title }}, Stitch can only extract data as quickly as it is returned. This means that if a database or SaaS application returns data slowly, especially for a large table, latency in the replication process may increase. This is more probable with tables using {{ page.title }}.

      - title: "Limitation {{ forloop.index }}: Increased row consumption"
        anchor: "limitation--high-row-usage"
        content: |
          Tables using {{ page.title }} are replicated fully during every replication job, regardless of whether individual records were updated or not.

          The more records a table contains, the more rows that will count towards usage. When paired with a high [Replication Frequency](), a single table can quickly consume an entire month's row quota.

          For example: A table contains 10,000 records and is using {{ page.title }}. The integration's Replication Frequency is every 30 minutes. The table below shows the number of rows replicated for the table per job as well as the total number used since the first job:

          {% assign column-headings = "Job name|Start time|Rows replicated this job|Total rows replicated" | split: "|" %}
          {% assign values = "name|time|this-job|running-total" | split: "|" %}

          <table class="attribute-list">
          <tr>
          {% for column-heading in column-headings %}
          <td>
          <strong>
          {{ column-heading }}
          </strong>
          </td>
          {% endfor %}
          </tr>
          {% for job in page.row-usage-example %}
          <tr>
          {% for value in values %}
          <td>
          {{ job[value] }}
          </td>
          {% endfor %}
          </tr>
          {% endfor %}
          </table>

          If the integration were to continue replicating every 30 minutes until 11:59:59, this table would use 480,000 rows in 24 hours. Depending on the [Stitch plan]({{ site.pricing }}){:target="new"} you're using, this type of usage can quickly use up your row allotment.

      - title: "Limitation {{ forloop.index }}: Unavailable for some integrations"
        anchor: "limitation--unavailable-integrations"
        content: |
          Currently, {{ page.title }} is unavailable for version v11-01-2016 of Stitch's MongoDB integration. This version of MongoDB only supports [Key-based Incremental Replication]({{ link.replication.key-based-incremental | prepend: site.baseurl }}).

          {{ page.title }} is supported for all other versions of Stitch's database and SaaS integrations.

      - title: "Limitation {{ forloop.index }}: Multiple data types in the _id field can cause discrepancies (MongoDB)"
        anchor: "limitation--mongo-multiple-data-types-discrepancies"
        content: |
          {% include note.html type="single-line" content="**Note**: This applies only to MongoDB-backed database integrations." %}

          Full Table Replication works a little differently for MongoDB-backed database integrations. For MongoDB, Stitch uses the `_id` field in MongoDB collections as a pseudo-Replication Key. 

          During the replication job, Stitch first determines the current maximum value of the `_id` column. Next, Stitch queries for documents with `_id` values that are **less than or equal to** the current maximum `_id` value. 

          For example: A query for Full Table Replication for a MongoDB collection would look like this:

          {% capture code %}
          SELECT field_you_selected_1,
                 field_you_selected_2,
                 [...]
            FROM schema.collection
           WHERE _id <= [max _id value]
          {% endcapture %}

          {% include layout/code-snippet.html code=code language="sql" %}

          The MongoDB integration functions this way to ensure that replication for the table can resume if a replication job is interrupted or doesn't finish before [the extraction job time limit]({{ link.troubleshooting.database-extraction-errors | prepend: site.baseurl | append: "#time-limit" }}).

          Because MongoDB ranks BSON data types, this affects how the maximum `_id` value is determined. As a result, if multiple data types are present in the `_id` column, discrepancies may occur. Refer to the [Missing Mongo data due to multiple data types guide]({{ link.troubleshooting.mongo-multiple-data-types | prepend: site.baseurl }}) for more info and examples.
---
{% include misc/data-files.html %}
{% include misc/icons.html %}