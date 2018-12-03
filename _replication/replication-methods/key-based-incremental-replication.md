---
title: Key-based Incremental Replication
permalink: /replication/replication-methods/key-based-incremental
keywords: replicate, replication, replication method, stitch replicates data
tags: [replication]
layout: general
category: "settings"

summary: ""
type: "settings"
toc: true
weight: 2

sections:
  - content: |
      {{ page.title }} is a method of replication that replicates new or updated data from a data source. In this guide, we'll cover:

      1. [How it works (with examples)](#how-key-based-incremental-replication-works),
      2. [When it should be used](#when-key-based-incremental-replication), and
      3. [Limitations of this Replication Method](#limitations)

  - title: "How {{ page.title }} works"
    anchor: "how-key-based-incremental-replication-works"
    content: |
      When using {{ page.title }}, Stitch uses a column called a [Replication Key]({{ link.replication.rep-keys | prepend: site.baseurl }}) to identify new and updated data in a table for replication. A Replication Key is a `timestamp`, `date-time`, or `integer` column that exists in a source table.

      {% capture replication-keys-note %}
      While this section touches on Replication Keys, a full walkthrough is outside the scope of this guide. Refer to the [Replication Keys]({{ link.replication.rep-keys | prepend: site.baseurl }}) documentation to learn about Replication Key requirements and how to select appropriate Replication Key columns.
      {% endcapture %}

      {% include note.html type="single-line" content=replication-keys-note %}

      When Stitch replicates a table using {{ page.title }}, a few things will happen:

      1. During a replication job, Stitch stores the **maximum value** of a table's Replication Key column.
      2. During the **next** replication job, Stitch will compare saved value from the previous job to Replication Key column values in the source.
      3. Any rows in the table with a Replication Key **greater than or equal to the stored value** are replicated.
      4. Stitch stores the new maximum value from the table's Replication Key column.
      5. Repeat.

      Let's use a SQL query as an example:

      ```sql
      SELECT *
        FROM schema.table
       WHERE replication_key_column >= 'last_saved_maximum_value'
      ```

    subsections:
      - title: "Data extraction and Replication Key types"
        anchor: "data-extraction-replication-key-types"
        content: |
          Below are examples of how different Replication Key types impact the data extracted using {{ page.title }}.

          **Note**: These examples only demonstrate how data is **extracted** from a data source, not how it will be loaded into your destination.

          {% include replication/extraction/replication-job-example-tabs.html replication-method="key-based-incremental" %}

      # - title: ""
      #   anchor: ""
      #   content: |
      #     The saved maximum Replication Key value is specific to each table that uses {{ page.title }}. This means that a saved Replication Key value isn't used to extract data from multiple tables in a job

      # - title: "Define a table's Replication Key"
      #   anchor: "define-replication-keys"
      #   content: |
      #     Defining Replication Keys depends on the type of integration:

      #     - For **database integrations**, you will need to select a Replication Key for the table when you set it to replicate. Refer to the [Replication Keys guide]({{ link.replication.rep-keys | prepend: site.baseurl }}) for useful tips for selecting a Replication Key.

      #     - For **SaaS integrations**, Stitch automatically selects default Replication Keys. These cannot be changed.

  - title: "When {{ page.title }} should be used"
    anchor: "when-key-based-incremental-replication"
    content: |
      Aside from [Log-based Replication](#log-based-replication) where it's supported, {{ page.title }} is the most efficient method for replicating your data. If Log-based Replication is unavailable for your source, {{ page.title }} may be a good fit if:

      1. A table contains a modification timestamp column, which is updated when the record changes
      2. Records aren't hard deleted from the source table. Refer to the [Limitations section](#limitation-2--hard-deletes-unsupported) below for more info.

      **Note**: In the case of SaaS integrations, Stitch will use {{ page.title }} whenever possible. Refer to the **Schema** section of any [integration's documentation]({{ site.baseurl }}/integrations/saas) for the Replication Method and Replication Key(s) used by specific tables.

  - title: "Limitations of {{ page.title }}"
    anchor: "limitations"
    content: |
      Before you select {{ page.title }} as the Replication Method for a table, you should be aware of the limitations this method can have. Being aware of these limitations can help prevent data discrepancies and ensure your data is replicated in the most efficient manner possible.

    subsections:
      - title: "Limitation 1: Works best with a modification timestamp column"
        anchor: "limitation-1--modification-timestamp-column"
        content: |
          While an `integer` column can be used as a Replication Key, {{ page.title }} functions best with a modification timestamp Replication Key. Unlike an auto-incrementing integer, a modification timestamp allows Stitch to identify both new and updated records for replication.

      - title: "Limitation 2: Hard deletes aren't captured"
        anchor: "limitation-2--hard-deletes-unsupported"
        content: |
          Hard deletes aren't able to be replicated with {{ page.title }}. This is due to the usage of Replication Keys to identify data for replication.

          When a record is hard deleted, or entirely removed from a source, its Replication Key value is also removed. Without a Replication Key value to check, Stitch can’t identify the change and update the record in the destination. This means that the record will remain in the destination.

          Refer to the [Deleted Record Handling]({{ link.replication.deleted-records | prepend: site.baseurl }}) guide for a more detailed explanation and examples.

      - title: "Limitation 3: Duplication in replication"
        anchor: "limitation-3--replication-key-inclusivity"
        content: |
          Due to the inclusive nature of Replication Keys, there will be some duplication during the extraction process. This is because Stitch checks for values that are greater than **or equal to** the last saved maximum Replication Key value.

          Because of this approach, the record or records with Replication Key values equal to the maximum value will be selected for extraction during subsequent jobs. Most of the time, the number of re-replicated rows will be small. If, however, a bulk update occurs and a large number of records all have the same Replication Key value, you could see a high amount of rows being replicated during every replication job until a greater Replication Key value is detected.

          #### Example {#extraction-duplication-example}

          In this example, we'll use a `customers` table with a Replication Key column named `updated_at`.

          1. In a database, you run a process that updates 100 records in the `customers` table.
          2. These records' `updated_at` values are updated to `2018-11-01 00:00:00`.
          3. During the next replication job - or Job 1 - Stitch extracts 101 records from the source `customers` table:
             - The 100 updated records with `updated_at` values of `2018-11-01 00:00:00`, and
             - The one record with an `updated_at` value equal to the last saved maximum value from the previous replication job.
          4. Stitch saves the new maximum Replication Key value as `updated_at: 2018-11-01 00:00:00`.
          5. No records are updated between Job 1 and the next job.
          6. When Job 2 begins, Stitch again extracts the 100 records with `updated_at: 2018-11-01 00:00:00` because their Replication Key values are **equal to** the last saved maximum value.

          Until a record with a greater `updated_at` value is added to the `customers` table, Stitch will continue to extract all records with `updated_at: 2018-11-01 00:00:00` values.

          #### Bulk update handling {#bulk-update-handling}

          To avoid the above scenario, add a single record with a greater Replication Key value at the end of a bulk update. This will ensure that the maximum Replication Key value Stitch saves will only be equal to one record instead of many.

          For example: If one of the 100 updated records in the `customers` table had had an `updated_at` value of `2018-11-01 00:00:01`, Stitch would have saved this as the maximum Replication Key value. Then, during Job 2, only one record - instead of 100 - would have been re-replicated.
---