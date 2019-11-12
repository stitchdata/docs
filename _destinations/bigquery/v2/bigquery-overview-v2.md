---
# -------------------------- #
#        Page Controls       #
# -------------------------- #
title: Google BigQuery v2 Destination Reference
permalink: /destinations/google-bigquery/reference/v2
keywords: bigquery, google bigquery, bigquery data warehouse, bigquery etl, etl to bigquery
summary: "Google BigQuery is a fully managed, cloud-based big data analytics web service for processing very large read-only data sets. BigQuery was designed for analyzing data on the order of billions of rows, using a SQL-like syntax."

destination: true
content-type: "destination-overview"
key: "bigquery-reference"

layout: general
sidebar: on-page
toc: false

this-version: "2"


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Connect a {{ page.display_name }} v2 destination"
    link: "{{ link.destinations.setup.bigquery | prepend: site.baseurl }}"

  - title: "TODO: Understanding loading behavior"
    link: "TODO"

  - title: "Loading nested structures in {{ page.display_name }}"
    link: "{{ link.destinations.storage.bigquery-nested-structures | prepend: site.baseurl }}"

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
## _data/destinations/bigquery/v2 for
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
    anchor: "replication-details"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "Replication process overview"
        anchor: "replication-process"
        content: |
          ![todo]({{ site.baseurl }}/images/destinations/bigquery-replication-process.png)

        sub-subsections:
          - title: "Step 1: Data extraction"
            anchor: "replication--data-extraction"
            content: |
              Stitch requests and extracts data from a data source. Refer to the [System overview guide]({{ link.getting-started.basic-concepts | prepend: site.baseurl | append: "#system-architecture--extraction" }}) for a more detailed explanation of the Extraction phase.

          - title: "Step 2: Stitch's internal pipeline"
            anchor: "replication--stitch-internal-pipeline"
            content: |
              The data extracted from sources is processed by Stitch. Stitch's internal pipeline includes the **Prepare** and **Load** phases of the replication process:

              - **Prepare**: {{ site.data.tooltips.prepare }}
              - **Load**: {{ site.data.tooltips.load }} Refer to the [Transformations](#transformations) section for more info about the transformations Stitch performs for {{ destination.display_name }} destinations.

              Refer to the [System overview guide]({{ link.getting-started.basic-concepts | prepend: site.baseurl | append: "#system-architecture--preparing" }}) for a more detailed explanation of these phases.

          - title: "Step 3: Google Cloud Storage bucket"
            anchor: "replication--gcs-bucket"
            content: |
              Stitch loads the data into a Stitch-owned Google Cloud Storage (GCS) bucket in the [region you select during destination setup](#supported-gcs-regions).

          - title: "Step 4: BigQuery staging tables"
            anchor: "replication--bigquery-staging-tables"
            content: |
              Using the IAM service account you provide during destination setup, data is read and transferred from the GCS bucket to staging tables in {{ destination.display_name }}. Staging tables from previous loads are deleted before the new load begins.

          - title: "Step 5: Data merge"
            anchor: "replication--data-merge"
            content: |
              Data is merged from the staging tables into datasets in {{ destination.display_name }}.

              The [loading behavior you select during setup](#loading-behavior) determines not only what the data looks like in the destination, but the method Stitch uses to load it. **Note**: The loading behavior can also affect your [{{ destination.display_name }} costs]({{ link.destinations.overviews.bigquery-pricing | prepend: site.baseurl | append:"#bigquery-query-pricing" }}).

              Once completed, the data is deleted from Stitch's internal GCS bucket.

      - title: "Loading behavior"
        anchor: "loading-behavior"
        content: |
          How data is loaded into {{ destination.display_name }} depends on the **Loading behavior** setting you define during destination setup:

          - **Upsert**: Existing rows are updated in tables with defined Primary Keys. A single version of a row will exist in the table.

          - **Append-Only**: Existing rows aren't updated. Multiple versions of a row can exist in a table, creating a log of how a row changed over time.

             Because of this loading strategy, querying may require a different strategy than usual. Using some of the system columns Stitch inserts into tables will enable you to locate the latest version of a record at query time. Refer to the [Querying Append-Only Tables documentation]({{ link.replication.append-only | prepend: site.baseurl }}) for more info.

          **Note**: Loading behavior can impact your [{{ destination.display_name }} costs]({{ link.destinations.overviews.bigquery-pricing | prepend: site.baseurl | append:"#bigquery-query-pricing" }}).

          [TODO - Add link to loading behavior guide]

      - title: "Primary Keys"
        anchor: "replication--primary-keys"
        content: |
          Stitch requires Primary Keys to de-dupe incrementally replicated data. To ensure Primary Key data is available, Stitch creates an `{{ stitch.system-tables.sdc-primary-keys.name }}`table in every integration dataset. This table contains a list of all tables in an integration's dataset and the columns those tables use as Primary Keys.

          Refer to the [{{ stitch.system-tables.sdc-primary-keys.name }} table documentation]({{ link.destinations.storage.primary-key-system-table | prepend: site.baseurl }}) for more info.

          **Note**: Removing or altering this table can lead to replication issues.

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
      - title: "Data typing"
        anchor: "transformations--data-typing"
        content: |
          Stitch converts data types only where needed to ensure the data is accepted by {{ destination.display_name }}. In the table below are the data types Stitch supports for {{ destination.display_name }} destinations, and the Stitch types they map to.

          Refer to the [Data typing documentation]({{ link.getting-started.basic-concepts | prepend: site.baseurl | append: "#data-typing" }}) for more info.

          {% include replication/templates/data-types/destination-data-types.html display-intro=true %}

      - title: "JSON structures"
        anchor: "transformations--json-structures"
        content: |
          {{ destination.display_name }} supports nested records within tables, whether it's a single record or repeated values. Refer to the [{{ destination.display_name }} and Storing Nested Data Structures documentation]({{ link.destinations.storage.bigquery-nested-structures | prepend: site.baseurl }}) for more info and examples.

      - title: "Column names"
        anchor: "transformations--column-naming"
        table:
          - transformation: "Convert uppercase and mixed case to lowercase"
            source-column: "<code>CUSTOMERID</code> or <code>cUsTomErId</code>"
            destination-column: &customerid "<code>customerid</code>"

          - transformation: "Convert spaces to underscores"
            source-column: "<code>customer id</code>"
            destination-column: &customerid2 "<code>customer_id</code>"

          - transformation: "Convert special characters to underscores"
            source-column: "<code>customer#id</code>"
            destination-column: *customerid2

          - transformation: "Remove leading non-letter characters, except for leading underscores"
            source-column: "<code>4customerid</code> or <code>!customerid</code>"
            destination-column: *customerid
        content: |
          Column names in {{ destination.display_name }}:

          {{ site.data.destinations.bigquery.destination-details.column-name-rules | flatify | markdownify }}

          Stitch will perform the following transformations to ensure column names [adhere to the rules imposed by {{ destination.display_name }}](https://cloud.google.com/bigquery/docs/schemas#column_names){:target="new"}:

          {% assign attributes = "transformation|source-column|destination-column" | split:"|" %}

          <table class="attribute-list">
          <tr>
          {% for attribute in attributes %}
          {% if forloop.first == true %}
          <td width="40%; fixed">
          {% else %}
          <td width="30%; fixed">
          {% endif %}
          <strong>{{ attribute | replace:"-"," " | capitalize }}</strong>
          </td>
          {% endfor %}
          </tr>
          {% for item in subsection.table %}
          <tr>
          {% for attribute in attributes %}
          <td>
          {{ item[attribute] }}
          </td>
          {% endfor %}
          </tr>
          {% endfor %}
          </table>

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