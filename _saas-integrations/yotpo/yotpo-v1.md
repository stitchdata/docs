---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Yotpo (v1.0)
permalink: /integrations/saas/yotpo
keywords: yotpo, integration, schema, etl yotpo, yotpo etl, yotpo schema
summary: "Connections instructions, replication info, and schema details for Stitch's Yotpo integration."
layout: singer
input: true

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "yotpo"
display_name: "Yotpo"

singer: true
tap-name: "Yotpo"
repo-url: https://github.com/singer-io/tap-yotpo

this-version: "1.0"

api: |
  [{{ integration.display_name }} Core API](https://apidocs.yotpo.com/reference){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false

historical: "1 year"
frequency: "1 hour"
tier: "Free"
status-url: "http://status.yotpo.com/"

anchor-scheduling: true
cron-scheduling: false

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: false

attribution-window: "30 days"

# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **To be the Account Administrator in {{ integration.display_name }}.** [This is required](https://support.yotpo.com/en/article/finding-your-app-key-and-your-secret-key){:target="new"} to access your {{ integration.display_name }} API credentials.

setup-steps:
  - title: "Retrieve your {{ integration.display_name }} API credentials"
    anchor: "retrieve-yotpo-api-credentials"
    content: |
      {% include note.html type="single-line" content="**Note**: You must be the Yotpo Account Administrator to complete this step." %}

      1. Sign into your [{{ integration.display_name }} account](https://yap.yotpo.com/#/login){:target="new"}.
      2. Click the user menu (person icon) in the top right corner.
      3. Click **Account Settings**.
      4. On the **Account Settings** page, click the **Store** tab.
      5. Locate the **API Credentials** section:

         ![The API Credentials section in Yotpo, highlighted]({{ site.baseurl }}/images/integrations/yotpo-api-credentials.png)

      6. The **App Key** field contains your **API Key**, and the **Secret Key** is your **API Secret**.

      Leave this page open for now - you'll need it to complete the next step.

  - title: "add integration"
    content: |
      4. In the **{{ integration.display_name }} API Key** field, paste the value from the **App Key** field in your {{ integration.display_name }} account.
      5. In the **{{ integration.display_name }} API Secret** field, paste the value from the **Secret Key** field in your {{ integration.display_name }} account.
  - title: "historical sync"
  - title: "replication frequency"
  - title: "track data"

# -------------------------- #
#      Replication Info      #
# -------------------------- #

replication-sections:
  - content: |
      {% assign window = "Attribution Window" %}
      {% assign table = "reviews" %}
      {% assign replication-key = "created_at" %}
      {% assign start-date ="06/03/2017" %}
      {% assign replication-key-historical = "2017-06-03 00:00:00" %}
      {% assign replication-key-ongoing = "2017-09-01 00:00:00" %}

      {% include integrations/saas/attribution-windows.html %}

      Refer to the documentation for each of these tables in the next section for more info.

      ### Attribution window examples

      In the tabs below are examples of attribution windows behave during historical (initial) and ongoing replication jobs.

      {% include integrations/saas/attribution-window-examples.html %}

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/yotpo
---
{% assign integration = page %}
{% include misc/data-files.html %}