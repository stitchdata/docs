---
title: Mailjet
permalink: /integrations/webhooks/mailjet
redirect_from: /integrations/saas/mailjet
## Some users may experience a blip while the redirect works - it's normal.

keywords: mailjet, integration, schema, etl mailjet, mailjet etl, mailjet schema, stitch webhooks
summary: "Connect your Mailjet data to Stitch using Stitch's Incoming Webhooks integration. In this guide, you'll find setup instructions, info about replication, and the data you can expect to see in your data warehouse."

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "mailjet"
display_name: "Mailjet"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

type: "Webhook"
branded: true
historical: "Webhook"
frequency: "Continuous"
primary-key:
  defined: false
  field: 
tier: "Standard"
status-url: "https://mailjet.statuspage.io/"
icon: /images/integrations/icons/mailjet.svg

table-selection: false
column-selection: false

extraction-logs: false
loading-reports: false

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
  - name: "data"
    doc-link: https://dev.mailjet.com/guides/#events
    description: ""
    notes: 
    replication-method: "Append-Only (Incremental)"
    primary-key: 
    nested-structures: false
    ## attribute-notes: if populated, this will replace the default "While we try to include everything here..." copy.
    attributes:
      - name: 

---
{% assign integration = page %}
{% include misc/data-files.html %}

{% contentfor setup %}
{% include integrations/webhooks/webhook-setup.html %}

1. Sign into your Mailjet account.
2. Click the **user menu (top right corner) > My Account**.
3. In the **REST API** section, click **Event tracking (triggers)**.
4. First, you'll select the events you want to track:
  - **To track specific events**, click the checkbox(es) next to the event(s) you want to track.
  - **To track ALL events**, click the checkbox next to **Select all**, which is the first row in the table.
5. In the **Endpoint URL** field, paste your Stitch-generated webhook URL. 
6. Paste the Stitch webhook URL in the **Endpoint URL** field **for every event you want to track:**
   ![Setting up Mailjet webhooks.]({{ site.baseurl }}/images/integrations/mailjet-webhook-setup.png)
7. If you want to test things out before saving, click the **Send** button in the **Send a test** column.
8. When you're finished, click **Save**.  
{% endcontentfor %}



{% contentfor replication-notes %}
{% include integrations/webhooks/webhook-replication.html %}
{% endcontentfor %}



{% contentfor schema-notes %}
{% include integrations/webhooks/webhook-schema.html %}
{% endcontentfor %}



{% contentfor revoke-urls %}
{% include integrations/webhooks/webhook-urls-and-security.html %}
{% endcontentfor %}