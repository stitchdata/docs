---
# -------------------------- #
#        Page Controls       #
# -------------------------- #
title: Microsoft Azure SQL Data Warehouse Destination Reference
permalink: /destinations/microsoft-azure-sql-data-warehouse/reference
keywords: microsoft azure, microsoft azure, microsoft azure data warehouse, microsoft azure etl, etl to microsoft azure
summary: "Reference documentation for Stitch's Microsoft Azure SQL Data Warehouse destination, including info about Stitch features, replication, and transformations."

content-type: "destination-overview"
key: "microsoft-azure-reference"

layout: general
sidebar: on-page
toc: false

data-loading: false


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Connect an {{ page.display_name }} destination"
    link: "{{ link.destinations.setup.azure | prepend: site.baseurl }}"

  - title: "Primary Keys system table"
    link: "{{ link.destinations.storage.primary-key-system-table | prepend: site.baseurl }}"

  - title: "All {{ page.display_name }} docs"
    link: |
      {{ page.permalink | prepend: site.baseurl | remove: "/reference" }}


# -------------------------- #
#    Destination Details     #
# -------------------------- #

display_name: "Microsoft Azure SQL Data Warehouse"
type: "microsoft-azure"
db-type: "mssql"

this-version: "1"


# -------------------------- #
#           Support          #
# -------------------------- #

## See _data/destinations/microsoft-azure for
## info about connection support, Stitch support,
## data limitations, reserved words, etc.

## Resource links can be found in
## _data/destinations/microsoft-azure/resource-links.yml

# -------------------------- #
#      Overview Content      #
# -------------------------- #

intro: |
  {% capture setup-notice %}
  Stitch's {{ destination.display_name }} destination only works with Microsoft's [Azure SQL Data Warehouse product](https://azure.microsoft.com/en-us/services/sql-data-warehouse/){:target="new"}.

  Stitch doesn't currently support using Azure SQL Server or Azure SQL Database as a destination.
  {% endcapture %}

  {% include note.html first-line="**Stitch only supports connecting to Azure SQL Data Warehouse instances**" content=setup-notice %}

  {{ site.data.destinations.microsoft-azure.destination-details.description | flatify }}

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
          {{ site.data.destinations.microsoft-azure.destination-details.pricing-details | flatify }}

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
          {% for sub-subsection in subsection.sub-subsections %}
          - [{{ sub-subsection.title | flatify }}](#{{ sub-subsection.anchor }})
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

          - title: "Step 3: Load data into Azure Blob Storage"
            anchor: "load-into-blob-storage"
            content: |
              Stitch loads the extracted data into [Azure Blob Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction){:target="new"}.

              Blob storage is intended for storing massive amounts of unstructured data. In the next step, Stitch will use Polybase to retrieve the data from Blob Storage and prepare it for loading into {{ destination.display_name }}.

          - title: "Step 4: Prep data using Polybase"
            anchor: "prep-data-polybase"
            content: |
              {% include note.html type="single-line" content="**Note**: Polybase has its own set of limitations that may make it impossible to load certain data. Refer to the [Limitations](#limitations) section for more info." %}

              [Polybase](https://docs.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-2017){:target="new"} is a Microsoft offering that integrates Microsoft SQL products with Hadoop. Polybase is needed to query data from Azure Blob Storage.

              In this step, Stitch will perform the following:

              1. **Create an external data source**. This creates an [external data source](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-external-data-source-transact-sql?view=sql-server-2017){:target="new"} for the Polybase queries Stitch will run.
              2. **Create an external file format**. This creates [an object that defines the external (extracted) data](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-external-file-format-transact-sql?view=sql-server-2017){:target="new"} Stitch will load. This is used in the next step to create an external table.
              3. **Create an external table**. Using the external file format, this will [create an external table](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-external-table-transact-sql?view=sql-server-2017){:target="new"}. The external table is used to stage the data from Azure blob storage and load it into your {{ destination.display_name }} data warehouse.

          - title: "Step 5: Insert data into the data warehouse"
            anchor: "bulk-load-from-polybase"
            content: |
              Lastly, Stitch will insert the data from the external table in Polybase into your {{ destination.display_name }} data warehouse.

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
          Stitch requires Primary Keys to de-dupe incrementally replicated data. To ensure Primary Key data is available, Stitch creates an `{{ stitch.system-tables.sdc-primary-keys.name }}`table in every integration dataset. This table contains a list of all tables in an integration's dataset and the columns those tables use as Primary Keys.

          Refer to the [{{ stitch.system-tables.sdc-primary-keys.name }} table documentation]({{ link.destinations.storage.primary-key-system-table | prepend: site.baseurl }}) for more info.

          **Note**: Removing or altering this table can lead to replication issues.

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

          - [{{ stitch.system-tables.sdc-primary-keys.name }}]({{ link.destinations.storage.primary-key-system-table | prepend: site.baseurl }})
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
          {{ destination.display_name }} destinations don't have native support for nested data structures. To ensure nested data can be loaded, Stitch will flatten objects and arrays into columns and subtables, respectively. For more info and examples, refer to the [Handling nested data structures guide]({{ link.destinations.storage.nested-structures | prepend: site.baseurl }}).

      - title: "Column names"
        anchor: "transformations--column-naming"
        content: |
          Column names in {{ destination.display_name }}:

          {{ site.data.destinations.microsoft-azure.destination-details.column-name-rules | flatify | markdownify }}

          Stitch will perform the following transformations to ensure column names [adhere to the rules imposed by {{ destination.display_name }}]({{ site.data.destinations.microsoft-azure.resource-links.object-names }}){:target="new"}:

          {% include destinations/templates/destination-column-name-transformations.html %}

      - title: "Timezones"
        anchor: "transformations--timezones"
        content: |
          {{ destination.display_name }} will store the value in UTC with the specified offset.

  - title: "Compare destinations"
    anchor: "compare-destinations"
    content: |
      **Not sure if {{ destination.display_name }} is the destinationfor you?** Check out the [Choosing a Stitch Destination]({{ link.destinations.overviews.choose-destination | prepend: site.baseurl }}) guide to compare each of Stitch's destination offerings.
---
{% assign destination = page %}
{% include misc/data-files.html %}