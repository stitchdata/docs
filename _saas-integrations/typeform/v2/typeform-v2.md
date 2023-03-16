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

title: Typeform (v2)
permalink: /integrations/saas/typeform
keywords: typeform, integration, schema, etl typeform, typeform etl, typeform schema
summary: "Connections instructions, replication info, and schema details for Stitch's Typeform integration."
layout: singer
# input: false

key: "typeform-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "typeform"
display_name: "Typeform"

singer: true 
tap-name: "Typeform"
repo-url: https://github.com/singer-io/tap-typeform

this-version: "2"

api: |
  [{{ integration.display_name }} Create](https://developer.typeform.com/create/){:target="new"} and [Responses](https://developer.typeform.com/responses/){:target="new"} APIs

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Standard"
status-url: "https://status.typeform.com/"

api-type: "platform.typeform"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

setup-steps:
  - title: "Retrieve {{ integration.display_name }} form IDs"
    anchor: "retrieve-typeform-form-ids"
    content: |
      Stitch's {{ integration.display_name }} will retrieve data only for the forms you specify in the {{ app.page-names.int-settings }} page. In this step, you'll retrieve the IDs of the forms you want Stitch to replicate.

      1. In your {{ integration.display_name }} account, navigate back to your workspaces.
      2. On the workspace page, click on a form you want to include in Stitch. This should open the form's edit page.
      3. Look at the URL of the page in your browser. It should be similar to `https://admin.typeform.com/form/FrZ6iD/create`. The string between `form/` and `/create` is the form's ID. In this example, the ID is `FrZ6iD`.
      4. Copy the form ID somewhere handy.
      5. Repeat steps 2-4 for every form you want to include in Stitch.

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      5. In the **Forms** field, enter a comma-separated list of the form IDs you retrieved in [Step 2](#retrieve-{{ integration.name }}-form-ids). For example:
         - **Single form**: `FrZ6iD`
         - **Multiple forms**: `FrZ6iD,f8nzFM`
  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Authorize Stitch"
    anchor: "authorize-stitch"
    content: |
      1. Next, you’ll be prompted to log into your {{ integration.display_name }} account and approve Stitch’s access to your data. **Note that we will only ever read your data.**
      2. Click **Authorize**.
      3. Sign in with your {{ integration.display_name }} account.
      4. Click **Accept**.

  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %}

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/typeform
---
{% assign integration = page %}
{% include misc/data-files.html %}