---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Understanding Integration Schema Structures in Your Destination
permalink: /data-structure/integration-schemas
keywords: integration schemas, stitch schema, _sdc, sdc, stitch creates schemas, data warehouse
tags: [replication]
summary: "Learn how Stitch organizes the data replicated from your sources in your data warehouse."

layout: general
toc: true

level: "guide"
key: "integration-schemas"

weight: 1


# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}
  For each integration that you add to Stitch, a schema specific to that integration will be created in your data warehouse. The integration's schema is where all the data Stitch replicates from the data source will be stored.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#      CONTENT SECTIONS      #
# -------------------------- #

sections:
  - title: "Schema terminology"
    anchor: "schema-terminology"
    summary: "Some schema terminology"
    content: |
      In Stitch, we use the term `schema` to refer to a location in a destination where integration data is loaded. Depending on the destination you're using, this might mean different things.

      For example:

      - In **destinations that are traditional databases**, data is loaded to integration-specific **schemas**. 
      - In **Google BigQuery** destinations, data is loaded to integration-specific [**datasets**](https://cloud.google.com/bigquery/docs/datasets-intro){:target="new"}.
      - In **Amazon S3** destinations, data is loaded into integration-specific **folders**. The integration names and [S3 Object Keys]({{ link.destinations.setup.amazon-s3 | prepend: site.baseurl | append:"#define-s3-object-key" }}) determine the exact location in the S3 bucket.

  - title: "Integration schema names"
    anchor: "integration-schema-names"
    summary: "How integration schemas are named"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "Create the schema name"
        anchor: "create-schema-name"
        content: |
          When you create an integration, you're asked to provide a name for the integration. This name is used to create the integration's schema in your destination.

          For example: An **Integration Name** of `Recurly Stitch` would create a schema named `recurly_stitch` in the destination.

          If you want the schema name to be different than the display name when initially creating an integration:

          1. Click the **Use a different schema name?** link below the **Integration Name** field:

             ![Naming an integration]({{ site.baseurl }}/images/integrations/integration-name.png)

          2. Then, enter a schema name in the **Integration Schema Name** field that displays:

             ![Using different names for schemas and display names.]({{ site.baseurl }}/images/integrations/change-schema-name.png)

          3. Complete the integration setup.
          4. Save and create the integration.

      - title: "Change a schema name"
        anchor: "changing-schema-names"
        content: |
          After an integration is initially saved and created, its schema name can't be changed.

          Changing an integration's schema name requires you to create a new integration and re-replicate all historical data.

      - title: "Re-use a schema name"
        anchor: "re-using-schema-names"
        content: |
          Schema names from deleted integrations can be re-used. However, if a naming collision occurs (two schema names canonicalize to the same name) the destination [may reject the data](#rejected-records-log). This is because deleting an integration in Stitch won't delete that integration's schema or data from your destination.

          **Note**: Free historical loads are allowed only once for each integration namespace, or schema name. Refer to the [Billing FAQ]({{ link.billing.billing-faq | prepend: site.baseurl | append: "#historical-data-loads" }}) for more info and examples.

  - title: "Integration schema composition"
    anchor: "integration-schema-composition"
    summary: "What's in an integration schema"
    content: |
      {% assign primary-keys-table = site.data.stitch.sdc-primary-keys %}
      {% include layout/image.html type="right" file="/stitch-schema-structure.png" max-width="400" enlarge=true %}

      Integration schemas created by Stitch will contain two types of tables:
      
      {% for subsection in section.subsections %}
      - [{{ subsection.title | flatify }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Integration tables"
        anchor: "integration-tables"
        content: |
          The tables that Stitch creates in an integration schema depends on whether the integration supports [data selection]({{ link.replication.syncing | prepend: site.baseurl | append: "#integrations-that-support-whitelisting" }}).

          If the integration supports data selection, the integration schema will contain only the tables (and columns, if column selection is supported) that you set to replicate.

          Otherwise, all available tables and columns in the integration will be replicated to your destination.

          Refer to the [Integration table schemas section](#integration-table-schemas) below more info on how individual integration tables are structured.

      - title: "Stitch system tables"
        anchor: "stitch-system-tables"
        content: |
          In addition to the integration tables, Stitch will create additional tables in the integration schema. These tables are prepended with `{{ system-column.prefix }}`.

          Every integration schema will contain an `{{ stitch.system-tables.sdc-rejected.name }}` table, which serves as the integration's log for data loading issues. Refer to the [{{ rejected-records.name }} guide]({{ link.destinations.storage.rejected-records | prepend: site.baseurl }}) for more info.

          If using a [Microsoft Azure SQL Data Warehouse destination]({{ link.destinations.overviews.azure | prepend: site.baseurl }}), every integration schema will also contain a table named `{{ stitch.system-tables.sdc-primary-keys.name }}`. This table contains the Primary Keys for the tables in the integration schema. Refer to the [{{ primary-keys-table.name }} guide]({{ link.destinations.storage.azure-primary-keys | prepend: site.baseurl }}) for more info.

  - title: "Integration table schemas"
    anchor: "integration-table-schemas"
    summary: "How tables in integration schemas are structured"
    content: |
      The integration tables in the schema contain the replicated data from tables set to replicate. **Note**: If you de-select a table from replication, doing so won't remove that table's data from your destination.

      {% for subsection in section.subsections %}
      - [{{ subsection.title | flatify }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Data storage"
        anchor: "data-storage"
        content: |
          How your data is stored in the schemas, tables, and columns created by Stitch depends on a few things:

          - How data is structured in that particular data source (For example: Use of nested data structures),
          - Any changes you might make to the data source (For example: adding/removing a column),
          - Stitch-specific data handling rules (For example: entirely `NULL` columns), and
          - How your destination handles data (For example: Columns with mixed data types, nested data structures)

          Stitch will encounter dozens of scenarios when replicating and loading your data. Familiarizing yourself with these scenarios and the nuances of your destination will enable you to better understand your data's structure and efficiently troubleshoot if issues arise.

          To learn more about how handles these scenarios, check out the [Data Loading guide for your destination]({{ link.destinations.storage.loading-data | prepend: site.baseurl }}).

      - title: "Stitch system ({{ system-column.prefix }}) columns"
        anchor: "sdc-columns"
        content: |
          In addition to the columns set to replicate in these tables, there are also a few columns prepended with `{{ system-column.prefix }}`. Stitch uses these columns to replicate your data. **Don't remove these columns**, as doing so will cause replication issues in Stitch.

          For descriptions of the system columns used by Stitch, refer to the [System tables and columns guide]({{ link.destinations.storage.system-tables-and-columns | prepend: site.baseurl }}).
---
{% include misc/data-files.html %}
{% assign sdc-columns = site.data.stitch.sdc-columns %}