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

title: Revinate
permalink: /integrations/saas/revinate
tags: [saas_integrations]
keywords: revinate, integration, schema, etl revinate, revinate etl, revinate schema
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "revinate"
display_name: "Revinate"

singer: true 
tap-name: "Revinate"
repo-url: https://github.com/singer-io/tap-revinate

# this-version: ""

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false 

historical: "1 year"
frequency: "1 hour"
tier: "Free"
icon: /images/integrations/icons/revinate.svg

anchor-scheduling: true
extraction-logs: true
loading-reports: true

table-selection: true/false
column-selection: true/false 

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **A {{ integration.display_name }} account with API access.** Reach out to your {{ integration.display_name }} sales representative or account manager to obtain the correct permissions.
  - item: |
      **A {{ integration.display_name }} API token and secret**. To obtain these credentials, reach out to your {{ integration.display_name }} sales representative or account manager.

setup-steps:
  - title: "add integration"
    content: |
      4. In the **Username** field, enter your {{ integration.display_name }} username.
      5. In the **API Key** field, paste your {{ integration.display_name }} API key. Your {{ integration.display_name }} API token must be obtained through [your {{ integration.display_name }} sales representative or account manager](#setup-requirements).
      6. In the **API Secret** field, paste your {{ integration.display_name }} API secret. Your {{ integration.display_name }} API secret must be obtained through [your {{ integration.display_name }} sales representative or account manager](#setup-requirements).
  - title: "historical sync"
  - title: "replication frequency"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/revinate
---
{% assign integration = page %}
{% include misc/data-files.html %}