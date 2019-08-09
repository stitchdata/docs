---
title: Google Analytics (AdWords)
permalink: /integrations/saas/google-analytics-adwords/v15-10-2015
redirect_from: 
  - /integrations/saas/google-adwords-old
  - /integrations/saas/google-adwords-new
  - /integrations/saas/google-analytics-adwords-v15-10-2015
tags: [saas_integrations]
keywords: google adwords, integration, schema, etl google adwords, google adwords etl, google adwords schema
summary: |
  Connection instructions, replication info, and schema details for Stitch's Google AdWords (Analytics) integration.

  This integration has been deprecated.
layout: singer
input: false ## Removes integration from displaying on category pages

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "google-analytics-adwords"
display_name: "Google Analytics (AdWords)"
author: "Stitch"
author-url: https://www.stitchdata.com
status-url: "https://www.google.com/appsstatus#hl=en&v=status"

this-version: "15-10-2015"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Deprecated"
certified: true

historical: "15 days"
frequency: "30 minutes"
tier: "Free"
icon: /images/integrations/icons/google-adwords-old.svg

table-selection: false
column-selection: false

anchor-scheduling: false
cron-scheduling: false

extraction-logs: false
loading-reports: true

# -------------------------- #
#      Querying Details      #
# -------------------------- #

## AdWords's default attribution window. Stitch queries for
## this number of days during each replication job to
## account for any updates to existing records made during 
## this time.

replication-notes: true
attribution-window: "15 days"

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: "**At least Read & Analyze permissions in the account you want to connect to Stitch**. [See Google's documentation for more info](https://support.google.com/analytics/answer/2884495?hl=en)."
  - item: "**To have recent data in the account you want to connect to Stitch.** Verify that there is data from the past 30 days in the account before continuing."
  - item: "**To link your AdWords and Google Analytics profiles.** [See Google's documentation for instructions](https://support.google.com/analytics/answer/1033961?hl=en)."
  - item: "**To pause any ad-blocking software**. Ad blockers can interfere with pop-ups, which are used in Google authorization and may prevent authorization from successfully completing."


setup-steps:
  - title: "add integration"
  - title: "historical sync"
  - title: "replication frequency"
  - title: "Authorize Stitch & Select a {{ integration.display_name }} profile"
    anchor: "auth-select-ga-profiles"
    content: |
      1. Next, you’ll be prompted to log into your Google account and to approve Stitch’s access to your Google AdWords data. **Note that we will only ever read your data.**
      2. Click **Allow** to continue.
      3. After your credentials are validated, you’ll be prompted to select the Google Analytics profile you want to connect to Stitch:

         ![Selecting a Google Analytics profile.]({{site.baseurl}}/images/integrations/ga-select-profiles.png)

         **Remember: profiles need to have Read & Analyze permissions to be detected by Stitch.** If you don’t see the profile you want in this list, we recommend that you double-check the permission settings.
      4. When finished, click **Continue** to save the integration.

replication-sections:
  - title: "attribution window"


schema-sections:
  - title: 
    content: |
      After the first successful sync of your {{ integration.display_name }} data, you'll see two tables in your destination. These tables follow this naming convention:

      `adwords[GA profile id]_integration version`

      For example: `adwords123456789_v2`. In this case, the profile ID is `123456789` and the version of the AdWords integration is `2`.

      In the section below, you'll find a list of the attributes in these tables, a brief description, and links to Google's more in-depth documentation.

  - title: "Campaign Names and Primary Keys"
    anchor: "campaign-names-primary-keys"
    content: |
      Stitch's {{ integration.display_name }} integration uses the campaign name (`campaign`) as part of the Primary Key for both the `adwords` and `campaign` tables. Because of this, **changing campaign names may lead to data discrepancies**.

      To account for the name change and resolve any data discrepancies, take the following steps:

      1. **Delete the affected AdWords data from your destination**. Feel free to delete the data back to the date of the earliest campaign which was renamed.
      2. **Re-replicate your AdWords data by [following these instructions]({{ link.replication.saas-historical | prepend: site.baseurl | append: "#after-the-initial-setup" }})**, setting the start date back to the date of the earliest campaign which was renamed. This will reset the integration's Replication Keys and re-replicate all data back to the integration's defined Start Date.

# -------------------------- #
#        Table Schemas       #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/google-adwords

---
{% assign integration = page %}
{% include misc/data-files.html %}


{% include integrations/saas/ga-not-set.html %}