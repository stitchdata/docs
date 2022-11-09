---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/how-tos/destinations/add-destination-reference
## FOR INSTRUCTIONS & REFERENCE INFO

# -------------------------- #
#        Page Controls       #
# -------------------------- #

title: Microsoft SQL Server Destination Reference
permalink: /destinations/microsoft-sql-server/reference/
keywords: microsoft sql server, microsoft sql server data warehouse, microsoft sql server data warehouse, microsoft sql server etl, etl to microsoft sql server, microsoft sql server destination
summary: "Reference documentation for Stitch's Microsoft SQL Server destination, including info about Stitch features, replication, and transformations."

content-type: "destination-overview"
key: "microsoft-sql-server-reference"

layout: general
sidebar: on-page
toc: false


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Connect a {{ page.display_name }} destination"
    link: "{{ link.destinations.setup.microsoft-sql-server | prepend: site.baseurl }}"

  - title: "All {{ page.display_name }} docs"
    link: |
      {{ page.permalink | prepend: site.baseurl | remove: "/reference" }}


# -------------------------- #
#    Destination Details     #
# -------------------------- #

type: "microsoft-sql-server"
display_name: "Microsoft SQL Server"

this-version: "1"


# -------------------------- #
#           Support          #
# -------------------------- #

## See _data/destinations/microsoft-sql-server for
## info about connection support, Stitch support,
## data limitations, reserved words, etc.

## Resource links can be found in 
## _data/destinations/microsoft-sql-server/resource-links.yml


# -------------------------- #
#      Overview Content      #
# -------------------------- #

intro: |
  {{ site.data.destinations.microsoft-sql-server.destination-details.description | flatify }}

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
          By default, Stitch will use **{{ site.data.destinations.microsoft-sql-server.v1.replication.default-loading-behavior }} loading** when loading data into {{ destination.display_name }}.

          If the conditions for Upsert loading aren't met, data will be loaded using Append-Only loading.

          Refer to the [Understanding loading behavior guide]({{ link.destinations.storage.loading-behavior | prepend: site.baseurl }}) for more info and examples.

      - title: "Primary Keys"
        anchor: "replication--primary-keys"
        content: |
          If Primary Keys are specified, Stitch creates a table in which Primary Key columns have a `NOT NULL` constraint. Errors occur when:
            - Primary Key data types differ between records
            - Primary Key names differ between records
            - The number of Primary Keys differs between records

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

          {% include replication/templates/data-types/destination-data-types.html display-intro=true %}

      - title: "JSON structures"
        anchor: "transformations--json-structures"
        content: |
          When Stitch replicates source data containing objects or arrays, Stitch will load the data intact into a column with the type `NVARCHAR(MAX)`. This is a {{ destination.display_name }} data type that can contain semi-structured data like JSON arrays and objects.

          You can then use {{ destination.display_name }}'s functions for semi-structured data to parse the data. Refer to [{{ destination.display_name }}'s documentation]({{ site.data.destinations.microsoft-sql-server.resource-links.json-functions }}){:target="new"} for more info.

      - title: "Column names"
        anchor: "transformations--column-naming"
        content: |
          Column names in {{ destination.display_name }}:

          {{ site.data.destinations.microsoft-sql-server.destination-details.column-name-rules | flatify | markdownify }}

          Stitch will perform the following transformations to ensure column names [adhere to the rules imposed by {{ destination.display_name }}]({{ site.data.destinations.microsoft-sql-server.resource-links.object-names }}){:target="new"}:

          {% include destinations/templates/destination-column-name-transformations.html %}
        
      - title: "Table and schema names"
        anchor: "transformations--table-schema-naming"
        content: |
          Table and schema names in {{ destination.display_name }}:

          {{ site.data.destinations.microsoft-sql-server.destination-details.table-name-rules | flatify | markdownify }}

          Stitch will perform the following transformations to ensure table and schema names [adhere to the rules imposed by {{ destination.display_name }}]({{ site.data.destinations.microsoft-sql-server.resource-links.object-names }}){:target="new"}:

          {% include destinations/templates/destination-table-name-transformations.html %}

      - title: "Timezones"
        anchor: "transformations--timezones"
        content: |
          {{ destination.display_name }} will store the value as `DATETIMEOFFSET(3)`.

  - title: "Compare destinations"
    anchor: "compare-destinations"
    content: |
      **Not sure if {{ destination.display_name }} is the destination for you?** Check out the [Choosing a Stitch Destination]({{ link.destinations.overviews.choose-destination | prepend: site.baseurl }}) guide to compare each of Stitch's destination offerings.
---
{% include misc/data-files.html %}
{% assign destination = page %}