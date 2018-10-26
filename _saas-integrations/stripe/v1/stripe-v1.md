---
title: Stripe
permalink: /integrations/saas/stripe
tags: [saas_integrations]
keywords: stripe, integration, schema, etl stripe, stripe etl, stripe schema
summary: "Connection instructions, replication info, and schema details for Stitch's Stripe integration."
format: ## controls formatting options in template
  schema-list: true
  table-desc: true
  list: expand

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "stripe"
display_name: "Stripe"
singer: false
author: "Stitch"
author-url: "https://www.stitchdata.com"
status-url: "https://status.stripe.com/"

this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
icon: /images/integrations/icons/stripe.svg

table-selection: false
column-selection: false

anchor-scheduling: false
extraction-logs: false
loading-reports: false

# -------------------------- #
#      Querying Details      #
# -------------------------- #

## Stripe's API uses an event-based approach to
## update each of its objects. This results in a 
## greater number of rows being created in Stripe
## than what will actually persist to a data warehouse.

replication-notes: true

# -------------------------- #
#      Incompatiblities      #
# -------------------------- #

## Incompatibilities with destinations are listed here.

incompatible:
  postgres: "sometimes"
  reason: "Tables and columns created as a result of de-nesting nested data may have names that exceed PostgreSQL's limit of 63 characters for tables and 59 characters for columns. PostgreSQL data warehouses will reject these tables and columns, meaning Stitch will be unable to load them."

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

## See this integration's folder in /_integration-schemas for details
## on the tables it contains.

---
{% assign integration = page %}
{% include misc/data-files.html %}



{% contentfor setup %}
Connecting your Stripe data to Stitch is a four-step process:

1. [Add Stripe as a Stitch data source](#add-stitch-data-source)
3. [Define the Historical Sync](#define-historical-sync)
4. [Define the Replication Frequency](#define-rep-frequency)
5. [Authorize Stitch to access Stripe](#authorize-stitch)

### Prerequisites

**The user who sets up the integration must have Admin permissions in Stripe**. If you don't have these permissions, please loop in a Stripe admin before continuing.

{% include integrations/shared-setup/connection-setup.html %}

{% include integrations/saas/setup/historical-sync.html %}

{% include integrations/shared-setup/replication-frequency.html %}

### Authorize Stitch to Access Stripe {#authorize-stitch}

Lastly, you'll be directed to Stripe's website to complete the setup. **Remember you must have Admin permissions in Stripe for the connection to be successful.**

1. A screen asking for authorization to Stripe will display. **Note that Stitch will only ever read your data.**
2. Click **Sign in with Stripe to connect**.
3. Enter your Stripe credentials and click **Sign into your account**.
4. After the authorization process successfully completes, you'll be redirected back to Stitch.
5. Click {{ app.buttons.finish-int-setup }}.

{% include integrations/shared-setup/initial-syncs.html %}
{% endcontentfor %}



{% contentfor replication-notes %}
Stripe's API uses an event-based approach to create and update data points. **Because this approach can create large numbers of records and drive up your row usage**, it's important to understand how Stripe's API works and how Stitch queries it for data as a result.

In this section, we'll be using the word "object" to refer to the entities (ex: customer) contained within an API.

#### Updates in "Traditional" APIs {#traditional-api-updates}
When we talk about "traditional" APIs, we mean the kind that only have a single type of object. In this case, when a record is updated, only that object is "notified."

If, for example, a customer email address is updated, only the `customers` object would be affected.

By this we mean that only the row in the `customers` table for that particular account would change. The `email` field would show the new email address and the `updated_at` field would show the time the change - or event - happened.

To summarize: one change = one row.

#### Updates in Stripe's API {#stripe-api-updates}
Stripe works a little differently than the traditional API we outlined above: it's designed to use a change - or an event - to one object to update another.

Instead of having just one object like `customers` that is directly updated, Stripe's API has two: a "parent" object (`customers`) and an "update" object (`update_customers`).

Let's use the updated customer email example again. If a customer email address is updated, several things will happen in Stripe's API as a result of its event-based update method:

1. A row will be created in the `stripe_events` table to record the event details,
2. A row will be created in the `stripe_update_customers` table,
3. The row in the `stripe_customers` table for that customer's account will be updated based on the corresponding data in `stripe_update_customers`

In this case, one change doesn't equate to a single row. That single change resulted in the creation of **three** rows.

Additionally, note that:

- **Stitch doesn't persist the update objects to your data warehouse as tables**, but still queries them to be able to update the parent object tables accordingly.
- **Updates to events that update other events aren't currently supported**. For example: if a `dispute` is updated, the related `charge` in the `stripe_charges` table will **not** be updated. 

   You can, however, find this info in the [`stripe_events`](#stripe_events) table.


#### Impact on Row Counts {#row-count-impact}
Because a single event can result in creating or updating multiple rows, Stripe can potentially drive up your row usage. Additionally, Stripe deeply nests their data. **If you use a data warehouse that doesn't natively support nested structures,** Stitch will de-nest these records and create subtables, resulting in a greater number of replicated rows.

To counter this, we recommend setting the Replication Frequency to something less frequent - like every 24 hours instead of every 30 minutes - to help keep your row count down and prevent overages.
{% endcontentfor %}
