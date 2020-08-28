---
title: Google ECommerce
permalink: /integrations/saas/google-ecommerce
keywords: google ecommerce, integration, schema, etl google ecommerce, google ecommerce etl, google ecommerce schema
summary: "Connection instructions, replication info, and schema details for Stitch's Google ECommerce integration."
layout: singer

key: "google-ecommerce-setup"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "google-ecommerce"
display_name: "Google ECommerce"
singer: false
status-url: "https://www.google.com/appsstatus#hl=en&v=status"

this-version: "15-10-2015"

api: |
  [Google Analytics Reporting API v4](https://developers.google.com/analytics/devguides/reporting/core/v4/){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

historical: "15 days"
frequency: "30 minutes"
tier: "Standard"

anchor-scheduling: true
cron-scheduling: false

table-selection: false
column-selection: false

extraction-logs: false
loading-reports: true

## Row usage details

row-usage-hog: true
row-usage-hog-reasons:
  data-structure: false
  data-volume: false
  lots-of-full-table: false


# -------------------------- #
#      Querying Details      #
# -------------------------- #

## GA's default attribution window. Stitch queries for
## this number of days during each replication job to
## account for any updates to existing records made during 
## this time.

replication-notes: true
attribution-window: "15 days"


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
      **At least Read & Analyze permissions in the account you want to connect to Stitch**. [See Google's documentation for more info](https://support.google.com/analytics/answer/2884495?hl=en){:target="new"}.

  - item: "**To have recent data in the account you want to connect to Stitch.** Verify that there is data from the past 30 days in the account before continuing."

  - item: "**To pause all ad-blocking software**. Because Google authentication uses pop ups, you may encounter issues if ad blockers aren't disabled during the setup."

  - item: |
      **To enable the [Enable ECommerce](https://support.google.com/analytics/answer/1009612?hl=en){:target="new"} setting in your Google Analytics account.** If you have ECommerce data in your account, this setting is already enabled and you can move on.


setup-steps:
  - title: "add integration"
  - title: "Authorize Stitch and select a Google Analytics profile"
    anchor: "auth-select-ga-profile"
    content: |
      1. Next, you’ll be prompted to log into your Google account and to approve Stitch’s access to your {{ integration.display_name }} data. **Note that we will only ever read your data.**
      2. Click **Allow** to continue.
      3. After your credentials are validated, you’ll be prompted to select the Google Analytics profile you want to connect to Stitch:

         ![Selecting a Google Analytics profile.]({{site.baseurl}}/images/integrations/ga-select-profiles.png)

         **Remember:** Profiles need to have Read & Analyze permissions to be detected by Stitch. If you don’t see the profile you want in this list, we recommend that you double-check the permission settings.
      4. When finished, click **Continue** to save the integration and complete the setup.
  - title: "replication frequency"


# -------------------------- #
#     Replication Notes      #
# -------------------------- #

replication-sections:
  - content: |
      {% include integrations/saas/attribution-windows.html %}

# -------------------------- #
#        Schema Notes        #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/google-ecommerce

schema-sections:
  - content: |
      After the first successful sync of your {{ integration.display_name }} data, you'll see a single table in your data warehouse. The table follows this naming convention:

      `ecommerce[GA profile id]_integration version`

      For example: `ecommerce123456789_v2`. In this case, the profile ID is `123456789` and the version of the ECommerce integration is `2`.
---
{% assign integration = page %}
{% include misc/data-files.html %}