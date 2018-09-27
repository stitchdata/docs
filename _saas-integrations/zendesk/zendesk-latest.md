---
title: Zendesk
permalink: /integrations/saas/zendesk
tags: [saas_integrations]
keywords: zendesk, integration, schema, etl zendesk, zendesk etl, zendesk schema
summary: "Connection instructions, replication info, and schema details for Stitch's Zendesk integration."
layout: singer

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "zendesk"
display_name: "Zendesk"
singer: true
author: "Stitch"
author-url: "https://www.stitchdata.com"
status-url: "https://status.zendesk.com/"
repo-url: "https://github.com/singer-io/tap-zendesk"

this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "1 year"
frequency: "60 minutes"
tier: "Paid"
icon: /images/integrations/icons/zendesk.svg

table-selection: true
column-selection: true

anchor-scheduling: true
extraction-logs: true
loading-reports: true


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **Administrator permissions in Zendesk**. Some data types in Zendesk may only be accessed with Admin permissions. For example: To replicate ticket metric or tag data, Zendesk's API requires a user with Admin permissions.

      To ensure you can replicate all the data you need, we recommend a user with Admin permissions set up the integration.

setup-steps:
  - title: "add integration"
    content: |
      4. In the **Zendesk Subdomain** field, enter your Zendesk site prefix. For example: For `stitchdata.zendesk.com`, only `stitchdata` would be entered into this field.

  - title: "historical sync"
  - title: "replication frequency"
  - title: "Authorize Stitch to access Zendesk"
    anchor: "grant-stitch-authorization"
    content: |
      {% include note.html content="A Zendesk user with Admin permissions must complete this step." %}

      1. Next, you'll be prompted to sign into your Zendesk account.
      2. After the authorization process is successfully completed, you'll be directed back to Stitch.
      3. Click {{ app.buttons.finish-int-setup }}.
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #
---
{% assign integration = page %}
{% include misc/data-files.html %}
