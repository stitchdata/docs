---
title: Google Analytics
permalink: /integrations/saas/google-analytics
tags: [saas_integrations]
keywords: google analytics, ga, ga schema, etl google analytics, google analytics etl, google analytics schema
summary: "Connection instructions, replication info, and schema details for Stitch's Google Analytics integration."
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
singer: false
author: "Stitch"
author-url: https://www.stitchdata.com
status-url: "https://www.google.com/appsstatus#hl=en&v=status"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "30 days"
frequency: "6 hours"
tier: "Free"
icon: /images/integrations/icons/google-analytics.svg

table-selection: false
column-selection: false

anchor-scheduling: false
extraction-logs: false
loading-reports: false

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
---
{% assign integration = page %}
{% include misc/data-files.html %}

{% contentfor setup %}
Connecting your Google Analytics data to Stitch is a five-step process:

1. [Add Google Analytics as a Stitch data source](#add-stitch-data-source)
2. [Define the Historical Sync](#define-historical-sync)
3. [Define the Replication Frequency](#define-rep-frequency)
4. [Authorize Stitch & select a Google Analytics profile to track](#auth-select-ga-profile)
5. [Select metrics and dimensions to sync](#syncing-data)

### Prerequisites
Before you get started, you should verify that:

1. **The user creating the integration has at least [Read & Analyze permissions](https://support.google.com/analytics/answer/2884495?hl=en) and that there's recent data in the account.** If the profile you use to connect doesn’t have these permissions (or there’s no data in the account), you’ll receive an error message like this:

   > “Something went wrong. None of the Google Analytics profiles associated with the credentials you’ve supplied contain data that Stitch can access. Please make sure that the credentials you’ve supplied have appropriate access.”

2. **All ad-blocking software you are currently using is paused**. Because Google authentication uses pop ups, you may encounter issues if ad blockers aren't disabled during the setup.

{% include integrations/shared-setup/connection-setup.html %}

{% include integrations/saas/setup/historical-sync.html %}

{% include integrations/shared-setup/replication-frequency.html %}

### Authorize Stitch & Select a Google Analytics Profile {#auth-select-ga-profile}

1. Next, you’ll be prompted to log into your Google account and to approve Stitch’s access to your Google Analytics data. **Note that we will only ever read your data.**
2. Click **Allow** to continue.
3. After your credentials are validated, you’ll be prompted to select the Google Analytics profile you want to connect to Stitch:

   ![Selecting a Google Analytics profile.]({{ site.baseurl }}/images/integrations/ga-select-profiles.png)

   **Remember: profiles need to have Read & Analyze permissions to be detected by Stitch.** If you don’t see the profile you want in this list, we recommend that you double-check the permission settings.
4. When finished, click **Continue.**

### Select Metrics & Dimensions to Sync {#syncing-data}

After you grant Stitch access to your Google Analytics profile, you can select the specific Metrics and Dimensions you want to replicate to your destination.

Before you get started, note the following:

1. **Metric/Dimension combos that adhere to Google's compatibility rules can be saved.** Stitch will display a notification if a conflict is found while adding Metrics and Dimensions. Integrations with incompatible Metric/Dimension combos can't be saved.

   We recommend creating additional Google Analytics integrations for different reports if you run into compatibility issues.

2. **Metric/Dimension combos can't be changed after the integration is saved.** The Primary Key Stitch creates for Google Analytics integration tables is a composite key composed of the Dimensions selected during setup. Adding or removing Dimensions will change the Primary Key, potentially leading to issues with identifying new data for replication or de-duping data.

3. **Google limits the number of Metrics and Dimensions you can select.** You can select up to 10 Metrics and seven Dimensions per integration. Refer to [Google's documentation](https://developers.google.com/analytics/devguides/reporting/core/v3/reference#metrics) for more info on these limits.

3. **Segments and Filters aren't currently supported.** If you're interested in us adding these features, please get in touch with us.

#### Select Metrics & Dimensions

{% include tip.html content="**Want to check a Metric/Dimension combo's compatibility?** Use [Google's Dimensions & Metrics Explorer](https://developers.google.com/analytics/devguides/reporting/core/dimsmets). If the combo is compatible there, it'll be compatible in Stitch." %}

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

{% include integrations/shared-setup/initial-syncs.html %}
{% endcontentfor %}



{% contentfor replication-notes %}
{% include integrations/saas/attribution-windows.html %}
{% endcontentfor %}



{% contentfor schema-notes %}
A single table - called `report` - will be created in your data warehouse **for each Google Analytics integration you create.**
  
The schema of this table will be composed of the Metrics and Dimensions you selected during the setup process and two other columns: `start_date` and `end_date`.

If, for example, you selected the following Metrics and Dimensions during setup:
  
- **Metrics**: `ga:sessions`, `ga:pageviews`
- **Dimensions**: `ga:referralPath`, `ga:country`

The table would look like the [`SAMPLE_TABLE`](#SAMPLE_TABLE) below.

### Primary Keys
The Primary Key for a Google Analytics table is a composite key made up of the **Dimension columns** and the `start_date` and `end_date` columns.

For example: the Primary Key for the [`SAMPLE_TABLE`](#SAMPLE_TABLE) would be: `referralpath:country:start_date:end_date`

### Table Rows & Data Pagination
Google Analytics data is paginated on a daily basis. This means that a single row in the `report` table pertains to a specific day. Use the `start_date` and `end_date` columns to identify what day the row is for.
{% endcontentfor %}



{% include integrations/saas/ga-not-set.html %}

---
