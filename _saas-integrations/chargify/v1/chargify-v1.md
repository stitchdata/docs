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

title: Chargify (v1)
permalink: /integrations/saas/chargify ## Add if there are multiple versions: /vVERSION
keywords: chargify, integration, schema, etl chargify, chargify etl, chargify schema
layout: singer
# input: false

key: "chargify-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "chargify"
display_name: "Chargify"

singer: true
status-url: "http://status.chargify.io/"

tap-name: "Chargify"
repo-url: https://github.com/singer-io/tap-chargify

this-version: "1"

api: |
  [{{ integration.display_name }} API](https://reference.chargify.com/v1/basics/introduction){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

api-type: "platform.chargify"

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
      **Owner or Admin access in {{ integration.display_name }}**. A user with either [level of access](https://help.chargify.com/my-account/users.html#access-levels){:target="new"} is required to create an API key for Stitch.

setup-steps:
  - title: "Create a {{ integration.display_name }} API key"
    anchor: "create-api-key"
    content: |
      {% include note.html type="single-line" content="**Note**: Completing this step requires Owner or Admin access in Chargify." %}

      1. Sign into your {{ integration.display_name }} account as a user with either Owner or Admin access.
      2. Navigate to **Config > Integrations**.
      3. Click **New API Key**.
      4. Copy your API key somewhere secure.

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **API Key** field, paste the API key you created in [Step 1](#create--key).
      5. In the **Subdomain** field, enter your {{ integration.display_name }} subdomain.

  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}

  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %} 


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/chargify
---
{% assign integration = page %}
{% include misc/data-files.html %}