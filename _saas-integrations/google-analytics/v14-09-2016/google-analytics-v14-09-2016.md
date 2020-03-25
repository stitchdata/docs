---
title: Google Analytics (v14-09-2016)
permalink: /integrations/saas/google-analytics/v14-09-2016
keywords: google analytics, ga, ga schema, etl google analytics, google analytics etl, google analytics schema
summary: "Connection instructions, replication info, and schema details for Stitch's Google Analytics integration."
layout: singer

key: "google-analytics-setup"

microsites:
  - title: "{{ page.display_name }} to BigQuery"
    url: "http://googleanalytics.tobigquery.com/"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "google-analytics"
display_name: "Google Analytics"

this-version: "14-09-2016"

singer: false
status-url: "https://www.google.com/appsstatus#hl=en&v=status"

api: |
  [{{ integration.display_name }} Reporting API v4](https://developers.google.com/analytics/devguides/reporting/core/v4/){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

historical: "30 days"
frequency: "6 hours"
tier: "Free"

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
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for details about the data Stitch will replicate.

  **Note**: A single {{ integration.display_name }} integration is limited to 10 Metrics and 7 Dimensions. This is due to limits enforced by Google. Refer to [Google's documentation](https://developers.google.com/analytics/devguides/reporting/core/v3/reference#metrics){:target="new"} for more info.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **At least Read & Analyze permissions in the account you want to connect to Stitch**. [See Google's documentation for more info](https://support.google.com/analytics/answer/2884495?hl=en){:target="new"}.

  - item: "**To have recent data in the account you want to connect to Stitch.** Verify that there is data from the past 30 days in the account before continuing."

  - item: "**To pause all ad-blocking software**. Because Google authentication uses pop ups, you may encounter issues if ad blockers aren't disabled during the setup."

setup-steps:
  - title: "add integration"
  - title: "historical sync"
  - title: "replication frequency"
  - title: "Authorize Stitch and select a Google Analytics profile"
    anchor: "auth-select-ga-profile"
    content: |
      1. Next, you’ll be prompted to log into your Google account and to approve Stitch’s access to your {{ integration.display_name }} data. **Note that we will only ever read your data.**
      2. Click **Allow** to continue.
      3. After your credentials are validated, you’ll be prompted to select the {{ integration.display_name }} profile you want to connect to Stitch:

         ![Selecting a Google Analytics profile.]({{ site.baseurl }}/images/integrations/ga-select-profiles.png)

         **Remember:** Profiles need to have Read & Analyze permissions to be detected by Stitch. If you don’t see the profile you want in this list, we recommend that you double-check the permission settings.
      4. When finished, click **Continue.**

  - title: "Select metrics and dimensions"
    anchor: "data-sync"
    content: |
      {% capture metrics-dims-considerations %}
      1. **Metric/Dimension combos that adhere to Google's compatibility rules can be saved.** Stitch will display a notification if a conflict is found while adding Metrics and Dimensions. Integrations with incompatible Metric/Dimension combos can't be saved.

         We recommend creating additional {{ integration.display_name }} integrations for different reports if you run into compatibility issues.

      2. **Metric/Dimension combos can't be changed after the integration is saved.** The Primary Key Stitch creates for {{ integration.display_name }} integration tables is a composite key composed of the Dimensions selected during setup. Adding or removing Dimensions will change the Primary Key, potentially leading to issues with identifying new data for replication or de-duping data.

      3. **Google limits the number of Metrics and Dimensions you can select.** You can select up to 10 Metrics and seven Dimensions per integration. Refer to [Google's documentation](https://developers.google.com/analytics/devguides/reporting/core/v3/reference#metrics){:target="new"} for more info on these limits.

      4. **Segments and Filters aren't currently supported.** If you're interested in us adding these features, please get in touch with us.

      5. **Lifetime value and cohort metrics aren't currently supported**. If you're interested in us adding these features, get in touch with us.

      After you grant Stitch access to your {{ integration.display_name }} profile, you can select the specific Metrics and Dimensions you want to replicate to your destination.
      {% endcapture %}

      {% include note.html first-line="Before you get started, note the following:" content=metrics-dims-considerations %}

      1. In the Metrics and Dimensions fields, you can search or use the drop-down to explore your options:

         ![Selecting Metrics & Dimensions.]({{site.baseurl}}/images/integrations/ga-add-metrics.gif)

      2. Click the Metric or Dimension in the menu to add it to the configuration.
      3. **To add a Custom Metric or Dimension,** type out the name exactly in its entirety. If you try to search for it and add a Metric/Dimension that looks like this - `ga:customMetricXX` - you’ll run into issues.

         For example: let’s say you want to add `custom metric 10` to the configuration. To add it, you would type `ga:metric10` in the Choose Metrics field like this:

         ![Adding a custom metric.]({{site.baseurl}}/images/integrations/ga-add-custom-metric.gif)

         {% include tip.html content="**Not sure what the name of a custom Metric or Dimension is**? Sign into your Google Analytics Dashboard and open the Custom Metrics or Dimensions page (**Admin > Property Column > Custom Definitions > Custom Metric/Dimension**). <br><br>
         In the row for the Metric or Dimension, take the number in the **Index** column and append it to either `ga:metric` or `ga:dimension`. For example: if the index for a custom Dimension is `1`, the name would be `ga:dimension1`" %}

         4. As you add Metrics and Dimensions, Stitch will check for compatibility. If there are any conflicts, you'll need to resolve them before you can save the integration. Use [Google's Dimensions & Metrics Explorer](https://developers.google.com/analytics/devguides/reporting/core/dimsmets) as a guide when selecting Metrics and Dimensions.

         5. **Review your selections**. Remember: once saved, Metrics and Dimensions can't be added or removed.

         6. When you're finished, click {{ app.buttons.save-int-settings }}.


# -------------------------- #
#     Replication Notes      #
# -------------------------- #

replication-sections:
  - content: |
      {% include integrations/saas/attribution-windows.html %}

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/google-analytics
---
{% assign integration = page %}
{% include misc/data-files.html %}