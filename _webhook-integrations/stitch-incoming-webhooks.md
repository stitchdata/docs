---
title: Stitch Incoming Webhooks
permalink: /integrations/webhooks/stitch-incoming-webhooks

tags: [stitch_webhooks]
keywords: incoming webhooks, etl webhooks, incoming webhooks etl, incoming webhooks schema, stitch webhooks, webhooks
summary: "Stitch’s Incoming Webhooks integration provides a simple and flexible method to integrate dozens of webhook APIs with Stitch. This guide will walk you through how to set up a generic Incoming Webhook integration, how replication works, and what data you can expect to see."

key: "incoming-webhooks-reference"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "incoming-webhooks"
display_name: "Incoming Webhooks"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

type: "Webhook"
branded: false
historical: "Webhook"
frequency: "Continuous"
primary-key:
  defined: false
  field: 
tier: "Free"
status-url: "http://status.stitchdata.com/"
icon:  /images/integrations/icons/incoming-webhooks.svg

table-selection: false
column-selection: false

extraction-logs: false
loading-reports: false

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
  - name: "data"
    doc-link: 
    description: "event data from [app]."
    notes: 
    replication-method: "Append-Only (Incremental)"
    nested-structures: false
    attributes:
      - name: ID (<code>id</code>)
      - name: event
      - name: value
---
{% assign integration = page %}
{% include misc/data-files.html %}

{% contentfor intro %}
Stitch’s Incoming Webhooks integration provides a simple and flexible method to integrate dozens of webhook APIs with Stitch. If Stitch doesn’t have a native integration for the webhook you want to integrate, then Stitch webhooks is your best bet. Webhooks are handy for anything that requires a notification and a potential follow-up response, including:

- Email events, such as bounces or spam
- Incoming support requests
- Incoming leads from a marketing website
- Important updates to product docs
- And so on!

---

## Prerequisites

To use Stitch Incoming Webhooks:

1. You must have a Stitch account. The Incoming Webhooks integration is available to all Stitch users, whether you're on a Free or Paid tier.

2. **The Webhook API you're integrating with meets the following requirements**:
   - The data sent by the webhook API must come to Stitch in **JSON format**. This is currently the only format Stitch supports.
   - The payload (or delivery) of the data must come via a `POST` request.
   - Request bodies must be less than 4MB

You can determine if the webhook API you want to use meets the above criteria by checking out that provider's webhook API documentation.

{% endcontentfor %}

{% contentfor setup %}
{% include integrations/webhooks/webhook-setup.html %}
{% endcontentfor %}



{% contentfor replication-notes %}
{% include integrations/webhooks/webhook-replication.html %}
{% endcontentfor %}



{% contentfor schema-notes %}
{% include integrations/webhooks/webhook-schema.html %}

### NULLs in Webhook Data {#nulls-webhook-data}

When working with webhook data, you'll likely notice that your data contains quite a few `NULLs`. There are two reasons for this: 

- The general nature of webhook data, and
- The design of the Incoming Webhooks integration

The Stitch Incoming Webhook integration is designed to create only one top-level table. This single table will contain all the data that Stitch receives from your webhook, which can include several types of records. For example: if you connect an email service like SendGrid using Incoming Webhooks, the table Stitch creates may contain records for `whitelist` events, `click` events, `bounce` events, and so on.

While each record type may contain some similar attributes (`id`, `created_at`, etc.), it's likely that each record type will have its own set of attributes, which will only be populated for that record type.

As such, some columns in some records will contain `NULLs`. Here's an example of a message send event, a whitelist add event, and a click event:

```markdown
| id | timestamp | event | action | type      | ip          | url           |
|----+------------+-------+--------+-----------+-------------+---------------|
| 1  | 1481730892 | send  | NULL   | NULL      | NULL        | NULL          |
| 2  | NULL       | NULL  | add    | whitelist | NULL        | NULL          |
| 3  | 1481732465 | click | NULL   | NULL      | 54.88.76.97 | http://hi.com |

// record 1 is a message send event
// record 2 is a whitelist add event
// record 3 is a click event
```

{% endcontentfor %}



{% contentfor revoke-urls %}
{% include integrations/webhooks/webhook-urls-and-security.html %}
{% endcontentfor %}