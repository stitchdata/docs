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

title: Microsoft Teams (v1)
permalink: /integrations/saas/ms-teams ## Add if there are multiple versions: /vVERSION
keywords: ms-teams, integration, schema, etl ms-teams, ms-teams etl, ms-teams schema
layout: singer
# input: false

key: "ms-teams-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "ms-teams"
display_name: "Microsoft Teams"

singer: true
status-url: "https://status.office365.com/"

tap-name: "Microsoft Teams" ## Ex: Intercom, not intercom
repo-url: https://github.com/singer-io/tap-ms-teams

this-version: "1"

api: |
  [Microstoft Graph API](https://docs.microsoft.com/en-us/graph/){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

api-type: "platform.ms-teams"

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

requirements-list:
  - item: "**A Microsoft Azure account**."
  - item: |
      **A Microsoft Azure application**. Stitch's {{ integration.display_name }} integration uses OAuth to authenticate. For instructions on how to set up an Azure application, refer to the [**App and Authentication** section in Singer](https://github.com/singer-io/tap-ms-teams#app-and-authentication){:target="new"}.

setup-steps:
  - title: ""
    anchor: ""
    content: |
      [Add content]

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}

  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}

  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Authorize Stitch to access {{ integration.display_name }}"
    anchor: "grant-stitch-authorization"
    content: |
      1. Next, you'll be redirected to {{ integration.display_name }}.
      2. Log into your {{ integration.display_name }} account and complete the authorization process.  When finished, you'll be redirected back to Stitch.
      3. Click {{ app.buttons.finish-int-setup }}.


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/ms-teams


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}