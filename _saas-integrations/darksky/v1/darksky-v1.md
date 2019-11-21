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

title: Dark Sky
permalink: /integrations/saas/darksky
keywords: darksky, integration, schema, etl darksky, darksky etl, darksky schema
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "darksky"
display_name: "Dark Sky"

singer: true 
tap-name: "darksky"
repo-url: https://github.com/singer-io/tap-darksky

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Open Beta"
certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: "https://status.darksky.net/"

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
  - item: "**Language**. The language will be a two-letter value. Example: 'en' for English, 'es' for Spanish, and 'ar' for Arabic."
  - item: "**Location List**. The lattitude and longitude of the locations that weather data should be returned for."
  - item: "**Secret Key**. The secret key grants Stitch access to the API. The key can be created on your Dark Sky API account home page at: https://darksky.net/dev/account"
  - item: "**Units**. This is the measurement system that the weather data will be returned. Example: 'us' for Imperial Units, and 'si' for International System of Units."

requirements-info: "To find the list of available languages and units, visit the Dark Sky Forecast Request docs at https://darksky.net/dev/docs#forecast-request"

setup-steps:
  - title: "Get Secret Key"
    anchor: "secret-key"
    content: |
      1. Log into your Dark Sky API account.
      2. On your account home page, your Secret Key is available at the top of the page. You will use this Secret Key to add your integration.
  - title: "add integration"
    # content: |
      # starting with 4., add instructions for additional fields in UI
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/darksky


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}