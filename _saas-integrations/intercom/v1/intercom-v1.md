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

title: Intercom
permalink: /integrations/saas/intercom
keywords: intercom, integration, schema, etl intercom, intercom etl, intercom schema
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "intercom"
display_name: "Intercom"

singer: true 
tap-name: "intercom"
repo-url: https://github.com/singer-io/tap-intercom

api: |
  [{{ integration.display_name }} API (V2.0)](https://developers.intercom.com/intercom-api-reference/v2.0/reference){:target="new"}

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true 

historical: "1 year"
frequency: "30 minutes"
tier: "Standard"
status-url: "https://status.intercom.io/"

anchor-scheduling: true
cron-scheduling: false

extraction-logs: true
loading-reports: true

table-selection: false
column-selection: false

## Row usage details

row-usage-hog: true
row-usage-hog-reasons:
  data-structure: true
  data-volume: true
  lots-of-full-table: false

# -------------------------- #
#      Querying Details      #
# -------------------------- #

## Intercom's default attribution window. Stitch queries for
## this number of days during each replication job to
## account for any updates to existing records made during 
## this time.

replication-notes: true
attribution-window: "30 days"
# attribution-is-configurable: 

# setup-name: ""

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

requirements-list:
  - item: "**Your {{ integration.display_name }} App ID.** You can find your {{ integration.display_name }} App ID by following [these instructions](https://docs.intercom.com/faqs-and-troubleshooting/getting-set-up/where-can-i-find-my-app-id)."

setup-steps:
  - title: "add integration"
    content: |
      4. In the **{{ integration.display_name }} App ID** field, enter your [{{ integration.display_name }} App ID](https://docs.intercom.com/faqs-and-troubleshooting/getting-set-up/where-can-i-find-my-app-id).
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"
  - title: "Authorize Stitch to Access {{ integration.display_name }}"
    anchor: "authorize-stitch"
    content: |
      Lastly, you'll be directed to Intercom's website to complete the setup.

      {% include layout/inline_image.html type="right" file="integrations/intercom-access-request.png" alt="List of permissions requested by Stitch to access Intercom" max-width="400px" %}1. If you aren't already logged into Intercom, you'll be prompted to do so.
      2. Next, a screen requesting access to Intercom will display. **Note**: Stitch will only ever read your data.
      3. Click **Connect.**
      4. After the authorization process successfully completes, you'll be redirected back to Stitch.
      5. Click {{ app.buttons.finish-int-setup }}.

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/saas-integration

---
{% assign integration = page %}
{% include misc/data-files.html %}