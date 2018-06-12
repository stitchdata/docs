---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: AppsFlyer
permalink: /integrations/saas/appsflyer
tags: [saas_integrations]
keywords: appsflyer, integration, schema, etl appsflyer, appsflyer etl, appsflyer schema
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "appsflyer"
display_name: "AppsFlyer"
repo-url: https://github.com/singer-io/tap-appsflyer

# this-version: ""

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: http://status.appsflyer.com/
icon: /images/integrations/icons/appsflyer.svg
whitelist:
  tables: false
  columns: false

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

# requirements-list:
#   - item: ""
#   - item: ""

requirements-info:

setup-steps:
  - title: "Retrieve the app ID"
    anchor: "retrieve-the-app-id"
    content: |
      Sign into your {{ integration.display_name }} account.

      Depending on the app's type (iOS, Android, or Windows), the app ID format will vary:

      - **iOS** - This will be the iTunes ID of your app, without the `id` portion. For example: If the app is `id987654321`, the ID would be `987654321`.
      - **Android** - This will be the package name registered on AppsFlyer. For example: If the package is registered as `com.stitchdata.test`, the ID would be `com.stitchdata.test`.
      - **Windows** - This will be the Windows app ID. For example: `f1e2d3c4b5a6`

      The location of each type of app ID is highlighted in the image below:

      ![AppsFlyer app ID locations]({{ site.baseurl }}/images/integrations/appsflyer-app-ids.png)

  - title: "Retrieve the app's API key"
    anchor: "retrieve-app-api-key"
    content: |
      1. In the list of apps, click the app you want to replicate data from. This will open the app's dashboard page.
      2. Under the **Integration** section, click **API Access.**
      3. Copy the key from the **Your API Key** field.

  - title: "add integration"
    content: |
      4. In the **App ID** field, enter the ID of the app you want to replicate data from.
      5. In the **API Token** field, paste the app's API key.
  - title: "historical sync"
  - title: "replication frequency"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/appsflyer
---
{% assign integration = page %}
{% include misc/data-files.html %}