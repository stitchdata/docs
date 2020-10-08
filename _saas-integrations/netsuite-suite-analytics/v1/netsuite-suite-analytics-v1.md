---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas/
## FOR INSTRUCTIONS & REFERENCE INFO


# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: NetSuite Suite Analytics (v1)
permalink: /integrations/saas/netsuite-suite-analytics
keywords: netsuite suite analytics, integration, schema, etl netsuite suite analytics, netsuite suite analytics etl, netsuite suite analytics schema
layout: singer
# input: false

key: "netsuite-analytics-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "netsuite-suite-analytics"
display_name: "NetSuite Suite Analytics"

singer: true
status-url: ""

tap-name: "NetSuite Suite Analytics"
repo-url: "Not applicable"

this-version: "1"

api: |
  SuiteAnalytics Connect JDBC driver


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

api-type: "platform.netsuite-suite-analytics"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true
define-replication-methods: true
define-replication-keys: true

table-selection: true
column-selection: true
table-level-reset: true


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Using this integration requires that the [SuiteAnalytics feature](#setup-requirements) be enabled in your NetSuite account.

  Refer to the [Schema](#schema) section for a list of objects available for replication.

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: "**Administrator permissions in NetSuite.**. This is required to complete the setup steps in NetSuite."
  - item: "**Access to the SuiteAnalytics feature in NetSuite.** Suite Analytics is a premium NetSuite feature. Contact your NetSuite administrator if you have questions about this feature."

setup-steps:
  - title: "Create a Stitch NetSuite role and configure permissions"
    anchor: "create-configure-stitch-role"
    content: |
      To connect {{ integration.display_name }} to Stitch, we recommend that you create a Stitch-specific role and user for us.

      1. Using the global search, type `page: new role` and click the **Page: New Role** result.
      2. In the **General** section, enter a name for the role in the **Name** field. For example: `Stitch SuiteAnalytics`
      3. Scroll down to the **Permissions** tab and click the **Setup** subtab, if it isn't already open.
      4. Using the **Permission** dropdown, search for `SuiteAnalytics Connect`:

         ![The SuiteAnalytics Connect permission in the Create Role screen in NetSuite]({{ site.baseurl }}/images/integrations/netsuite-suite-analytics-role-permissions.png)
      5. Click **Add** to add the permission to the role.
      6. When finished, click **Save** to create the role.

# SuiteAnalytics Connect permissions documentation:
# https://1796361.app.netsuite.com/app/help/helpcenter.nl?fid=section_3998867068.html

  - title: "Get the role's internal ID"
    anchor: "get-role-internal-id"
    content: |
      1. Using the global search, type `page: manage roles` and click the **Page: Manage Roles** result.
      2. Locate the role you created [in the previous step](#create-configure-stitch-role).
      3. Locate the role's **Internal ID**:

         ![The role's internal ID in the Manage Roles screen in NetSuite]({{ site.baseurl }}/images/integrations/netsuite-suite-analytics-role-id.png)

         **Note**: If you don't see the **Internal ID** column, click the **Edit View** button to add it.

      Keep this info handy - you'll need it to complete the setup in Stitch.

  - title: "Create a Stitch NetSuite user and assign the role"
    anchor: "create-stitch-netsuite-user"
    content: |
      {% include integrations/saas/netsuite-create-user.html step-number="1" step-anchor="create-configure-stitch-role" %}

  - title: "Retrieve SuiteAnalytics Connect details"
    anchor: "retrieve-suite-analytics-connect"
    content: |
      In this step, you'll retrieve the details required to connect to {{ integration.display_name }} from NetSuite.

      1. On the home page of your NetSuite account, click **Settings > Set Up SuiteAnalytics Connect**:

         ![The NetSuite homepage with the Set Up SuiteAnalytics Connect option highlighted]({{ site.baseurl }}/images/integrations/netsuite-suite-analytics-home-settings.png)
      2. The next page will display the connection details in the **Your Configuration** section:

         ![The Your Configuration section of the Set Up SuiteAnalytics Connect page in NetSuite]({{ site.baseurl }}/images/integrations/netsuite-suiteanalytics-connect-page.png)

      Keep this page open - you'll need it in the next step.

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      1. In the **Host** field, paste the host value from [Step 4](#retrieve-suite-analytics-connect).
      2. In the **Port** field, paste the port value from [Step 4](#retrieve-suite-analytics-connect).
      3. In the **Account ID** field, paste the account ID field from [Step 4](#retrieve-suite-analytics-connect).
      4. In the **Role ID** field, enter the role's internal ID from [Step 2](#get-role-internal-id).
      5. In the **Username** and **Password** fields, enter the Stitch user's username and password from [Step 1](#create-configure-stitch-role).
      
  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %}


# -------------------------- #
#      Replication Info      #
# -------------------------- #

replication-sections:
  - content: |
      In this section:

      {% for section in page.replication-sections %}
      {% if section.title %}
      - [{{ section.summary | flatify }}](#{{ section.anchor }})
      {% endif %}
      {% endfor %}

  - title: "Extraction"
    anchor: "extraction-details"
    summary: "Details about Extraction, including object discovery, data typing, and selecting data for replication"
    content: |
      For every table set to replicate, Stitch will perform the following during Extraction:

      {% for subsection in section.subsections %}
      - [{{ subsection.summary | flatify }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Discovery"
        anchor: "extraction--discovery"
        summary: "Discover tables, their schemas, and data type columns"
        content: |
          During Discovery, Stitch will:

          {% for sub-subsection in subsection.sub-subsections %}
          - [{{ sub-subsection.summary | flatify }}](#{{ sub-subsection.anchor }})
          {% endfor %}
        sub-subsections:
          - title: "Discover tables"
            anchor: "discovery--objects"
            summary: "Discover tables and their schemas"
            columns:
              - name: "table_name"
                description: "The name of the table."

              - name: "table_qualifer"
                description: "The name of the table qualifier. Stitch uses this data to filter out system tables."

              - name: "table_owner"
                description: "The name of the table owner. Stitch uses this data to filter out system tables."

              - name: "column_name"
                description: "The name of a column in the table."

              - name: "type_name"
                description: "The data type of the `column_name` column. Stitch uses this data to [type columns](#discovery--data-types)."

              - name: "oa_scale"
                description:  "For `NUMBER` data types, the scale of the data in the `column_name` column. Stitch uses this data to [type columns](#discovery--data-types)."
            content: |
              To discover tables and their schemas, Stitch queries the `OA_COLUMNS` system table in the [Connect Schema](https://1796361.app.netsuite.com/app/help/helpcenter.nl?fid=section_158695828012.html){:target="new"} for the following info:

              <table class="attribute-list">
              <tr>
              <td class="attribute-name"><strong>Column name</strong></td>
              <td><strong>Description</strong></td>
              </tr>
              {% for column in sub-subsection.columns %}
              <tr>
              <td class="attribute-name"><strong>{{ column.name }}</strong></td>
              <td>{{ column.description | flatify | markdownify }}</td>
              </tr>
              {% endfor %}
              </table>

              All tables where `table_qualifer != SCHEMA` and `table_owner != SYSTEM` will be returned and displayed in Stitch as avaiilable for replication.

              Refer to [NetSuite's documentation](https://1796361.app.netsuite.com/app/help/helpcenter.nl?fid=section_4410183892.html){:target="new"} for more info about the `OA_COLUMNS` system table.

          - title: "Identifying Primary Keys"
            anchor: "discovery--primary-keys"
            summary: "Identify Primary Keys"
            content: |
              Stitch's approach to Primary Keys for {{ integration.display_name }} is a bit different than other integrations. In {{ integration.display_name }}, we've found that some tables might not have Primary Keys at all, or Primary Key columns may sometimes contain `NULL` values.

              To determine if a table has Primary Keys, Stitch queries the `OA_FKEYS` system table. If the table has Primary Keys, Stitch will:
              
              1. Combine all Primary Key column values on a per record basis
              2. Hash the result and place the hash in a [system column]({{ link.destinations.storage.sdc-columns | prepend: site.baseurl }}) named `{{ system-column.record-hash }}`
              3. Designate `{{ system-column.record-hash }}` as the table's Primary Key. Primary Key columns will have a {{ site.data.ui.icons.primary-key | flatify }} icon next to their name in Stitch.
              4. Automatically set `{{ system-column.record-hash }}` and the table's Primary Key columns to replicate

              **Note**: The presence of Primary Keys partially determines [how data is loaded into your destination](#loading-details).

              Refer to [NetSuite's documentation](https://1796361.app.netsuite.com/app/help/helpcenter.nl?fid=section_4410184091.html){:target="new"} for more info about the `OA_FKEYS` system table.

          - title: "Data typing"
            anchor: "discovery--data-types"
            summary: "Type the data in discovered columns"
            data-types:
              - name: "varchar2"
                stitch-type: "string"
                notes: |
                  The `VARCHAR2` data type includes `BOOLEAN` data due to how NetSuite stores these values.

                  NetSuite stores `BOOLEAN` values as `VARCHAR2` with either a length of one (`"t"` or `"f"`) or three (`"yes"` or `"no"`). As typing can't be correctly asserted based on a length of one or three, these values are dicovered as strings.
              
              - name: "number"
                stitch-type: "integer"
                notes: |
                  If the column's `oa_scale` value is `0`, Stitch will type the data as an `INTEGER`.

              - name: "number"
                stitch-type: "number"
                notes: |
                  If the column's `oa_scale` value is greater than `0`, Stitch will type the data as a `NUMBER`.
              
              - name: "timestamp"
                stitch-type: "string (date-time)"
                notes: |
                  Stitch will type `TIMESTAMP` data as a `DATE-TIME`-formatted string.
            content: |
              Next, Stitch will assign data types to columns. To determine data types, Stitch uses the `type_name` and `oa_scale` columns returned from the `OA_COLUMNS` system table [during table discovery](#discovery--objects).

              In the following table:

              - **NetSuite data type**: The data type in NetSuite, based on the column's `type_name` value.
              - **Stitch data type**: The Stitch data type the NetSuite type will be mapped to.
              - **Description:** Details about the data type or mapping.

              <table class="attribute-list">
              <tr>
              <td class="attribute-name">
              <strong>NetSuite data type</strong>
              </td>
              <td width="18%; fixed">
              <strong>Stitch data type</strong>
              </td>
              <td>
              <strong>Description</strong>
              </td>
              </tr>
              {% for data-type in sub-subsection.data-types %}
              <tr>
              <td class="attribute-name">
              <strong>{{ data-type.name | upcase }}</strong>
              </td>
              <td>
              {{ data-type.stitch-type | upcase }}
              </td>
              <td>
              {{ data-type.notes | flatify | markdownify }}
              </td>
              </tr>
              {% endfor %}
              </table>

      - title: "Data replication"
        anchor: "extraction--data-replication"
        summary: "Select records for replication"
        content: |
          After discovery is completed, Stitch will move onto extracting data. The [Replication Method]({{ link.replication.rep-methods | prepend: site.baseurl }}) Stitch uses is dependent on whether the table contains valid [Replication Key columns]({{ link.replication.rep-keys | prepend: site.baseurl }}).

          Stitch will default to using [Key-based Incremental Replication]({{ link.replication.key-based-incremental | prepend: site.baseurl }}) if a table contains any of the following columns:

          - `last_modified_date`
          - `date_last_modified`
          - `date_deleted`
          - `date_last_modified_gmt` (`transaction_lines` table only)

          If a table contains more than one of the above columns, you'll be prompted to select a column to use as a Replication Key when you set the table to replicate. Otherwise, Stitch will use the single column as the Replication Key for the table.

          If a table doesn't contain any of the above columns, Stitch will default to using [Full Table Replication]({{ link.replication.full-table | prepend: site.baseurl }}).

          As this integration supports configuring Replication Methods, you can toggle between Replication Methods for tables on the **Table Settings** page in Stitch.

  - title: "Loading"
    anchor: "loading-details"
    summary: "Details about how data replicated from {{ integration.display_name }} is loaded into a destination"
    content: |
      How data replicated from an {{ integration.display_name }} integration is loaded into your destination depends on two factors:

      1. **If the table has Primary Keys** identified [during discovery](#discovery--primary-keys).

      2. **If your destination supports upserts, or updating existing rows**. For destinations that support upserts, Stitch uses Primary Keys to de-dupe data during loading. {{ site.data.tooltips.primary-key }}

         **Note**: For Append-Only destinations, data will be loaded in an Append-Only manner regardless of whether a table has Primary Keys.

    subsections:
      - title: "Loading with Primary Keys"
        anchor: "loading--with-primary-keys"
        content: |
          If the destination supports upserts and the table has Primary Keys, Stitch will de-dupe records using `{{ system-column.record-hash }}` as the Primary Key.

          This means that existing rows will be overwritten with the most recent version of the row. A record can only have a single unique Primary Key value, ensuring that only one version of the record exists in the destination at a time.

      - title: "Loading without Primary Keys"
        anchor: "loading--without-primary-keys"
        content: |
          If the destination is Append-Only, or if the table doesn't have Primary Keys, data will be loaded in an Append-Only manner.

          This means that existing rows will never be updated with new data. New and updated records will be appended to the end of the table as new rows.

          **Note**: Querying Append-Only tables requires a different strategy than you might normally use. For instructions and a sample query, check out the [Querying Append-Only tables guide]({{ link.replication.append-only-querying | prepend: site.baseurl }}).


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/netsuite-analytics/v1

append-only-loading: |
  **Note**: As this table doesn't have a Primary Key, data will be loaded using [Append-Only loading]({{ link.destinations.storage.loading-behavior | prepend: site.baseurl }}) even if your destination supports and is configured to use Upserts.

netsuite-primary-keys: |
  {% assign netsuite-pks = table.attributes | where:"netsuite-primary-key",true %}

  NetSuite designates the following columns as Primary Keys for this table:

  {% for pk in netsuite-pks %}
  - `{{ pk.name }}`
  {% endfor %}

netsuite-primary-key-description: "**Note**: This column is used to create the `{{ system-column.record-hash }}` value."

netsuite-replication-keys: |
  {% assign netsuite-rks = table.attributes | where:"replication-key",true %}

  If you set this table to replicate and select Key-based Incremental Replication, you'll need to also select a Replication Key.

  There are multiple possible Replication Keys for this table:

  {% for rk in netsuite-rks %}
  - `{{ rk.name }}`
  {% endfor %}


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}