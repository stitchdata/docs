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

title: Zoom (v2) (Beta)
permalink: /integrations/saas/zoom/v2
keywords: zoom, integration, schema, etl zoom, zoom etl, zoom schema
layout: singer
input: false

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
      {% capture beta-note %}
      This feature is currently in beta and is not publicly available. Check the [{{ integration.display_name }} v1 setup documentation](https://www.stitchdata.com/docs/integrations/saas/zoom#setup) for the current version of the integration.
      {% endcapture %}

      {% include note.html type="single-line" content=beta-note %}

      1. Click **Authorize** to sign into your {{ integration.display_name }} account. You’ll be taken through a series of steps to allow Stitch to access data from {{ integration.display_name }}.
      2. Click **Okay** for each step.
      3. Once your credentials are validated, you will be redirected back to Stitch. Click **Check and Save** to save the connection.

  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %}

removal-info: |
  To completely disconnect Stitch from your {{ page.display_name }} account, you need to delete the integration from Stitch, and uninstall the Stitch app from {{ page.display_name }}.
  
  Disconnecting {{ page.display_name }} from Stitch will stop the replication of {{ page.display_name }} data to your Stitch destination. There will be no impact to the {{ page.display_name }} data, as Stitch is a read-only integration with {{ page.display_name }}. All data that has already replicated to your Stitch destination will be maintained and under your control.

removal-steps:
  - title: "Deleting your {{ page.display_name }} integration"
    anchor: "delete-integration"
    content: |
      To delete your {{ page.display_name }} integration from your Stitch account:
      1. Log in to your Stitch account and open the **Integrations** tab.
      2. Click your {{ page.display_name }} integration and click **Settings**.
      3. Scroll down to the bottom of the page and click **Delete**.
      4. Click **Delete** to confirm.

  - title: "Uninstalling Stitch in your {{ page.display_name }} account"
    anchor: "uninstall-stitch"
    content: |
      To uninstall Stitch in your {{ page.display_name }} account:
      1. Log in to your {{ page.display_name }} account go to the [**Added Apps**](https://marketplace.zoom.us/user/installed) page in the App Marketplace.
      2. Under **Apps in Production**, find the Stitch app and click **Remove**.
      3. In the dialog box that appears, click **Remove** to confirm.

      Once the Stitch app is removed from your {{ page.display_name }} App Marketplace, the access token credentials associated with your {{ page.display_name }} integration connection will no longer be authorized and will be deleted from the Stitch environment.

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/zoom/v1
---
{% assign integration = page %}
{% include misc/data-files.html %}