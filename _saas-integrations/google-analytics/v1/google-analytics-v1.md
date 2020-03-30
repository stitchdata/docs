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

title: Google Analytics (v1)
permalink: /integrations/saas/google-analytics
keywords: google-analytics, integration, schema, etl google-analytics, google-analytics etl, google-analytics schema
layout: singer
input: true

key: "google-analytics-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "google-analytics"
display_name: "Google Analytics"

singer: true
status-url: "https://www.google.com/appsstatus#hl=en&v=status"

tap-name: "Google Analytics"
repo-url: https://github.com/singer-io/tap-google-analytics

this-version: "1"

api: |
  [](){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true 

historical: "1 year"
frequency: "1 hour"
tier: "Free"

api-type: "platform.google-analytics"

anchor-scheduling: true
cron-scheduling: true

table-selection: true
column-selection: true
table-level-reset: true

extraction-logs: true
loading-reports: true


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration allows you to create custom reports by selecting the metrics and dimension you want to replicate. You can create multiple reports and configure each of them individually. Refer to the [Schema](#schema) section for more info and an example table schema.

  This integration:

  - Supports creating multiple custom reports
  - Supports [custom metrics and dimensions](#custom-metrics-dimensions)
  - Supports Lifetime Values and Cohorts
  - Doesn't currently support Filters or Segments


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
  - title: "Configure your custom reports"
    anchor: "configure-reports"
    content: |
      Next, you'll configure the custom report(s) you want to replicate. The report(s) you enter on this page are used to create the tables in your destination.

      In the **Report Name** field, enter the name of report. This will be used to dynamically create the name of the report's corresponding table in the destination:

      ![Creating a custom Google Analytics report named Visitor Traffic]({{ site.baseurl }}/images/integrations/google-analytics-custom-report.png)

      To add another report, click **Configure another report** and enter a name for the report.

      {% include note.html type="single-line" content="**Renaming and deleting reports**: After the integration is created, renaming and deleting reports will have implications how data from this integration is loaded into your destination. Refer to the [Renamed](#renamed-reports) and [Deleted reports](#deleted-reports) sections for more info." %}

  - title: "historical sync"

  - title: "replication frequency"

  - title: "Authorize Stitch and select a Google Analytics profile"
    anchor: "auth-select-ga-profile"
    content: |
      {% include layout/image.html type="right" file="/integrations/ga-select-profiles.png" alt="Selecting a Google Analytics profile." max-width="400" %}
      1. Next, you’ll be prompted to log into your Google account and approve Stitch’s access to your {{ integration.display_name }} data. **Note that we will only ever read your data.**
      2. Click **Allow** to continue.
      3. After your credentials are validated, you’ll be prompted to select the {{ integration.display_name }} profile you want to connect to Stitch.

         **Remember:** Profiles need to have Read & Analyze permissions to be detected by Stitch. If you don’t see the profile you want in this list, we recommend that you double-check the permission settings.
      4. When finished, click **Continue.**

  - title: "Set metrics and dimensions to replicate"
    anchor: "track-data"
    content: |
      To complete the setup, you’ll need to select metrics and dimensions for each [report](#configure-reports) you want to replicate to your destination.

      1. In the list of reports that displays - or in the **Tables to Replicate** tab, if you skipped this step during setup - locate a report you want to replicate.
      2. To track a report, click the **checkbox** next to the report's name. You'll be redirected to a page with a list of metrics and dimensions available for replication.
      3. Select the metrics and dimensions you want to include in the report. When making your selections, keep the following in mind:

         - **You can select up to 10 metrics and 7 dimensions per report.** This limit is imposed by Google and can't be changed or worked around. When you reach this limit, you won't be able to make any other selections until you de-select a metric or dimension.
         - **Metric and dimension combinations are subject to Google's compatibility rules.** When you select a metric or dimension, all other metrics and dimensions incompatible with the selection will be greyed out. To test your combos before selecting them in Stitch, use [Google's Dimensions & Metrics Explorer](https://ga-dev-tools.appspot.com/dimensions-metrics-explorer/){:target="new"}.
         - **Custom metrics and dimensions** will display as either `ga:metricXX` or `ga:dimensionXX`, where `XX` is replaced with the specific number of the metric or dimension. Refer to the [Custom metrics and dimensions section](#custom-metrics-dimensions) for help identifying custom metrics and dimensions in your {{ integration.display_name }} account.

      4. Repeat this process for your remaining reports.
      5. When finished, click the **Finalize Your Selections** button at the bottom of the screen to save your selections.

      **Note:** If these settings are changed while a replication job is still in progress, they will not be used until the next job starts.


# -------------------------- #
#   Integration Replication  #
# -------------------------- #

replication-sections:
  - content: |
      {% for section in page.replication-sections %}
      {% if section.summary %}
      - [{{ section.summary }}](#{{ section.anchor }})
      {% endif %}
      {% endfor %}

  - title: "Custom report replication"
    anchor: "custom-report-replication"
    summary: "How Stitch replicates your custom reports"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Replication Method"
        anchor: "replication-method"
        content: |
          Custom reports in {{ integration.display_name }} are replicated using Key-based Incremental Replication with `start_date` as a Replication Key. A `start_date` value is a date in `YYYY-MM-DD` format.

          Google Analytics report data is aggregated per day, meaning that the day's data isn't complete until the next day begins. For this reason, data for the current day may be re-replicated until the day is 'complete'. **Note**: The [attribution modeling of your account](https://support.google.com/analytics/answer/1662518?hl=en){:target="new"} may also affect when data is considered complete.

          For example: Data for `2020-03-26` isn't considered complete by Google until `2020-03-27` begins. The integration may re-replicate data for `2020-03-26` until records for `2020-03-27` start to become available.

      - title: "Renamed reports"
        anchor: "renamed-reports"
        content: |
          {% include note.html type="single-line" content="**Note**: Stitch won't send a notification when a report is renamed. We recommend informing your colleagues when a report is renamed to ensure they're using the new, correct destination table." %}

          When you rename a report after the integration has been created, Stitch will:

          1. **Load data into a new table in your destination.** From the date the report is renamed, Stitch will load all data into a new table. The original table will remain in the destination unless you choose to drop it.

          2. **Continue replicating data from the Replication Key value saved for the table.** You'll need to reset the report to re-replicate all data [from the integration's **Start Date**](#define-historical-sync) and have it loaded into the new table.

             To reset a report, click into the report and then click **Report Settings** on the right side of the page. Click the **Reset Report** button.

          3. **Retain your metric and dimension selections for the report.** You won't need to re-select metrics and dimensions.

      - title: "Deleted reports"
        anchor: "deleted-reports"
        content: |
          To delete a report, open the integration's settings page, click **Configure another report**, and click **Remove this report**.

          This will permanently remove the report from the integration, including any selected metrics and dimensions.

          **Note**: Deleting a report in Stitch won't automatically remove the corresponding table in your destination.

  - title: "Metrics and dimensions"
    anchor: "metrics-and-dimensions"
    summary: "Selecting metrics and dimensions in your custom reports"
    content: |
      When selecting metrics and dimensions in Stitch, keep the following in mind:

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Maximum selection limits"
        anchor: "maximum-selection-limits"
        content: |
          For each report in a {{ integration.display_name }} integration, you can select up to [10 metrics](https://developers.google.com/analytics/devguides/reporting/core/v3/reference#metrics){:target="new"} and [7 dimensions](https://developers.google.com/analytics/devguides/reporting/core/v3/reference#dimensions){:target="new"}. 

          These limits are imposed by Google and can't be changed or worked around. When you reach these limits, you won't be able to make any other selections until you de-select a metric or dimension.

      - title: "Compatibility rules"
        anchor: "compatibility-rules"
        content: |
          The metrics and dimensions you select in custom reports are subject to [Google's compatibility rules](https://support.google.com/analytics/answer/1033861?hl=en#ValidDimensionMetricCombinations){:target="new"}. Refer to [Google's Dimensions and Metrics Explorer](https://developers.google.com/analytics/devguides/reporting/core/dimsmets){:target="new"} for a list of valid dimension and metric pairs.

      - title: "Custom metrics and dimensions"
        anchor: "custom-metrics-dimensions"
        content: |
          Custom metrics and dimensions will display as either `ga:metricXX` or `ga:dimensionXX`, where `XX` is replaced with the specific number of the metric or dimension.

          To identify a custom metric or dimension:

          1. Sign into your {{ integration.display_name }} Dashboard.
          2. Open the Custom Metrics or Dimensions page by navigating to **Admin > Property Column > Custom Definitions > Custom Metric/Dimension**.
          3. In the row for the metric or dimension, locate the **Index** column.
          4. Append the value in the **Index** column to either `ga:metric` or `ga:dimension`. For example: If the index for a custom dimension is `1`, the name that displays in Stitch would be `ga:dimension1`.


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/google-analytics/v1
---
{% assign integration = page %}
{% include misc/data-files.html %}