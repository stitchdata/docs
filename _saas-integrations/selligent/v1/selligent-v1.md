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

title: Selligent
permalink: /integrations/saas/selligent
keywords: selligent, integration, schema, etl selligent, selligent etl, selligent schema
layout: singer
# input: true

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "selligent"
display_name: "Selligent"

singer: true 
tap-name: "Selligent"
repo-url: https://github.com/singer-io/tap-selligent

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false 

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: ""

anchor-scheduling: true
cron-scheduling: false

extraction-logs: true
loading-reports: true

table-selection: false
column-selection: false

# attribution-window: "# days"
# attribution-is-configurable: 

# setup-name: ""

# -------------------------- #
#      Incompatibilities     #
# -------------------------- #

## uncomment section below if integration is compatible with any Stitch destinations
## if incompatible with multiple destinations, create a section for each destination

## incompatible:
  ## [redshift]: "always,sometimes,never"
  ## reason: "copy" 

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: "**Personal {{ integration.display_name }} API Key**. This is required to connect {{ integration.display_name }} to Stitch."

setup-steps:
  - title: "Obtain {{ integration.display_name }} API Key"
    anchor: "obtain-api-key"
    content: |
      Contact your {{ integration.display_name }} account manager to obtain the API key for your organization.
      
      After you receive your API key, you can proceed with the setup in Stitch.
  - title: "add integration"
    content: |
      4. In the **Base URL** field, enter the base URL for your {{ integration.display_name }} installation. It will be similar to `https://organization.some-host.com:443`
      5. In the **API Key** field, paste the API key you obtained in [Step 1](#obtain-api-key).

  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/selligent

---
{% assign integration = page %}
{% include misc/data-files.html %}
