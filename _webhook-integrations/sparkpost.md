---
title: SparkPost
permalink: /integrations/webhooks/sparkpost
redirect_from: /integrations/saas/sparkpost
keywords: sparkpost, integration, schema, etl sparkpost, sparkpost etl, sparkpost schema, stitch webhooks
summary: "Connect your SparkPost data to Stitch using Stitch's Incoming Webhooks integration. In this guide, you'll find setup instructions, info about replication, and the data you can expect to see in your data warehouse."


# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "sparkpost"
display_name: "SparkPost"

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
status-url: "https://status.sparkpost.com/"
icon: /images/integrations/icons/sparkpost.svg

table-selection: false
column-selection: false

extraction-logs: false
loading-reports: false

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
  - name: "data"
    doc-link: https://developers.sparkpost.com/api/webhooks.html
    description: ""
    notes: 
    replication-method: "Append-Only (Incremental)"
    nested-structures: false
    ## attribute-notes: if populated, this will replace the default "While we try to include everything here..." copy.
    attributes:
      - name: type
      - name: bounce_class
      - name: campaign_id
      - name: customer_id
      - name: delv_method
      - name: device_token
      - name: error_code
      - name: event_id
      - name: friendly_from
      - name: geo_ip__country
      - name: geo_ip__region
      - name: geo_ip__city
      - name: geo_ip__latitude
      - name: geo_ip__longitude
      - name: ip_address
      - name: ip_pool
      - name: message_id
      - name: msg_from
      - name: msg_size
      - name: num_retries
      - name: queue_time
      - name: rcpt_meta
      - name: rcpt_tags
      - name: rcpt_to
      - name: raw_rcpt_to
      - name: rcpt_type
      - name: raw_reason
      - name: reason
      - name: routing_domain
      - name: sending_ip
      - name: sms_coding
      - name: sms_dst
      - name: sms_dst_npi
      - name: sms_dst_ton
      - name: sms_remoteids
      - name: sms_segments
      - name: sms_src
      - name: sms_src_npi
      - name: sms_src_ton
      - name: subaccount_id
      - name: subject
      - name: template_id
      - name: template_version
      - name: timestamp
      - name: transmission_id
      - name: user_agent
      - name: user_str
---
{% assign integration = page %}
{% include misc/data-files.html %}

{% contentfor setup %}
{% include integrations/webhooks/webhook-setup.html %}

1. Sign into your SparkPost account.
2. Click **Account** in the left nav tab.
3. Click **Webhooks**.
4. Click the **New Webhook** button.
5. In the **Webhook Name** field, enter a name for the webhook. We recommend using a name that will tell you, at a glance, what the webhook is for.
5. In the **Target URL** field, paste your Stitch-generated webhook URL.
6. In the **Authentication** field, ensure that **None** is selected.
7. In the **Events** section, you can select the events you want to track. By default everything is selected, but to pick and choose, click **Select** and then use the checkboxes to select the events you want:

   ![Setting up SparkPost webhooks.]({{ site.baseurl }}/images/integrations/sparkpost-webhook-setup.png)

8. When finished, click **Add Webhook**.

### Testing the Setup
To ensure everything is set up properly, you can send a test call to your Stitch webhook by clicking the **Test** button next to the Stitch webhook and then clicking **Send Test Batch**:

![Testing webhook setup in SparkPost.]({{ site.baseurl }}/images/integrations/sparkpost-webhook-test.gif)

If you encounter a `5xx` error (ex: `503 - Service Unavailable`), check the [Stitch Status Page]({{ site.status }}) to see if we've reported any issues. 
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