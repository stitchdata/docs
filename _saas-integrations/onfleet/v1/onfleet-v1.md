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

title: Onfleet
permalink: /integrations/saas/onfleet
keywords: onfleet, integration, schema, etl onfleet, onfleet etl, onfleet schema
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "onfleet"
display_name: "Onfleet"

singer: true 
tap-name: "Onfleet"
repo-url: https://github.com/singer-io/tap-onfleet

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Open Beta"
certified: false 

historical: "1 year"
frequency: "1 hour"
tier: "Free"
status-url: "http://status.onfleet.com/"

anchor-scheduling: true
extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **An {{ integration.display_name }} Basic plan or above**. {{ integration.display_name }} limits API access to these plans, which is required to use Stitch's {{ integration.display_name }} integration. Refer to [{{ integration.display_name }}'s pricing page](https://onfleet.com/pricing){:target="new"} for more info.
  - item: |
      **Administrator privileges in {{ integration.display_name }}**. Only [administrators can create API keys](https://support.onfleet.com/hc/en-us/articles/203798149-API){:target="new"}, which is required to use Stitch's {{ integration.display_name }} integration.

setup-steps:
  - title: "Create an {{ integration.display_name }} API key"
    anchor: "create-onfleet-api-key"
    content: |
      {% capture administrator-note %}
      **Note**: This step requires [administrator privileges in {{ integration.display_name }}](https://support.onfleet.com/hc/en-us/articles/203798149-API){:target="new"}.
      {% endcapture %}

      {% include note.html type="single-line" content=administrator-note %}

      1. Sign into your [{{ integration.display_name }} account]().
      2. Navigate to the [**API & Webhooks** tab](https://support.onfleet.com/hc/en-us/articles/360013121812-API-webhooks-tab){:target="new"}.
      3. Click the **+** button in the bottom of the **API Keys** section to create a new API key.
      4. In the **Name** prompt that displays, enter a name for the API key. For example: `Stitch`
      5. Click **Create Key**.

      Keep the API key somewhere handy - you'll need it in the next step.
  - title: "add integration"
    content: |
      4. In the **API Key** field, paste the {{ integration.display_name }} API key you created in [Step 1](#create-onfleet-api-key).
      5. In the **Quota Limit** field, 
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/onfleet
---
{% assign integration = page %}
{% include misc/data-files.html %}