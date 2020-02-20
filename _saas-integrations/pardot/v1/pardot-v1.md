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

title: Pardot
permalink: /integrations/saas/pardot
keywords: pardot, integration, schema, etl pardot, pardot etl, pardot schema
layout: singer
# input: false

key: "pardot-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "pardot"
display_name: "Pardot"

singer: true
status-url: "https://trust.pardot.com/"

tap-name: "Pardot"
repo-url: https://github.com/singer-io/tap-pardot

this-version: "1"

api: |
  [{{ integration.display_name }} API](http://developer.pardot.com/#official-pardot-api-documentation){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

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

setup-steps:
  - title: "Retrieve your {{ integration.display_name }} user key."
    anchor: "retrieve-user-key"
    content: |
      1. Sign into your {{ integration.display_name }} account.
      2. In the upper right corner of the screen, hover over where your email address is displayed.
      3. From the dropdown menu, click **Settings**. Your user account information should be displayed.
      4. Your user key will be in the **API User Key** row. Keep your user key available to complete your setup in Stitch.

  - title: "add integration"
    content: |
      4. In the **Email** and **Password** fields, enter the email and password you use to access your {{ integration.display_name }} account.
      5. In the **User Key** field, enter the **API User Key** you retrieved in [step 1](#retrieve-user-key).
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data" ## remove this if the integration doesn't support at least table selection


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/pardot


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}