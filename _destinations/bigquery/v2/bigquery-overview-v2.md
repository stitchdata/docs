---
# -------------------------- #
#        Page Controls       #
# -------------------------- #
title: Google BigQuery v2 Destination Reference
permalink: /destinations/google-bigquery/reference/v2
keywords: bigquery, google bigquery, bigquery data warehouse, bigquery etl, etl to bigquery
summary: "Google BigQuery is a fully managed, cloud-based big data analytics web service for processing very large read-only data sets. BigQuery was designed for analyzing data on the order of billions of rows, using a SQL-like syntax."

content-type: "destination-overview"
key: "bigquery-reference"

toc: true
layout: general
destination: true

this-version: "2.0"


# -------------------------- #
#    Destination Details     #
# -------------------------- #

display_name: "BigQuery"
type: &name "bigquery"
name: *name
description: "Google BigQuery is a fully managed, cloud-based big data analytics web service for processing very large read-only data sets. BigQuery was designed for analyzing data on the order of billions of rows, using a SQL-like syntax."


# -------------------------- #
#           Support          #
# -------------------------- #

## See _data/destinations/reference/bigquery.yml for
## info about connection support, Stitch support,
## data limitations, reserved words, etc.

## Resource links can be found in _data/destinations/links.yml

# -------------------------- #
#      Overview Content      #
# -------------------------- #

introduction: |
  {{ destination.description }}

  For more information, check out [Google's {{ destination.display_name }} overview]({{ destination.what-is-bq }}).

sections:
  - title: "Pricing"
    anchor: "pricing"
    content: |
      Unlike many other cloud-based data warehouse solutions, {{ destination.display_name }}'s pricing model is based on **usage** and not a fixed-rate. This means that your bill can vary over time. 

      Before fully committing yourself to using {{ destination.display_name }} as your data warehouse, we recommend familiarizing yourself with the {{ destination.display_name }} pricing model and how using Stitch may impact your costs.

      **[Learn more about Stitch & {{ destination.display_name }} pricing]({{ link.destinations.overviews.bigquery-pricing | prepend: site.baseurl }})**

  - title: "Setup info"
    anchor: "stitch-details-setup-info"
    content: |
      {% include destinations/overviews/destination-reference-table.html list="stitch-details" %}

  - title: "Replication"
    anchor: "replication"
    content: |
      {% include destinations/overviews/destination-reference-table.html list="replication" %}
    subsections:
      - title: "Replication process overview"
        anchor: "process"
        content: |
          ![todo]({{ site.baseurl }}/images/destinations/bigquery-replication-process.png)

      - title: "Loading behavior"
        anchor: "loading-behavior"
        content: |
          How data is loaded into {{ destination.display_name }} depends on the **Loading behavior** setting you define during destination setup:

          - **Upsert**: Existing rows are updated in tables with defined Primary Keys. A single version of a row will exist in the table.

          - **Append-Only**: Existing rows aren't updated. Multiple versions of a row can exist in a table, creating a log of how a row changed over time.

             Because of this loading strategy, querying may require a different strategy than usual. Using some of the system columns Stitch inserts into tables will enable you to locate the latest version of a record at query time. Refer to the [Querying Append-Only Tables documentation]({{ link.replication.append-only | prepend: site.baseurl }}) for more info.

          **Note**: Loading behavior can impact your {{ destination.display_name }} costs. Refer to the [TODO](todo) guide for more info.


  - title: "Limitations"
    anchor: "limitations"
    content: |
      In this section:

      {% assign list-items = "object-name-limits|table-limits|data-limits|column-naming" | split: "|" %}

      {% for item in list-items %}
      {% for category in reference-categories[item] %}
      - [**{{ category.name }}**](#{{ item }}) - {{ category.description | flatify }}
      {% endfor %}
      {% endfor %}

    subsections:
      - title: "Object name limits"
        anchor: "object-name-limits"
        content: |
          {% include destinations/overviews/destination-reference-table.html list="object-name-limits" %}

      - title: "Table limits"
        anchor: "table-limits"
        content: |
          {% include destinations/overviews/destination-reference-table.html list="table-limits" %}

      - title: "Data limits"
        anchor: "data-limits"
        content: |
          {% include destinations/overviews/destination-reference-table.html list="data-limits" %}

      - title: "Column naming"
        anchor: "column-naming"
        content: |
          {% include destinations/overviews/destination-reference-table.html list="column-naming" %}

  - title: "Compare destinations"
    anchor: "compare-destinations"
    content: |
      **Not sure if {{ destination.display_name }} is the data warehouse for you?** Check out the [Choosing a Stitch Destination]({{ link.destinations.overviews.choose-destination | prepend: site.baseurl }}) guide to compare each of Stitch's destination offerings.
---
{% assign destination = page %}
{% include misc/data-files.html %}