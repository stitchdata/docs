---
title: Vero
permalink: /integrations/webhooks/vero
redirect_from: /integrations/saas/vero

tags: [stitch_webhooks]
keywords: vero, integration, schema, etl vero, vero etl, vero schema, stitch webhooks
summary: "Connect your Vero data to Stitch using Stitch's Incoming Webhooks integration. In this guide, you'll find setup instructions, info about replication, and the data you can expect to see in your data warehouse."

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "vero"
display_name: "Vero"

this-version: "1"

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
status-url: "http://status.getvero.com/"
icon:  /images/integrations/icons/vero.svg

table-selection: false
column-selection: false

extraction-logs: false
loading-reports: false

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
  - name: "data"
    doc-link:  http://help.getvero.com/articles/setting-up-veros-webhooks.html#webhook-format
    description: ""
    notes: 
    replication-method: "Append-Only (Incremental)"
    nested-structures: false
    ## attribute-notes: if populated, this will replace the default "While we try to include everything here..." copy.
    attributes:
      - name: type
---
{% assign integration = page %}
{% include misc/data-files.html %}

{% contentfor setup %}
{% include integrations/webhooks/webhook-setup.html %}

1. Sign into your Vero account.
2. Click **Settings** (the gear icon) in the left nav tab.
3. Click **Integrations**.
4. Click **View** next to the **Custom Integration (Webhooks)** option.
5. Click the **Add Webhooks Integration** button.
6. In the **Notification URL** field, paste your Stitch-generated webhook URL.
7. Click the **Save** button.
8. After the webhook has been saved, you can select the individual events you want to track. Use the checkboxes to select events:

   ![Setting up webhooks in Vero]({{ site.baseurl }}/images/integrations/vero-webhook-setup.gif)

9. When you're finished selecting events, click the **Save** button again.
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