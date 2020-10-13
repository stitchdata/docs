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

title: Asana (v2)
permalink: /integrations/saas/asana
keywords: asana, integration, schema, etl asana, asana etl, asana schema
layout: singer
# input: false

key: "asana-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "asana"
display_name: "Asana"

singer: true 
tap-name: "Asana"
repo-url: https://github.com/singer-io/tap-asana

this-version: "2"

api: |
  [{{ integration.display_name }} API](https://asana.com/developers/documentation/examples-tutorials/overview){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false 

historical: "1 year"
frequency: "1 hour"
tier: "Standard"
status-url: "https://trust.asana.com/"

api-type: "platform.asana"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true


# -------------------------- #
#      Feature Summary.      #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.

 
# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **Access to all the data you want to replicate in {{ integration.display_name }}.** This includes projects, tasks, tags, users, and workspaces. If the user authorizing the integration in Stitch doesn't have access to something in {{ integration.display_name }}, Stitch will be unable to replicate it.

setup-steps:
  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Authorize Stitch to access {{ integration.display_name }}"
    anchor: "grant-stitch-authorization"
    content: |
      1. Next, you'll be prompted to sign into your {{ integration.display_name }} account.
      2. Enter your {{ integration.display_name }} credentials and sign into your account.
      3. After the authorization process is successfully completed, you'll be directed back to Stitch.
      4. Click {{ app.buttons.finish-int-setup }}.
  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %}

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/asana
---
{% assign integration = page %}
{% include misc/data-files.html %}