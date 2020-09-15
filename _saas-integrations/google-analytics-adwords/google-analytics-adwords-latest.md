---
title: Google Analytics (AdWords)
permalink: /integrations/saas/google-analytics-adwords
tags: [saas_integrations]
keywords: google adwords, integration, schema, etl google adwords, google adwords etl, google adwords schema
summary: "Connection instructions, replication info, and schema details for Stitch's Google Analytics (AdWords) integration."
layout: singer

key: "google-analytics-adwords-setup"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "google-analytics-adwords"
display_name: "Google Analytics (AdWords)"
setup-name: "Google Analytics"

this-version: "05-12-2017"

api: |
  [Google Analytics Reporting API v4](https://developers.google.com/analytics/devguides/reporting/core/v4/){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

historical: "30 days"
frequency: "6 hours"
tier: "Standard"

table-selection: false
column-selection: false

anchor-scheduling: false
cron-scheduling: false

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

## AdWords's default attribution window. Stitch queries for
## this number of days during each replication job to
## account for any updates to existing records made during 
## this time.

attribution-window: "15 days"

# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.

  **Note**: This guide describes how to replicate Google AdWords data using Stitch's Google Analytics integration. Additionally, this approach replaces the [deprecated 15-10-2015 version of Stitch's {{ integration.display_name }} integration]({{ site.baseurl }}/integrations/saas/{{ integration.name }}-v15-10-2015).

  As this approach uses the Analytics API, there may be some differences in the data when compared between AdWords and Analytics. You can find out more about these differences in [Google's documentation](https://support.google.com/analytics/answer/1034383?hl=en).

  If you want to use the AdWords API, use Stitch's [Google AdWords integration]({{ site.baseurl }}/integrations/saas/google-adwords).


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
  - title: "Authorize Stitch and select a {{ integration.display_name }} profile"
    anchor: "auth-select-ga-profiles"
    content: |
      1. Next, you’ll be prompted to log into your Google account and to approve Stitch’s access to your Google AdWords data.
      2. Click **Allow** to continue.
      3. After your credentials are validated, you’ll be prompted to select the Google Analytics profile you want to connect to Stitch:

         ![Selecting a Google Analytics profile.]({{site.baseurl}}/images/integrations/ga-select-profiles.png)

         **Remember**: Profiles need to have Read & Analyze permissions to be detected by Stitch. If you don’t see the profile you want in this list, double-check the permission settings of the profile.
      4. When finished, click **Continue** to save the integration.
  - title: "Select Metrics and Dimensions"
    anchor: "select-metrics-and-dimensions"
    content: |
      After you grant Stitch access to your Google Analytics profile, you can select {{ integration.display_name }} Metrics and Dimensions you want to replicate to your destination.

      Before you make your selections, note that:

      - **The following instructions use the Metrics and Dimensions that a deprecated version of Stitch's Google AdWords integration replicated**. You can select other Metrics or Dimensions, but we're listing them here for those who may want to mimic the old integration.

      - **Metric/Dimension combinations must comply with Google's compatibility rules before the integration can be saved**. Stitch will check the validity of your selections as you go and notify you if something isn't allowed. [Google's Dimensions & Metrics Explorer](https://developers.google.com/analytics/devguides/reporting/core/dimsmets#cats=adwords) can be used to validate different combinations before you enter them in Stitch.

      - **Google limits the number of Metrics and Dimensions you can select.** You can select up to 10 Metrics and seven Dimensions per integration. Refer to [Google's documentation](https://developers.google.com/analytics/devguides/reporting/core/v3/reference#metrics) for more info on these limits.

      - **Metric/Dimension combinations can't be changed after the integration is saved**. The Primary Key Stitch will create is a composite key composed of the Dimensions selected during this step.

      Refer to [Google's documentation](https://developers.google.com/analytics/devguides/reporting/core/dimsmets#view=detail&group=adwords) for more info about Google AdWords Metrics and Dimensions.

      #### Choose your data

      To complete the setup, you'll select the Metrics and Dimensions you want to replicate.

      1. In the **Choose Metrics** field, select up to 10 Metrics to replicate.

         If you want to replicate the same Metrics as [Stitch's old Google AdWords integration]({{ site.baseurl }}/integrations/saas/{{ integration.name }}//v15-10-2015), select the following:

         - `ga:adClicks`
         - `ga:adCost`
         - `ga:impressions`

      2. In the **Choose Dimensions** field, select up to seven Dimensions to replicate.

         If you want to replicate the same Dimensions as [Stitch's old Google AdWords integration]({{ site.baseurl }}/integrations/saas/{{ integration.name }}//v15-10-2015), select the following:

         - `ga:adContent`
         - `ga:adGroup`
         - `ga:adDestinationUrl`
         - `ga:adwordsCampaignID`
         - `ga:campaign`
         - `ga:date`
         - `ga:keyword`

      3. As you add Metrics and Dimensions, Stitch will check them for recent data and compatibility according to [Google's compatibility rules](https://developers.google.com/analytics/devguides/reporting/core/dimsmets#cats=adwords). To be considered recent, data must be from the past 30 days.
      4. Review your selections. **Remember**: Metrics/Dimensions cannot be added or removed after the integration is saved.
      5. When finished, click {{ app.buttons.save-int-settings }}.


# -------------------------- #
#      Replication Info      #
# -------------------------- #

replication-sections:
  - title: "attribution window"


# -------------------------- #
#        Table Schemas       #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/google-adwords/ga

---
{% assign integration = page %}
{% include misc/data-files.html %}


{% include integrations/saas/ga-not-set.html %}