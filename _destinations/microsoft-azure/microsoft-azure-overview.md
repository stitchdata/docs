---
# -------------------------- #
#        Page Controls       #
# -------------------------- #
title: Microsoft Azure SQL Data Warehouse Destination
permalink: /destinations/microsoft-azure-sql-data-warehouse/
keywords: microsoft azure, microsoft azure, microsoft azure data warehouse, microsoft azure etl, etl to microsoft azure
summary: &summary |
  Microsft Azure SQL Data Warehouse is a fast, fully-managed, petabyte-scale data warehouse. It's ideal for batch-based data warehouse workloads, and designed with a decoupled storage and compute model that allows it to scale quickly and be maintained in a cost-effective way.

content-type: "destination-overview"

toc: true
layout: general
destination: true
data-loading: false


# -------------------------- #
#    Destination Details     #
# -------------------------- #

display_name: "Azure SQL Data Warehouse"
type: "microsoft-azure"
db-type: "mssql"
port: 1433


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

intro: |
  {% capture setup-notice %}
  Stitch's {{ destination.display_name }} destination only works with Microsoft's [Azure SQL Data Warehouse product](https://azure.microsoft.com/en-us/services/sql-data-warehouse/){:target="new"}.

  Stitch doesn't currently support using Azure SQL Server or Azure SQL Database as a destination.
  {% endcapture %}

  {% include note.html first-line="**Stitch only supports connecting to Azure SQL Data Warehouse instances**" content=setup-notice %}

  {{ destination.summary | flatify }}

sections:
  - title: "Pricing"
    anchor: "pricing"
    content: |
      {{ site.data.destinations.reference[destination.type]destination-details-info.pricing-details | flatify }}

  - title: "Setup info"
    anchor: "stitch-details-setup-info"
    content: |
      {% include destinations/overviews/destination-reference-table.html list="stitch-details" %}

  - title: "Replication"
    anchor: "replication"
    content: |
      {% include destinations/overviews/destination-reference-table.html list="replication" %}

    subsections:
      - title: "Loading process overview"
        anchor: "loading-process-overview"
        content: |
          After the data is extracted from your integrations, Stitch will perform the following steps to prepare and load that data into your {{ destination.display_name }} destination.
        
        sub-subsections:
          - title: "Step 1: Load data into Azure Blob Storage"
            anchor: "load-into-blob-storage"
            content: |
              The first step in the loading process for {{ destination.display_name }} destinations is to load the extracted data into [Azure Blob Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction){:target="new"}.

              Blob storage is intended for storing massive amounts of unstructured data. In the next step, Stitch will use Polybase to retrieve the data from Blob Storage and prepare it for loading into {{ destination.display_name }}.

          - title: "Step 2: Prep data using Polybase"
            anchor: "prep-data-polybase"
            content: |
              {% include note.html type="single-line" content="**Note**: Polybase has its own set of limitations that may make it impossible to load certain data. Refer to the [Limitations](#limitations) section for more info." %}

              [Polybase](https://docs.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-2017){:target="new"} is a Microsoft offering that integrates Microsoft SQL products with Hadoop. Polybase is needed to query data from Azure Blob Storage.

              In this step, Stitch will perform the following:

              1. **Create an external data source**. This creates an [external data source](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-external-data-source-transact-sql?view=sql-server-2017){:target="new"} for the Polybase queries Stitch will run.
              2. **Create an external file format**. This creates [an object that defines the external (extracted) data](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-external-file-format-transact-sql?view=sql-server-2017){:target="new"} Stitch will load. This is used in the next step to create an external table.
              3. **Create an external table**. Using the external file format, this will [create an external table](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-external-table-transact-sql?view=sql-server-2017){:target="new"}. The external table is used to stage the data from Azure blob storage and load it into your {{ destination.display_name }} data warehouse.

          - title: "Step 3: Insert data into the data warehouse"
            anchor: "bulk-load-from-polybase"
            content: |
              Lastly, Stitch will insert the data from the external table in Polybase into your {{ destination.display_name }} data warehouse. 

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