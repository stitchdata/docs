---
title: Delighted
permalink: /integrations/webhooks/delighted
redirect_from: /integrations/saas/delighted
## Some users may experience a blip while the redirect works - it's normal.

keywords: delighted, integration, schema, etl delighted, delighted etl, delighted schema, stitch webhooks
summary: "Connect your Delighted data to Stitch using Stitch's Incoming Webhooks integration. In this guide, you'll find setup instructions, info about replication, and the data you can expect to see in your data warehouse."

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "delighted"
display_name: "Delighted"

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
tier: "Free"
status-url: "https://status.delighted.com/"

table-selection: false
column-selection: false

extraction-logs: false
loading-reports: false

---
{% assign integration = page %}
{% include misc/data-files.html %}

{% contentfor setup %}
{% include integrations/webhooks/webhook-setup.html %}

{% include layout/image.html type="right" file="/integrations/delighted-webhook-setup.png" max-width="450" %}

1. Sign into your Delighted account.
2. Click **Integrations**.
3. Click the **Webhooks** option.
4. Select the event(s) you want to track using the drop-down menu. You can also track everything by selecting the **All Responses** option.
5. In the next field, paste your Stitch-genereated webhook URL.
6. If you want to track more than one event, click the **Add a New Rule** link and repeat steps 5 and 6 until all the events you want to track have been added.
7. When finished, click **Save changes.**
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