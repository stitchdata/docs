---

## See the following for info about what's in this template:
## https://docs-about-stitch-docs.netlify.com/reference/destination-templates/destination-overview/

# -------------------------- #
#        Page Controls       #
# -------------------------- #
title: Microsoft Azure Destination
permalink: /destinations/microsoft-azure/
layout: destination-overview
keywords: microsoft azure, microsoft azure, microsoft azure data warehouse, microsoft azure etl, etl to microsoft azure
summary: ""
toc: true
destination: true


# -------------------------- #
#    Destination Details     #
# -------------------------- #
display_name: "Microsoft Azure"
type: "microsoft-azure"
db-type: "azure"
pricing_tier: "standard" ## for Stitch
status: "In development"
description: |

pricing_model: "Hourly" ## provider model
free_option: "Free (plan & trial)"
fully-managed: true
pricing_notes: |
  Microsoft Azure pricing is based on your compute and storage usage. Compute usage is charged using an hourly rate, meaning you'll only be billed for the hours your data warehouse is active. Compute usage is billed in one hour increments.

  Storage charges include the size of your primary database and seven days of incremental snapshots. Microsoft Azure rounds charges to the nearest terabyte (TB). For example: If the data warehouse is 1.5 TB and you have 100 GB of snapshots, your bill will be fore 2 TB of data.

  Refer to [Microsoft's documentation](https://azure.microsoft.com/en-us/pricing/details/sql-data-warehouse/gen2/){:target="new"} for more info and examples.
icon: /images/destinations/icons/microsoft-azure.svg


# -------------------------- #
#           Support          #
# -------------------------- #

ssl: 
ssh: 

incremental-replication: "Upserts, Append-Only"
connection-methods: "SSH, SSL"
supported-versions: "n/a"

nested-structures: false
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
reserved-words: ""

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
  - title: "pricing"
    content: |
      {{ destination.pricing_notes }}

  - title: "setup"
    content: |

  - title: "limitations"
    include: |
      {% include destinations/overviews/limitations.html %}

  - title: "replication"
    include: |
      {% include destinations/overviews/replication-process.html %}

  - title: "schema"
    include: |
      {% include destinations/overviews/integration-schemas.html %}
---
{% assign destination = page %}
{% include misc/data-files.html %}