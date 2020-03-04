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

title: UJET
permalink: /integrations/saas/ujet
keywords: ujet, integration, schema, etl ujet, ujet etl, ujet schema
layout: singer
# input: false

key: "ujet-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "ujet"
display_name: "UJET"

singer: true
status-url: ""

tap-name: "UJET"
repo-url: https://github.com/singer-io/tap-ujet

this-version: "1"

api: |
  [{{ integration.display_name }} API](https://support.ujet.co/hc/en-us/articles/115006908127-UJET-Data-API#h_7d95eafc-6c02-446b-bcc6-b733f4e1143e){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false 

historical: "1 year"
frequency: "1 hour"
tier: "Free"

api-type: "platform.ujet"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: ""
  - item: ""

setup-steps:
  - title: ""
    anchor: ""
    content: |
      [Add content]
  - title: "add integration"
    # content: |
      # starting with 4., add instructions for additional fields in UI. EX:
      # 4. In the [FIELD_NAME] field, [instructions]
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data" ## remove this if the integration doesn't support at least table selection


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/ujet/v1
---
{% assign integration = page %}
{% include misc/data-files.html %}