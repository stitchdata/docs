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

title: Help Scout
permalink: /integrations/saas/helpscout
keywords: helpscout, integration, schema, etl helpscout, helpscout etl, helpscout schema
layout: singer
# input: false

key: "helpscout-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "helpscout"
display_name: "Help Scout"

singer: true 
tap-name: "Help Scout"
repo-url: https://github.com/singer-io/tap-helpscout

this-version: "1.0"

api: |
  [{{ integration.display_name }} Mailbox API 2.0](https://developer.helpscout.com/mailbox-api/){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false

historical: "1 year"
frequency: "60 minutes"
tier: "Free"
status-url: "https://status.helpscout.com/"

anchor-scheduling: true
cron-scheduling: false

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

# Row usage details

row-usage-hog: false
row-usage-hog-reasons:
  data-structure: false
  data-volume: false
  lots-of-full-table: false


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
      **An active, invited {{ integration.display_name }} user.** The {{ integration.display_name }} user setting up the integration in Stitch must be [active and invited in {{ integration.display_name }}](https://developer.helpscout.com/mailbox-api/overview/authentication/){:target="new"}.

      To verify a user's status, click **Manage > Users** in {{ integration.display_name }}.

setup-steps:
  - title: "add integration"
  - title: "historical sync"
  - title: "replication frequency"
    content: |
      When finished, click the **Authorize** button to continue.
  - title: "Authorize Stitch to access {{ integration.display_name }}"
    anchor: "grant-stitch-authorization"
    content: |
      {% include layout/inline_image.html file="integrations/helpscout-authorize-stitch.png" type="right" max-width="300px" %}
      1. After you click **Authorize** in Stitch, you'll be prompted to sign into your {{ integration.display_name }} account. Enter your {{ integration.display_name }} credentials and click **Log in**.
      3. On the next page, click the **Authorize** button to continue.
      4. After the authorization process is successfully completed, you'll be directed back to Stitch.
      5. Click {{ app.buttons.finish-int-setup }}.
  - title: "track data"


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/helpscout/v1
---
{% assign integration = page %}
{% include misc/data-files.html %}