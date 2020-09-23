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

title: Eloqua
permalink: /integrations/saas/eloqua
keywords: eloqua, integration, schema, etl eloqua, eloqua etl, eloqua schema
layout: singer
# input: false

key: "eloqua-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "eloqua"
display_name: "Eloqua"

singer: true 
tap-name: "Eloqua"
repo-url: https://github.com/singer-io/tap-eloqua

this-version: "1"

api: |
  [Oracle {{ integration.display_name }} Marketing Cloud Service REST API](https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/index.html){:target="new"} and [{{ integration.display_name }} bulk export API](https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAB/Developers/BulkAPI/Tutorials/Export.htm){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false 

historical: "1 year"
frequency: "1 hour"
tier: "Standard"
status-url: "https://community.oracle.com/community/topliners/eloqua-system-status"

api-type: "platform.eloqua"

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
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Replication](#replication) section for a list of objects and the API Stitch uses to extract data from them.

  Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

setup-steps:
  - title: "add integration"
  - title: "historical sync"
  - title: "replication frequency"
  - title: "Authorize Stitch to access {{ integration.display_name }}"
    anchor: "grant-stitch-authorization"
    content: |
      1. Next, you'll be prompted to sign into your {{ integration.display_name }} account. Click **Sign In** to sign in.
      2. Enter your {{ integration.display_name }} credentials and click **Sign In** again.
      3. The next page will display the application (`Stitch`) requesting access to {{ integration.display_name }}. Click **Sign In** to continue.
      4. The next page will display the company and user you are currently logged into {{ integration.display_name }} as. Click **Accept**.
      5. After the authorization process is successfully completed, you'll be directed back to Stitch.
      6. Click {{ app.buttons.finish-int-setup }}.
  - title: "track data"


# -------------------------- #
#     Replication Details    #
# -------------------------- #

replication-sections:
  - content: |
      In this section:

      {% for section in integration.replication-sections %}
      - [{{ section.title | flatify }}](#{{ section.anchor }})
      {% endfor %}

  - title: "Tables using the {{ integration.display_name }} Bulk API"
    anchor: "tables-bulk-api"
    content: |
      Stitch uses the [{{ integration.display_name }} Bulk API](https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/Getting_Started_Bulk.html){:target="new"} to replicate data for the following tables:

      - [`accounts`](#accounts)
      - [`activity_bounceback`](#activity_bounceback)
      - [`activity_email_clickthrough`](#activity_email_clickthrough)
      - [`activity_email_open`](#activity_email_open)
      - [`activity_email_send`](#activity_email_send)
      - [`activity_form_submit`](#activity_form_submit)
      - [`activity_page_view`](#activity_page_view)
      - [`activity_subscribe`](#activity_subscribe)
      - [`activity_unsubscribe`](#activity_unsubscribe)
      - [`activity_web_visit`](#activity_web_visit)
      - [`contacts`](#contacts)
      - [Custom object tables](#custom-objects)

  - title: "Tables using the {{ integration.display_name }} REST API"
    anchor: "tables-rest-api"
    content: |
      Stitch uses the {{ integration.display_name }} Application REST API to replicate data for the following tables:

      - [`assets`](#assets)
      - [`campaigns`](#campaigns)
      - [`emails`](#emails)
      - [`forms`](#forms)
      - [`visitors`](#visitors)

  - title: "Custom objects and fields"
    anchor: "custom-objects-fields"
    content: |
      Stitch's {{ integration.display_name }} integration supports replicating custom fields and objects.

      For each custom object in your {{ integration.display_name }} account, Stitch will display a table as available for selection. The name of the table will be the normalized name of the object, using snake case (spaces replaced with underscores) and removing special characters. For example: If your account contains an `Enrichement Attributes` custom object, there will be a corresponding `enrichment_attributes` available for selection in Stitch.


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/eloqua
---
{% assign integration = page %}
{% include misc/data-files.html %}