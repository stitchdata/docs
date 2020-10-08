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
tap-name: "Darksky"
repo-url: https://github.com/singer-io/tap-darksky

this-version: "1"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false

historical: "1 year"
frequency: "1 hour"
tier: "Standard"
status-url: https://status.darksky.net/

api-type: "platform.darksky"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: false
column-selection: false
select-all: false
select-all-reason: |
  As this integration doesn't support table or column selection, all available tables and columns are automatically replicated.

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-info: |
  To find the list of available languages and units, please visit the [{{ integration.display_name }} Forecast Request docs](https://darksky.net/dev/docs#forecast-request){:target="new"}.

setup-steps:
  - title: "Retrieve your {{ integration.display_name }} secret key"
    anchor: "secret-key"
    content: |
      1. Log into your {{ integration.display_name }} API account [here](https://darksky.net/dev/){:target="new"}.
      2. On your account home page, your Secret Key is available at the top of the page. You will use this Secret Key to add your integration.

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **Language** field, enter the language code. Ex: 'en' for English, 'es' for Spanish, and 'fr' for French. For a full list of available language codes, check the `Request Parameters` section of the [{{ integration.display_name }} API documentation](https://darksky.net/dev/docs#forecast-request).
      5. In the **Location List** field, enter the latitude and longitude of the the locations to be returned for weather forecast information. The locations must be semi-colon deliniated. Ex: `<latitude>,<longitude>` is an accepted value for a single location, and `<latitude>,<longitude>;<latitude>,<longitude>; ... etc` is accepted for multiple locations.
      6. In the **Secret Key** field, paste your {{ integration.display_name }} secret key that you retrieved in [Step 1](#secret-key). 
      7. In the **Units** field, enter the measurement system to be returned for weather forecast information. Ex: 'us' for Imperial Units, and 'si' for International System of Units. For a full list of available measurement systems, check the `Request Parameters` section of the [Dark Sky API documentation](https://darksky.net/dev/docs#forecast-request)
  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}


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