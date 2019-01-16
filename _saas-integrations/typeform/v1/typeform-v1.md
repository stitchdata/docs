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

title: Typeform
permalink: /integrations/saas/typeform
tags: [saas_integrations]
keywords: typeform, integration, schema, etl typeform, typeform etl, typeform schema
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "typeform"
display_name: "Typeform"

singer: true 
tap-name: "Typeform"
repo-url: https://github.com/singer-io/tap-typeform

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Open Beta"
certified: false 

historical: "1 year"
frequency: "1 hour"
tier: "Free"
status-url: "https://status.typeform.com/"
icon: /images/integrations/icons/typeform.svg

anchor-scheduling: true
extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

setup-steps:
  - title: "Generate a {{ integration.display_name }} API token"
    anchor: "generate-{{ integration.name }}-api-token"
    content: |
      1. Sign into your {{ integration.display_name }} account.
      2. Click the user menu (your icon) in the top right corner of the page.
      3. In the menu, click **My Account**.
      4. On the page that displays, click **Personal tokens** on the left side of the page.
      5. The **Personal tokens** page will display. Click the **Generate a new token** button.
      6. Enter a **Token name**. For example: `Stitch`
      7. In the **Scopes** section, click **Custom scopes**. 
      8. In the list that displays, select the **Read** option for the following permissions:
         - **Accounts**
         - **Forms**
         - **Images**
         - **Responses**
         - **Themes**
         - **Workspaces**
      9. Click **Generate token**.
      10. A window with the token will display. Copy the token somewhere handy, as you'll need it to complete the setup. **Note**: {{ integration.display_name }} will only display the token once. If you close this window, you'll need to re-generate the token.

  - title: "Retrieve {{ integration.display_name }} form IDs"
    anchor: "retrieve-{{ integration.name }}-form-ids"
    content: |
      Stitch's {{ integration.display_name }} will retrieve data only for the forms you specify in the {{ app.page-names.int-settings }} page. In this step, you'll retrieve the IDs of the forms you want Stitch to replicate.

      1. In your {{ integration.display_name }} account, navigate back to your workspaces.
      2. On the workspace page, click on a form you want to include in Stitch. This should open the form's edit page.
      3. Look at the URL of the page in your browser. It should be similar to `https://admin.typeform.com/form/FrZ6iD/create`. The string between `form/` and `/create` is the form's ID. In this example, the ID is `FrZ6iD`.
      4. Copy the form ID somewhere handy.
      5. Repeat steps 2-4 for every form you want to include in Stitch.

  - title: "add integration"
    content: |
      4. In the **API Token** field, paste the {{ integration.display_name }} API token you generated in [Step 1](#generate-{{ integration.name }}-api-token).
      5. In the **Forms** field, enter a comma-separated list of the form IDs you retrieved in [Step 2](#retrieve-{{ integration.name }}-form-ids). For example:
         - **Single form**: `FrZ6iD`
         - **Multiple forms**: `FrZ6iD, f8nzFM`
      6. In the **Incremental Range** dropdown, select the type of data aggregation you want Stitch to use:

         - **Daily**: Data will be aggregated by day.
         - **Hourly**: Data will be aggregated by hour.
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/typeform
---
{% assign integration = page %}
{% include misc/data-files.html %}