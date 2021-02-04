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

title: Pardot (v1)
permalink: /integrations/saas/pardot
keywords: pardot, integration, schema, etl pardot, pardot etl, pardot schema
layout: singer
# input: false

key: "pardot-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "pardot"
display_name: "Pardot"

singer: true
status-url: "https://trust.pardot.com/"

tap-name: "Pardot"
repo-url: https://github.com/singer-io/tap-pardot

this-version: "1"

api: |
  [{{ integration.display_name }} API](http://developer.pardot.com/#official-pardot-api-documentation){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

api-type: "platform.pardot"

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

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
  - item: |
      **A user with a preferred timezone of UTC.** This is required to ensure you don't encounter Extraction errors during Daylight Savings Time, as some Replication Key fields used by Stitch are reported in {{ integration.display_name }} using the user's preferred timezone. By using UTC, this ensures that time data is accurately reported during extraction. Otherwise, you might encounter [Extraction errors during Daylight Savings Time]({{ link.troubleshooting.pardot-extraction-errors | prepend: site.baseurl | append: "#out-of-order-data" }}).

setup-steps:
  - title: "Retrieve your {{ integration.display_name }} Business Unit ID"
    anchor: "retrieve-business-unit"
    content: |
      1. Sign into your Salesforce account.
      2. Navigate to the **Setup** page.
      3. Enter `{{ integration.display_name}} Account Setup` in the Quick Find.
      4. The {{ integration.display_name }} setup will appear. Copy your 18-charater {{ integration.display_name }} Business Unit and keep it readily available for the next step.

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **{{ integration.display_name }} Business Unit Id** field, paste your Business Unit ID that you copied in [step 1](#retrieve-business-unit).

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
      1. When finished in the **Integration Settings** page, click the **Authorize** button. You'll be prompted to sign into your {{ integration.display_name }} account.
      2. Sign into your {{ integration.display_name }} account.
      3. After the authorization process is successfully completed, you'll be directed back to Stitch.
      4. Click {{ app.buttons.finish-int-setup }}.    

  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %}


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/pardot


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}