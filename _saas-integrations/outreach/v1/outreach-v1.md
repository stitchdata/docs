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

title: Outreach
permalink: /integrations/saas/outreach
keywords: outreach, integration, schema, etl outreach, outreach etl, outreach schema
layout: singer
# input: false

key: "outreach-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "outreach"
display_name: "Outreach"

singer: true
status-url: "https://status.outreach.io/"

tap-name: "Outreach"
repo-url: https://github.com/singer-io/tap-outreach

this-version: "1"

api: |
  [{{ integration.display_name}} REST API](https://api.outreach.io/api/v2/docs){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false

api-type: "platform.outreach"

historical: "1 year"
frequency: "1 hour"
tier: "Free"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

# attribution-window: "# days"
# attribution-is-configurable: 

# setup-name: ""


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


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
  
setup-steps:
  - title: "add integration"
    anchor: "add-integration"
    content: |
      4. In the **Quota Limit** field, define the percentage of your standard {{ integration.display_name }} API quota Stitch is allowed to use. This is an optional field. Before you define the limit, refer to the [{{ integration.display_name }} API documentation](https://api.outreach.io/api/v2/docs#rate-limiting) to learn about your {{ integration.display_name }} rate limit.
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data" ## remove this if the integration doesn't support at least table selection


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/outreach


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}