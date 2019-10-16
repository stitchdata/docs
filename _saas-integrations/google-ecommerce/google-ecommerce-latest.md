---
title: Google ECommerce
permalink: /integrations/saas/google-ecommerce
keywords: google ecommerce, integration, schema, etl google ecommerce, google ecommerce etl, google ecommerce schema
summary: "Connection instructions, replication info, and schema details for Stitch's Google ECommerce integration."
format: ## controls formatting options in template
  schema-list: false
  table-desc: true
  list: expand

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
tier: "Free"

anchor-scheduling: false
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
#     Integration Tables     #
# -------------------------- #

tables:
## ECommerce Table
  - name: "ecommerce123456789_v2"
    doc-link: 
    description: "your Google ECommerce data."
    notes:
    replication-method: "Key-based Incremental"
    attribution-window: true
    primary-key: "id"
    nested-structures: false
    attribute-notes: This table will contain the following attributes. For more info, click the links to check out Google's documentation.
    attributes:
      - name: ID (<code>id</code>) - This column is a unique identifier generated during replication.
      - name: <strong>accountid</strong> - This column contains the account ID associated with your Google Analytics ECommerce account.
      - name: <strong><a href="https://developers.google.com/analytics/devguides/reporting/core/dimsmets#view=detail&group=traffic_sources&jump=ga_campaign" target="new">campaign</a></strong> - This column contains the campaign name (<a href="https://support.google.com/analytics/answer/1033867?hl=en">utm_campaign</a>)
      - name: <strong><a href="https://developers.google.com/analytics/devguides/reporting/core/dimsmets#view=detail&group=traffic_sources&jump=ga_keyword" target="new">keyword</a></strong> - This column contains the keyword description (<a href="https://support.google.com/analytics/answer/1033867?hl=en" target="new">utm_term</a>)
      - name: <strong><a href="https://developers.google.com/analytics/devguides/reporting/core/dimsmets#view=detail&group=traffic_sources&jump=ga_medium" target="new">medium</a></strong> - This column contains the medium name (<a href="https://support.google.com/analytics/answer/1033867?hl=en" target="new">utm_medium</a>)
      - name: <strong>profileid</strong> - This column contains your Google Analytics profile ID.
      - name: <strong>profilename</strong> - This column contains your Google Analytics profile name.
      - name: <strong><a href="https://developers.google.com/analytics/devguides/reporting/core/dimsmets#view=detail&group=traffic_sources&jump=ga_socialnetwork" target="new">socialnetwork</a></strong> - This column contains the name of the social network (e.g. Facebook, YouTube, etc.)
      - name: <strong><a href="https://developers.google.com/analytics/devguides/reporting/core/dimsmets#view=detail&group=traffic_sources&jump=ga_source" target="new">source</a></strong> - This column contains the name of the order source. (<a href="https://support.google.com/analytics/answer/1033867?hl=en" target="new">utm_source</a>)
      - name: <strong>transactionid</strong> - This column contains the order ID, which you can use to join the referral data back to your orders data. You can refer to <a href="https://support.google.com/analytics/answer/1009612?hl=en" target="new">Google’s documentation</a> if you need some background on tracking setup and management.
      - name: <strong>transactions</strong> - This column contains the total number of transactions.
---
{% assign integration = page %}
{% include misc/data-files.html %}

{% contentfor setup %}
Connecting your Google ECcommerce data to Stitch is a three-step process:

1. [Add Google ECcommerce as a Stitch data source](#add-stitch-data-source)
3. [Authorize Stitch & select a Google Analytics profile](#auth-select-ga-profile)
4. [Define the Replication Frequency](#define-rep-frequency)

### Prerequisites
Before you get started, you should verify that:

1. **The user creating the integration has at least [Read & Analyze permissions](https://support.google.com/analytics/answer/2884495?hl=en) and that there's data in the account.** If the profile you use to connect doesn’t have these permissions (or there’s no data in the account), you’ll receive an error message like this:

   > “Something went wrong. None of the Google Analytics profiles associated with the credentials you’ve supplied contain data that Stitch can access. Please make sure that the credentials you’ve supplied have appropriate access.”

2. **All ad-blocking software you are currently using is paused**. Because Google authentication uses pop ups, you may encounter issues if ad blockers aren't disabled during the setup.
3. **Your account has the [Enable ECommerce](https://support.google.com/analytics/answer/1009612?hl=en) setting turned on.** If you have ECommerce data in your accuont, this setting is already enabled and you can move on.

{% include integrations/shared-setup/connection-setup.html %}

### Authorizing Stitch & Selecting a Google Analytics Profile {#auth-select-ga-profile}
1. Next, you’ll be prompted to log into your Google account and to approve Stitch’s access to your Google ECommerce data. **Note that we will only ever read your data.**
2. Click **Allow** to continue.
3. After your credentials are validated, you’ll be prompted to select the Google Analytics profile you want to connect to Stitch:

   ![Selecting a Google Analytics profile.]({{site.baseurl}}/images/integrations/ga-select-profiles.png)

   **Remember: profiles need to have Read & Analyze permissions to be detected by Stitch.** If you don’t see the profile you want in this list, we recommend that you double-check the permission settings.
4. When finished, click **Continue** to save the integration and complete the setup.

{% include integrations/shared-setup/replication-frequency.html %}

{% include integrations/shared-setup/initial-syncs.html %}
{% endcontentfor %}



{% contentfor replication-notes %}
{% include integrations/saas/attribution-windows.html %}
{% endcontentfor %}



{% contentfor schema-notes %}
After the first successful sync of your Google ECommerce data, you'll see a single table in your data warehouse. The table follows this naming convention:

`ecommerce[GA profile id]_integration version`

Here's an example: `ecommerce123456789_v2`. In this case, the profile ID is `123456789` and the version of the ECommerce integration is `2`.

In the section below, you'll find a list of the attributes in this table, a brief description, and links to Google's more in-depth documentation.
{% endcontentfor %}