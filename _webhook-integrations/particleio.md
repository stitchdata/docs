---
title: Particle.io
permalink: /integrations/webhooks/particleio
redirect_from: /integrations/saas/particleio
## Some users may experience a blip while the redirect works - it's normal.

tags: [stitch_webhooks]
keywords: particle.io, integration, schema, etl particle.io, particle.io etl, particle.io schema, stitch webhooks
summary: "Connect your Particle.io data to Stitch using Stitch's Incoming Webhooks integration. In this guide, you'll find setup instructions, info about replication, and the data you can expect to see in your data warehouse."

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "particleio"
display_name: "Particle.io"
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
status-url: "http://status.particle.io/"
icon:  /images/integrations/icons/particle.svg

table-selection: false
column-selection: false

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
  - name: "data"
    doc-link: https://docs.particle.io/guide/tools-and-features/webhooks#webhooks
    description: ""
    notes: 
    replication-method: "Append-Only (Incremental)"
    nested-structures: false
    attribute-notes: |
      The schema of this table will depend entirely on the data you're sending into Stitch.
    attributes:
      - name: 
---
{% assign integration = page %}
{% include misc/data-files.html %}

{% contentfor setup %}
{% capture prerequisites %}
### Particle.io Webhook Limits
Before you dive into connecting Particle.io to Stitch, take note of the following:

1. **Particle.io allows a user to create up to 20 webhooks**.
2. A Particle.io webhook may be triggered up to 10 times per minute for every device registered to that user's account.
{% endcapture %}

{% include integrations/webhooks/webhook-setup.html %}

1. Sign into your [Particle.io console](https://console.particle.io/).
2. Click **Integrations** in the left nav tab.
3. Click **Webhook**.
4. In the **Event Name** field, enter the name of the event you want to track.
5. In the **URL** field, paste your Stitch-generated webhook URL.
6. The **Request Type** field should have **POST** selected - leave this as-is.
7. In the **Device** field, select the device you want to trigger the webhook:

   ![Setting up webhooks in Particle.io.]({{ site.baseurl }}/images/integrations/particleio-webhook-setup.png)

8. When finished, click **Create Webhook**.
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