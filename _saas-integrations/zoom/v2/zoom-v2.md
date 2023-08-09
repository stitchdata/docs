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

title: Zoom (v2)
permalink: /integrations/saas/zoom
keywords: zoom, integration, schema, etl zoom, zoom etl, zoom schema
layout: singer
# input: false

key: "zoom-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "zoom"
display_name: "Zoom"

singer: true
status-url: "https://status.zoom.us/"

tap-name: "Zoom"
repo-url: https://github.com/singer-io/tap-zoom

this-version: "2"

api: |
  [{{ integration.display_name }} REST API v2](https://marketplace.zoom.us/docs/api-reference/introduction){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false

api-type: "platform.zoom"

# historical: ""
frequency: "1 hour"
tier: "Standard"

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
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **Admin access in Zoom.** This is required to allow Stitch to replicate data.
  
setup-steps:      
  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Authorize Stitch to access {{ integration.display_name }}"
    anchor: "grant-stitch-authorization"
    content: |
      1. Click **Authorize** to sign into your {{ integration.display_name }} account. You’ll be taken through a series of steps to allow Stitch to access data from {{ integration.display_name }}.
      2. Click **Okay** for each step.
      3. Once you have authorized Stitch to access {{ integration.display_name }}, select the account you want to pull data from by selecting the check box in the **Connect** check box. 
      
          If you don't see the profiles you expect, make sure to check your {{ integration.display_name }} permissions. Reach out to support if you're still having issues.
      4. Click **Save Connections**. Once your credentials are validated, you will be redirected back to Stitch.
      5. Click {{ app.buttons.finish-int-setup }}.

  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %}


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/zoom/v1
---
{% assign integration = page %}
{% include misc/data-files.html %}
