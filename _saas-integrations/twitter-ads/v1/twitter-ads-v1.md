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

title: Twitter Ads
permalink: /integrations/saas/twitter-ads
keywords: twitter-ads, integration, schema, etl twitter-ads, twitter-ads etl, twitter-ads schema
layout: singer
# input: false

key: "twitter-ads-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "twitter-ads"
display_name: "Twitter Ads"

singer: true
status-url: ""

tap-name: "twitter-ads"
repo-url: https://github.com/singer-io/tap-twitter-ads

this-version: "1"

api: |
  [Twitter Ads API v.7](https://developer.twitter.com/en/docs/ads/general/overview){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

api-type: "platform.twitter-ads"

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

setup-steps:
  - title: "Retrieve account ID"
    anchor: "retrieve-account-id"
    content: |
      1. Login to your {{ integration.display_name }} account.
      2. Select the ads account that you'd like to use for this integration.
      3. Click on your account icon upper right corner of the screen.
      4. Click on **Settings** in the dropdown menu.
      5. Copy your account ID and keep it readily available for the next step.

      **Note**: if you would like to add multiple ads accounts for this integration, repeat the above steps for each account.

  - title: "add integration"
    content: |
      4. In the **Account IDs** field, paste the account ID you copied from [step 1](#retrieve-account-id). If you're adding multiple accounts IDs, paste them all in the same field, comma-delimited.
      5. The **Attribution Window** field is optional. If you would like to replicate data for only a certain amount of days at a time, add the number of days into the field. Whatever number you enter into the field is how many days worth of historical data that will be replicated.
      6. Check off the **with Deleted** box if you would like to include the records that were deleted due to falling outside of the attribution Window.
      7. In the **Country Codes** field, enter the comma-delimited list of ISO 2-letter country codes for targeting and segmenttation in your {{ integration.display_name }}.
      8. In the **Report Name** field, enter a name for the custom report you want to create.
      9. In the **Entity** dropdown menu, select which {{ integration.display_name }} object you want the integration to source data from for your custom report. Refer to the [{{ integration.display_name }} developer docs](https://developer.twitter.com/en/docs/tutorials/ads-api-hierarchy-terminology){:target="new"} for more information on entities.
      10. In the **Segment** dropdown menu, select the segment of data you want in your custom report.
      11. In the Granularity dropdown menu, select the level of detail you want in the report.
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data" ## remove this if the integration doesn't support at least table selection


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/twitter-ads


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}