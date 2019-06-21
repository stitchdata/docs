---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Quick Base (v1.0)
permalink: /integrations/saas/quick-base
keywords: quick-base, integration, schema, etl quick-base, quick-base etl, quick-base schema
layout: singer
old-schema-template: true

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "quick-base"
display_name: "Quick Base"

singer: true
repo-url: https://github.com/singer-io/tap-quickbase

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false

historical: "1 year"
frequency: "1 hour"
tier: "Free"
status-url: https://service.quickbase.com/#!/

table-selection: true
column-selection: true

anchor-scheduling: true
cron-scheduling: false

extraction-logs: true
loading-reports: true

# -------------------------- #
#  Quick Base Default Fields #
# -------------------------- #

## The fields included in every Quick Base table by default.

default-table-fields:
  - name: "rid"
    type: "string"
    description: "The unique record ID. **This is the Primary Key for the table.**"

  - name: "record_id"
    type: "string"
    description: "The unique record ID."

  - name: "date_created"
    type: "date-time"
    description: "The date the record was created."

  - name: "date_modified"
    type: "date-time"
    description: |
      The date the record was last modified. This is the column Stitch will use as a [Replication Key]({{ link.replication.rep-keys | prepend: site.baseurl }}).

  - name: "last_modified_by"
    type: "string"
    description: "The ID of the user who last modified the record."

  - name: "record_owner"
    type: "string"
    description: "The ID of the user who created the record."


# -------------------------- #
#    Column name examples    #
# -------------------------- #

example-field-names:
  - quickbase: "Customer Name"
    stitch: "customer_name"

  - quickbase: "Is a VIP?"
    stitch: "is_a_vip"

  - quickbase: "EmAiLAdDrEsS"
    stitch: "emailaddress"

  - quickbase: "Street!Address"
    stitch: "streetaddress"

  - quickbase: "Phone #number"
    stitch: "phone_number"

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

setup-steps:
  - title: "Retrieve your {{ integration.display_name }} URL and app ID"
    anchor: "retrieve-url-app-id"
    substeps:
      - title: "Retrieve your {{ integration.display_name }} URL"
        anchor: "retrieve-quick-base-url"
        content: |
          To retrieve your URL, sign into your {{ integration.display_name }} account.

          You'll need to enter the URL that displays in your browser into Stitch. You should include the `https://` portion, and omit anything after `db/`.

          For example: Based on the URL in the image below, we'd enter `https://stitchdata.quickbase.com/db/` into Stitch:

          ![]({{ site.baseurl }}/images/integrations/quick-base-url.png)

      - title: "Retrieve your {{ integration.display_name }} app ID"
        anchor: "retrieve-quick-base-app-id"
        content: |
          Next, you need to retrieve the ID of the {{ integration.display_name }} app you want to replicate data from.

          In {{ integration.display_name }}, click the desired app in the **My Apps** section.

          When the app opens, the URL in your browser will now contain the app's ID. This is the alpha-numeric string after `db/`. In this example, the app ID is `bngf9ix7e`.

          ![]({{ site.baseurl }}/images/integrations/quick-base-app-id.png)

  - title: "Create a {{ integration.display_name }} user token"
    anchor: "create-quick-base-user-token"
    content: |

      {% capture user-tokens %}
      {{ integration.display_name }} user tokens are linked to the user who creates them. This means that Stitch will only be able to access the same data in {{ integration.display_name }} as the user who creates the token.

      Before proceeding, verify that you can access the tables and fields in {{ integration.display_name }} that you want to replicate.
      {% endcapture %}

      {% include note.html first-line="**QuickBase user tokens**" content=user-tokens %}

      1. In {{ integration.display_name }}, click the user menu (your name) in the top right corner.
      2. Click **My preferences**.
      3. In the **My User Information** section, click **Manage my user tokens for [company name] realm...**, located next to **Manage User Tokens**.
      4. On the **My User Tokens** page, click **+ New user token**.
      5. Fill in the following:
         - **Name**: Enter a name for the token. For example: `Stitch`
         - **Description**: If desired, enter a description.
         - **Assign token to apps**: From the dropdown, select the app you want to replicate data from.
      6. Click **Save**.

      The token will display in the **Token** field of the **My User Tokens** page. Keep this page open for now - you'll need it to complete the next step.
  - title: "add integration"
    content: |
      4. In the **Quick Base API URL** field, enter the {{ integration.display_name }} URL you retrieved in Step 1. For example: `https://stitchdata.quickbase.com/db/`
      5. In the **Quick Base APP ID** field, enter the {{ integration.display_name }} app ID you retrieved in Step 1. For example: `bngf9ix7e`
      6. In the **Quick Base User Token** field, paste the user token you created in Step 2.
  - title: "historical sync"
  - title: "replication frequency"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/quick-base

schema-sections:
  - content: |
      Every table in a {{ integration.display_name }} app will display as a selectable table in the Stitch app. Tables are named according to this convention: `[app_name]__[table_name]`.

      For example: If an app named `event_handling` contained `customers`, `events`, and `rsvps` tables, you could expect the following tables to be created in your destination:

      - `event_handling__customers`
      - `event_handling__events`
      - `event_handling__rsvps`

  - title: "Table attributes"
    anchor: "table-attributes"
    content: |
      The schema of {{ integration.display_name }} tables will contain the fields the user linked with the [user token](#create-quick-base-user-token) has access to, along with a handful of other fields:

      <table class="attribute-list">
      {% for attribute in integration.default-table-fields %}
      <tr>
      <td class="attribute-name">
      <strong>{{ attribute.name }}</strong><br>
      {{ attribute.type | upcase }}
      </td>
      <td class="description">
      {{ attribute.description | flatify | markdownify }}
      </td>
      </tr>
      {% endfor %}
      </table>

      #### Attribute names {#table-attribute-names}

      Some destinations restrict the use of special characters and spaces in column names. While {{ integration.display_name }} doesn't restrict the use of these characters in their app, attempting to load column names as-is from {{ integration.display_name }} may cause issues.

      To prevent loading issues, Stitch's {{ integration.display_name }} will perform the following on column names:

      - Replace spaces and hyphens (`-`) with underscores (`_`)
      - Remove all other nonalphanumeric characters, such as `!` or `#`
      - Lowercase capitalized characters

      Below are a handful of examples of how {{ integration.display_name }} column names will appear in Stitch:

      <table class="attribute-list">
      <tr>
      <td width="50%; fixed">
      <strong>Column name in {{ integration.display_name }}</strong>
      </td>
      <td>
      <strong>Column name in Stitch</strong>
      </td>
      </tr>
      {% for attribute in integration.example-field-names %}
      <tr>
      <td>
      {{ attribute.quickbase }}
      </td>
      <td>
      {{ attribute.stitch }}
      </td>
      </tr>
      {% endfor %}
      </table>
---
{% assign integration = page %}
{% include misc/data-files.html %}