---
title: Microsoft Azure SQL Data Warehouse Primary Key Handling
permalink: /destinations/microsoft-azure-sql-data-warehouse/primary-key-handling
keywords: microsoft azure, microsoft azure, microsoft azure data warehouse, microsoft azure etl, etl to microsoft azure
layout: destination

summary: "Microsoft Azure SQL Data Warehouses don't have native support for Primary Keys. To ensure data can be de-duped during loading, Stitch will create a Primary Keys table for each integration schema."
type: "mirosoft-azure"

## The info about the sdc_primary_keys table is kept in _data/stitch/sdc-primary-keys.yml.
## This includes the table's description, its list of attributes and their descriptions, etc.

sections:
  - content: |
      {% assign primary-keys-table = site.data.stitch.sdc-primary-keys %}

      {{ primary-keys-table.description | flatify }}

  - title: "Usage in replication"
    anchor: "usage-in-replication"
    content: |
      Because Azure SQL Data Warehouse destinations don’t have native support for Primary Keys, Stitch uses the `{{ primary-keys-table.name }}` table to store Primary Key information and de-dupe data during loading.

      {% include important.html type="single-line" content="**Do not remove or alter this table.** This will cause replication issues and data discrepancies." %}

  - title: "Determining Primary Keys"
    anchor: "determining-primary-keys"
    content: |
      Depending on the data source type, Primary Keys are determined in one of two ways:

      - For **database integrations**, Primary Keys are defined by you in the source database. This will usually be columns with a Primary Key constrant or some other equivalent, depending on the type of database being used.

         **Note**: For [database views]({{ link.replication.db-views | prepend: site.baseurl }}) you set to replicate in Stitch, the Primary Key will be the field you define for the view during setup.
      - For **SaaS integrations**, Primary Keys are pre-defined by Stitch. Refer to the [schema documentation for your SaaS integration]({{ link.integrations.saas | prepend: site.baseurl }}) for info on the Primary Keys Stitch uses for specific tables.

      In every schema created by a Stitch integration will be a `{{ primary-keys-table.name }}` table. The Primary Key data for every table set to replicate will be stored in this table.

  - title: "Primary Keys table schema"
    anchor: "table-schema"
    content: |
      The `{{ primary-keys-table.name }}` table contains the following columns:

      <table class="attribute-list">
      <tr>
      <td class="attribute-name">
      <strong>Column name</strong>
      </td>
      <td class="attribute-description">
      <strong>Description</strong>
      </td>
      </tr>
      {% for attribute in primary-keys-table.attributes %}
      <tr>
      <td class="attribute-name">
      <strong>{{ attribute.name }}</strong>
      </td>
      <td class="attribute-description">
      {{ attribute.description | flatify | markdownify }}
      </td>
      </tr>
      {% endfor %}
      </table>
    subsections:
      - title: "Example table"
        anchor: "example-table"
        content: |
          {{ primary-keys-table.example-records-description | flatify | markdownify }}

          <table class="attribute-list">
          <tr>
          {% for attribute in primary-keys-table.attributes %}
          <td class="attribute-description">
          <strong>{{ attribute.name }}</strong>
          </td>
          {% endfor %}
          </tr>
          {% for record in primary-keys-table.example-records %}
          <tr>
          <td class="attribute-description">
          {{ record.table-name }}
          </td>

          <td class="attribute-description">
          {{ record.column-name }}
          </td>

          <td class="attribute-description">
          {{ record.ordinal-position }}
          </td>
          </tr>
          {% endfor %}
          </table>
---
{% include misc/data-files.html %}
{% assign destination = site.destinations | where:"type",page.type | first %}