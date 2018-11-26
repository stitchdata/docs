---

## See the following for info about what's in this template:
## https://docs-about-stitch-docs.netlify.com/reference/destination-templates/destination-overview/

# -------------------------- #
#        Page Controls       #
# -------------------------- #
title: Microsoft Azure Destination
permalink: /destinations/microsoft-azure-sql-data-warehouse/
layout: destination
keywords: microsoft azure, microsoft azure, microsoft azure data warehouse, microsoft azure etl, etl to microsoft azure
summary: &summary |
  Microsft Azure SQL Data Warehouse is a fast, fully-managed, petabyte-scale data warehouse. It's ideal for batch-based data warehouse workloads, and designed with a decoupled storage and compute model that allows it to scale quickly and be maintained in a cost-effective way.

content-type: "destination-overview"

toc: true
destination: true
data-loading: false


# -------------------------- #
#    Destination Details     #
# -------------------------- #
display_name: "Azure SQL Data Warehouse"
type: "microsoft-azure"
db-type: "mssql"
pricing_tier: "standard" ## for Stitch

status: "Closed Beta"
description: *summary
port: 1433
pricing_model: "Usage" ## provider model
free_option: "Free (plan & trial)"
fully-managed: true
pricing_notes: |
  {{ destination.display_name }} bases their pricing on your compute and storage usage. Compute usage is charged using an hourly rate, meaning you'll only be billed for the hours your data warehouse is active. Compute usage is billed in one hour increments.

  Storage charges include the size of your primary database and seven days of incremental snapshots. Microsoft Azure rounds charges to the nearest terabyte (TB). For example: If the data warehouse is 1.5 TB and you have 100 GB of snapshots, your bill will be for 2 TB of data.

  Refer to [Microsoft's documentation](https://azure.microsoft.com/en-us/pricing/details/sql-data-warehouse/gen2/){:target="new"} for more info and examples.
icon: /images/destinations/icons/microsoft-azure.svg


# -------------------------- #
#           Support          #
# -------------------------- #

ssl: true
ssh: true

incremental-upsert-support: true
connection-methods: "SSH, SSL"
supported-versions: "n/a"

nested-structure-support: false
case: "Case Insensitive"
table-name-limit: "128" ## max # of characters
column-name-limit: "255" ## max # of characters
column-limit: "1,024" ## max # of columns allowed in tables
timestamp-range: "January 1, 1753 00:00:00 AD, through December 31, 9999 23:59:59.997 AD"
timezones:
  supported: false
varchar-limit: "4,000 characters" ## max width for varchars
decimal-limit: "38 numbers, or places"
decimal-range: "6 numbers after the decimal"
reserved-words: "https://docs.microsoft.com/en-us/sql/t-sql/language-elements/reserved-keywords-transact-sql?view=sql-server-2017"

# -------------------------- #
#    Incompatible Sources    #
# -------------------------- #
incompatible-with: 0



# -------------------------- #
#            Links           #
# -------------------------- #
status-url: https://azure.microsoft.com/en-us/status/
sign-up: https://azure.microsoft.com/en-us/
documentation: https://docs.microsoft.com/en-us/azure/sql-database/
pricing: https://azure.microsoft.com/en-us/pricing/details/sql-database/managed/
price-calculator: "https://azure.microsoft.com/en-us/pricing/calculator/?service=sql-database"
database-object-limits: "https://docs.microsoft.com/en-us/azure/sql-data-warehouse/sql-data-warehouse-service-capacity-limits#database-objects"

# -------------------------- #
#      Overview Content      #
# -------------------------- #

introduction: |
  {{ destination.description | flatify | markdownify }}

sections:
  - content: |
      {{ destination.summary | flatify }}

  - title: "Pricing"
    anchor: "pricing"
    content: |
      {{ destination.pricing_notes | flatify }}

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