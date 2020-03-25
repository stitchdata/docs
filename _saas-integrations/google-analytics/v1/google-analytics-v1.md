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
input: false

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

extraction-logs: true
loading-reports: true


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration allows you to create custom reports by selecting the metrics and dimension you want to replicate. You can create multiple reports and configure each of them individually. Refer to the [Schema](#schema) section for more info and an example table schema.


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

      {% include note.html type="single-line" content="**Renaming reports**: You can rename reports after the integration has been created, but doing so will have implications on where Stitch loads the report's data in your destination. Refer to the [Custom report replication section](#custom-report-replication) for more info." %}

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
      4. Repeat this process for your remaining reports.
      5. When finished, click the **Finalize Your Selections** button at the bottom of the screen to save your selections.

      **Note:** If these settings are changed while a replication job is still in progress, they will not be used until the next job starts.


# -------------------------- #
#   Integration Replication  #
# -------------------------- #

replication-sections:
  - title: "Custom report replication"
    anchor: "custom-report-replication"
    content: |
      1. Metric and dimension selections will be retained.
      2. Load data into a new table in your destination.
      3. Will continue replicating data from the bookmark value saved for the table. A new table doesn't equal a full re-replication of that table's data.

  - title: "Metrics and dimensions"
    anchor: "metrics-and-dimensions"
    content: |
      TODO

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/google-analytics


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}