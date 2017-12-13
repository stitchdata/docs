---
title: Facebook Ads
permalink: /integrations/saas/facebook-ads
tags: [saas_integrations]
keywords: facebook ads, integration, schema, etl facebook ads, facebook ads etl
summary: "Connection instructions, replication info, and schema details for Stitch's Facebook Ads integration."
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "facebook-ads"
display_name: "Facebook Ads"
singer: true
author: "Stitch"
author-url: https://www.stitchdata.com
repo-url: 

# this-version: 1.0

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true # Stitch-supported integration

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
auth: "oauth"
status-url: "https://developers.facebook.com/status/"
icon: /images/integrations/icons/facebook-ads.svg
whitelist:
  tables: true
  columns: true

# -------------------------- #
#      Querying Details      #
# -------------------------- #

## FB's default attribution window. Stitch queries for
## this number of days during each replication job to
## account for any updates to existing records made during
## this time.

replication-notes: true
attribution-window: "28 days"

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **Verify your access in Facebook Ads.** If the user who creates the integration has restricted permissions - if the user doesn't have access to all campaigns or ads, for example - Stitch may encounter issues replicating data.

      Even if you only intend to sync certain pieces of data post-setup, the user completing the initial setup should still have full access.
  - item: |
      **Pause all ad-blocking software currently in use.** Because Facebook authentication uses pop ups, you may encounter issues if ad blockers aren't disabled during the setup.

setup-steps:
  - title: "add integration"
  - title: "historical sync"
  - title: "replication frequency"
  - title: "Authorize Stitch to Access Facebook Ads"
    anchor: "grant-stitch-authorization"
    content: |
      1. After clicking the **Authorize** button, a small pop-up window will display.

         You'll be taken through a series of steps to allow Stitch to access data from your Public Profile, Facebook Ads, and related stats. 
      2. Click **Okay** to advance through these steps.
      3. After you've finished authorizing Stitch, you'll be prompted to select the Facebook Ad Account you want to pull data from. Select the desired account by clicking the checkbox in the **Connect** column.

         If you don't see the profiles that you would expect to, verify your Facebook Ads permissions before reaching out to support.
      3. Click the **Save Connections** button.

      After your credentials are validated, you'll be directed back to Stitch (click the {{ app.buttons.finish-int-setup }} button to wrap things up) and the {{ app.page-names.int-details }} page will display.
  - title: "track data"

# -------------------------- #
#      Replication Info      #
# -------------------------- #

replication-sections:
  - title: "attribution window"

# -------------------------- #
#        Table Schemas       #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/facebook-ads

schema-sections:
  - content: |
      Facebook Ads' campaign structure contains three levels: **campaigns, ad sets, and ads**. There is also a fourth level for developers called **creatives**.

      To learn more about how Facebook Ads data is structured, we recommend checking out their [API guide](https://developers.facebook.com/docs/marketing-api/buying-api).

---
{% assign integration = page %}
{% include misc/data-files.html %}