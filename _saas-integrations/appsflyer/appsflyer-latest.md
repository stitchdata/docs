---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: AppsFlyer (v1)
permalink: /integrations/saas/appsflyer
keywords: appsflyer, integration, schema, etl appsflyer, appsflyer etl, appsflyer schema
summary: "Connection instructions, replication info, and schema details for Stitch's AppsFlyer integration."
layout: singer

key: "appsflyer-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "appsflyer"
display_name: "AppsFlyer"
repo-url: https://github.com/singer-io/tap-appsflyer

api: |
  [{{ integration.display_name }} Raw Data Reports V5 API](https://help.fullstory.com/develop-rest/data-export-api){:target="new"}

this-version: "1"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false

historical: "60 days"
frequency: "30 minutes"
tier: "Standard"
status-url: http://status.appsflyer.com/

api-type: "platform.appsflyer"

anchor-scheduling: true
cron-scheduling: true

table-selection: false
column-selection: false

extraction-logs: true
loading-reports: true


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: "**To be the {{ integration.display_name }} Account Owner.** Only Account Owners have access to API credentials in {{ integration.display_name }}, which is required to set up the integration."
  - item: |
      **Access to raw data exports in {{ integration.display_name }}.** Stitch's {{ integration.display_name }} integration uses the [Raw Data Report API](https://support.appsflyer.com/hc/en-us/articles/208387843-Raw-Data-Reports-V5-) to replicate installation and in-app event data. Access to raw data is an {{ integration.display_name }} premium feature, which may only be available on their higher tiers.

      To determine if you have access to raw data pulling, [follow these instructions](https://support.appsflyer.com/hc/en-us/articles/207034366-API-Policy#2-raw-data-reports-via-pull-api) in {{ integration.display_name }}'s documentation.

setup-steps:
  - title: "Retrieve the app ID"
    anchor: "retrieve-the-app-id"
    content: |
      Sign into your {{ integration.display_name }} account.

      Depending on the app's type (iOS, Android, or Windows), the app ID format will vary:

      - **iOS** - This will be the iTunes ID of your app. Example: `id987654321`.
      - **Android** - This will be the package name registered on AppsFlyer. For example: If the package is registered as `com.stitchdata.test`, the ID would be `com.stitchdata.test`.
      - **Windows** - This will be the Windows app ID. For example: `f1e2d3c4b5a6`

      The location of each type of app ID is highlighted in the image below:

      ![AppsFlyer app ID locations]({{ site.baseurl }}/images/integrations/appsflyer-app-ids.png)

  - title: "Retrieve the account's API key"
    anchor: "retrieve-your-api-key"
    content: |
      {% include note.html type="single-line" content="You must be the Account Owner in AppsFlyer to complete this step." %}

      1. In the list of apps, click the app you want to replicate data from. This will open the app's dashboard page.
      2. Under the **Integration** section, click **API Access.**
      3. Copy the key from the **Your API Key** field.

  - title: "add integration"
    content: |
      4. In the **App ID** field, enter the ID of the app you want to replicate data from.
      5. In the **API Token** field, paste the API key from [Step 2](#retrieve-your-api-key).
  - title: "historical sync"
    content: |
      **Note**: {{ integration.display_name }} imposes limits on date ranges for replicating historical data. If the **Start Date** is more than 90 days from the current date, replication will be unsuccessful. Refer to the [Historical AppsFlyer data limitations](#historical-appsflyer-data-limitations) section for more info.
  - title: "replication frequency"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/appsflyer

replication-sections:
  - title: "Historical {{ integration.display_name }} data limitations"
    anchor: "historical-appsflyer-data-limitations"
    content: |
      [Due to limits imposed by {{ integration.display_name }} on date ranges while querying](https://support.appsflyer.com/hc/en-us/articles/209680773-Export-Data-Reports#the-reports), only the past **90 days'** of historical data is available for any given app.

      If the integration's **Start Date** setting in Stitch is set to a date older than 90 days ago, extraction errors will occur and be surfaced in the integration's [Extraction Logs]({{ link.replication.extraction-logs | prepend: site.baseurl }}).

  - title: "{{ integration.display_name }} API call limits and Replication Frequency"
    anchor: "api-call-limits"
    content: |
      In addition to historical limitations, {{ integration.display_name }} also [imposes a limit on the number of raw data API calls](https://support.appsflyer.com/hc/en-us/articles/207034366-API-Policy#2-raw-data-reports-via-pull-api) that can be made per day. Currently, the maximum is **10 API calls per day, per app** and increases when upgrading to a higher {{ integration.display_name }} tier.

      Each time Stitch requests data for an app - or a single {{ integration.display_name }} integration - two API calls will be used: One to replicate `in_app_events`, and one for `installations`.

      If your Stitch {{ integration.display_name }} integration is set to replicate frequently (ex: every 30 minutes), you may quickly consume your {{ integration.display_name }} API quota. When this occurs, Stitch will pause replication and resume where it left off when more quota is available.

      To avoid disruptions in replication, we recommend selecting a lower [Replication Frequency]({{ link.replication.rep-frequency | prepend: site.baseurl }}), such as 12 or 24 hours.
---
{% assign integration = page %}
{% include misc/data-files.html %}