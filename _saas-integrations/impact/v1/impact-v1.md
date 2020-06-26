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

title: Impact
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
  [Impact REST API](https://developer.impact.com/default){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

api-type: "platform.impact"

historical: "1 year"
frequency: "1 hour"
tier: "Free"

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

requirements-info: |
  There are no role types in {{ integration.display_name }}, but you do need to have API Access enabled on your account to access the API info. To do this, login to the {{ integration.display_name }} console. Locate the gear icon. Then, go to **Technical Settings > API Access**. There you can click **Enable API Access Now**.

setup-steps:
  - title: "Retrieve your Account SID and Auth Token"
    anchor: "retrieve-sid-auth"
    content: |
      1. Login to your {{ integration.display_name }} console.
      2. Click on the verticle ellipsis is the lower-left corner to open a pop-up up menu.
      3. Click **Settings**.
      4. On the settings page, locate the **Technical** section and click **API**.
      5. Copy the read-only versions of your **Account SID** and **Auth Token**, and save it in a safe place.
  - title: "add integration"
    content: |
      4. In the **Account SID** field, paste the read-only Account SID you copied from [step 1](#retrieve-sid-auth).
      5. In the **API Catalog** field, enter `Agencies`. This is the only API that Stitch's {{ integration.display_name }} supports for the time being.
      6. In the **Auth Token** field, paste the read-only Auth Token that you copied from [step 1](#retrieve-sid-auth).
      7. In the **Model ID** field, which is an optional field, enter your Model ID. It is an optional parameter for the `conversion_paths` endpoint, which shows conversions from clicks to conversion purchases. The only way to access this ID, you need to contact **Impact Radius Support** ([support@impactradius.com](support@impactradius.com)) or [open an {{ form-property.display-name }} help desk request](https://help.impactradius.com/hc/en-us/requests).
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data" ## remove this if the integration doesn't support at least table selection


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/impact


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}