---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: SendGrid Core (v1.0)
permalink: /integrations/saas/sendgrid-core
keywords: sendgrid, integration, schema, etl sendgrid, sendgrid etl, sendgrid schema
summary: "Connections instructions, replication info, and schema details for Stitch's SendGrid Core integration."
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "sendgrid-core"
display_name: "SendGrid Core"

singer: true 
repo-url: https://github.com/singer-io/tap-sendgrid

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: http://status.sendgrid.com/

table-selection: true
column-selection: true

anchor-scheduling: true
cron-scheduling: false

extraction-logs: true
loading-reports: true

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **Access to the objects you want to replicate from SendGrid.** This is required to grant the required permissions to the API key Stitch uses to connect to your SendGrid account.

      For example: If you want to replicate campaign data, you need to be able to access campaigns in your SendGrid account.

setup-steps:
  - title: "Create a SendGrid general API key for Stitch"
    anchor: "create-a-sendgrid-general-api-key"
    content: |
      {% include layout/inline_image.html type="right" file="integrations/sendgrid-core-api-key.png" alt="" max-width="300px" %}

      **Note:** You can't assign an API key greater permissions than you currently have in SendGrid.

      1. Sign into your SendGrid account.
      2. On the dashboard page, click **Settings > API Keys**.
      3. Click **Create API Key**.
      4. In the **API Key Name** field, enter a name for the key. For example: `Stitch API key`
      5. In the **API Key Permissions** section, select **Restricted Access**.
      6. In the **Access Details** section, enable the following:
         - **Email Activity** - Read Access
         - **Marketing Campaigns** - Full Access (**Note**: SendGrid doesn't currently provide a read-only level for this object.)
         - **Suppressions** - Read Access
         - **Template Engine** - Read Access
         - **Tracking** - Read Access
      7. Click **Create & View**.
      8. The API key will display. **Copy the key before closing the page**, as SendGrid won't display it again.

  - title: "add integration"
    content: |
      4. In the **SendGrid API Key** field, paste your SendGrid API key.
  - title: "historical sync"
  - title: "replication frequency"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/sendgrid
---
{% assign integration = page %}
{% include misc/data-files.html %}