---
title: Drip
permalink: /integrations/webhooks/drip
redirect_from: /integrations/saas/drip
## Some users may experience a blip while the redirect works - it's normal.

tags: [stitch_webhooks]
keywords: drip, integration, schema, etl drip, drip etl, drip schema, stitch webhooks
summary: "Connect your Drip data to Stitch using Stitch's Incoming Webhooks integration. In this guide, you'll find setup instructions, info about replication, and the data you can expect to see in your data warehouse."

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "drip"
display_name: "Drip"
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
status-url: "https://drip.statuspage.io/"
icon: /images/integrations/icons/drip.svg

table-selection: false
column-selection: false

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
  - name: "data"
    doc-link: https://www.getdrip.com/docs/webhooks#events
    description: ""
    notes: 
    replication-method: "Append-Only (Incremental)"
    primary-key: 
    nested-structures: false
    attribute-notes: |
      A Drip webhook event contains two parts: the subscriber's info and then the details about the event itself.

      In the list below are links to Drip's documentation, which contain detailed examples of the fields in both the subscriber object and the individual events available for tracking.
    attributes:
      - name: subscriber
      - name: subscriber.created
      - name: subscriber.deleted
      - name: subscriber.marked_as_deliverable
      - name: subscriber.marked_as_undeliverable
      - name: subscriber.subscribed_to_campaign
      - name: subscriber.removed_from_campaign
      - name: subscriber.unsubscribed_from_campaign
      - name: subscriber.unsubscribed_all
      - name: subscriber.reactivated
      - name: subscriber.completed_campaign
      - name: subscriber.applied_tag
      - name: subscriber.removed_tag
      - name: subscriber.updated_custom_field
      - name: subscriber.updated_email_address
      - name: subscriber.updated_time_zone
      - name: subscriber.received_email
      - name: subscriber.opened_email
      - name: subscriber.clicked_email
      - name: subscriber.bounced
      - name: subscriber.complained
      - name: subscriber.clicked_trigger_link
      - name: subscriber.visited_page
      - name: subscriber.became_lead
      - name: subscriber.became_non_prospect
      - name: subscriber.updated_lead_score
      - name: subscriber.performed_custom_event

---
{% assign integration = page %}
{% include misc/data-files.html %}

{% contentfor setup %}
{% include integrations/webhooks/webhook-setup.html %}

1. Sign into your Drip account.
2. Navigate to the **[Webhooks](https://www.getdrip.com/webhooks)** page.
3. Paste the Stitch-generated webhook URL into the URL field.
4. Click **Create Webhook**.
 
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