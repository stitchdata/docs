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

title: Platform Purple
permalink: /integrations/saas/platformpurple
keywords: platformpurple, integration, schema, etl platformpurple, platformpurple etl, platformpurple schema
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "platformpurple"
display_name: "Platform Purple"

singer: true 
repo-url: https://github.com/singer-io/tap-platformpurple

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
icon: /images/integrations/icons/platformpurple.svg

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
      **The following credentials from {{ integration.display_name }}**:

      - **Your environment name**, and
      - **Your API key**

      Reach out to {{ integration.display_name }} to obtain this info. After you receive it from {{ integration.display_name }}, you can proceed with the setup of the integration in Stitch.

setup-steps:
  - title: "add integration"
    content: |
      4. In the **API Key** field, paste your {{ integration.display_nane }} API key.
      5. In the **Environment** field, paste the name of your {{ integration.display_name }} environment.
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/platformpurple

---
{% assign integration = page %}
{% include misc/data-files.html %}