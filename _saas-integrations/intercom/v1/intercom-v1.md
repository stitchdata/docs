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

title: Intercom (v1)
permalink: /integrations/saas/intercom
keywords: intercom, integration, schema, etl intercom, intercom etl, intercom schema
layout: singer
# input: false

key: "intercom-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "intercom"
display_name: "Intercom"

singer: true 
tap-name: "Intercom"
repo-url: https://github.com/singer-io/tap-intercom

this-version: "1"

api: |
  [{{ integration.display_name }} API (V2.0)](https://developers.intercom.com/intercom-api-reference/v2.0/reference){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

historical: "1 year"
frequency: "30 minutes"
tier: "Standard"
status-url: "https://status.intercom.io/"

api-type: "platform.intercom"

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

setup-steps:
  - title: "add integration"
  - title: "historical sync"
  - title: "replication frequency"
  - title: "Authorize Stitch to access {{ integration.display_name }}"
    anchor: "authorize-stitch"
    content: |
      Lastly, you'll be directed to {{ integration.display_name }}'s website to complete the setup.

      {% include layout/inline_image.html type="right" file="integrations/intercom-access-request.png" alt="List of permissions requested by Stitch to access Intercom" max-width="400px" %}1. If you aren't already logged into {{ integration.display_name }}, you'll be prompted to do so.
      2. Next, a screen requesting access to {{ integration.display_name }} will display. **Note**: Stitch will only ever read your data.
      3. Click **Connect.**
      4. After the authorization process successfully completes, you'll be redirected back to Stitch.
      5. Click {{ app.buttons.finish-int-setup }}.

  - title: "track data"
  

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/saas-integration

---
{% assign integration = page %}
{% include misc/data-files.html %}