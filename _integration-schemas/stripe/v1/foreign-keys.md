---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "stripe"

version: "1.0"

foreign-keys:
  - id: "balance-transaction-id"
    table: "balance_transactions"
    attribute: "balance_transaction"
    all-foreign-keys:
      - table: "balance_transactions"
        join-on: "id"
      - table: "charges"
      - table: "payouts"
      - table: "payouts"
        join-on: "failure_balance_transaction"
      - table: "transfers"
      - table: "transfers"
        join-on: "failure_balance_transaction"

  - id: "charge-id"
    table: "charges"
    attribute: "charge"
    all-foreign-keys:
      - table: "charges"
        join-on: "id"
      - table: "invoices"

  - id: "coupon-id"
    table: "coupons"
    attribute: "charge"
    all-foreign-keys:
      - table: "coupon"
        join-on: "id"

  - id: "customer-id"
    table: "customers"
    attribute: "customer"
    all-foreign-keys:
      - table: "charges"
      - table: "customers"
        join-on: "id"
      - table: "invoice_items"
      - table: "invoices"
      - table: "subscription_items"
      - table: "subscriptions"

  - id: "event-id"
    table: "events"
    attribute: "event"
    all-foreign-keys:
      - table: "events"
        join-on: "id"

  - id: "invoice-id"
    table: "invoices"
    attribute: "invoice"
    all-foreign-keys:
      - table: "charges"
      - table: "invoice_items"
      - table: "invoice_line_items"
      - table: "invoices"
        join-on: "id"

  - id: "invoice-item-id"
    table: "invoice_items"
    attribute: "invoice_item"
    all-foreign-keys:
      - table: "invoice_items"
        join-on: "id"

  - id: "invoice-line-item-id"
    table: "invoice_line_items"
    attribute: "invoice_line_item"
    all-foreign-keys:
      - table: "invoice_line_items"
        join-on: "id"

      - table: "invoices"
        subtable: "lines"
        join-on: "value"

  - id: "plan-id"
    table: "plans"
    attribute: "plan"
    all-foreign-keys:
      - table: "invoice_items"
        subattribute: "plan"
        join-on: "id"
      - table: "plans"
        join-on: "id"
      - table: "subscriptions"
        subattribute: "plan"
        join-on: "id"

  - id: "payout-id"
    table: "payouts"
    attribute: "payout"
    all-foreign-keys:
      - table: "payouts"
        join-on: "id"  

  - id: "subscription-item-id"
    table: "subscription_items"
    attribute: "subscription_item"
    all-foreign-keys:
      - table: "invoice_items"
        join-on: "subscription_item"
      - table: "subscription_items"
        join-on: "id"
      - table: "subscriptions"
        subtable: "items"
        join-on: "value"

  - id: "subscription-id"
    table: "subscriptions"
    attribute: "subscription"
    all-foreign-keys:
      - table: "invoice_items"
      - table: "invoice_line_items"
      - table: "invoices"
      - table: "subscriptions"
        join-on: "id"
      - table: "subscription_items"

  - id: "transfer-id"
    table: "transfers"
    attribute: "transfer"
    all-foreign-keys:
      - table: "transfers"
        join-on: "id"
---