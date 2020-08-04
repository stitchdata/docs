---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Replication Keys
permalink: /replication/extractions/replication-keys
redirect_from: 
  - /replication/replication-keys
  - /replication/mongo-replication-keys
keywords: replicate, replication, replication key, keys, stitch replicates data, rp
summary: "Replication Keys are columns that Stitch uses to identify new and updated data for replication when performing Key-based Incremental Replication. Learn about how they work, what to consider when selecting one, and how to define them for your tables."
layout: general

key: "replication-keys"
content-type: "replication-keys"
toc: true
weight: 5


# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}

  {{ page.summary }} In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#          CONTENT           #
# -------------------------- #
sections:
  - title: "Applicable integrations"
    anchor: "applicable-integrations"
    summary: "The integrations this guide applies to"
    content: |
      This guide is applicable to all SaaS and database integrations.

  - title: "How Replication Keys work"
    anchor: "how-replication-keys-work"
    summary: "How Replication Keys work"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "How Replication Keys are used during replication"
        anchor: "replication-key-usage"
        summary: "How Replication Keys are used during replication"
        content: |
          When a table uses [Key-based Incremental Replication]({{ link.replication.rep-methods | prepend: site.baseurl | append: "#key-based-incremental-replication" }}), a column called a Replication Key is used to identify new and updated data for replication. This column exists in the source table and, depending on the integration type, [is either defined by you or Stitch](#replication-keys-defined).

          When Stitch replicates a table using {{ page.title }}, a few things will happen:

          1. During a replication job, Stitch stores the **maximum value** of a table's Replication Key column.
          2. During the **next** replication job, Stitch compares the saved value from the previous job to Replication Key column values in the source.
          3. Any records in the table with a Replication Key **greater than or equal to the stored value**`*` are replicated.
          4. Stitch stores the new maximum value from the table's Replication Key column.
          5. Repeat.

          Let's use a SQL query as an example:

          ```sql
          SELECT replication_key_column,
                 column_you_selected_1,
                 column_you_selected_2,
                 [...]
            FROM table
           WHERE replication_key_column >= 'last_saved_maximum_value'
          ```

          `*` Some integrations may not use Replication Keys inclusively. In this case, records with Replication Key values that are **greater than** the last saved value are extracted.
      
      - title: "How Stitch defines Replication Keys"
        anchor: "replication-keys-defined"
        summary: "How Stitch defines Replication Keys"
        content: |
          How Replication Keys are defined depends on the type of integration containing the table.

          - **Database integrations**: When [Key-based Incremental Replication]({{ link.replication.key-based-incremental | prepend: site.baseurl }}) is selected for a table, Replication Keys are defined by you.

          - **File-based integrations**: Stitch uses the modification time of the file backing the table as the Replication Key. This applies to the following integrations:
             {% assign file-based-integrations = site.documents | where:"file-system",true | sort:"display_name" %}

             {% for integration in file-based-integrations %}
             - [{{ integration.display_name }}]({{ integration.url | prepend: site.baseurl | append: "#extraction--data-replication" }})
             {% endfor %}

          - **SaaS integrations**: For the majority of SaaS integrations, Replication Keys are defined by Stitch and can't be modified. Refer to the [Schema documentation]({{ link.integrations.saas | prepend: site.baseurl }}) for your integration for info about how each table replicates.

      - title: "Replication Keys versus Primary Keys"
        anchor: "replication-keys-vs-primary-keys"
        content: |
          When it comes to replicating your data, there are a lot of ‘keys’ involved. It can be difficult to keep them all straight, but aside from Replication Keys, there’s one more you should keep in mind: Primary Keys.

          In Stitch, Replication Keys and Primary Keys serve two different purposes:

          - **Replication Keys** are used during the Extraction phase of the replication process - or when Stitch is querying your data source - to identify new and updated data for replication.

            In the Stitch app, Replication Keys have a <img src="{{ site.baseurl }}/images/replication/replication-key-icon.png" alt="Replication Key icon" style="border: 0px;"> next to the column name.

          - **Primary Keys** are used to perform [Upsert Loading]({{ link.destinations.storage.loading-behavior | prepend: site.baseurl }}) during the last phase of the replication process. Primary Keys identify unique records within a table and ensure that only the most recently updated version of that record appears in your destination.

            In the Stitch app, Primary Keys have a <img src="{{ site.baseurl }}/images/replication/primary-key-icon.png" alt="Primary Key icon" style="border: 0px;"> next to the column name.

          While a column can sometimes be used as both a Replication Key and a Primary Key, these are not necessarily always the same column.

  - title: "Requirements for Replication Keys"
    anchor: "replication-key-requirements"
    summary: "Stitch's requirements for Replication Keys"
    content: |
      {% capture rep-key-menu %}
      **Note**: Only columns meeting all of Stitch's requirements can be used as Replication Keys. **For database integrations**, only columns that meet all of the requirements will display in the **Replication Key** menu in the **Table Settings** page.
      {% endcapture %}
      {% include note.html type="single-line" content=rep-key-menu %}

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "General requirements"
        anchor: "replication-key-requirements--general"
        content: |
          Replication Key fields:

          - Must be a top-level field
          - Must be one of the following data types:

          <table class="attribute-list">
            <tr>
              <td width="25%; fixed" align="right"><strong>Data type</strong>
              </td>
              <td>
                <strong>Available for</strong>
              </td>
              <td>
                <strong>Notes</strong>
              </td>
            </tr>
              {% assign all-types = site.data.taps.extraction.replication-methods.key-based-incremental.allowed-data-types %}
                {% assign types-all-integrations = all-types | where:"integration","All" %}
                {% assign types-mongodb-integrations = all-types | where:"integration","MongoDB v1+" %}
              
                  {% assign supported-data-types = types-all-integrations | concat: types-mongodb-integrations %}

            {% for data-type in supported-data-types %}
              <tr>
                <td align="right">
                  <strong>{{ data-type.type | upcase }}</strong>
                </td>
                <td>
                  {{ data-type.integration | append: " integrations" }}
                </td>
                <td>
                  {{ data-type.notes | flatify | markdownify }}
                </td>
              </tr>
            {% endfor %}
          </table>

      - title: "Additional general guidelines"
        anchor: "replication-key-requirements--general-additional"
        content: |
          In addition to the [general requirements](#replication-key-requirements--general), Replication Keys:

          - Shouldn't contain `NULL` values
          - Should contain only one data type

          **Note**: While these aren't hard requirements, Replication Keys that don't follow these guidelines may result in data discrepancies.

      - title: "Additional MongoDB requirements"
        anchor: "replication-key-requirements--mongodb"
        content: |
          In addition to the [general requirements](#replication-key-requirements--general), Replication Keys for MongoDB integrations:

          {% for requirement in site.data.taps.extraction.replication-methods.key-based-incremental.other-requirements %}
          {% if requirement contains "MongoDB" %}
          - {{ requirement | remove: "(MongoDB only)" }}
          {% endif %}
          {% endfor %}

  - title: "Selecting a column to use as a Replication Key"
    anchor: "selecting-a-replication-key"
    summary: "Things to think about when selecting a Replication Key"
    content: |
      When deciding which source column to use as a Replication Key, keep in mind that incorrectly selecting a Replication Key can cause data discrepancies and negatively impact your row usage.

      For example: A `BIGINT` column used in a boolean fashion is selected as a Replication Key. This column only contains values of `0` and `1`. As most integrations use Replication Key values inclusively - [that is, greater than or equal to](#replication-key-usage) - records with a Replication Key value of `1` will replicate continuously and count towards your row usage, even if the record isn't actually modified. Additionally, records with a Replication Key value of `0` won't be replicated after the initial replication job, as the value hasn't increased.

      To avoid these issues, we recommend considering the following when selecting Replication Keys:

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Does the column meet all of the Replication Key requirements?"
        anchor: "selecting-a-replication-key--requirements"
        content: |
          Consider a column meeting [Stitch's requirements](#replication-key-requirements) as the minimum for it being a good Replication Key candidate.

          **Note**: To be selectable as a Replication Key in the **Table Settings** page, a column must meet all of [Stitch's requirements](#replication-key-requirements).

      - title: "How is the source table updated?"
        anchor: "selecting-a-replication-key--table-updates"
        content: |
          Are existing records in the table updated? 

          If existing records can be updated, is there a column that indicates a modification occurred? 

          If so, is this column's value always incremented when modification occurs?

          For example: Consider the difference between using `created_at` and `updated_at` columns containing `TIMESTAMP` data:

          - `created_at` is populated when the record is initially created. This value doesn't change when the record is modified, meaning that updates occurring after creation wouldn't be captured during Extraction.

          - `updated_at` is populated when the record is initially created and incremented when the record is modified. The initial record would be captured during Extraction, along with updates occurring after creation.

      - title: "Is the column ever null?"
        anchor: "selecting-a-replication-key--null"
        content: |
          Records with `NULL` Replication Key values will only be replicated during the first extraction of an integration. This means subsequent extractions will not capture records where the Replication Key is `NULL`. Stitch uses the Replication Key column to detect new and updated data - without it, data can't be correctly detected and replicated.

          If the Replication Key field is entirely `NULL`, the table will be extracted in full during each job until a non-`NULL` value is received and stored as a bookmark.

          **Note**: Columns must contain at least one non-`NULL` value for the column [to be created in your destination]({{ link.replication.syncing | prepend: site.baseurl | append: "#replication-requirements" }}). This means that in this scenario, the entirely null Replication Key column won't be created in the destination until Stitch recieves a non-`NULL` value.

          **NULL is a defined BSON data type in MongoDB.** Unlike SQL, `NULLs` can actually compare to other data types and replicate without issue.

      - title: "Does the column's data type auto-increment?"
        anchor: "selecting-a-replication-key--auto-increment"
        content: |
          If the column's data type doesn't auto-increment, data discrepancies can occur. This is due to Key-based Incremental Replication relying on Replication Key values increasing to detect new and modified data.

          Additionally, note that auto-incrementing integers may only be suitable Replication Keys for tables where existing records aren't updated. If an auto-incrementing integer is used as the Replication Key and existing records are updated, Stitch will only be able to detect updates if the Replication Key value also increases. This can lead to data discrepancies.

          Refer to the [Key-based Incremental Replication guide]({{ link.replication.key-based-incremental | prepend: site.baseurl | append: "#data-extraction-replication-key-types" }}) for examples.

      - title: "Are records ever hard deleted from the source table?"
        anchor: "selecting-a-replication-key--hard-deletes"
        content: |
          If records are hard deleted, Key-based Incremental Replication won't be the best Replication Method for the table. Refer to the [Key-based Incremental Replication guide]({{ link.replication.key-based-incremental | prepend: site.baseurl | append: "#limitation-2--hard-deletes-unsupported" }}) for more info.

      - title: "For MongoDB integrations, does the column only contain a single data type?"
        anchor: "selecting-a-replication-key--single-data-type"
        content: |
          {% assign mongo-data-type-guide = site.troubleshooting | where:"key","mongo-multiple-data-types" | first %}

          Fields in MongoDB (even `_id`) can contain more than one data type. These data types also have a hierarchy. In addition, [MongoDB "ranks" data types](https://docs.mongodb.com/manual/reference/bson-types/#bson-types){:target="new"}, meaning that some are considered greater than others. This can lead to problems detecting new data.

          Because Stitch may be unable to correctly identify new and updated data due to how data types are sorted, it’s best to keep Replication Key fields to a single data type. Refer to the [Missing Mongo Data Due to Fields with Multiple Data Types guide]({{ mongo-data-type-guide.url | prepend: site.baseurl }}) for more info and examples.

  - title: "Defining a table's Replication Key"
    anchor: "define-a-table-replication-key"
    summary: "How to define a table's Replication Key"
    content: |
      1. [Set a table to replicate]({{ link.replication.syncing | prepend: site.baseurl }}).
      2. In the **Table Settings** page, select [Key-based Incremental Replication]({{ link.replication.key-based-incremental | prepend: site.baseurl }}) as the Replication Method.
      3. In the **Replication Key** dropdown, select a column to use as a Replication Key:

         ![Selecting a Replication Key for a table in the Table Settings page]({{ site.baseurl }}/images/replication/define-replication-key-for-table.png){:style="max-width: 450px;"}

         If a column doesn't appear in this dropdown, verify that it meets all the [requirements](#replication-key-requirements).

      4. When finished, click the **Update Settings** button.

      **Note**: A table's Replication Key can be changed at any time, but doing so will queue a full re-replication of the table. You will be asked to confirm before the change is applied.

  - title: "Resetting Replication Keys"
    anchor: "resetting-replication-keys"
    summary: "How to reset Replication Keys"
    content: |
      Replication Key resets clear saved Replication Key values for incremental tables and queue a full re-replication of data. Refer to the [Resetting Replication Keys guide]({{ link.replication.reset-rep-keys | prepend: site.baseurl }}) to learn how resets work, what you should consider beforehand, and how to perform them.
--- 