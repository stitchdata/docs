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

title: LinkedIn Ads (v1)
permalink: /integrations/saas/linkedin-ads
keywords: linkedin ads, integration, schema, etl linkedin ads, linkedin ads etl, linkedin ads schema, linkedin, 
layout: singer
input: true

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "linkedin-ads"
display_name: "LinkedIn Ads"

singer: true 
tap-name: "LinkedIn Ads"
repo-url: https://github.com/singer-io/tap-linkedin-ads

# this-version: "1"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true
api-type: "platform.linkedin-ads"

historical: "1 year"
frequency: "1 hour"
tier: "Free"
status-url: ""

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: "**Access to a {{ integration.display_name }} account**. This is necessary to login to the Campaign Manager account."
  - item: "**Access to a {{ integration.display_name }} Campaign Manager account**. Verify that you have access to use the Ad accounts you want to replicate data from. This is necessary to connect to Stitch."

setup-steps:
  - title: "Retrieve your {{ integration.display_name }} account IDs"
    anchor: "retrieve-account-ids"
    content: |
      1. Login to your LinkedIn account.
      2. Click the **Work** menu, then **Advertise**:

         ![The LinkedIn Work and Advertise menus, highlighted]({{ site.baseurl }}/images/integrations/linkedin-ads-work-dropdown.png){:style="max-width: 400px"}

      3. In the Accounts table, locate the IDs for the accounts you want to replicate data from:

         ![LinkedIn Ads account IDs highlighted in the Accounts table of the Campaign Manager page.]({{ site.baseurl }}/images/integrations/linkedin-ads-account-ids.png){:style="max-width: 500px"}
      
  - title: "add integration"
    content: |
      4. In the **Accounts** field, enter a comma-separated list of the account IDs of the campaign accounts you want to replicate data from. These will be the account IDs you retrieved in [Step 1](#retrieve-account-ids). For example: `503123456,503234567`, etc.
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/linkedin-ads/v1
---
{% assign integration = page %}
{% include misc/data-files.html %}
