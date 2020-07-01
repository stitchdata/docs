---
title: Missing Mongo Data Due to Fields with Multiple Data Types
keywords: troubleshooting, integration, database integration, trouble, issue, help, mongo, mongodb, data discrepancy, data types
permalink: /troubleshooting/missing-mongo-data-multiple-data-types
tags: [data_discrepancy, database_integrations]

key: "mongo-multiple-data-types"

summary: "Missing some Mongo data? The root cause may be multiple data types in the Replication Key or Primary Key (_id) fields."
toc: true
type: "discrepancy, database-integration, replication"

layout: general

intro: |
  Missing some Mongo data in your destination? [Due to how Mongo sorts data based on data type](https://docs.mongodb.com/manual/reference/bson-type-comparison-order/){:target="new"}, Stitch may be unable to correctly identify new and updated data. If you don’t see data that you’d expect to, the root cause may be multiple data types in the collection's Replication Key or Primary Key (`_id`) fields.

sections:
  - title: "Symptoms"
    anchor: "symptoms"
    content: |
      Missing or stale data in the destination for Mongo-backed database integrations.

  - title: "Cause"
    anchor: "cause"
    content: |
      The cause of this problem is two-fold:

      1. Fields in Mongo may contain more than one BSON data type
      2. [Mongo ranks data types](https://docs.mongodb.com/manual/reference/bson-type-comparison-order/){:target="new"}, which affects how Mongo determines the current maximum value for a field

    subsections:
      - title: "Replication Methods and value sorting"
        anchor: "cause--replication-methods"
        rep-methods:
          - name: "Key-based Incremental"
            key-field: "Replication Key"
            description: |
              Documents with a Replication Key value **greater than or equal to** the last saved maximum value for the Replication Key field are replicated.

          - name: "Full Table"
            key-field: "Primary Key (`_id`)"
            description: |
              Documents with a Primary Key (`_id`) value **less than or equal to** the last saved maximum value for the Primary Key field are replicated.

              This ensures that replication can resume if the replication job is interrupted.

          - name: "Log-based Incremental"
            key-field: "Primary Key (`_id`)"
            description: |
              **Applicable only to the historical replication of a collection.** This is not applicable when Stitch reads updates from the database's logs.

              Documents with a Primary Key (`_id`) value **less than or equal to** the last saved maximum value for the Primary Key field are replicated.

              This ensures that historical replication for a collection can resume if the replication job is interrupted.
        content: |
          For Mongo-backed database integrations, Stitch uses a field's maximum value to identify new and updated data during replication.

          The field itself and how its values are used depend on the [Replication Method]({{ link.replication.rep-methods | prepend: site.baseurl }}) the collection uses:

          <table class="attribute-list table-hover">
          <tr>
          <td align="right" width="25%; fixed">
          <strong>Replication Method</strong>
          </td>
          <td width="20%; fixed">
          <strong>Field used</strong>
          </td>
          <td>
          <strong>Description</strong>
          </td>
          </tr>
          {% for rep-method in subsection.rep-methods %}
          <tr>
          <td align="right">
          {{ rep-method.name }}
          </td>
          <td>
          {{ rep-method.key-field | markdownify }}
          </td>
          <td>
          {{ rep-method.description | flatify | markdownify }}
          </td>
          </tr>
          {% endfor %}
          </table>

          Mongo's data type ranking determines what the current maximum value of a field is. This, in turn, can affect how Stitch identifies and replicates data from a Mongo database.

      - title: "Examples"
        anchor: "cause--examples"
        content: |
          Consider these examples, which demonstrate how multiple data types in either the Replication Key or Primary Key (`_id`) field can cause data discrepancies.
        sub-subsections:
          - title: "Example: Replication Key"
            anchor: "cause--examples--replication-keys"
            content: |
              {% include note.html type="single-line" content="**Note**: This example applies to collections using Key-based Incremental Replication. Key-based Incremental Replication will only replicate records with Replication Key values greater than or equal to the Replication Key's last saved maximum value." %}

              This example demonstrates how multiple values in a Replication Key field can cause data discrepancies.

              1. A collection is set to replicate, using a field named `table_id` as the Replication Key. The `table_id` field contains both `ObjectId` and `String` data.
              2. A historical replication of the collection completes.
              3. Stitch saves the maximum value of `table_id`. Because Mongo ranks `ObjectId` data types as greater than `Strings`, the maximum value Stitch saves is an `ObjectId` value.
              4. New documents are added to the collection.
              5. During the next replication job, Stitch uses the last recorded maximum value - an `OjbectId` value ` to identify new and updated data.
              6. Because `ObjectIds > Strings`, all documents with `Strings` are considered to be less than the last recorded maximum value. This means Stitch won’t be able to detect these documents and replicate them.

          - title: "Example: Primary Key"
            anchor: "cause--examples--primary-keys"
            content: |
              {% include note.html type="single-line" content="**Note**: This example applies to collections using Full Table Replication or the historical replication of a collection using Log-based Incremental Replication." %}

              This example demonstrates how multiple values in a Primary Key (`_id`) field can cause data discrepancies.

              1. A collection is set to replicate. Stitch automatically uses its `_id` field as the Primary Key. The `_id` field contains both `ObjectId` and UUID data.
              2. During the replication job, Stitch identifies and saves the maximum value of `_id`. In this example, it's an `ObjectId` value.
              3. Stitch queries for all documents with an `_id` value **less than or equal to** the saved maximum `_id` value.
              4. Because Mongo considers `ObjectIds` and UUID values to be neither greater than or less than each other, UUID records may be excluded from the results of Stitch's query. This means Stitch won't be able to detect these documents and replicate them.

  - title: "Diagnose the issue"
    anchor: "diagnosis"
    content: |
      {% include note.html type="single-line" content="**Note**: The queries in this section are written for Mongo versions 3.0 and newer. You may need to modify the queries work with your version." %}

      To determine if a field contains multiple data types, you'll run queries and compare the count of specific data type values in the Replication Key or Primary Key (`_id`) field to the total number of documents in the collection.

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "Step 1: Get a count of data types for the field"
        anchor: "diagnosis--count-single-data-type"
        content: |
          First, you'll need to get a count how many instances of a single data type there are in a given field in the collection.

          Run the query below, replacing the following:

          - `nameOfCollection`: The name of the collection
          - `keyField`: This is dependent on the Replication Method the collection uses:
             - For **Key-based Incremental Replication**: The name of the field used as the collection's Replication Key
             - For **Log-based Incremental or Full Table Replication**: This value should be `_id`
          - `knownDataTypeId`: The ID of the known BSON data type used by the `keyField`. Refer to [Mongo’s documentation](https://docs.mongodb.com/manual/reference/bson-types/#bson-types){:target="new"} for a list of BSON data type IDs.

          {% capture code %}
          db.<nameOfCollection>.count({<keyField>: {$type: <knownDataTypeId>}});
          {% endcapture %}

          {% include layout/code-snippet.html code=code %}

      - title: "Step 2: Count all records in the collection"
        anchor: "diagnosis--count-all-records"
        content: |
          Next, run this query to get a count of all records in the collection:

          {% capture code %}
          db.<nameOfCollection>.count();
          {% endcapture %}

          {% include layout/code-snippet.html code=code %}

      - title: "Step 3: Retrieve the field's current maximum value"
        anchor: "diagnosis--retrieve-current-max-value"
        content: |
          Next, run the following query to return the maximum value for the specified Replication or Primary Key field in the collection. This can be helpful when comparing your source database to what’s in your destination:

          {% capture code %}
          db.<nameOfCollection>.find().sort({<keyField>:-1}).limit(1);
          {% endcapture %}

          {% include layout/code-snippet.html code=code %}

      - title: "Step 4: Compare the query results"
        anchor: "diagnosis--compare-results"
        content: |
          Compare the results between the queries from [Step 1](#diagnosis--count-single-data-type) and [Step 2](#diagnosis--count-all-records).

          **If the results are equal**, then the Replication or Primary Key field contains only one data type. The root cause may require additional investigation.

          **If the results aren't equal**, multiple data types in the Replication or Primary Key field may be interfering with Stitch's replication process. Refer to the [Solution](#solution) section for next steps.

  - title: "Solution"
    anchor: "solution"
    content: |
      If you've determined the field contains multiple data types, you have a few options:

      - **To continue using the collection's current Replication Method**:

         1. Modify the field to only contain a single data type. 
         2. After this is completed in the source, [reset the collection]({{ link.replication.reset-rep-keys | prepend: site.baseurl }}) to queue a historical replication.

      - **To use a different Replication Method**:
         1. Verify that the Replication Key field (if switching to Key-based Incremental Replication) or the `_id` field (if switching to Full Table or Log-based Incremental Replication) only contains a single data type. Make any modifications before proceeding.
         2. [Configure the new Replication Method]({{ link.replicaiton.rep-methods | prepend: site.baseurl | append: "#define-replication-method-table" }}) for the collection in Stitch. Changing a Replication Method automatically queues a historical replication.

      If you've determined multiple data types aren't causing the discrepancy, we recommend working through the [Data discrepancy troubleshooting guide]({{ link.troubleshooting.discrepancy-guide | prepend: site.baseurl }}) before contacting support. 

      Additionally, providing support with the info from the queries in this guide can help us investigate more quickly.
---