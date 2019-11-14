---
# -------------------------- #
#        Page Controls       #
# -------------------------- #
title: PostgreSQL Destination
permalink: /destinations/postgresql/v1/reference
keywords: postgres, postgresql, postgres data warehouse, postgres etl, etl to postgres, postgresql data warehouse, etl to postgresql
summary: "Reference documentation for Stitch's PostgreSQL destination, including info about Stitch features, replication, and transformations."

destination: true
content-type: "destination-overview"
key: "postgresql-reference"

layout: general
sidebar: on-page
toc: false


# -------------------------- #
#    Destination Details     #
# -------------------------- #

display_name: "PostgreSQL"
type: "postgres"

this-version: "1"

# -------------------------- #
#           Support          #
# -------------------------- #

## See _data/destinations/postgres for
## info about connection support, Stitch support,
## data limitations, reserved words, etc.

## Resource links can be found in 
## _data/destinations/postgres/resource-links.yml


# -------------------------- #
#      Overview Content      #
# -------------------------- #

intro: |
  {{ site.data.destinations.postgres.destination-details.description | flatify }}

  For a more in-depth look at {{ destination.display_name }}, [click here]({{ site.data.destinations.postgres.resource-links.main-site }}){:target="new"}.

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

      - title: "{{ page.display_name }} pricing"
        anchor: "pricing"
        content: |
          Pricing for {{ destination.display_name }} depends on where your instance is hosted.

          - **Self-hosted:** {{ destination.display_name }} is open-source, meaning you don't need to pay an upfront cost to obtain the necessary software. You may, however, have hosting and maintenance costs associated with the server housing the instance. You may have to do a little bit of internal number crunching to figure out these potential costs. 

          - **Heroku:** Heroku has a [variety of plans to choose from](https://www.heroku.com/pricing), and [a guide to help you select the right plan](https://devcenter.heroku.com/articles/heroku-postgres-plans){:target="new"} for you or your company.

          - **Amazon Aurora and RDS:** Amazon offers [a variety of plans](https://aws.amazon.com/rds/postgresql/pricing/) for both on-demand instances and Multi-AZ Deployment. To get an estimate of what your monthly bill might look like, check out their [monthly calculator]({{ site.data.destinations.postgres.resource-links.aws-calculator }}){:target="new"}.

          - **Google CloudSQL PostgreSQL:** Unlike many other cloud-based data warehouse solutions, [Google's pricing model]({{ site.data.destinations.postgres.resource-links.cloudsql-pricing }}){:target="new"} is based on **usage** and not a fixed-rate. This means that your bill can vary over time. 

             Before fully committing yourself to using Google CloudSQL PostgreSQL as your data warehouse, we recommend familiarizing yourself with Google's pricing model and [using their pricing calculator to estimate your potential costs]({{ site.data.destinations.postgres.resource-links.price-calculator }}){:target="new"}.

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
          When data is loaded into {{ destination.display_name }}, Stitch will upsert the data. This means that existing rows are updated in tables with [defined Primary Keys](#replication--primary-keys). A single version of a row will exist in the table.

          If a table doesn't have defined Primary Keys, data will be loaded in an Append-Only fashion. New rows and modifications to existing rows will be appended at the end of the table. Multiple versions of a row can exist in a table, creating a log of how a row changed over time.

          [TODO - Add link to loading behavior guide]

      - title: "Primary Keys"
        anchor: "replication--primary-keys"
        content: |
          Stitch requires Primary Keys to de-dupe incrementally replicated data. When tables are created in the destination, Stitch will apply [Primary Key constraints](https://www.postgresql.org/docs/10/static/ddl-constraints.html#DDL-CONSTRAINTS-PRIMARY-KEYS){:target="new"} to columns used as Primary Keys. Primary Key constraints require that column values be unique and not null.

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

      - title: "Data typing"
        anchor: "transformations--data-typing"
        content: |
          Stitch converts data types only where needed to ensure the data is accepted by {{ destination.display_name }}. In the table below are the data types Stitch supports for {{ destination.display_name }} destinations, and the Stitch types they map to.

          Refer to the [Data typing documentation]({{ link.getting-started.basic-concepts | prepend: site.baseurl | append: "#data-typing" }}) for more info.

          {% include replication/templates/data-types/destination-data-types.html display-intro=true %}

      - title: "JSON structures"
        anchor: "transformations--json-structures"
        content: |
          {{ destination.display_name }} destinations don't have native support for nested data structures. To ensure nested data can be loaded, Stitch will flatten objects and arrays into columns and subtables, respectively. For more info and examples, refer to the [Handling nested data structures guide]({{ link.destinations.storage.nested-structures | prepend: site.baseurl }}).

      - title: "Column names"
        anchor: "transformations--column-naming"
        content: |
          Column names in {{ destination.display_name }}:

          {{ site.data.destinations.postgres.destination-details.column-name-rules | flatify | markdownify }}

          Stitch will perform the following transformations to ensure column names adhere to the rules imposed by {{ destination.display_name }}:

          {% include destinations/templates/destination-column-name-transformations.html %}

      - title: "Timezones"
        anchor: "transformations--timezones"
        content: |
          [TODO]({{ link.getting-started.basic-concepts | prepend: site.baseurl | append: "#timezones" }})

          {{ destination.display_name }} will store the value as `TIMESTAMP WITH TIMEZONE`. In {{ destination.display_name }}, this data is stored with timezone information and expressed as UTC.

  - title: "Compare destinations"
    anchor: "compare-destinations"
    content: |
      **Not sure if {{ destination.display_name }} is the data warehouse for you?** Check out the [Choosing a Stitch Destination]({{ link.destinations.overviews.choose-destination | prepend: site.baseurl }}) guide to compare each of Stitch's destination offerings.
---
{% assign destination = page %}
{% include misc/data-files.html %}