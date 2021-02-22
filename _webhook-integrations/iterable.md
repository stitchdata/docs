---
title: Iterable
permalink: /integrations/webhooks/iterable
redirect_from: /integrations/saas/iterable
## Some users may experience a blip while the redirect works - it's normal.

keywords: iterable, integration, schema, etl iterable, iterable etl, iterable schema, stitch webhooks
summary: "Connect your Iterable data to Stitch using Stitch's Incoming Webhooks integration. In this guide, you'll find setup instructions, info about replication, and the data you can expect to see in your data warehouse."

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "iterable"
display_name: "Iterable"

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
status-url: "http://status.iterable.com/"
icon: /images/integrations/icons/iterable.svg

table-selection: false
column-selection: false

extraction-logs: false
loading-reports: false

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
  - name: "data"
    doc-link: https://support.iterable.com/hc/en-us/articles/208013936-System-Webhooks
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

1. Sign into your Iterable account.
2. Click **Integrations > Webhooks**.
3. In the **Endpoint** field, paste your Stitch-generated webhook URL.
4. Click **Create Webhook**.
5. After the webhook is saved, click the **Edit** button to the far right to select the [events](https://support.iterable.com/hc/en-us/articles/208013936-System-Webhooks) you want to track.
6. Check the events you want to track:

   ![Setting up Iterable webhooks.]({{ site.baseurl }}/images/integrations/iterable-webhook-setup.png)

Your changes will save automatically, so you're good to go.
 
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