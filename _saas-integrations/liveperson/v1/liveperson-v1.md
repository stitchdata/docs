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

title: LivePerson (v1)
permalink: /integrations/saas/liveperson
keywords: liveperson, integration, schema, etl liveperson, liveperson etl, liveperson schema
layout: singer
# input: false

key: "liveperson-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "liveperson"
display_name: "LivePerson"

singer: true 
tap-name: "LivePerson"
repo-url: https://github.com/singer-io/tap-liveperson

this-version: "1"

api: |
  [{{ integration.display_name }} Data Access API](https://developers.liveperson.com/data-access-api-overview.html){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false

historical: "1 year"
frequency: "1 hour"
tier: "Standard"
status-url: "https://status.liveperson.com/"

api-type: "platform.liveperson"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

## Row usage details

row-usage-hog: true
row-usage-hog-reasons:
  data-structure: false
  data-volume: false
  lots-of-full-table: true


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **The API key administration privilege in {{ integration.display_name }}**. This is required to generate API credentials in {{ integration.display_name }}.

setup-steps:
  - title: "Generate {{ integration.display_name }} API credentials"
    anchor: "generate-api-credentials"
    content: |
      {% include note.html type="single-line" content="**Note**: This step requires the LivePerson API key administration privilege." %}

      {% include layout/inline_image.html type="right" file="integrations/liveperson-api-credentials.png" alt="" max-width="450px" %}

      1. Sign into your {{ integration.display_name }} account.
      2. Click the **Campaigns** tab at the top of the page.
      3. On the **Campaigns** page, locate and click on the **Data Sources** link.
      4. On the **Data Sources** page, click the **API** tab.
      5. Click **+ Add new**.
      6. In the **Application details** section, enter `Stitch` into the **Application name** and **Developer name** fields.
      7. In the **Select APIs** section:
         1. Click the **Show advanced options** option.
         2. Open the **Data** option.
         3. Click the **Data Access** option. This should also automatically check the **Data Access API** option.
         4. Click the **Engagement History / Messaging Interactions** option. This should also automatically check the **Interaction History** option.
      8. When finished, click the **Save** button in the lower right corner of the page.

      An **Authentication details** section will display. Leave this page open for now - you'll need it in the next step.

  - title: "add integration"
    content: |
      4. In the **{{ integration.display_name }} App Key** field, paste value from the **App key** field in {{ integration.display_name }}.
      5. In the **{{ integration.display_name }} App Secret** field, paste the value from the **Secret** field in {{ integration.display_name }}.
      6. In the **{{ integration.display_name }} Access Token** field, paste the value from the **Access token** field in {{ integration.display_name }}.
      7. In the **{{ integration.display_name }} Access Token Secret** field, paste the value from the **Access token secret** field in {{ integration.display_name }}.
      8. In the **{{ integration.display_name }} Account ID** field, enter your {{ integration.display_name }} account ID.
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/liveperson
---
{% assign integration = page %}
{% include misc/data-files.html %}