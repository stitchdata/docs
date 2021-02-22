---
title: SendGrid
permalink: /integrations/webhooks/sendgrid
redirect_from: /integrations/saas/sendgrid

keywords: sendgrid, integration, schema, etl sendgrid, sendgrid etl, sendgrid schema
summary: "Connection instructions and schema details for Stitch's SendGrid integration."

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "sendgrid"
display_name: "SendGrid"

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
status-url: "http://status.sendgrid.com/"
icon: /images/integrations/icons/sendgrid.svg
doc-link: "https://sendgrid.com/docs/API_Reference/Webhooks/event.html"

table-selection: false
column-selection: false

extraction-logs: false
loading-reports: false

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
## Events
  - name: "events"
    doc-link: https://sendgrid.com/docs/API_Reference/Webhooks/event.html#-Event-Types
    description: "details about events."
    notes: "The attributes listed below may not be applicable to every single event type - because of this, you may see some rows that have <code>NULL</code> values."
    replication-method: "Append-Only (Incremental)"
    primary-key: "event:email:timestamp"
    nested-structures: false
    attributes:
      - name: event
      - name: email
      - name: timestamp
      - name: asm_group_id
      - name: attempt
      - name: category
      - name: cert_err
      - name: ip
      - name: reason
      - name: response
      - name: sg_event_id
      - name: sg_message_id
      - name: smtp_id
      - name: status
      - name: tls
      - name: type
      - name: url
      - name: url_offset_index
      - name: url_offset_type
      - name: useragent

## Events - Category
  - name: "events__category"
    doc-link: https://sendgrid.com/docs/API_Reference/Webhooks/event.html#-Event-Types
    description: "info about an event category. This is a subtable of <code>events</code>."
    notes: 
    replication-method: "Append-Only (Incremental)"
    primary-key: "_sdc_source_key_event: _sdc_source_key_email: _sdc_source_key_timestamp: _sdc_level_0_id"
    nested-structures: false
    attributes:
      - name: _sdc_source_key_event
      - name: _sdc_source_key_email
      - name: _sdc_source_key_timestamp
      - name: _sdc_level_0_id
      - name: value
---
{% assign integration = page %}
{% include misc/data-files.html %}

{% contentfor setup %}
{% include integrations/webhooks/webhook-setup.html %}

1. Sign into your SendGrid account.
2. In the pane on the left side of the screen, click **Settings**.
3. In the Settings menu, click **Mail Settings**.
4. Click **Event Notification**. This will expand the notification settings.
5. Click **On** to enable event notifications.
6. In the **HTTP Post URL** field, paste the Stitch-generated webhook URL.
7. In the **Actions** section, select the action types you want to send to Stitch:

   ![Setting up webhooks in SendGrid.]({{ site.baseurl }}/images/integrations/sendgrid-webhook-setup.png)

8. When finished, click the **checkmark** on the right side of the notification settings.
{% endcontentfor %}


{% contentfor replication-notes %}
{% include integrations/webhooks/webhook-replication.html %}

### Dropped Email Events & Stitch Replication

On occasion, SendGrid's API will send `dropped` event records with `email: null`. In conjunction with the `timestamp` and `event` fields, Stitch uses the `email` field to create a composite Primary Key for SendGrid integrations. 

When Primary Key fields are `NULL`, Stitch will not persist them to a destination.

The following record would not persist to a destination because `email` is `NULL`:

```json
{
  "sg_event_id":"sendgrid_internal_event_id",
  "sg_message_id":"sendgrid_internal_message_id",
  "email":null,
  "timestamp":1513375274,
  "smtp-id":"<original-smtp-id@domain.com>",
  "unique_arg_key":"unique_arg_value",
  "category":["category1", "category2", "category3"],
  "reason":"Bounced Address",
  "event":"dropped"
}
```

This record, however, would:

```json
{
  "sg_event_id":"sendgrid_internal_event_id",
  "sg_message_id":"sendgrid_internal_message_id",
  "email":"stitch@stitchdata.com",
  "timestamp":1513375288,
  "smtp-id":"<original-smtp-id@domain.com>",
  "unique_arg_key":"unique_arg_value",
  "category":["category1", "category2"],
  "reason":"Unsubscribed Address",
  "event":"dropped"
}
```

[Read more about SendGrid dropped events here](https://sendgrid.com/docs/Classroom/Deliver/Undeliverable_Email/my_emails_are_being_dropped.html).
{% endcontentfor %}



{% contentfor schema-notes %}
{% include integrations/webhooks/webhook-schema.html %}
{% endcontentfor %}



{% contentfor revoke-urls %}
{% include integrations/webhooks/webhook-urls-and-security.html %}
{% endcontentfor %}