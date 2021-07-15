---
title: Zendesk Chat (v1)
permalink: /integrations/saas/zendesk-chat
keywords: zopim, integration, schema, etl zopim, zopim etl, zopim schema, zendesk chat, zendesk
summary: "Connection instructions and schema details for Stitch's Zendesk Chat integration."
layout: singer

key: "zendesk-chat-setup"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "zendesk-chat"
display_name: "Zendesk Chat"

singer: true
status-url: "https://status.zendesk.com/"

this-version: "1"

api: |
  [{{ integration.display_name }} API](https://developer.zendesk.com/rest_api/docs/chat/introduction){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Standard"

anchor-scheduling: false
cron-scheduling: false

table-selection: false
column-selection: false
select-all: false
select-all-reason: |
  As this integration doesn't support table or column selection, all available tables and columns are automatically replicated.

extraction-logs: true
loading-reports: true


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
      **Owner permissions in {{ integration.display_name }}**. The user who authorizes the integration must have [Owner permissions in {{ integration.display_name }}](https://chat.zendesk.com/hc/en-us/articles/212679597-Understanding-and-managing-roles-in-Zendesk-Chat){:target="_blank"}. Otherwise, Stitch will encounter authentication issues and be unable to replicate data.

  - item: |
      **An Advanced or Premium {{ integration.display_name }} account.** Zendesk only allows customers on their Advanced or Paid {{ integration.display_name }} plans to utilize the Rest API, which is what Stitch uses to connect to your {{ integration.display_name }} account and replicate data.

        If your {{ integration.display_name }} account is on Lite or Basic, you will need to upgrade your {{ integration.display_name }} plan. [More info on {{ integration.display_name }} plans can be found on Zendesk's website](https://www.zendesk.com/chat/compare/#compare){:target="_blank"}.

setup-steps:
  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Authorize Stitch to access {{ integration.display_name }}"
    anchor: "authorize-stitch"
    content: |
      Lastly, you'll be directed to Zendesk's website to complete the setup.

      1. Enter your {{ integration.display_name }} credentials and click **Login**.
      2. Complete the authorization process.
      3. After the authorization process successfully completes, you'll be redirected back to Stitch.
      4. Click {{ app.buttons.finish-int-setup }}.
---
{% assign integration = page %}
{% include misc/data-files.html %}