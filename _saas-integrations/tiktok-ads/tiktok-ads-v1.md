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

title: TikTok Ads (v1)
permalink: /integrations/saas/tiktok-ads ## Add if there are multiple versions: /vVERSION
keywords: tiktok ads, integration, schema, etl tiktok ads, tiktok ads etl, tiktok ads schema
layout: singer
# input: false

key: "tiktok-ads-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "tiktok-ads"
display_name: "TikTok Ads"

singer: true
status-url: ""

tap-name: "tiktok-ads"
repo-url: https://github.com/singer-io/tap-tiktok-ads

this-version: "1"

api: |
  [{{ integration.display_name }} API (v1.3)](https://ads.tiktok.com/marketing_api/docs){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

api-type: "platform.tiktok-ads"

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
  - item: "**Access to a {{ integration.display_name }} account.** This is necessary to login to the Ad Manager account."
  - item: "**Access to a {{ integration.display_name }} Ad Manager account.** Verify that you have access to use the Ad accounts you want to replicate data from. This is necessary to connect to Stitch."

# requirements-info:

setup-steps:
  # - title: ""
  #   anchor: ""
  #   content: |
  #     [Add content]

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. Check the **include_deleted** box to have Stitch replicate data from deleted campaigns, ads, and adgroups.

  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}

  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Authorize Stitch"
    anchor: "authorize-stitch"
    content: |
      1. Next, you’ll be prompted to log into your TikTok account and approve Stitch’s access to your {{ integration.display_name }} data. **Note that we will only ever read your data.**
      2. Click **Sign in with TikTok** to connect.
      3. Sign in with your TikTok account.
      4. After your credentials are validated, you’ll be directed back to Stitch and prompted to select the {{ integration.display_name }} accounts you want to for which you want to run extractions.
      4. When finished, click **Check and Save**, then click **All Done**.

## remove this if the integration doesn't support at least table selection
  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %} 


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/tiktok-ads


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}