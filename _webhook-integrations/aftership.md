---
title: AfterShip
permalink: /integrations/webhooks/aftership
redirect_from: /integrations/saas/aftership
## Some users may experience a blip while the redirect works - it's normal.

tags: [stitch_webhooks]
keywords: aftership, integration, schema, etl aftership, aftership etl, aftership schema, stitch webhooks
summary: "Connect your AfterShip data to Stitch using Stitch's Incoming Webhooks integration. In this guide, you'll find setup instructions, info about replication, and the data you can expect to see in your data warehouse."

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "aftership"
display_name: "AfterShip"
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
status-url: "https://status.aftership.com/"
icon: /images/integrations/icons/aftership.svg

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
  - name: "data"
    doc-link: https://www.aftership.com/docs/api/4/webhook
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
{% capture prerequisites %}
### Prerequisites
**Your AfterShip account must be a [premium account](https://www.aftership.com/pricing)** to use webhooks in AfterShip.
{% endcapture %}

{% include integrations/webhooks/webhook-setup.html %}

1. Sign into your AfterShip account.
2. Click **Settings** (the gear icon) in the left nav tab.
3. Click **Triggers**.
4. Click the **Webhook** tab.
5. In the **Webhook URL** field, paste your Stitch-generated webhook URL.
6. In the **Version** field, enter the [number of the webhook version](https://www.aftership.com/docs/api/4/webhook) you're using. As of 1/17/2017, the latest version of AfterShip's webhook is **4.0**. We recommend using the latest version, if possible.
7. In the **Status** section, use the checkboxes to select the events you want to track:

   ![Setting up webhooks in AfterShip.]({{ site.baseurl }}/images/integrations/aftership-webhook-setup.png)
8. When finished, click **Save**.

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