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

title: Deputy
permalink: /integrations/saas/deputy
keywords: deputy, integration, schema, etl deputy, deputy etl, deputy schema
layout: singer
# input: false

key: "deputy-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "deputy"
display_name: "Deputy"

singer: true 
tap-name: "Deputy"
repo-url: https://github.com/singer-io/tap-deputy

this-version: "1"

api: |
  [{{ integration.display_name }} API](https://www.deputy.com/api-doc/API/Getting_Started){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false 

historical: "1 year"
frequency: "1 hour"
tier: "Free"
status-url: "https://status.deputy.com/"

api-type: "platform.deputy"

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
  - title: "Authorize Stitch to access {{ integration.display_name }}"
    anchor: "grant-stitch-authorization"
    content: |
      ![]({{ site.baseurl }}/images/integrations/deputy-organization-access.png){:align="right" style="margin-left: 15px; max-width: 300px;"}

      In this step, you'll grant Stitch access to the {{ integration.display_name }} organization you want to connect.

      1. When finished, click **Authorize**. You'll be prompted to sign into your {{ integration.display_name }} account if you aren't already.
      2. After you log into {{ integration.display_name }}, a screen with a list of your {{ integration.display_name }} organizations will display. Select the organization you want to connect to Stitch and click **Authorize**.
      3. After the authorization process is successfully completed, you'll be directed back to Stitch.
      4. Click {{ app.buttons.finish-int-setup }}.
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/deputy/v1
---
{% assign integration = page %}
{% include misc/data-files.html %}