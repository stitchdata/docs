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

title: Darksky
permalink: /integrations/saas/darksky
keywords: darksky, integration, schema, etl darksky, darksky etl, darksky schema
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "darksky"
display_name: "Darksky"

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
frequency: "1 hour"
tier: "Free"
status-url: https://status.darksky.net/

anchor-scheduling: true
cron-scheduling: true

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

requirements-info: |
  To find the list of available languages and units, please visit the [Dark Sky Forecast Request docs](https://darksky.net/dev/docs#forecast-request)

setup-steps:
  - title: "Retrieve Your {{ integration.display_name }} Secret Key"
    anchor: "secret-key"
    content: |
      1. Log into your {{ integration.display_name }} API account [here](https://darksky.net/dev/).
      2. On your account home page, your Secret Key is available at the top of the page. You will use this Secret Key to add your integration.
  - title: "add integration"
    content: |
      4. In the **Language** field, enter the language code. Ex: 'en' for English, 'es' for Spanish, and 'fr' for French. For a full list of available language codes, check the `Request Parameters` section of the [Dark Sky API documentation](https://darksky.net/dev/docs#forecast-request)
      5. In the **Location List** field, enter the latitude and longitude of the the locations to be returned for weather forecast information. The locations must be semi-colon deliniated. Ex: `<latitude>,<longitude>` is an accepted value for a single location, and `<latitude>,<longitude>;<latitude>,<longitude>; ... etc` is accepted for multiple locations.
      6. In the **Secret Key** field, paste your {{ integration.display_name }} secret key that you retrieved in [Step 1](#secret-key). 
      7. In the **Units** field, enter the measurement system to be returned for weather forecast information. Ex: 'us' for Imperial Units, and 'si' for International System of Units. For a full list of available measurement systems, check the `Request Parameters` section of the [Dark Sky API documentation](https://darksky.net/dev/docs#forecast-request)
  - title: "historical sync"
  - title: "replication frequency"

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