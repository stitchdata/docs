---
# -------------------------- #
#        Page Controls       #
# -------------------------- #
title: Google BigQuery v1 Destination Reference
permalink: /destinations/google-bigquery/v1/reference/

keywords: bigquery, google bigquery, bigquery data warehouse, bigquery etl, etl to bigquery
summary: "Reference documentation for version 1 of Stitch's Google BigQuery destination, including info about Stitch features, replication, and transformations."

destination: true
content-type: "destination-overview"
key: "bigquery-reference"

layout: general
sidebar: on-page
toc: false

this-version: "1"


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Connect a {{ page.display_name }} v1 destination"
    link: "{{ link.destinations.setup.bigquery-v1 | prepend: site.baseurl }}"

  - title: "TODO: Understanding loading behavior"
    link: "TODO"

  - title: "Stitch impact on {{ page.display_name }} costs"
    link: "{{ link.destinations.overviews.bigquery-pricing | prepend: site.baseurl }}"

  - title: "TODO: All {{ page.display_name }}"
    link: ""


# -------------------------- #
#    Destination Details     #
# -------------------------- #

display_name: "Google BigQuery"
type: &name "bigquery"
name: *name
description: "Google BigQuery is a fully managed, cloud-based big data analytics web service for processing very large read-only data sets. BigQuery was designed for analyzing data on the order of billions of rows, using a SQL-like syntax."


# -------------------------- #
#           Support          #
# -------------------------- #

## See _data/destinations/bigquery and 
## _data/destinations/bigquery/v1 for
## info about connection support, Stitch support,
## data limitations, reserved words, etc.

## Resource links can be found in:
## _data/destinations/bigquery/resource-links.yml

# -------------------------- #
#      Overview Content      #
# -------------------------- #

intro: |
  {{ destination.description }}

  For more information, check out [Google's {{ destination.display_name }} overview]({{ site.data.destinations.bigquery.resource-links.what-is-bq }}){:target="new"}.

  This guide serves as a reference for version {{ destination.this-version }} of Stitch's {{ destination.display_name }} destination.

sections:
  - title: "Details and features"
    anchor: "details-and-features"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Stitch features"
        anchor: "stitch-features"
        content: |
          {% include destinations/overviews/destination-reference-table.html category="stitch-details" %}

      - title: "Destination details"
        anchor: "destination-details"
        content: |
          {% include destinations/overviews/destination-reference-table.html category="destination-details" %}

      - title: "Supported Google Cloud Storage regions"
        anchor: "supported-gcs-regions"
        content: |
          When you set up a {{ destination.display_name }} destination, you'll select a Google Storage location. This determines the location of the internal Google Storage bucket Stitch uses during the replication process.

          Stitch supports the following Google Cloud Storage regions for version {{ destination.this-version }} of the {{ destination.display_name }} destination:

          {% include destinations/templates/bigquery-supported-regions-table.html %}

      - title: "Google BigQuery pricing"
        anchor: "pricing"
        content: |
          Unlike many other cloud-based data warehouse solutions, {{ destination.display_name }}'s pricing model is based on **usage** and not a fixed-rate. This means that your bill can vary over time. 

          Before fully committing yourself to using {{ destination.display_name }} as your data warehouse, we recommend familiarizing yourself with the {{ destination.display_name }} pricing model and how using Stitch may impact your costs.

          **[Learn more about Stitch & {{ destination.display_name }} pricing]({{ link.destinations.overviews.bigquery-pricing | prepend: site.baseurl }})**

  - title: "Replication"
    anchor: "replication"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Loading behavior"
        anchor: "loading-behavior"
        content: |
          Stitch will use Append-Only replication when loading data into this version of the {{ destination.display_name }} destination.

          In Append-Only replication, existing rows aren't updated. Multiple versions of a row can exist in a table, creating a log of how a row changed over time. **Note**: While this may look like a discrepancy, it is intended functionality for {{ destination.display_name }} {{ destination.this-version | prepend: "v" }} destinations.

          Because of this loading strategy, querying may require a different strategy than usual. Using some of the system columns Stitch inserts into tables will enable you to locate the latest version of a record at query time. Refer to the [Querying Append-Only Tables documentation]({{ link.replication.append-only | prepend: site.baseurl }}) for more info.

          More info and examples can be found in the [Replication Method documentation]({{ link.replication.append-only | prepend: site.baseurl }}) and [Append-Only querying guide]({{ link.replication.append-only-querying | prepend: site.baseurl }}).

          [TODO - Add link to loading behavior guide]

      - title: "Primary Keys"
        anchor: "replication--primary-keys"
        content: |
          {{ destination.display_name }} destinations don't have native support for Primary Keys. While Primary Key columns will be present in destination tables, no constraints will be applied to the columns.

      - title: "Incompatible sources"
        anchor: "replication--incompatible-sources"
        content: |
          TODO

  - title: "Transformations"
    anchor: "transformations"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "System tables and columns"
        anchor: "transformations--system-tables-columns"
        content: |
          Stitch will create the following tables in each integration's dataset:

          - [{{ stitch.system-tables.sdc-rejected.name }}]({{ link.destinations.storage.rejected-records | prepend: site.baseurl }})

          Additionally, Stitch will insert [system columns]({{ link.destinations.storage.system-tables-and-columns | prepend: site.baseurl }}) (prepended with `{{ system-column.prefix }}`) into each table.

      - title: "Data typing"
        anchor: "transformations--data-typing"
        content: |
          Stitch converts data types only where needed to ensure the data is accepted by {{ destination.display_name }}. In the table below are the data types Stitch supports for {{ destination.display_name }} destinations, and the Stitch types they map to.

          Refer to the [Data typing documentation]({{ link.getting-started.basic-concepts | prepend: site.baseurl | append: "#data-typing" }}) for more info.

          {% include replication/templates/data-types/destination-data-types.html display-intro=true %}

      - title: "Column names"
        anchor: "transformations--column-naming"
        content: |
          Column names in {{ destination.display_name }}:

          {{ site.data.destinations.bigquery.destination-details.column-name-rules | flatify | markdownify }}

          Stitch will perform the following transformations to ensure column names [adhere to the rules imposed by {{ destination.display_name }}](https://cloud.google.com/bigquery/docs/schemas#column_names){:target="new"}:

          {% include destinations/templates/destination-column-name-transformations.html %}

      - title: "Timezones"
        anchor: "transformations--timezones"
        content: |
          [TODO]({{ link.getting-started.basic-concepts | prepend: site.baseurl | append: "#timezones" }})

          {{ destination.display_name }} will store the value in UTC as `TIMESTAMP`.

          More info about timestamp data types can be found in [BigQuery's documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#timestamp-type){:target="new"}.

  - title: "Compare destinations"
    anchor: "compare-destinations"
    content: |
      **Not sure if {{ destination.display_name }} is the data warehouse for you?** Check out the [Choosing a Stitch Destination]({{ link.destinations.overviews.choose-destination | prepend: site.baseurl }}) guide to compare each of Stitch's destination offerings.
---
{% assign destination = page %}
{% include misc/data-files.html %}