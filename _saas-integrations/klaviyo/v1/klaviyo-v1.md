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

title: Klaviyo
permalink: /integrations/saas/klaviyo
keywords: klaviyo, integration, schema, etl klaviyo, klaviyo etl, klaviyo schema
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "klaviyo"
display_name: "Klaviyo"

singer: true 
tap-name: "Klaviyo"
repo-url: https://github.com/singer-io/tap-klaviyo

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false 

historical: "1 year"
frequency: "30 minutes"
tier: "Free/Paid"
status-url: ""

anchor-scheduling: true
cron-scheduling: false

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: false

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

setup-steps:
  - title: "Create a {{ integration.display_name }} API key"
    anchor: "create-api-key"
    content: |
      1. Sign into your {{ integration.display_name }} account.
      2. Click the user menu (top right corner of the page), then click **Account**.
      3. On the **Account** page, click **Settings > API Keys**.
      4. On the **API Keys** page, click the **Create API Key** button to create an API key.
      5. In the **Label** column, click the pencil icon next to the API key you just created.
      6. Enter a label for the API key. For example: `Stitch integration`.
      7. Click **Save API Key**.

      ![Klaviyo API key]({{ site.baseurl }}/images/integrations/klaviyo-api-key.png)

      Keep this page open for now - you'll need it to complete the setup in Stitch.

  - title: "add integration"
    content: |
      4. In the **API Key** field, paste the {{ integration.display_name }} API key you created in [Step 1](#create-api-key).
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/klaviyo
---
{% assign integration = page %}
{% include misc/data-files.html %}