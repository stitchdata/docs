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

title: Sailthru (v1)
permalink: /integrations/saas/sailthru ## Add if there are multiple versions: /vVERSION
keywords: sailthru, integration, schema, etl sailthru, sailthru etl, sailthru schema
layout: singer
# input: false

key: "sailthru-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "sailthru"
display_name: "Sailthru"

singer: true
status-url: "https://status.sailthru.com/#!/"

tap-name: "Sailthru" ## Ex: Intercom, not intercom
repo-url: https://github.com/singer-io/tap-sailthru

this-version: "1"

api: |
  [{{ integration.display_name }} API](https://getstarted.sailthru.com/developers/api-basics/introduction/){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

api-type: "platform.sailthru"

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
  - title: "Retrieve your API key and secret"
    anchor: "retrieve-api-key-secret"
    content: |
      1. [Log into](https://my.sailthru.com/oauth/login/){:target="new"} your {{ integration.display_name }} account.
      2. Navigate to the **API & Postbacks** settings page in **My Sailthru**.
      3. Click the lock icon to display your API key and API secret.
      4. Copy these values and have them readily available for the next step.

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **API Key** field, paste the API key you copied from from [step 1](#retrieve-api-key-secret).
      5. In the **API Secret** field, paste the API secret you copied from [step 1](#retrieve-api-key-secret).

  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}

  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

## remove this if the integration doesn't support at least table selection
  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %} 


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/sailthru


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}