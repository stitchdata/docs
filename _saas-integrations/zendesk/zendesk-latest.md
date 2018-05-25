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
singer: false
author: "Stitch"
author-url: "https://www.stitchdata.com"
status-url: "https://status.zendesk.com/"

this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "1 year"
frequency: "30 minutes"
tier: "Premium"
icon: /images/integrations/icons/zendesk.svg
whitelist:
  tables: true
  columns: false


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **Administrator permissions in Zendesk**. Only users with the [Zendesk Administrator role can create an API token](https://support.zendesk.com/hc/en-us/articles/226022787-Generating-a-new-API-token-){:target="_blank"}, which is required to complete the setup.

setup-steps:
  - title: "add integration"
    content: |
      4. In the **Zendesk Subdomain** field, enter your Zendesk site prefix. For example: For `stitchdata.zendesk.com`, only `stitchdata` would be entered into this field.

  - title: "historical sync"
  - title: "replication frequency"
  - title: "Authorize Stitch to access Zendesk"
    anchor: "grant-stitch-authorization"
    content: |
      1. Next, you'll be prompted to sign into your Zendesk account.
      2. After you log into Zendesk, [TODO: NEXT STEP NEEDED]
      3. After the authorization process is successfully completed, you'll be directed back to Stitch.
      4. Click {{ app.buttons.finish-int-setup }}.
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #
---
{% assign integration = page %}
{% include misc/data-files.html %}