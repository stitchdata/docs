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

title: Twilio (v1)
permalink: /integrations/saas/twilio ## Add if there are multiple versions: /vVERSION
keywords: twilio, integration, schema, etl twilio, twilio etl, twilio schema
layout: singer
# input: false

key: "twilio-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "twilio"
display_name: "Twilio"

singer: true
status-url: "https://status.twilio.com/"

tap-name: "Twilio" ## Ex: Intercom, not intercom
repo-url: https://github.com/singer-io/tap-twilio

this-version: "1"

api: |
  [{{ integration.display_name }} REST API ](https://www.twilio.com/docs/usage/api){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

api-type: "platform.twilio"

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

setup-steps:
  - title: "Retrieve Auth token and Account SID"
    anchor: "retrieve-auth-sid"
    content: |
      1. Log into your {{ integration.display_name }} account.
      2. Click on **Console**.
      3. Copy your **Account SID** and **Auth Token** and have it ready for the next step.

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **Account Sid** field, paste the Account SID you copied in [step 1](#retrieve-auth-sid).
      5. In the **Auth Token** field, paste the Auth Token you copied in [step 1](#retrieve-auth-sid).
      6. In the **Date Window Days** field, enter a value. This parameter should be set to an optimum value to improve historical sync performance. Setting this value too low will take longer to complete historical sync and setting it larger may result in request timeouts or memory overflow issues. The default value is `30`.
  
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
# Each table has a its own .md file in /_integration-schemas/twilio


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}