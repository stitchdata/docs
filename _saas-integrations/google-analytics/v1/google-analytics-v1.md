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

title: Google Analytics
permalink: /integrations/saas/google-analytics
keywords: google-analytics, integration, schema, etl google-analytics, google-analytics etl, google-analytics schema
layout: singer
# input: false

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

anchor-scheduling: true
cron-scheduling: true

table-selection: true
column-selection: true

extraction-logs: true
loading-reports: true

# attribution-window: "# days"
# attribution-is-configurable: 

# setup-name: ""

## Row usage details todo: remove if no attribution window

row-usage-hog: true
row-usage-hog-reasons:
  data-structure: false
  data-volume: false
  lots-of-full-table: false


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.

  field metadata: https://www.googleapis.com/analytics/v3/metadata/{reportType}/columns


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
  - title: "Configure your reports"
    anchor: "configure-reports"
    content: |
      Next, you'll configure the report(s) you want to replicate. The report(s) you enter on this page are used to create the tables in your destination.

      In the **Report Name** field, enter the name of report. This will be used to dynamically create the name of the report's corresponding table in the destination. For example: A report named `Visitor Traffic` might create a table named `visitor_traffic` in your destinaiton.

      To add another report, click **Configure another report** and enter a name for the report.

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
  - title: "track data"

  - title: "Set metrics and dimensions to replicate"
    anchor: "track-data"
    content: |
      To complete the setup, you’ll need to select metrics and dimensions for each [report](#configure-reports) you want to replicate to your destination.

      1. In the list of reports that displays - or in the **Tables to Replicate** tab, if you skipped this step during setup - locate a report you want to replicate.
      2. To track a report, click the **checkbox** next to the report's name. You'll be redirected to a page with a list of metrics and dimensions available for replication.
      3. Select the metrics and dimensions you want to include in the report. When making your selections, keep the following in mind:

         - **TODO: Each report should have at least one metric and one dimension**
         - **Each report may have a total of 10 metrics and 7 dimensions.** This limit is imposed by Google and can't be changed. When you reach this limit, you won't be able to make any other selections until you de-select a metric or dimension.
         - **Metric and dimension combinations are subject to Google's compatibility rules.** When you select a metric or dimension, all other metrics and dimensions incompatible with the selection will be greyed out. To test your combos before selecting them in Stitch, use [Google's Dimensions & Metrics Explorer](https://ga-dev-tools.appspot.com/dimensions-metrics-explorer/){:target="new"}.
      4. Repeat this process for your remaining reports.
      5. When finished, click the **Finalize Your Selections** button at the bottom of the screen to save your selections.

      **TODO: determine if this should stay** Note: If you change these settings while a replication job is still in progress, they will not be used until the next job starts.

 


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