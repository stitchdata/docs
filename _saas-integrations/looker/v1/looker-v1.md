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

title: Looker (v1)
permalink: /integrations/saas/looker ## Add if there are multiple versions: /vVERSION
keywords: looker, integration, schema, etl looker, looker etl, looker schema
layout: singer
# input: false

key: "looker-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "looker"
display_name: "Looker"

singer: true
status-url: ""

tap-name: "Looker" ## Ex: Intercom, not intercom
repo-url: https://github.com/singer-io/tap-looker

this-version: "1"

api: |
  [Looker v3.1 API](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

api-type: "platform.looker"

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

requirements-list:
  - item: "**{{ integration.display_name }} Admin Privileges.** You will need admin privileges to generate your API3 keys - **Client ID** and **Client Secret**."

setup-steps:
  - title: "Generate API3 keys."
    anchor: "api3-keys"
    content: |
      1. Login to your {{ integration.display_name }} account.
      2. Go to the **Edit Users** page.
      3. On that page, click the **Edit Keys** button. This will take you to the **Edit User API3 Keys** page.
      4. Click the **New API3 key** button to generate a new key.
      5. Copy your Client ID and Client Secret and have it readily available for the next steps.


  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **API Port** field, enter your API Port number. This value is usually `19999` unless you host {{ integration.display_name }} internally. If hosting internally, use your internal API Port value.
      5. In the **API Version** field, enter `3.1`.
      6. In the **Client ID** field, paste your Client ID that you copied in [step 1](#api3-keys).
      7. In the **Client Secret** field, paste your Client Secret that you copied in [step 1](#api3-keys).
      8. In the **Domain** field, enter your {{ integration.display_name }} account domain. It is typically `looker.com`, unless you use a white-labeled URL.
      9. In the **Subdomain** field, paste your {{ integration.display_name }} account subdomain. Your subdomain is the leading part of your {{ integration.display_name }} URL. For example: https://`stitch`.looker.com.

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
# Each table has a its own .md file in /_integration-schemas/looker


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}