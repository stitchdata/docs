---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Setting Tables and Columns to Replicate
permalink: /replication/extractions/data-selection/setting-tables-and-columns-to-replicate
redirect_from: /replication/syncing-data
keywords: syncing, sync, replicate, replication, select data, sync data, sync table, sync column
summary: "After you connect an integration and Stitch performs a structure sync, the next thing you'll do is select tables and columns to replicate."

key: "select-data"
category: "extraction"
content-type: "select-data"

layout: general
toc: true
weight: 1


# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  {% include misc/icons.html %}

  {{ page.summary }} In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#          CONTENT           #
# -------------------------- #

sections:
  - title: "Table and column selection support"
    anchor: "table-column-selection-support"
    summary: "What's supported for each integration"
    content: |
      Below is the level of support each integration has for table and column selection:

      - {{ supported | replace:"TOOLTIP","Supported" }} indicates that table/column selection is supported for the integration. **Note**: Only the data you select will be replicated. If nothing is selected, the integration will have a status of `Not Configured`.

      - {{ not-supported | replace:"TOOLTIP","Not supported" }} indicates that table and/or column selection isn't supported for the integration:

          - **For table selection**, all available tables and columns will be automatically set to replicate. For detailed info on the data Stitch replicates from [SaaS integrations]({{ site.baseurl }}/integrations/saas), check out the **Schema** section of any integration's guide.
          - **For column selection**, all available columns in the tables you select will be automatically set to replicate.

      {% include replication/integrations-with-whitelisting.html %}

  - title: "Object selection and replication requirements"
    anchor: "object-selection-and-replication-requirements"
    summary: "What's required to select and replicate an object"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Requirements to select an object"
        anchor: "selection-requirements"
        content: |
          **For an object to be selectable in Stitch**, all of the following must be true:

          - The user authorizing the integration has permission to access the object in the source
          - Stitch has completed a structure sync. Stitch will automatically detect new objects, but [a structure sync](#select-new-additional-columns) must complete before the object will display in Stitch.
          - **For tables**, there are additional requirements:
             - For SaaS integrations, the integration supports the API endpoint associated with the table. Refer to the [integration's schema documentation]({{ site.baseurl }}/integrations/saas) for a list of available objects and endpoints associated with them.
          - **For columns**, there are additional requirements:
             - The column contains data typed using a [supported data type]({{ link.replication.supported-data-types | prepend: site.baseurl }}). Columns containing unsupported data types will display as [Not supported](##not-supported-table-column-message) in Stitch.
             - For SaaS integrations backed by Singer taps, the JSON schema used to create the table containing the column contains the column. Refer to the [integration's schema documentation]({{ site.baseurl }}/integrations/saas) for more info.

      - title: "Requirements to successfully replicate an object"
        anchor: "replication-requirements"
        content: |
          **For an object to replicate successfully**, the following requirements, along with the [selection requirements](#selection-requirements), must be met:

          - [All parent objects are set to replicate](#parent-object-not-set-to-replicate)
          - The object is set to replicate
          - The user authorizing the destination has the required permissions for your destination type
          - The name of the object adheres to your destination's requirements. Refer to the [documentation for your destination type]({{ link.destinations.main | prepend: site.baseurl }}) for more info.
          - **For tables**, there are additional requirements:
             - The table and at least one column are set to replicate
             - The table has a defined [Replication Method]({{ link.replication.rep-methods | prepend: site.baseurl }}) and [Replication Key]({{ link.replication.rep-keys | prepend: site.baseurl }}), if applicable
             - For integrations that replicate files, the file meets the integration's requirements. For example: A [Google Sheet]({{ site.baseurl }}/integrations/saas/google-sheets) must contain a header row and a second row of data.
             - The table doesn't exceed the columns per table maximum allowed by your destination type, if applicable
          - **For columns**, there are additional requirements:
             - The column contains at least [one non-`NULL` value]({{ link.troubleshooting.column-nulls | prepend: site.baseurl }})

  - title: "Setting objects to replicate"
    anchor: "set-data-to-replicate"
    summary: "How to set objects to replicate in Stitch"
    content: |
      To set objects to replicate, click into the integration from the {{ app.page-names.dashboard }} page and find the table or column you want to replicate. Then, {{ app.menu-paths.sync | replace: "Click","click" }} Keep in mind that:

      - **For database integration tables**, all columns will be set to replicate automatically. 

        **Note**: The process varies slightly for the following integrations:

        - **Amazon DynamoDB:** Fields are selected using [projection expressions]({{ link.integrations.dynamodb-projection-expressions | prepend: site.baseurl }})
        - **MongoDB**: Fields are selected by using [projection queries]({{ link.integrations.mongodb-projection-queries | prepend: site.baseurl }})

      - **For SaaS integration tables that support column selection**, you can select columns by clicking on the **table name** and then tracking columns to replicate.

      If the integration supports configuring [Replication Methods]({{ link.replication.rep-methods | prepend: site.baseurl }}), you'll also be prompted to define this setting when you set a table to replicate.

      **Note**: Parent objects - or objects that contain other objects - must be set to replicate for the objects they contain to replicate. For example: For a column to replicate, the table that contains it must also be selected. If applicable, so must the schema containing the table, and the database containing the schema. You'll receive an [error in Stitch](#parent-object-not-set-to-replicate) if the parent object isn't selected.

    subsections:
      - title: "Selecting new and additional columns in already-selected tables"
        anchor: "select-new-additional-columns"
        content: |
          What happens when you've added a brand-new column in the data source or you want to replicate additional columns on an already-replicating table?

          For more info check out the [Setting New and Additional Columns to Replicate]({{ link.replication.syncing-new-columns | prepend: site.baseurl }}) guide.

      - title: "Selecting database views"
        anchor: "select-database-views"
        content: |
          While the steps for replicating a database view are almost the same as those for replicating a table, there are some slight differences.

          For more info check out the [Replicating Database Views]({{ link.replication.db-views | prepend: site.baseurl }}) guide.

  - title: "Troubleshooting common issues"
    anchor: "troubleshooting-common-issues"
    summary: "How to troubleshoot common object selection issues"
    content: |
      In this section:

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}]({{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Missing objects"
        anchor: "missing-objects"
        content: |
          {% capture code %}
          Stitch cannot detect any objects (databases, tables, etc.) at or below this level.
          {% endcapture %}

          {% include layout/code-snippet.html code=code %}

          If you receive this message or you can't find an object (database, table, column, etc.), [it's typically a permissions issue]({{ link.troubleshooting.missing-objects | prepend: site.baseurl }}).

      - title: "Not supported table/column messages"
        anchor: "not-supported-table-column-message"
        content: |
          If you see a status of `Not Supported` for a table or column in a database integration, there a few potential root causes:

          - **Insufficient permissions.** Verify that the Stitch user has all the required permissions as outlined in the **Setup** instructions for the database. Refer to the documentation for [your database]({{ site.baseurl }}/integrations/databases) for more info.

             After you grant the required permissions and a full replication cycle has completed, the table's **Sync Status** should change to `Supported` and be available for syncing.
          - **Unsupported column.** If a column is displayed as `Not Supported`, it may be that the column contains an [unsupported data type]({{ link.troubleshooting.unsupported-data-types | prepend: site.baseurl }}).

      - title: "Parent object not set to replicate"
        anchor: "parent-object-not-set-to-replicate"
        content: |
          {% capture code %}
          The table containing these columns is not set to sync. Please sync the parent table to ensure replication of columns selected on this screen.
          {% endcapture %}

          {% include layout/code-snippet.html code=code %}

          If you receive this message, it means that the object above it isn't set to replicate. For example: The table that contains a selected column isn't set to replicate. [Parent objects must be selected for the objects they contain to also replicate](#set-data-to-replicate).
---
{% include misc/data-files.html %}