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

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
icon: /images/integrations/icons/stripe.svg
whitelist:
  tables: false
  columns: false

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

tables:
## Balance History
  - name: "stripe_balance_history"
    doc-link: https://stripe.com/docs/api/curl#balance_history
    description: "info about transactions have have contributed to your Stripe account balance, including charges, transfers, etc."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Balance History ID (<code>id</code>)
      - name: amount
      - name: available_on
      - name: created
      - name: currency
      - name: description
      - name: fee
      - name: fee_details<code>*</code>
      - name: net
      - name: source__sourced_transfers__data<code>*</code>
      - name: status
      - name: type

## Charges
  - name: "stripe_charges"
    doc-link: https://stripe.com/docs/api/curl#charge_object
    description: "info about charges to credit and debit cards.<br><br>

    <strong>Note that charge dispute data is not included in this table.</strong> See Table Info & Attributes for details."
    notes: |
      ### Charge Dispute Support
      Due to the current structure of our Stripe integration and [how updates work in the Stripe API](#stripe-api-updates), records in this table will not be updated if a related dispute is updated.

      You can, however, find this info in the [`stripe_events`](#stripe_events) table.
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Charge ID (<code>id</code>)
      - name: received_at
      - name: amount
      - name: amount_refunded
      - name: balance_transaction
      - name: captured
      - name: created
      - name: currency
      - name: customer_id
      - name: description
      - name: dispute_id
      - name: failure_code
      - name: failure_message
      - name: fraud_details_stripe_report
      - name: fraud_details_user_report
      - name: invoice_id
      - name: paid
      - name: receipt_email
      - name: receipt_number
      - name: refunded
      - name: statement_descriptor
      - name: status

## Coupons
  - name: "stripe_coupons"
    doc-link: https://stripe.com/docs/api/curl#coupon_object
    description: "info about percent or amount-off discounts that may be applied to a customer. <strong>Note that coupons only apply to invoices; they don't apply to one-off charges.</strong>"
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Coupon ID (<code>id</code>)
      - name: received_at
      - name: created
      - name: duration
      - name: duration_in_months
      - name: metadata__quota_calls
      - name: metadata__quota_level
      - name: metadata__service
      - name: percent_off
      - name: times_redeemed
      - name: valid

## Customers
  - name: "stripe_customers"
    doc-link: https://stripe.com/docs/api/curl#customer_object
    description: "info about your Stripe customers. This table allows you to track multiple charges associated with a single customer."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Customer ID (<code>id</code>)
      - name: received_at
      - name: account_balance
      - name: created
      - name: currency
      - name: delinquent
      - name: description
      - name: discount_id
      - name: email
      - name: metadata__id
      - name: metadata__extra
      - name: metadata__name
      - name: metadata__settings
      - name: workspace

## Events
  - name: "stripe_events"
    doc-link: https://stripe.com/docs/api/curl#event_object
    description: info about events. <a href="https://stripe.com/docs/api/curl#event_types" target="new">When an interesting event occurs</a>, a new event object is created. For example, when a charge succeeds a <code>charge.succeeded</code> event is created; or, when an invoice can't be paid, an <code>invoice.payment_failed</code> event is created.
    notes: |
      ### Event Replication {#events-replication}
      The `stripe_events` table is sort of a "grab bag" of all events across all endpoints, or tables. For every event that takes place on a parent object, a row will be added to the table.

      For example: If a customer account is updated, you'll see the latest state of the customer's account info in the `stripe_customers` table. You'll also see a row in **this** table for the actual **update** event itself.
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Event ID (<code>id</code>)
      - name: created
      - name: data__object__business_url
      - name: data__object__charges_enabled
      - name: data__object__country
      - name: data__object__default_currency
      - name: data__object__default_source
      - name: data__object__delinquent
      - name: data__object__description
      - name: data__object__details_submitted
      - name: data__object__discount
      - name: data__object__display_name
      - name: data__object__email
      - name: data__object__id
      - name: data__object__managed
      - name: data__object__object
      - name: data__object__shipping
      - name: data__object__sources__data<code>*</code>
      - name: data__object__statement_descriptor
      - name: data__object__subscriptions__data<code>*</code>
      - name: data__object__support_phone
      - name: data__object__timezone
      - name: data__object__transfers_enabled
      - name: livemode
      - name: object
      - name: pending_webhooks
      - name: request
      - name: type

## Invoice Items
  - name: "stripe_invoice_items"
    doc-link: https://stripe.com/docs/api/curl#invoiceitem_object
    description: "info about items contained in customer invoices."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Invoice Item ID (<code>id</code>)
      - name: received_at
      - name: amount
      - name: currency
      - name: customer_id
      - name: date
      - name: description
      - name: discountable
      - name: invoice_id
      - name: period_end
      - name: period_start
      - name: plan_id
      - name: proration
      - name: quantity
      - name: bigint
      - name: subscription_id

## Invoices
  - name: "stripe_invoices"
    doc-link: https://stripe.com/docs/api/curl#invoice_object
    description: "info about customer invoices. <strong>Note that this does not include upcoming invoices</strong> - see the Table Info section for details."
    notes: |
      ### Upcoming Invoices

      Stitch's Stripe integration doesn't currently replicate [upcoming invoices](https://stripe.com/docs/subscriptions/invoices#previewing){:target="_blank"}, which Stripe defines as "the next upcoming invoice."

      This is due to the way Stripe generates and assigns IDs to invoices. Existing invoices have IDs while upcoming invoices do not. As Stitch uses the `id` column to identify new data for replication, if an invoice doesn't have an ID, Stitch will be unable to replicate it.
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Invoice ID (<code>id</code>)
      - name: received_at
      - name: amount_due
      - name: attempt_count
      - name: attempted
      - name: charge_id
      - name: closed
      - name: currency
      - name: customer_id
      - name: date
      - name: discount_id
      - name: ending_balance
      - name: forgiven
      - name: lines<code>*</code>
      - name: next_payment_attempt
      - name: paid
      - name: period_end
      - name: period_start
      - name: receipt_number
      - name: starting_balance
      - name: subscription_id
      - name: subtotal
      - name: total
      - name: webhooks_delivered_at

## Plans
  - name: "stripe_plans"
    doc-link: https://stripe.com/docs/api/curl#plan_object
    description: "pricing information for different products and feature levels on your site. For example, you may have a $10/month plan for basic features and a $20/month plan for premium features."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Plan ID (<code>id</code>)
      - name: received_at
      - name: amount
      - name: created
      - name: currency
      - name: interval
      - name: interval_count
      - name: metadata__available
      - name: metadata__grandfathered
      - name: metadata__overage_rows_fee
      - name: metadata__overage_rows_per
      - name: metadata__quota_calls
      - name: metadata__quota_level
      - name: metadata__quota_rows
      - name: metadata__service
      - name: metadata__tier
      - name: name
      - name: statement_descriptor
      - name: trial_period_days

## Subscriptions
  - name: "stripe_subscriptions"
    doc-link: https://stripe.com/docs/api/curl#subscription_object
    description: "the details of subscription plans your customers belong to."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Subscription ID (<code>id</code>)
      - name: received_at
      - name: cancel_at_period_end
      - name: current_period_end
      - name: current_period_start
      - name: customer_id
      - name: discount_id
      - name: metadata__quota_calls
      - name: metadata__quota_rows
      - name: plan_id
      - name: quantity
      - name: start
      - name: status
      - name: trial_end
      - name: trial_start
      - name: canceled_at

## Transfers
  - name: "stripe_transfers"
    doc-link: https://stripe.com/docs/api/curl#transfers
    description: "info about your transfers. A transfer is created any time Stripe sends you money or you initiiate a transfer to a connected account, including bank accounts and debit cards."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Transfer ID (<code>id</code>)
      - name: amount
      - name: amount_reversed
      - name: application_fee
      - name: balance_transaction
      - name: created
      - name: currency
      - name: date
      - name: description
      - name: destination
      - name: destination_payment
      - name: failure_code
      - name: failure_message
      - name: livemode
      - name: medata__method
      - name: metadata__recipient
      - name: metadata__reversals<code>*</code>
      - name: reversed
      - name: source_transaction
      - name: source_type
      - name: statement_descriptor
      - name: status
      - name: type

## Transfers / Transactions
  - name: "stripe_transfer_transactions"
    doc-link: https://stripe.com/docs/api/curl#balance_history
    description: "transfer and transaction IDs, which will allow you to join transfers with the transactions in the <code>stripe_balance_history</code> table."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "transfer_id:transaction_id"
    nested-structures: false
    attributes:
      - name: transfer_id
      - name: transaction_id
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