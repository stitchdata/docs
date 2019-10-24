---
title: Google Analytics
permalink: /integrations/saas/google-analytics
tags: [saas_integrations]
keywords: google analytics, ga, ga schema, etl google analytics, google analytics etl, google analytics schema
summary: "Connection instructions, replication info, and schema details for Stitch's Google Analytics integration."
layout: singer
format:
  schema-list: false
  table-desc: false
  list: expand

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

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.

  **Note**: A single {{ integration.display_name }} integration is limited to 10 Metrics and 7 Dimensions. This is due to limits enforced by Google. Refer to [Google's documentation](https://developers.google.com/analytics/devguides/reporting/core/v3/reference#metrics){:target="new"} for more info.


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
## Sample Table
  - name: "SAMPLE_TABLE"
    doc-link: 
    description: "<strong>This is a sample table.</strong> The section below contains the real info for the <code>report</code> table that will be created in your data warehouse."
    notes:
    replication-method: "Key-based Incremental"
    attribution-window: true
    primary-key: "referralpath:country:start_date:end_date"
    nested-structures: false
    attribute-notes: |
      If the `ga:sessions`, `ga:pageviews`, `ga:referralPath`, `ga:country` Metrics & Dimensions were selected during setup, the schema of the table would include these attributes:
    attributes:
      - name: sessions
      - name: pageviews
      - name: referralpath
      - name: country
      - name: start_date
      - name: end_date

## Report  
  - name: "report"
    doc-link: 
    description: "<strong>This is the table that will be created in your data warehouse.</strong> The columns in this table will be the Metrics and Dimensions you selected during setup."
    notes:
    replication-method: "Key-based Incremental"
    attribution-window: true
    primary-key: "dimension_columns:start_date:end_date"
    nested-structures: false
    attribute-notes: |
      For more info on the Metrics and Dimensions in Google Analytics, check out their [documentation](https://developers.google.com/analytics/devguides/reporting/core/dimsmets).
    attributes:
      - name: Metrics selected by you during setup
      - name: Dimensions selected by you during setup
      - name: start_date
      - name: end_date

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: "**An account with [Read & Analyze permissions](https://support.google.com/analytics/answer/2884495?hl=en) and recent data.** If the profile you use to connect doesn’t have these permissions (or there’s no data in the account), you’ll receive an error message like this:

   > “Something went wrong. None of the Google Analytics profiles associated with the credentials you’ve supplied contain data that Stitch can access. Please make sure that the credentials you’ve supplied have appropriate access.”
   "

  - item: "**All ad-blocking software you are currently using to be paused**. Because Google authentication uses pop ups, you may encounter issues if ad blockers aren't disabled during the setup."


setup-steps:
  - title: "add integration"
  - title: "historical sync"
  - title: "replication frequency"
  - title: "Authorize Stitch & Select a Google Analytics Profile"
    anchor: "auth-select-ga-profile"
    content: |
      1. Next, you’ll be prompted to log into your Google account and to approve Stitch’s access to your Google Analytics data. **Note that we will only ever read your data.**
      2. Click **Allow** to continue.
      3. After your credentials are validated, you’ll be prompted to select the Google Analytics profile you want to connect to Stitch:

         ![Selecting a Google Analytics profile.]({{ site.baseurl }}/images/integrations/ga-select-profiles.png)

         **Remember: profiles need to have Read & Analyze permissions to be detected by Stitch.** If you don’t see the profile you want in this list, we recommend that you double-check the permission settings.
      4. When finished, click **Continue.**
  - title: "Select Metrics & Dimensions to Sync"
    anchor: "data-sync"
    content: |
      After you grant Stitch access to your Google Analytics profile, you can select the specific Metrics and Dimensions you want to replicate to your destination.

      Before you get started, note the following:

      1. **Metric/Dimension combos that adhere to Google's compatibility rules can be saved.** Stitch will display a notification if a conflict is found while adding Metrics and Dimensions. Integrations with incompatible Metric/Dimension combos can't be saved.

         We recommend creating additional Google Analytics integrations for different reports if you run into compatibility issues.

      2. **Metric/Dimension combos can't be changed after the integration is saved.** The Primary Key Stitch creates for Google Analytics integration tables is a composite key composed of the Dimensions selected during setup. Adding or removing Dimensions will change the Primary Key, potentially leading to issues with identifying new data for replication or de-duping data.

      3. **Google limits the number of Metrics and Dimensions you can select.** You can select up to 10 Metrics and seven Dimensions per integration. Refer to [Google's documentation](https://developers.google.com/analytics/devguides/reporting/core/v3/reference#metrics) for more info on these limits.

      4. **Segments and Filters aren't currently supported.** If you're interested in us adding these features, please get in touch with us.
    substeps:
      - title: "Select Metrics & Dimensions"
        anchor: "select-metrics-dimensions"
        content: |
            
  - title: "track data"

# -------------------------- #
#        Schema Notes        #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/saas-integration


# Remove this if you don't need it:
# schema-sections:
  - title: "Schema Notes"
    anchor: "schema-notes"
    content: |
       A single table - called `report` - will be created in your data warehouse **for each Google Analytics integration you create.**
  
       The schema of this table will be composed of the Metrics and Dimensions you selected during the setup process and two other columns: `start_date` and `end_date`.

       If, for example, you selected the following Metrics and Dimensions during setup:
  
       - **Metrics**: `ga:sessions`, `ga:pageviews`
       - **Dimensions**: `ga:referralPath`, `ga:country`

       The table would look like the [`SAMPLE_TABLE`](#SAMPLE_TABLE) below.
    substeps:
      - title: "Primary Keys"
        anchor: "primary-keys"
        content: |
          The Primary Key for a Google Analytics table is a composite key made up of the **Dimension columns** and the `start_date` and `end_date` columns.

          For example: the Primary Key for the [`SAMPLE_TABLE`](#SAMPLE_TABLE) would be: `referralpath:country:start_date:end_date`   
      - title: "Table Rows & Data Pagination"
        anchor: "table-rows-data-pagination"
        content: |
          Google Analytics data is paginated on a daily basis. This means that a single row in the `report` table pertains to a specific day. Use the `start_date` and `end_date` columns to identify what day the row is for.
---
{% assign integration = page %}
{% include misc/data-files.html %}
