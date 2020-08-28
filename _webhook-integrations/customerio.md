---
title: Customer.io
permalink: /integrations/webhooks/customerio
redirect_from: /integrations/saas/customerio
## Some users may experience a blip while the redirect works - it's normal.

keywords: customerio, integration, schema, etl customerio, customerio etl, customerio schema, stitch webhooks
summary: "Connect your Customer.io data to Stitch using Stitch's Incoming Webhooks integration. In this guide, you'll find setup instructions, info about replication, and the data you can expect to see in your data warehouse."


# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "customerio"
display_name: "Customer.io"

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
  defined: true
  field: "event_id"
tier: "Standard"
status-url: "http://status.customer.io/"
icon: /images/integrations/icons/customerio.svg

table-selection: false
column-selection: false

extraction-logs: false
loading-reports: false

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
  - name: "data"
    doc-link: http://learn.customer.io/developer-documentation/webhooks.html#list-of-webhook-attributes
    description: ""
    notes: 
    replication-method: "Incremental"
    primary-key: event_id
    nested-structures: false
    ## attribute-notes: if populated, this will replace the default "While we try to include everything here..." copy.
    attributes:
      - name: event_id

---
{% assign integration = page %}
{% include misc/data-files.html %}

{% contentfor setup %}
{% include integrations/webhooks/webhook-setup.html %}

1. Sign into your Customer.io account.
2. Click **Integrations** in the menu on the left.
3. In the **Streaming Data Out** section, click the **Get Started** button next to **Email Activity Webhook**.
4. In the **Webhook Endpoint** field, paste your Stitch-generated webhook URL.
5. Next, you'll select the [**Webhook Events**](http://learn.customer.io/developer-documentation/webhooks.html#events) you want to track:
   - **To track specific events**, click the **Edit Webhook Events** link (it's under the **Webhooks Endpoint** field) to display the list of events:

      ![Setting up Customer.io webhooks.]({{ site.baseurl }}/images/integrations/customerio-webhook-setup.png)

      Use the checkboxes to select the events you want to track, clicking **Save Changes** when finished.
   - **To track all available events,** you don't need to do anything else - skip ahead to the last step.

6. Click **Update**.

### Test the Setup
To ensure everything is set up properly, you can send a test call to your Stitch webhook by clicking the **Test** button next to the the **Webhook Endpoint** field. 
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