---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas/
## FOR INSTRUCTIONS & REFERENCE INFO

title: Stripe
permalink: /integrations/saas/stripe
tags: [saas_integrations]
keywords: stripe, integration, schema, etl stripe, stripe etl, stripe schema
summary: "Connection instructions, replication info, and schema details for Stitch's Stripe integration."
layout: singer
# input: false

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "stripe"
display_name: "Stripe"

singer: false
tap-name: "Stripe"
repo-url: https://github.com/singer-io/tap-stripe

this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: "https://status.stripe.com/"
icon: /images/integrations/icons/stripe.svg

table-selection: true
column-selection: true

anchor-scheduling: true
extraction-logs: true
loading-reports: true

# -------------------------- #
#      Incompatiblities      #
# -------------------------- #

## Incompatibilities with destinations are listed here.

incompatible:
  postgres: "sometimes"
  reason: "Tables and columns created as a result of de-nesting nested data may have names that exceed PostgreSQL's limit of 63 characters for tables and 59 characters for columns. PostgreSQL data warehouses will reject these tables and columns, meaning Stitch will be unable to load them."

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **Admin permissions in {{ integration.display_name }}.** This is required to grant Stitch access to {{ integration.display_name }}.

setup-steps:
  - title: "add integration"
  - title: "historical sync"
  - title: "replication frequency"
  - title: "Authorize Stitch to access {{ integration.display_name }}"
    anchor: "grant-stitch-authorization"
    content: |
      1. Next, you'll be prompted to sign into your {{ integration.display_name }} account.
      2. A screen explaining what you're authorizing will display. **Note**: Stitch will only ever read your {{ integration.display_name }} data, and cannot create charges or any other records in {{ integration.display_name }}.
      3. Click **Sign in with {{ integration.display_name }} to connect**.
      4. Sign into your {{ integration.display_name }} account.
      5. After the authorization process is successfully completed, you'll be directed back to Stitch.
      6. Click {{ app.buttons.finish-int-setup }}.
  - title: "track data"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

## See this integration's folder in /_integration-schemas for details
## on the tables it contains.

---
{% assign integration = page %}
{% include misc/data-files.html %}

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