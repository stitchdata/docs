---
title: SendWithUs
permalink: /integrations/webhooks/sendwithus
redirect_from: /integrations/saas/sendwithus

tags: [stitch_webhooks]
keywords: sendwithus, integration, schema, etl sendwithus, sendwithus etl, sendwithus schema, stitch webhooks
summary: "Connect your SendWithUs data to Stitch using Stitch's Incoming Webhooks integration. In this guide, you'll find setup instructions, info about replication, and the data you can expect to see in your data warehouse."

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "sendwithus"
display_name: "SendWithUs"
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
status-url: "https://status.sendwithus.com/"
icon:  /images/integrations/icons/sendwithus.svg

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
  - name: "data"
    doc-link:  https://support.sendwithus.com/analytics/webhook_faq/#what-do-these-webhooks-look-like
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

#### Existing Email Service Providers

1. Sign into your SendWithUs account.
2. Click **Delivery Settings** in the left nav tab.
3. In your list of Email Service Providers (ESP), find the one you want to add the webhook to.
4. Click the **Actions** menu for that ESP, then click **Settings**.
5. The Account Settings for the ESP will display. In the **Forward Webhooks To** field, paste your Stitch-generated webhook URL:

   ![Setting up webhooks in SendWithUs]({{ site.baseurl }}/images/integrations/sendwithus-webhook-setup.png)
6. Click **Save**.

#### New Email Service Providers

**If you're brand new to SendWithUs and haven't yet set up an ESP,** you can define the webhook during the initial setup for most ESPs by pasting your Stitch webhook URL in the **Forward Webhooks To** field. For example:

![Setting up webhooks for a new ESP in SendWithUs]({{ site.baseurl }}/images/integrations/sendwithus-new-esp-webhook-setup.gif)
{% endcontentfor %}



{% contentfor replication-notes %}
{% include integrations/webhooks/webhook-replication.html %}
{% endcontentfor %}



{% contentfor schema-notes %}
{% include integrations/webhooks/webhook-schema.html %}

The data sent by SendGrid's webhook API is based entirely off of the ESP that you're using. For example: say you're using Mandrill as your ESP. The schema of the table created by Stitch **for your Mandrill ESP** will look different than a table created for a SparkPost ESP.

{% capture schema %}
**About the Tables Listed Below**
The next section demonstrates the possible attributes that could be in 

{% endcapture %}
{% endcontentfor %}



{% contentfor revoke-urls %}
{% include integrations/webhooks/webhook-urls-and-security.html %}
{% endcontentfor %}