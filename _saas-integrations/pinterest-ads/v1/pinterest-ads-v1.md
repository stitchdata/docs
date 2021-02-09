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

title: Pinterest Ads (v1)
permalink: /integrations/saas/pinterest-ads ## Add if there are multiple versions: /vVERSION
keywords: pinterest-ads, integration, schema, etl pinterest-ads, pinterest-ads etl, pinterest-ads schema
layout: singer
# input: false

key: "pinterest-ads-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "pinterest-ads"
display_name: "Pinterest Ads"

singer: true
status-url: ""

tap-name: "Pinterest Ads" ## Ex: Intercom, not intercom
repo-url: https://github.com/singer-io/tap-pinterest-ads

this-version: "1"

api: |
  [{{ integration.display_name }} Ads API V3](https://developers.pinterest.com/docs/redoc/adsreporting/){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Standard"

api-type: "platform.pinterest-ads"

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
      A {{ integration.display_name }} OAuth App. If you don't have one, refer to {{ integration.display_name }}'s [documentation](https://developers.pinterest.com/docs/redoc/adsreporting/#section/User-Authorization){:target="new"} for instructions on how to create one.

setup-steps:
  - title: "Identify your advertisers"
    anchor: "identify-advertisers"
    content: |
      1. Login to your {{ integration.display_name }} account.
      2. Navigate to the overhead menu bar and click **`Ads` > `Overview`**.
      3. In the column on the left-hand side of the page, navigate to the **Ad Status** section and click **All**.
      4. Your advertisers should display. Copy the names of the advertisers you'd like to replicate in Stitch and paste those values someplace safe to use for the next step.

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **Advertisers** field, paste the advertisers you copied in [step 1](#identify-advertisers), separated by commas.
      
         For example: `advertiser_1, advertiser_2`

  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}    

  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}
      
      When finished, click **Authorize**.

  - title: "Authorize Stitch to access {{ integration.display_name }}"
    anchor: "grant-stitch-authorization"
    content: |
      1. Next, you'll be redirected to {{ integration.display_name }}.
      2. Log into your {{ integration.display_name }} account and complete the authorization process.  When finished, you'll be redirected back to Stitch.
      3. Click {{ app.buttons.finish-int-setup }}.    

  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %} 


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/pinterest-ads


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}
