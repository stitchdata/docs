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

title: Mixpanel
permalink: /integrations/saas/mixpanel
keywords: mixpanel, integration, schema, etl mixpanel, mixpanel etl, mixpanel schema
layout: singer
# input: false

key: "mixpanel-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "mixpanel"
display_name: "Mixpanel"

singer: true
status-url: ""

tap-name: "Mixpanel"
repo-url: https://github.com/singer-io/tap-mixpanel

this-version: "2"

api: |
  [Mixpanel Event Export API & Mixpanel Query API.](https://developer.mixpanel.com/docs/mixpanel-apis){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false

api-type: "platform.mixpanel"

historical: "1 year"
frequency: "1 hour"
tier: "Free"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

## Row usage details

row-usage-hog: true
row-usage-hog-reasons:
  data-structure: true
  data-volume: true
  lots-of-full-table: false


# setup-name: ""

# -------------------------- #
#      Querying Details      #
# -------------------------- #

## Pepperjam's attribution windows. Stitch queries for
## this number of days during each replication job to
## account for any updates to existing records made during
## this time.

attribution-window: "5 days"
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
  - item: |
      **Admin privileges**. Your role in your {{ integration.display_name }} must be admin in order to be able to retrieve your API secret.

setup-steps:
  - title: "Retrieve your Mixpanel project timezone and API secret"
    anchor: "retrieve-timezone-api-secret"
    content: |
      1. Login to your {{ integration.display_name }} account.
      2. In the dropdown menu in the upper left corner of the page, select the project you want to replicate data from.
      3. Hover over the **Settings** icon in the upper right corner. In the **PROJECT SETTINGS** portion of the dropdown menu, click on the link with the name of your project.
      4. Copy the **Project Timezone** and **API Secret**, and paste those values someplace safe to use for the next step.
  - title: "add integration"
    content: |
      4. In the **API Secret** field, paste the **API Secret** you retrieved from [step 1](#retrieve-timezone-api-secret).
      5. In the **Attribution Window** field, enter the number of days you want your tables' attribution window to be. For more information on attribution windows refer to the [replication section](#attribution-windows-extraction).
      6. In the **Date Window Size** field, enter the number of days you want for date window looping through transactional endpoints with `from_date` and `to_date`. The default `date_window_size` is 30 days.
      **Note**: You may want to decrease the number of days if your project has a large volume of events. 
      7. In the **Project Timezone** field, paste the **F
      8. In the **Select Properties By Default**
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data" ## remove this if the integration doesn't support at least table selection


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/mixpanel


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}