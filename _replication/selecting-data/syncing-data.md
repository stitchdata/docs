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
  - title: "Applicable integrations"
    anchor: "applicable-integrations"
    summary: "The integrations this guide is applicable to"
    content: |
      This guide is applicable to all database and SaaS integrations.

      **Note**: Webhook integrations don't support table and column selection. By default, all data sent to Stitch in a webhook message will be loaded to your destination. Refer to the webhook provider's documentation for info about possible attributes.

  - title: "How object selection works"
    anchor: "how-object-selection-works"
    summary: "How object selection works"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "How objects are discovered"
        anchor: "how-objects-are-discovered"
        content: |
          During the Discovery phase of Extraction, Stitch detects the objects available for replication in a data source. Sometimes called a structure sync, this process is how Stitch determines the structure of the tables and columns in an integration. Objects must meet the [selection requirements](#object-selection-and-replication-requirements) to display and be selectable in Stitch.

          In an integration's {{ app.buttons.tables }} tab, you can select the individual databases (if applicable), tables, and columns you want to replicate. Integrations will have a status of `Not Configured` until at least one table and column are selected.

      - title: "Levels of object selection support"
        anchor: "object-selection-support"
        content: |
          While the majority of Stitch's integrations support table and column selection, some may only support table selection, while others don't have any object selection support.

          When an integration doesn't support table and/or column selection:

          - **Table selection**: If an integration doesn't support table selection, all available tables and columns are automatically set to replicate. For detailed info on the data Stitch replicates from [SaaS integrations]({{ site.baseurl }}/integrations/saas), check out the **Schema** section of any integration's guide.

          - **Column selection**: If an integration supports table selection but not column selection, all available columns in selected tables will automatically be set to replicate.

          Refer to the [Object selection support reference](#table-column-selection-support) for more info about what each of Stitch's integrations support.

  - title: "Object selection and replication requirements"
    anchor: "object-selection-and-replication-requirements"
    summary: "What's required to select and replicate objects in Stitch"
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
          - Stitch successfully completes Discovery, or a structure sync. Stitch will automatically detect new objects, but [a structure sync](#individual-objects--new-additional-columns) must complete before the object will display in Stitch.
          - **For tables**, there are additional requirements:
             - For SaaS integrations, the integration supports the API endpoint associated with the table. Refer to the [integration's schema documentation]({{ site.baseurl }}/integrations/saas) for a list of available objects and endpoints associated with them.
          - **For columns**, there are additional requirements:
             - The column contains data typed using a [supported data type]({{ link.replication.supported-data-types | prepend: site.baseurl }}). Columns containing unsupported data types will display as [Not supported](#not-supported-table-column-message) in Stitch.
             - For SaaS integrations backed by Singer taps, the tap must either dynamically include the field or the JSON schema used to create the given table must contain the column. Refer to the [integration's schema documentation]({{ site.baseurl }}/integrations/saas) for more info.

      - title: "Requirements to successfully replicate an object"
        anchor: "replication-requirements"
        content: |
          **For an object to replicate successfully**, the following requirements, along with the [selection requirements](#selection-requirements), must be met:

          - The object is set to replicate
          - [All parent objects are set to replicate](#parent-object-not-set-to-replicate). This means that an object that contains other objects must be set to replicate for the objects they contain to replicate.

            For example: For a column to replicate, the table that contains it must also be selected. If applicable, so must the schema containing the table, and the database containing the schema. You'll receive an [error in Stitch](#parent-object-not-set-to-replicate) if the parent object isn't selected.
          
          - The user authorizing the destination has the required permissions for your destination type
          - The name of the object adheres to your destination's requirements. Refer to the [documentation for your destination type]({{ link.destinations.main | prepend: site.baseurl }}) for more info.
          - **For tables**, there are additional requirements:
             - The table and at least one column are set to replicate
             - The table has a defined [Replication Method]({{ link.replication.rep-methods | prepend: site.baseurl }}) and [Replication Key]({{ link.replication.rep-keys | prepend: site.baseurl }}), if applicable
             - For integrations that replicate files, the file meets the integration's requirements. For example: A [Google Sheet]({{ site.baseurl }}/integrations/saas/google-sheets) must contain a header row and a second row of data.
             - The table doesn't exceed the maximum columns per table allowed by your destination type, if applicable
          - **For columns**, there are additional requirements:
             - The column contains at least [one non-`NULL` value]({{ link.troubleshooting.column-nulls | prepend: site.baseurl }})

  - title: "Setting objects to replicate"
    anchor: "set-data-to-replicate"
    summary: "How to set objects to replicate"
    content: |
      In this section:

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "Selecting individual objects"
        anchor: "select-individual-objects"
        content: |
          {% for sub-subsection in subsection.sub-subsections %}
          - [{{ sub-subsection.title | remove: "Selecting " | capitalize }}](#{{ sub-subsection.anchor }})
          {% endfor %}
        sub-subsections:
          - title: "Selecting tables and columns"
            anchor: "individual-objects--tables-columns"
            content: |
              To set objects to replicate:

              1. Click into the integration from the {{ app.page-names.dashboard }} page.
              2. Click the {{ app.buttons.tables }} tab.
              3. Locate the table or column you want to replicate. **Note**: If there's a parent object such as a schema, verify that it's also selected.
              4. {{ app.menu-paths.sync | replace: "replicate.", "replicate:" }}

                 ![Selected tables in Stitch, which have blue checkmarks]({{ site.baseurl }}/images/replication/table-selection.png)

                 When a table is selected, keep in mind that:

                 - **For database integrations**, all columns are automatically set to replicate. **Note**: The process varies slightly for **Amazon DynamoDB** and **MongoDB-backed** integrations, which use [projection expressions]({{ link.integrations.dynamodb-projection-expressions | prepend: site.baseurl }}) and [projection queries]({{ link.integrations.mongodb-projection-queries | prepend: site.baseurl }}) to select columns.

                 - **For SaaS integrations that support column selection**, you need to select columns by clicking into the table. In the list of columns, click the checkbox next to the column you want to replicate.
              5. If setting a table to replicate, define the table's [Replication Method]({{ link.replication.rep-methods | prepend: site.baseurl }}), if prompted. Only integrations that support configuring Replication Methods will display this prompt.
              6. {{ app.menu-paths.finalize-selections | flatify }}

          - title: "Selecting new and additional columns in already-selected tables"
            anchor: "individual-objects--new-additional-columns"
            content: |
              What happens when you've added a brand-new column in the data source or you want to replicate additional columns on an already-replicating table?

              For more info check out the [Setting New and Additional Columns to Replicate]({{ link.replication.syncing-new-columns | prepend: site.baseurl }}) guide.

          - title: "Selecting database views"
            anchor: "individual-objects--database-views"
            content: |
              While the steps for replicating a database view are almost the same as those for replicating a table, there are some slight differences.

              For more info, check out the [Replicating Database Views]({{ link.replication.db-views | prepend: site.baseurl }}) guide.

      - title: "Selecting all objects"
        anchor: "set-all-data-to-replicate"
        summary: "How to set all objects to replicate"
        content: |
          {% for sub-subsection in subsection.sub-subsections %}
          - [{{ sub-subsection.title }}](#{{ sub-subsection.anchor }})
          {% endfor %}

        sub-subsections:
          - title: "How the Select all feature works"
            anchor: "select-all--functionality"
            content: |
              The **Select all** feature, located in an integration's {{ app.buttons.tables }} tab, allows you to select all of an integration's tables and columns with just a few clicks.

              When used to select all tables, the following occurs:

              - All tables and [supported columns](#selection-requirements) are set to replicate. **Note**: Database views are not supported with this feature and won't be selected.
              - Previous column selections are overwritten. **Note**: Selections aren't final until **Finalize Your Selections** is clicked. Clicking **Cancel** will restore your previous selections.
              - Tables with defined Replication Methods will continue to use that Replication Method.

          - title: "Requirements to use the Select all feature"
            anchor: "select-all--requirements"
            content: |
              To use the **Select all** feature, all of the following must be true for an integration:

              - The integration is backed by a Singer tap
              - The integration supports table selection. If the integration doesn't support table selection, all available tables and columns will be set to replicate by default.
              - **For database integrations**, there are additional requirements:
                 - **Stitch supports Log-based Incremental Replication for the database.** Some database cloud providers may not support the features Stitch requires to perform Log-based Incremental Replication, even if the source database supports those features. For example: Heroku doesn't currently support logical replication for PostgreSQL.
                 - **The Default Replication Method setting is available and enabled for the integration**. In addition to having Log-based Incremental Replication support in Stitch, the **Default Replication Method** setting must be available and enabled.

              - **For SaaS integrations**, there is an additional requirement:
                 - **The API the integration uses must allow the selection of all fields.** Some sources - like Google Ads and Microsoft Advertising - have compatibility rules that determine the combinations of fields that can be selected together. Selecting all columns for these integrations would result in incompatible combinations and unsuccessful replication.

              Refer to the [Object selection support reference](#table-column-selection-support) for a list of integrations that support this feature.

          - title: "Selecting all tables and columns"
            anchor: "select-all--usage"
            content: |
              {% capture note %}
              - **Previous column selections will be overwritten**, but new selections aren't final until **Finalize Your Selections** is clicked. Clicking **Cancel** will restore your previous selections.
              - **Not all integrations support this feature.** While the majority of do, there are some that don't. Refer to the [Object selection support reference](#table-column-selection-support) for more info.
              {% endcapture %}

              {% include note.html first-line="**Before using this feature**, note that:" content=note %}

              1. Click into the integration from the {{ app.page-names.dashboard }} page.
              2. Click the {{ app.buttons.tables }} tab.
              3. In the list of tables, click the box next to the **Table Names** column.
              4. In the menu that displays, click **Track All Tables and Fields**:

                 ![The Select/Deselect All Tables and Fields menu in the Tables to Replicate tab]({{ site.baseurl }}/images/replication/select-all-tables-menu.png)

              5. {{ app.menu-paths.finalize-selections | flatify }}

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

  - title: "Object selection support reference"
    anchor: "table-column-selection-support"
    summary: "What's supported for each integration"
    content: |
      {% include note.html type="single-line" content="**Note**: This section doesn't include webhook integrations, [as they aren't applicable to this guide](#applicable-integrations)." %}

      This section details the level of support each of Stitch's database and SaaS integrations have for the features outlined in this guide:

      - **Table selection**: Support for setting [individual tables](#individual-objects--tables-columns) to replicate
      - **Column selection**: Support for setting [individual columns](#individual-objects--tables-columns) in a table to replicate
      - **Select all**: Support for the [Select all](#set-all-data-to-replicate) feature

      Icons in the table represent the following:

      - {{ supported | replace:"TOOLTIP","Supported" }} indicates that the feature is supported
      - {{ sometimes-supported | replace:"TOOLTIP","Supported if requirements are met" }} indicates that the feature is supported, but has specific configuration requirements. Hover over the icon to view a tooltip with additional details.
      - {{ not-supported | replace:"TOOLTIP","Not supported" }} indicates that the feature isn't currently supported. Hover over the icon to view a tooltip with additional details.
          
      {% capture table %}
      {% assign saas-database-integrations = site.saas-integrations | concat: site.database-integrations | where:"content-type","integration" | sort:"display_name" %}

      {% assign feature-list = "table-selection|column-selection|select-all" | split:"|" %}

      <table class="attribute-list" id="filter-table">
      <thead>
      <tr>
      <th style="text-align: right;" width="35%; fixed">
      Integration
      </th>
      <th>
      Version
      </th>
      <th>
      Table<br>
      selection
      </th>
      <th>
      Column<br>
      selection
      </th>
      <th>
      Select all
      </th>
      </tr>
      </thead>

      <tbody id="filter-body">
      {% for integration in saas-database-integrations %}
      {% if integration.type != "import-api" %}

      {% include shared/versioning/integration-version-logic.html item-name="integration" %}

      {% unless this-version.status == "sunset" %}
      <tr>
      <td align="right" width="35%; fixed">
      <a href="{{ integration.url | prepend: site.baseurl }}">{{ integration.display_name }}</a>
      </td>
      <td>
      {% if non-sunset-versions.size > 1 and integration.this-version == latest-version %}
      {{ integration.this-version | prepend: "v" }} (latest)
      {% else %}
      {{ integration.this-version | prepend: "v" }}
      {% endif %}
      </td>
      {% for feature in feature-list %}
      {% assign feature-reason = feature | append: "-reason" %}
      <td>
      {% case integration[feature] %}
      {% when false %}
      {% if integration[feature-reason] %}
      {% assign reason = integration[feature-reason] | flatify %}
      {% else %}
      {% assign reason = "Not supported" %}
      {% endif %}

      {{ not-supported | replace:"TOOLTIP",reason | flatify }}

      {% when 'sometimes' %}
      {% if integration[feature-reason] %}
      {% assign reason = integration[feature-reason] | flatify %}
      {% else %}
      {% assign reason = "Not supported" %}
      {% endif %}

      {{ sometimes-supported | replace:"TOOLTIP",reason | flatify }}

      {% else %}

      {{ supported | replace:"TOOLTIP","Supported" }}
      {% endcase %}
      </td>
      {% endfor %}
      </tr>
      {% endunless %}
      {% endif %}
      {% endfor %}

      <tr id="noConnectionYet" style="display: none">
      <td id="noConnectionYetName" colspan="5" align="center">
        <strong>Don't see the source you want?</strong> <a href="mailto:{{site.support}}">Let us know</a>!
      </td>
      </tr>

      </tbody>
      </table>
      {% endcapture %}

      {% include layout/on-page-search/table-search.html placeholder-copy="Find an integration" table=table %}

      [Back to Object selection support reference](#table-column-selection-support)
---
{% include misc/data-files.html %}