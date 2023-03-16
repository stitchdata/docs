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

title: Zoom (v1)
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

this-version: "1"

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
      **A {{integration.display_name }} authentication app**. You'll need one of the following apps to connect your {{integration.display_name }} account to Stitch:
        - **An OAuth app**. [Click here](https://marketplace.zoom.us/docs/guides/build/oauth-app){:target="new"} for more information on OAuth apps. If using a {{ integration.display_name }} OAuth App to connect to Stitch, make sure that the following scopes are included in the app:
          - `account:read:admin`
          - `meeting:read:admin`
          - `report:read:admin`
          - `user:read:admin`
          - `webinar:read:admin`

        - **A JSON Web Tokens (JWT) app**. [Click here](https://marketplace.zoom.us/docs/guides/build/jwt-app){:target="new"} for more information on JWT apps. 
  
setup-steps:
  - title: "Obtain your {{ integration.display_name }} authentication app tokens"
    anchor: "obtain-tokens"
    content: |
      1. Login to your {{ integration.display_name }} account on the [{{ integration.display_name }} App Marketplace](https://marketplace.zoom.us/){:target="new"}.
      2. Click **Manage** in the upper right corner of the page.
      3. Click on the OAuth or JWT app you'd like to use to connect to Stitch.
      4. If using a JWT app, copy the **JWT**. If using an OAuth app, copy the **Client ID**, **Client Secret**, and **Refresh Token**.
      5. Keep your token(s) readily available for the next step.
      
  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. If connecting to Stitch with a {{ integration.display_name }} OAuth app, paste the **Client ID**, **Client Secret**, and **Refresh Token** you obtained in [Step 1](#obtain-tokens) into their respective fields.
      5. If connecting to Stitch with a {{ integration.display_name }} JWT app, paste the **JWT** you obtained in [Step 1](#obtain-tokens) into the **JWT** field.
  
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
# Each table has a its own .md file in /_integration-schemas/zoom/v1
---
{% assign integration = page %}
{% include misc/data-files.html %}
