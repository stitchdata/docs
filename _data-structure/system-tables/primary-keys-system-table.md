---
# -------------------------- #
#        Page Controls       #
# -------------------------- #

title: Primary Key System Table Reference (_sdc_primary_keys)
permalink: /replication/reference/system-tables-columns/primary-keys
redirect_from:
  - /replication/loading/primary-keys-system-table
  - /destinations/microsoft-azure-sql-data-warehouse/primary-key-handling
keywords: microsoft azure, microsoft azure, microsoft azure data warehouse, microsoft azure etl, etl to microsoft azure
summary: "Some of Stitch's destinations don't have native support for Primary Keys. To ensure data can be de-duped during loading, Stitch will create a Primary Keys table for each integration schema."

key: "primary-key-system-table"
type: "system, interaction"

layout: general
toc: false
weight: 2
content-type: "destination-general"

## The info about the _sdc_primary_keys table is kept in: 
## _data/stitch/system-tables/sdc-primary-keys.yml.
## This includes the table's description, its list of attributes and their descriptions, etc.


# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}
  {% assign primary-keys-table = site.data.stitch.system-tables.sdc-primary-keys %}

  {{ primary-keys-table.description | flatify }}
  
  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary | flatify }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#      CONTENT SECTIONS      #
# -------------------------- #

sections:
  - title: "Applicable destinations"
    anchor: "applicable-destinations"
    summary: "The destinations this guide applies to"
    content: |
      This guide is applicable to the following destinations:

      - [Google BigQuery (v2)]({{ link.destinations.overviews.bigquery | prepend: site.baseurl }})
      - [Microsoft Azure Synapse Analytics]({{ link.destinations.overviews.azure | prepend: site.baseurl }})

  - title: "Usage in replication"
    anchor: "usage-in-replication"
    summary: "How the {{ primary-keys-table.name }} table is used in replication"
    content: |
      Because [some destinations](#applicable-destinations) don’t have native support for Primary Keys, Stitch uses the `{{ primary-keys-table.name }}` table to store Primary Key information and de-dupe data during loading incrementally-replicated tables.
    
      De-duplicating data only applies to tables using an [Incremental Replication Method]({{ link.replication.rep-methods | prepend: site.baseurl }}) and destinations configured to use [Upsert loading]({{ link.destinations.storage.loading-behavior | prepend: site.baseurl }}). This ensures that only the most recent version of a record is loaded into the table.

      Tables using [Full Table Replication]({{ link.replication.full-table-rep | prepend: site.baseurl }}) are not de-duped, but loaded in full during each replication job.

  - title: "Determining Primary Keys"
    anchor: "determining-primary-keys"
    summary: "How Stitch determines Primary Keys"
    content: |
      Depending on the data source type, Primary Keys are determined in one of two ways:

      - For **database integrations**, Primary Keys are defined by you in the source database. These will usually be columns with a Primary Key constrant or some other equivalent, depending on the type of database being used.

         **Note**: For [database views]({{ link.replication.db-views | prepend: site.baseurl }}) you set to replicate in Stitch, the Primary Key will be the field you define for the view during setup.
      - For **SaaS integrations**, Primary Keys are pre-defined by Stitch. Refer to the [schema documentation for your SaaS integration]({{ link.integrations.saas | prepend: site.baseurl }}) for info on the Primary Keys Stitch uses for specific tables.

  - title: "Primary Keys table creation"
    anchor: "table-creation"
    summary: "How Stitch creates the Primary Keys table"
    content: |
      Every schema created by a Stitch integration contains a `{{ primary-keys-table.name }}` table, which Stitch uses to store the Primary Key data for every table set to replicate.

      **Note**: Stitch will create the `{{ primary-keys-table.name }}` even if none of the tables in the integration have a Primary Key. Primary Key data will be added to the table when and if a table is replicated that has a defined Primary Key. This means it's possible to have an empty `{{ primary-keys-table.name }}` table.

  - title: "Primary Keys table schema"
    anchor: "table-schema"
    summary: "The schema of the Primary Keys table"
    content: |
      The `{{ primary-keys-table.name }}` table contains the following columns:

      {% assign attribute-list=site.data.stitch.system-tables.sdc-primary-keys.attributes %}

      {% include stitch/stitch-system-table.html attribute-list=attribute-list %}

    subsections:
      - title: "Example tables"
        anchor: "example-tables"
        content: |
          For every column a table uses as a Primary Key, the `{{ primary-keys-table.name }}` table will contain a row containing the table's name, the name of the column, and for Microsoft Azure Synapse Analytics destinations, the column's position in the Primary Key array Stitch receives.

          When Stitch loads data for the `emails` table, it will reference these records in `{{ primary-keys-table.name }}` to de-duplicate the data. This will ensure that only the most recent version of a record exists in the `emails` table.
        example-table: |
          <table class="attribute-list">
          <tr>
          {% for attribute in attributes %}
          <td>
          <strong>{{ attribute }}</strong>
          </td>
          {% endfor %}
          </tr>
          {% for record in primary-keys-table.example-records %}
          <tr>
          {% for attribute in attributes %}
          <td>
          {{ record[attribute] }}
          </td>
          {% endfor %}
          </tr>
          {% endfor %}
          </table>

        sub-subsections:
          - title: "Example table: Google BigQuery (v2)"
            anchor: "example-table--google-bigquery"
            content: |
              {% assign attributes = "table_name|column_name" | split:"|" %}

              In Google BigQuery (v2) destinations, the Primary Key data for the `emails` table will look like this in `{{ primary-keys-table.name }}`:

              {{ subsection.example-table | flatify }}

          - title: "Example table: Microsoft Azure Synapse Analytics"
            anchor: "example-table--azure-sql-data-warehouse"
            content: |
              {% assign attributes = "table_name|column_name|ordinal_position" | split:"|" %}

              In Microsoft Azure Synapse Analytics destinations, the Primary Key data for the `emails` table will look like this in `{{ primary-keys-table.name }}`:

              {{ subsection.example-table | flatify }}

  - title: "Effects of Primary Key changes"
    anchor: "effects-of-primary-key-changes"
    summary: "The effects of Primary Key changes in the source"
    content: |
      Replication issues can arise if Primary Keys in the source change, or if data in the `{{ primary-keys-table.name }}` is incorrectly altered or removed.

      Along with being unable to load data, Stitch will surface the following error if this occurs:

      ```
      Primary Keys for table do not match Primary Keys of incoming data
      ```

      If you receive this error, you should [reset the table(s)]({{ link.replication.reset-rep-keys | prepend: site.baseurl }}) mentioned in the error. This will queue a full re-replication of the table, which will ensure Primary Keys are correctly captured and used to de-dupe data when loading.
---
{% include misc/data-files.html %}
{% assign destination = site.destinations | where:"type",page.type | first %}