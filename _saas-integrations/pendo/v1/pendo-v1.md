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

title: Pendo (v1)
permalink: /integrations/saas/pendo
keywords: pendo, integration, schema, etl pendo, pendo etl, pendo schema
layout: singer
# input: false

key: "pendo-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "pendo"
display_name: "Pendo"

singer: true
status-url: "https://status.pendo.io/"

tap-name: "Pendo"
repo-url: https://github.com/singer-io/tap-pendo

this-version: "1"

api: |
  [{{ integration.display_name }} v1 API](){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

api-type: "platform.pendo"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

attribution-window: "10 days"
attribution-is-configurable: true


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
  - item: ""
  - item: ""

requirements-info:

setup-steps:
  - title: ""
    anchor: ""
    content: |
      [Add content]
  - title: "add integration"
    content: |
      4. In the **Lookback Window** field,
      5. In the **Period** field,
      6. In the **X Pendo Integration Key** field, paste the integration key you [todo] in [Step 1]([TODO]).
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"


# -------------------------- #
#   Integration Replication  #
# -------------------------- #

replication-sections:
  - content: |
      {% for section in page.replication-sections %}
      {% if section.title %}
      - [{{ section.title | flatify }}](#{{ section.anchor }})
      {% endif %}
      {% endfor %}

  - title: "Event replication"
    anchor: "event-replication"
    content: |
      The **Lookback Window** and **Period** settings you define 

      **Note**: The **Lookback Window** you define determines the number of days' worth of data Stitch will replicate during every replication job. For example: If you entered `10`, Stitch would replicate the past 10 days' worth of event data for this table during every replication job.


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/pendo/v1
---
{% assign integration = page %}
{% include misc/data-files.html %}