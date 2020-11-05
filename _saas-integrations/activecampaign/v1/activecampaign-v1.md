---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/activecampaign-templates/saas/
## FOR INSTRUCTIONS & REFERENCE INFO


# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: ActiveCampaign (v1)
permalink: /integrations/saas/activecampaign ## Add if there are multiple versions: /vVERSION
keywords: activecampaign, integration, schema, etl activecampaign, activecampaign etl, activecampaign schema
layout: singer
# input: false

key: "activecampaign-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "activecampaign"
display_name: "ActiveCampaign"

singer: true
status-url: "http://status.activecampaign.com/"

tap-name: "ActiveCampaign" ## Ex: Intercom, not intercom
repo-url: https://github.com/singer-io/tap-activecampaign

this-version: "1"

api: |
  [{{ integration.display_name }} v3 API](https://developers.activecampaign.com/reference#overview){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

api-type: "platform.activecampaign"

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

## uncomment section below if activecampaign is compatible with any Stitch destinations
## if incompatible with multiple destinations, create a section for each destination

## incompatible:
  ## [redshift]: "always,sometimes,never"
  ## reason: "copy" 

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

setup-steps:
  - title: "Retrieve your API URL and token"
    anchor: "retrieve-api"
    content: |
      1. Login to your {{ integration.display_name }} account.
      2. Go to the **My Settings** page.
      3. Click on the **Developer** tab.
      4. Copy your API URL and API token and keep it readily available for the next step.

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **API Token** field, paste the token you copied from [step 1](#retrieve-api).
      5. In the **API Url** field, paste the URL you copied from [step 1](#retrieve-api).

  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}

  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

## remove this if the activecampaign doesn't support at least table selection
  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %} 


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_activecampaign-schemas/activecampaign


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign activecampaign = page %}
{% include misc/data-files.html %}
