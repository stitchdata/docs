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
      2. Select the ads account that you'd like to integrate.
      
  - title: "add integration"
    # content: |
      # starting with 4., add instructions for additional fields in UI. EX:
      # 4. In the [FIELD_NAME] field, [instructions]
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