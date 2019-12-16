---
# -------------------------- #
#        Page Controls       #
# -------------------------- #

title: DESTINATION-NAME Destination Reference
permalink: /destinations/destination-type/<version, if applicable>/reference
keywords: destination-type, destination-type data warehouse, destination-type data warehouse, destination-type etl, etl to destination-type, destination-type destination
summary: "Reference documentation for Stitch's DESTINATION-NAME destination, including info about Stitch features, replication, and transformations."

destination: true
content-type: "destination-overview"
key: "destination-type-reference"

layout: general
sidebar: on-page
toc: false


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Connect a {{ page.display_name }} destination"
    link: "{{ link.destinations.setup.destination-type | prepend: site.baseurl }}"

  - title: ""
    link: ""

  - title: "All {{ page.display_name }} docs"
    link: |
      {{ page.permalink | prepend: site.baseurl | remove: "/reference" }}


# -------------------------- #
#    Destination Details     #
# -------------------------- #

type: "destination-type"
display_name: "DESTINATION-NAME"

this-version: ""


# -------------------------- #
#           Support          #
# -------------------------- #

## See _data/destinations/destination-type for
## info about connection support, Stitch support,
## data limitations, reserved words, etc.

## Resource links can be found in 
## _data/destinations/destination-type/resource-links.yml


# -------------------------- #
#      Overview Content      #
# -------------------------- #

intro: |
  {{ site.data.destinations.destination-type.destination-details.description | flatify }}

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
          > INCLUDE IF RELEVANT.

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
          > IN GENERAL, THIS CONTENT WILL SUFFICE. IF ADDITIONAL INFO IS AVAILABLE ABOUT HOW DATA IS LOADED, INCLUDE IT. EX: HOW BIGQUERY AND AZURE WORK.

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

          > DEFAULT UPSERT LOADING:
          If the conditions for Upsert loading aren't met, data will be loaded using Append-Only loading.

          > DEFAULT APPEND-ONLY LOADING:
          In Append-Only replication, existing rows aren't updated. Multiple versions of a row can exist in a table, creating a log of how a row changed over time. **Note**: While this may look like a discrepancy, it is intended functionality for {{ destination.display_name }} {{ destination.this-version | prepend: "v" }} destinations.

          Because of this loading strategy, querying may require [a different strategy than usual]({{ link.replication.append-only | prepend: site.baseurl }}). Using some of the system columns Stitch inserts into tables will enable you to locate the latest version of a record at query time.

          Refer to the [Understanding loading behavior guide]({{ link.destinations.storage.loading-behavior | prepend: site.baseurl }}) for more info and examples.

      - title: "Primary Keys"
        anchor: "replication--primary-keys"
        content: |
          > HOW DOES THE DESTINATION HANDLE PRIMARY KEYS, IF AT ALL?

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
          > ADD OTHER TABLES OR COLUMNS IF NECESSARY.

          Stitch will create the following tables in each integration's dataset:

          - [{{ stitch.system-tables.sdc-rejected.name }}]({{ link.destinations.storage.rejected-records | prepend: site.baseurl }})

          Additionally, Stitch will insert [system columns]({{ link.destinations.storage.system-tables-and-columns | prepend: site.baseurl }}) (prepended with `{{ system-column.prefix }}`) into each table.

      - title: "Data typing"
        anchor: "transformations--data-typing"
        content: |
          Stitch converts data types only where needed to ensure the data is accepted by {{ destination.display_name }}. In the table below are the data types Stitch supports for {{ destination.display_name }} destinations, and the Stitch types they map to.

          {% include replication/templates/data-types/destination-data-types.html display-intro=true %

      - title: "JSON structures"
        anchor: "transformations--json-structures"
        content: |
          > NO NATIVE SUPPORT:

          {{ destination.display_name }} destinations don't have native support for nested data structures. To ensure nested data can be loaded, Stitch will flatten objects and arrays into columns and subtables, respectively. For more info and examples, refer to the [Handling nested data structures guide]({{ link.destinations.storage.nested-structures | prepend: site.baseurl }}).

          > NATIVE SUPPORT:

          > NATIVE SUPPORT, BQ-LIKE APPROACH:
          {{ destination.display_name }} supports nested records within tables, whether it's a single record or repeated values. This means that when nested data structures are loaded into {{ destination.display_name }}, they will be maintained.

          > NATIVE SUPPORT, USING A SPECIFIC DATA TYPE:

          When Stitch replicates source data containing objects or arrays, Stitch will load the data intact into a [`` column](). This is a {{ destination.display_name }} data type that can contain semi-structured data like JSON arrays and objects.

          You can then use {{ destination.display_name }}'s functions for semi-structured data to parse the data. Refer to [{{ destination.display_name }}'s documentation](){:target="new"} for more info.

      - title: "Column names"
        anchor: "transformations--column-naming"
        content: |
          Column names in {{ destination.display_name }}:

          {{ site.data.destinations.destination-type.destination-details.column-name-rules | flatify | markdownify }}

          Stitch will perform the following transformations to ensure column names [adhere to the rules imposed by {{ destination.display_name }}]({{ site.data.destinations.destination-type.resource-links.object-names }}){:target="new"}:

          {% include destinations/templates/destination-column-name-transformations.html %}

      - title: "Timezones"
        anchor: "transformations--timezones"
        content: |
          {{ destination.display_name }} will store the value as `TIMESTAMP WITHOUT TIMEZONE`. In {{ destination.display_name }}, this data is stored without timezone information and expressed as UTC.

  - title: "Compare destinations"
    anchor: "compare-destinations"
    content: |
      **Not sure if {{ destination.display_name }} is the destination for you?** Check out the [Choosing a Stitch Destination]({{ link.destinations.overviews.choose-destination | prepend: site.baseurl }}) guide to compare each of Stitch's destination offerings.
---
{% include misc/data-files.html %}
{% assign destination = page %}