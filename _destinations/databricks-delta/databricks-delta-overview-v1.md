---
# -------------------------- #
#        Page Controls       #
# -------------------------- #

title: Databricks Delta Destination Reference
permalink: /destinations/databricks-delta/reference
keywords: delta, databricks delta, delta data warehouse, databricks delta etl, etl to databricks delta
summary: "Reference documentation for Stitch's Databricks Delta destination, including info about Stitch features, replication, and transformations."

content-type: "destination-overview"
key: "databricks-delta-reference"

layout: general
sidebar: on-page
toc: false


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Connect a {{ page.display_name }} destination"
    link: "{{ link.destinations.setup.databricks-delta | prepend: site.baseurl }}"

  - title: "All {{ page.display_name }} docs"
    link: |
      {{ page.permalink | prepend: site.baseurl | remove: "/reference" }}


# -------------------------- #
#    Destination Details     #
# -------------------------- #

display_name: "Databricks Delta"
name: "databricks-delta"
type: "databricks-delta"

this-version: "1"


# -------------------------- #
#           Support          #
# -------------------------- #

## See _data/destinations/databricks-delta for
## info about connection support, Stitch support,
## data limitations, reserved words, etc.

## Resource links can be found in 
## _data/destinations/databricks-delta/resource-links.yml

# -------------------------- #
#      Overview Content      #
# -------------------------- #

intro: |
  {{ site.data.destinations.databricks-delta.destination-details.description | flatify }}

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

          - title: "Step 2: Stitch's internal pipeline"
            anchor: "replication--stitch-internal-pipeline"
            content: |
              {% include replication/replication-process-phases.html phase="internal-pipeline" %}

          - title: "Step 3: Amazon S3 bucket"
            anchor: "replication--amazon-s3-bucket"
            content: |
              Data is loaded into the Amazon S3 bucket you provide during destination setup. During this step, the data is staged before being merged into {{ destination.display_name }}.

          - title: "Step 4: Data merge"
            anchor: "replication--amazon-s3-bucket"
            content: |
              Data is merged from the staging tables into tables in {{ destination.display_name }}.

      - title: "Loading behavior"
        anchor: "loading-behavior"
        content: |
          {% assign version = destination.this-version | prepend: "v" %} 
          By default, Stitch will use **{{ site.data.destinations.databricks-delta.v1.replication.default-loading-behavior }} loading** when loading data into {{ destination.display_name }}.

          If the conditions for Upsert loading aren't met, data will be loaded using Append-Only loading.

          Refer to the [Understanding loading behavior guide]({{ link.destinations.storage.loading-behavior | prepend: site.baseurl }}) for more info and examples.

      - title: "Primary Keys"
        anchor: "replication--primary-keys"
        content: |
          Stitch requires Primary Keys to de-dupe incrementally replicated data. To ensure Primary Key data is available, Stitch creates a `stitch.pks` [table property comment]({{ site.data.destinations.databricks-delta.resource-links.table-properties }}){:target="new"} when the table is initially created in {{ destination.display_name }}. The table property comment is an array of strings that contain the names of the Primary Key columns for the table. 

          For example: A table property comment for a table with a single Primary Key:

          ```json
          (stitch.pks='id')
          ```

          And a table property comment for a table with a composite Primary Key:

          ```json
          (stitch.pks='id,created_at')
          ```

          **Note**: Removing or incorrectly altering Primary Key table property comments can lead to replication issues.

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
          {{ destination.display_name }} supports nested records within tables. When JSON objects and arrays are replicated, Stitch will load the JSON intact into a `STRING` column and add a property of `"json"` to the column.

          For example: [TODO]

          Refer to [Databricks' documentation]({{ site.data.destinations.databricks-delta.resource-links.complex-data }}){:target="new"} for examples and instructions on working with complex data structures.

      - title: "Column names"
        anchor: "transformations--column-naming"
        content: |
          Column names in {{ destination.display_name }}:

          {{ site.data.destinations.databricks-delta.destination-details.column-name-rules | flatify | markdownify }}

          Stitch will perform the following transformations to ensure column names [adhere to the rules imposed by {{ destination.display_name }}]({{ site.data.destinations.databricks-delta.resource-links.object-names }}){:target="new"}:

          {% include destinations/templates/destination-column-name-transformations.html %}

      - title: "Timezones"
        anchor: "transformations--timezones"
        content: |
          {{ destination.display_name }} will store the value as `TIMESTAMP WITHO TIMEZONE`. In {{ destination.display_name }}, this data is stored with timezone information and expressed as UTC.

  - title: "Compare destinations"
    anchor: "compare-destinations"
    content: |
      **Not sure if {{ destination.display_name }} is the destination for you?** Check out the [Choosing a Stitch Destination]({{ link.destinations.overviews.choose-destination | prepend: site.baseurl }}) guide to compare each of Stitch's destination offerings.
---
{% assign destination = page %}
{% include misc/data-files.html %}