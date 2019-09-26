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

title: LinkedIn Ads (v1.0)
permalink: /integrations/saas/linkedin-ads/v1
tags: [saas_integrations]
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

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Open Beta"
certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Free"
status-url: ""

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true/false
column-selection: true

# attribution-window: "# days"
# attribution-is-configurable: 

# setup-name: ""


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: "**Access to a LinkedIn account**. This is necessary to login to the Campaign Manager account."
  - item: "**Access to a LinkedIn Campaign Manager account**. Make sure you have access to use the Ad accounts you want to replicate data from. This is necesary to set up a connection to Stitch for integration."

requirements-info:

setup-steps:
  - title: "Retreive your LinkedIn Ads Account IDs"
    anchor: "retrieve-account-ids"
    content: |
      1. Login to your LinkedIn account.
      2. Click the **Work** menu, then **Advertise**.
      3. Locate the account IDs of the campaign accounts you want to replicate data from:
         ![Image description here]({{ site.baseurl }}/images/integrations/linkedin-ads-work-dropdown.png)
      3. Retrieve account IDs for the accounts you wish to replicate data from.
         ![Image description here]({{ site.baseurl }}/images/integrations/linkedin-ads-account-ids.png)
      
  - title: "add integration"
    # content: |
      # starting with 4., add instructions for additional fields in UI
  - title: "historical sync"
  - title: "replication frequency"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/linkedin-ads


---
{% assign integration = page %}
{% include misc/data-files.html %}
