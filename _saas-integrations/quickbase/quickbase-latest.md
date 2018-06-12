---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Quick Base
permalink: /integrations/saas/quick-base
tags: [saas_integrations]
keywords: quick-base, integration, schema, etl quick-base, quick-base etl, quick-base schema
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "quick-base"
display_name: "Quick Base"
singer: true
repo-url: https://github.com/singer-io/tap-quickbase

# this-version: ""

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false

historical: "1 year"
frequency: "1 hour"
tier: "Free"
status-url: https://service.quickbase.com/#!/
icon: /images/integrations/icons/quick-base.svg
whitelist:
  tables: true
  columns: false

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: ""
  - item: ""

requirements-info:

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
      {{ integration.display_name }} user tokens are linked to the user who creates them. This means that Stitch will only be able to access the same data in {{ integration.display_name }} as the user who creates the token.<br><br>
      Before proceeding, verify that you can access the tables and fields in {{ integration.display_name }} that you want to replicate.
      {% endcapture %}

      {% include note.html content=user-tokens %}

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
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/quick-base

schema-sections:
  - title: "Milliseconds"
    anchor: ""
    content: |
      https://github.com/singer-io/tap-quickbase/blob/master/tap_quickbase/__init__.py#L89

---
{% assign integration = page %}
{% include misc/data-files.html %}

