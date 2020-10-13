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

title: Impact (v1)
permalink: /integrations/saas/impact
keywords: impact, integration, schema, etl impact, impact etl, impact schema
layout: singer
# input: false

key: "impact-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "impact"
display_name: "Impact"

singer: true
status-url: ""

tap-name: "Impact"
repo-url: https://github.com/singer-io/tap-impact

this-version: "1"

api: |
  [{{ integration.display_name }} Radius API](https://developer.impact.com/default){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false

api-type: "platform.impact"

historical: "1 year"
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
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }} and the Advertisers API catalog.

  Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **To have API access enabled for your {{ integration.display_name }} account.** To do this, login to the {{ integration.display_name }} console. Locate the gear icon and then click **Technical Settings > API Access**. Click **Enable API Access Now**.

setup-steps:
  - title: "Retrieve your {{ integration.display_name }} account SID and auth token"
    anchor: "retrieve-sid-auth"
    content: |
      1. Login to your {{ integration.display_name }} console.
      2. Click on the verticle ellipsis in the lower-left corner.
      3. Click **Settings**.
      4. On the settings page, locate the **Technical** section and click **API**.
      5. Copy the read-only versions of your **Account SID** and **Auth Token**, and save it in a safe place.

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **Account SID** field, paste the read-only Account SID you retrieved in [Step 1](#retrieve-sid-auth).
      5. In the **API Catalog** field, select `Advertisers`.
      6. In the **Auth Token** field, paste the read-only Auth Token that you retrieved in [Step 1](#retrieve-sid-auth).
      7. **Optional**: In the **Model ID** field, enter your model ID. This is used in the `conversion_paths` table to extract data about conversions from clicks to conversion purchases.

         To access your model ID, contact [{{ integration.display_name }} Radius Support](mailto:support@impactradius.com) or [open an {{ form-property.display-name }} help desk request](https://help.impactradius.com/hc/en-us/requests){:target="new"} with {{ integration.display_name }}.
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
# Each table has a its own .md file in /_integration-schemas/impact/v1
---
{% assign integration = page %}
{% include misc/data-files.html %}