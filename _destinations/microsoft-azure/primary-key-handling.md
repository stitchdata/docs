---
title: Microsoft Azure SQL Data Warehouse Primary Key Handling
permalink: /destinations/microsoft-azure-sql-data-warehouse/primary-key-handling
keywords: microsoft azure, microsoft azure, microsoft azure data warehouse, microsoft azure etl, etl to microsoft azure
layout: destination

summary: "Microsoft Azure SQL Data Warehouses don't have native support for Primary Keys. To ensure data can be de-duped during loading, Stitch will create a Primary Keys table for each integration schema."
type: "mirosoft-azure"

sections:
  - content: |
      {% assign primary-keys-table = site.data.stitch.sdc-primary-keys %}

      {{ primary-keys-table.description }}

  - title: "Usage in replication"
    anchor: "usage-in-replication"
    content: |
      Because Azure SQL Data Warehouse destinations don’t have native support for Primary Keys, Stitch uses the `{{ primary-keys-table.name }}` table to store Primary Key information and de-dupe data during loading.

      {% include important.html type="single-line" content="**Do not remove or alter this table.** This will cause replication issues and data discrepancies." %}

  - title: "Table schema"
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