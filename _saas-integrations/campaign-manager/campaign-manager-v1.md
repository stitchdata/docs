---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Campaign Manager
permalink: /integrations/saas/campaign-manager
redirect_from: /integrations/saas/doubleclick-campaign-manager
keywords: doubleclick campaign manager, integration, schema, etl doubleclick campaign manager, doubleclick campaign manager etl, doubleclick campaign manager schema
summary: "Connection instructions, replication info, and schema details for Stitch's Campaign Manager integration."
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "campaign-manager"
display_name: "Campaign Manager"

singer: true 
tap-name: "DoubleClick Campaign Manager"
repo-url: https://github.com/singer-io/tap-doubleclick-campaign-manager

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: "https://ads.google.com/status#hl=en&v=status"

anchor-scheduling: true
extraction-logs: true
loading-reports: true

table-selection: true
column-selection: false

# https://support.google.com/dcm/partner/answer/6110224?hl=en&ref_topic=4388017
# Info about data freshness for metrics

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **A Campaign Manager account**. Refer to [Google's website](https://www.google.com/doubleclick/advertisers/){:target="new"} for signup information.
  - item: |
      **API access.** Most Campaign Manager accounts have this enabled by default. If you're not sure, contact your DoubleClick representative or the [Campaign Manager support team](mailto: dcm-support@google.com).
  - item: |
      **Access to the reports you want to replicate.** Stitch will only be able to replicate the reports that the user who authorizes the integration has access to.

setup-steps:
  - title: "Verify report access"
    anchor: "verify-report-access"
    content: |
      Before you connect {{ integration.display_name }} to Stitch, you should verify that you have access to the reports you want to replicate. Stitch will only be able to replicate data for the same reports that you have access to in {{ integration.display_name }}.

      1. [Sign into your {{ integration.display_name }} account and navigate to the **Report Builder** page](https://www.google.com/analytics/dfa/){:target="new"}.
      2. Under **Reports**, click **My Reports**.
      3. A list of all the reports you have access to will display:

         ![List of reports in {{ integration.display_name }}]({{ site.baseurl }}/images/integrations/doubleclick-campaign-manager-all-reports.png)
      4. Verify that the reports you want to replicate are listed on this page.

  - title: "Locate your {{ integration.display_name }} profile ID"
    anchor: "locate-your-profile-id"
    content: |
      {%- capture multiple-profiles -%}
      **Need to connect multiple profiles?** To connect more than one {{ integration.display_name }} profile, you'll need to create additional {{ integration.display_name }} integrations in your Stitch account.
      {%- endcapture -%}
      {% include note.html type="single-line" content=multiple-profiles %}

      {% include layout/inline_image.html type="right" file="integrations/doubleclick-campaign-manager-profile-id.png" max-width="250px" alt="" %}
      1. [Sign into your {{ integration.display_name }} account](https://www.google.com/dfa/trafficking){:target="new"}.
      2. Click the user menu (your icon) in the top right corner.
      3. In the dropdown beneath the **Sign out** button will be a list of the profiles you have access to.
      4. Locate the ID of the profile you want to connect. This will be a seven digit number next to the name of the profile. For example: `9999999`

         An example is highlighted in the image to the right.
      5. Copy the profile ID.

      Keep this handy - you'll need it in the next step.

  - title: "add integration"
    content: |
      4. In the **Profile ID** field, paste the ID of the {{ integration.display_name }} profile from [Step 2](#locate-your-profile-id). This value should be a seven digit number such as `9999999`.
  - title: "replication frequency"
  - title: "Authorize Stitch to access {{ integration.display_name }}"
    anchor: "grant-stitch-authorization"
    content: |
      1. If you aren't already signed into your Google account, you'll be prompted for your credentials.
      2. After you sign in, you'll see a list of the permissions requested by Stitch:
         - **View and manage DoubleClick for Advertisers reports** - This is required to allow Stitch to view and run reports. **Note**: Stitch will not alter report settings, and will only ever read data. Refer to the [Replication section](#replication) below for more info.
      3. To grant access, click the **Allow** button.
      4. After you've granted access, you'll be redirected back to Stitch to finish setting up the integration.
  - title: "track data"

# -------------------------- #
#      Replication Info      #
# -------------------------- #

replication-sections:
  - content: |
      When Stitch replicates data from {{ integration.display_name }}, the process will look like this:

      1. Stitch runs the selected report using the report's defined date range and included dimensions and metrics.
      2. {{ integration.display_name }} creates a CSV file of the report results.
      3. Stitch replicates the results from the CSV.

      Each run of a report will have its own CSV file in {{ integration.display_name }}, which you can access by [signing into your {{ integration.display_name }} account](https://www.google.com/dfa/trafficking){:target="new"}.
    subsections:
      - title: "Report date ranges"
        anchor: "report-date-ranges"
        content: |
          When Stitch replicates data for a given report, it will use the date range currently defined in {{ integration.display_name }} for that report.

          For example: The image below shows the configuration for a report named `ad_performance_report`, where the date range is set to the last 30 days. When Stitch replicates data for this report, it will run the report using these settings:

          ![Report date range field highlighted in {{ integration.display_name }}]({{ site.baseurl }}/images/integrations/doubleclick-campaign-manager-report-settings.png)

  - title: "Data loading and Append-Only Replication"
    anchor: "data-loading-append-only"
    content: |
      {% include integrations/saas/ads-append-only-replication.html type="data-loading" %}
    subsections:
      - title: "Query for the latest data"
        anchor: "query-for-the-latest-data"
        content: |
          {% include integrations/saas/ads-append-only-replication.html type="append-only-query" %}

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/doubleclick-campaign-manager

# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |

---
{% assign integration = page %}
{% include misc/data-files.html %}