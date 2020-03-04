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

title: SaaSOptics
permalink: /integrations/saas/saasoptics
keywords: saasoptics, integration, schema, etl saasoptics, saasoptics etl, saasoptics schema
layout: singer
# input: false

key: "saasoptics-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "saasoptics"
display_name: "SaaSOptics"

singer: true

tap-name: "SaaSOptics"
repo-url: https://github.com/singer-io/tap-saasoptics

this-version: "1"

api: |
  [{{ integration.display_name }} REST API](){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false 

historical: "1 year"
frequency: "1 hour"
tier: "Free"

api-type: "platform.saasoptics"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true/false
column-selection: true/false

# attribution-window: "# days"
# attribution-is-configurable: 

# setup-name: ""


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

requirements-info:

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
# Each table has a its own .md file in /_integration-schemas/saasoptics
---
{% assign integration = page %}
{% include misc/data-files.html %}