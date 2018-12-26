---
title: Delighted
permalink: /integrations/webhooks/delighted
redirect_from: /integrations/saas/delighted
## Some users may experience a blip while the redirect works - it's normal.

tags: [stitch_webhooks]
keywords: delighted, integration, schema, etl delighted, delighted etl, delighted schema, stitch webhooks
summary: "Connect your Delighted data to Stitch using Stitch's Incoming Webhooks integration. In this guide, you'll find setup instructions, info about replication, and the data you can expect to see in your data warehouse."

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "delighted"
display_name: "Delighted"
author: "Stitch"
author-url: "https://www.stitchdata.com"

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
icon: /images/integrations/icons/delighted.svg

table-selection: false
column-selection: false

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
  - name: "data"
    doc-link: https://delighted.com/docs/api/webhooks
    description: ""
    notes: 
    replication-method: "Append-Only (Incremental)"
    nested-structures: true
    ## attribute-notes: if populated, this will replace the default "While we try to include everything here..." copy.
    attributes:
      - name: Shipment ID (<code>id</code>)
---
{% assign integration = page %}
{% include misc/data-files.html %}

{% contentfor setup %}
{% include integrations/webhooks/webhook-setup.html %}

1. Sign into your Delighted account.
2. Click **Settings**, located in the top right corner.
3. In the Settings menu, click **Integrations**.
4. Locate the **Webhooks** option, then click the **Set Up** link.
5. Using the drop-down menu, select the event you want to track. You can also track everything by selecting the **All Responses** option.
6. In the next field, paste your Stitch-genereated webhook URL.
7. If you want to track more than one event, click the **Add a New Rule** link and repeat steps 5 and 6 until all the events you want to track have been added:

   ![Setting up webhooks in Delighted.]({{ site.baseurl }}/images/integrations/delighted-webhook-setup.png)

8. When finished, click **Save & Turn On.**
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