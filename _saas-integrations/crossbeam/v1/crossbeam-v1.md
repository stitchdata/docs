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

title: Crossbeam (v1)
permalink: /integrations/saas/crossbeam ## Add if there are multiple versions: /vVERSION
keywords: crossbeam, integration, schema, etl crossbeam, crossbeam etl, crossbeam schema
layout: singer
# input: false

key: "crossbeam-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "crossbeam"
display_name: "Crossbeam"

singer: true
status-url: ""

tap-name: "Crossbeam" ## Ex: Intercom, not intercom
repo-url: https://github.com/singer-io/tap-crossbeam

this-version: "1"

api: |
  [Crossbeam API](https://developers.crossbeam.com/){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false 

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

api-type: "platform.crossbeam"

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
  - item: |
      **A {{ integration.display_name }} application**. For information on how to create one, see {{ integration.display_name }}'s [Developer Docs](https://developers.crossbeam.com/#authentication){:target="new"}.

requirements-info:

setup-steps:
  - title: "Obtain your {{ integration.display_name }} Uuid"
    anchor: "obtain-uuid"
    content: |
      1. Login to your {{ integration.display_name }} account.
      2. In the upper right-hand corner of the home page, click on your organization's avatar.
      3. In the dropdown menu, click **Settings**.
      4. On the **Settings** page you'll see your ogranization's avatar and name. Underneath the name is the Uuid. Copy the Uuid and keep it readily available to continue with the integration.

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **Organization Uuid** field, paste the {{ integration.display_name }} Uuid that you obtained in [step 1](#obtain-uuid).

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
# Each table has a its own .md file in /_integration-schemas/crossbeam


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}