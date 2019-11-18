---
# -------------------------- #
#        Page Controls       #
# -------------------------- #

title: Snowflake Destination Reference
permalink: /destinations/snowflake/v1/reference
keywords: snowflake, snowflake destination, snowflake data warehouse, snowflake etl, etl to snowflake
summary: "Reference documentation for Stitch's Snowflake destination, including info about Stitch features, replication, and transformations."

destination: true
content-type: "destination-overview"
key: "snowflake-reference"

layout: general
sidebar: on-page
toc: false


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Connect a {{ page.display_name }} destination"
    link: "{{ link.destinations.setup.snowflake | prepend: site.baseurl }}"

  - title: "Loading nested structures in {{ page.display_name }}"
    link: ""

  - title: "TODO: All {{ page.display_name }} docs"
    link: ""


# -------------------------- #
#    Destination Details     #
# -------------------------- #

display_name: "Snowflake"
type: "snowflake"

this-version: "1"


# -------------------------- #
#           Support          #
# -------------------------- #

## See _data/destinations/snowflake for
## info about connection support, Stitch support,
## data limitations, reserved words, etc.

## Resource links can be found in:
## _data/destinations/snowflake/resource-links.yml


# -------------------------- #
#      Overview Content      #
# -------------------------- #
intro: |
  {{ site.data.destinations.snowflake.destination-details.description | flatify }}

  A fully-managed SaaS data warehouse solution, Snowflake runs on [Amazon Web Services](http://aws.amazon.com/){:target="new"} cloud infrastructure: AWS EC2 virtual compute instances are used for compute needs, while S3 is utilized for persistent data storage.

  This guide serves as a reference for version {{ destination.this-version }} of Stitch's {{ destination.display_name }} destination.

sections:
  - title: "Details and features"
    anchor: "details-and-features"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title | flatify }}](#{{ subsection.anchor }})
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

      - title: "Snowflake pricing"
        anchor: "pricing"
        content: |
          {{ site.data.destinations.snowflake.destination-details.pricing-details | flatify }}
        sub-subsections:
          - title: "Snowflake warehouse sizes"
            anchor: "warehouse-sizes"
            content: |
              Snowflake data warehouses can be different sizes - X-Small, Large, and 3X-Large, for example - which defines how many servers will comprise each cluster in a warehouse.

              While the size of a warehouse can impact the time required to execute queries, bigger doesn't always mean better. Warehouse size is directly tied to the number of credits used, which will directly impact your Snowflake costs. [Learn more about Snowflake warehouse sizes here](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html){:target="_blank"}.

              To help you select the warehouse size that fits your needs and budget, check out [Snowflake's Warehouse Considerations guide](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html){:target="_blank"} before getting started.

          - title: "Automated warehouse management"
            anchor: "automated-warehouse-management"
            content: |
              To reduce usage, you can elect to automate the management of your Snowflake warehouse. This means that you can elect to suspend the warehouse when there's no activity after a specified period of time, and then automatically resume when there is. Note that these settings apply to the entire warehouse and not individual clusters.

              Enabling these settings depends on your workload and availability needs. [Learn more about the Auto Suspend and Auto Resume features here](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html#automating-warehouse-management){:target="_blank"}.

              **Note**: Stitch will only ever impact your Snowflake usage when loading data.

  - title: "Replication"
    anchor: "replication"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "Replication process overview"
        anchor: "replication-process-overview"
        content: |
          A Stitch replication job consists of three stages:

          {% for sub-subsection in subsection.sub-subsections %}
          - [{{ sub-subsection.title }}](#{{ sub-subsection.anchor }})
          {% endfor %}
        sub-subsections:
          - title: "Step 1: Data extraction"
            anchor: "replication--data-extraction"
            content: |
              {% include replication/replication-process-phases.html phase="data-extraction" %}

          - title: "Step 2: Preparation"
            anchor: "replication--stitch-internal-pipeline"
            content: |
              {{ site.data.tooltips.prepare }} Refer to the [System overview guide]({{ link.getting-started.basic-concepts | prepend: site.baseurl | append: "#system-architecture--preparing" }}) for a more detailed explanation of the Preparation phase.

          - title: "Step 3: Loading"
            anchor: "replication--loading"
            content: |
              Stitch loads the data into {{ destination.display_name }}.

      - title: "Loading behavior"
        anchor: "loading-behavior"
        content: |
          {% assign version = destination.this-version | prepend: "v" %} 
          By default, Stitch will use **{{ site.data.destinations[destination.type][version]replication.default-loading-behavior }} loading** when loading data into {{ destination.display_name }}.

          If the conditions for Upsert loading aren't met, data will be loaded using Append-Only loading.

          Refer to the [Understanding loading behavior guide]({{ link.destinations.storage.loading-behavior | prepend: site.baseurl }}) for more info and examples.

      - title: "Primary Keys"
        anchor: "replication--primary-keys"
        content: |
          Stitch requires Primary Keys to de-dupe incrementally replicated data. When tables are created in the destination, Stitch will apply [Primary Key constraints](https://docs.snowflake.net/manuals/sql-reference/constraints-overview.html){:target="new"} to columns used as Primary Keys. Primary Key constraints require that column values be unique and not null.

      - title: "Incompatible sources"
        anchor: "replication--incompatible-sources"
        content: |
          {% include shared/incompatibilities/destination-version-incompatibilities.html %}

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

# Refer to the [Data typing documentation]({{ link.getting-started.basic-concepts | prepend: site.baseurl | append: "#data-typing" }}) for more info.
      - title: "Data typing"
        anchor: "transformations--data-typing"
        content: |
          Stitch converts data types only where needed to ensure the data is accepted by {{ destination.display_name }}. In the table below are the data types Stitch supports for {{ destination.display_name }} destinations, and the Stitch types they map to.

          {% include replication/templates/data-types/destination-data-types.html display-intro=true %}

      - title: "JSON structures"
        anchor: "transformations--json-structures"
        content: |
          When Stitch replicates source data containing objects or arrays, Stitch will load the data intact into a [`VARIANT` column]({{ site.data.destinations.snowflake.resource-links.variant-type }}){:target="new"}. This is a {{ destination.display_name }} data type that can contain semi-structured data like JSON arrays and objects.

          You can then use {{ destination.display_name }}'s functions for semi-structured data to parse the data. Refer to [{{ destination.display_name }}'s documentation](https://docs.snowflake.net/manuals/sql-reference/functions-semistructured.html){:target="new"} for more info.

      - title: "Column names"
        anchor: "transformations--column-naming"
        content: |
          Column names in {{ destination.display_name }}:

          {{ site.data.destinations.snowflake.destination-details.column-name-rules | flatify | markdownify }}

          Stitch will perform the following transformations to ensure column names adhere to the rules imposed by {{ destination.display_name }}:

          {% include destinations/templates/destination-column-name-transformations.html %}

      - title: "Timezones"
        anchor: "transformations--timezones"
        content: |
          [TODO]({{ link.getting-started.basic-concepts | prepend: site.baseurl | append: "#timezones" }})

          {{ destination.display_name }} will store the value as `TIMESTAMP_TZ(9)` and express it as UTC.

  - title: "Compare destinations"
    anchor: "compare-destinations"
    content: |
      **Not sure if {{ destination.display_name }} is the data warehouse for you?** Check out the [Choosing a Stitch Destination]({{ link.destinations.overviews.choose-destination | prepend: site.baseurl }}) guide to compare each of Stitch's destination offerings.
---
{% assign destination = page %}
{% include misc/data-files.html %}