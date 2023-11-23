---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "chargify"

version: "1"

foreign-keys:
  - id: "component-id"
    table: "components"
    attribute: "component_id"
    all-foreign-keys:
      - table: "components"
        join-on: "id"
      - table: "components"
        subattribute: "prices"
        join-on: "id"
      - table: "invoices"
        subattribute: "charges"
      - table: "invoices"
        subattribute: "payments_and_credits"
      - table: "price_points"
      - table: "price_points"
        subattribute: "prices"
      - table: "statements"
        subattribute: "transactions"
      - table: "transactions"

  - id: "coupon-id"
    table: "coupons"
    attribute: "coupon_id"
    all-foreign-keys:
      - table: "coupons"
        join-on: "id"

  - id: "customer-id"
    table: "customers"
    attribute: "customer_id"
    all-foreign-keys:
      - table: "customers"
        join-on: "id"
      - table: "customers"
        join-on: "parent_id"
      - table: "invoices"
        subattribute: "charges"
      - table: "invoices"
        subattribute: "payments_and_credits"
      - table: "statements"
        subattribute: "transactions"
      - table: "subscriptions"
        subattribute: "credit_card"
      - table: "subscriptions"
        subattribute: "customer"
        join-on: "id"
      - table: "transactions"

  - id: "event-id"
    table: "events"
    attribute: "event_id"
    all-foreign-keys:
      - table: "events"
        join-on: "id"
      - table: "statements"
        subattribute: "events.event"
        join-on: "id"

  - id: "invoice-id"
    table: "invoices"
    attribute: "invoice_id"
    all-foreign-keys:
      - table: "invoices"
        join-on: "id"

  - id: "price-point-id"
    table: "price_points"
    attribute: "price_point_id"
    all-foreign-keys:
      - table: "components"
        join-on: "default_price_point_id"
      - table: "components"
        subattribute: "prices"
      - table: "price_points"
        join-on: "id"

  - id: "product-family-id"
    table: "product_families"
    attribute: "product_family_id"
    all-foreign-keys:
      - table: "components"
      - table: "coupons"
      - table: "product_family"
        join-on: "id"
      - table: "products"
        subattribute: "product_family"
        join-on: "id"
      - table: "subscriptions"
        subattribute: "product.product_family"
        join-on: "id"

  - id: "product-id"
    table: "products"
    attribute: "product_id"
    all-foreign-keys:
      - table: "events"
        subattribute: "event_specific_data"
      - table: "invoices"
        subattribute: "charges"
      - table: "invoices"
        subattribute: "payments_and_credits"
      - table: "products"
        join-on: "id"
      - table: "statements"
        subattribute: "events.event.event_specific_data"
      - table: "statements"
        subattribute: "transactions"
      - table: "subscriptions"
        join-on: "next_product_id"
      - table: "subscriptions"
        subattribute: "product"
        join-on: "id"
      - table: "transactions"

  - id: "statement-id"
    table: "statements"
    attribute: "statement_id"
    all-foreign-keys:
      - table: "invoices"
      - table: "statements"
        join-on: "id"
      - table: "statements"
        subattribute: "transactions"
      - table: "transactions"

  - id: "subscription-id"
    table: "subscriptions"
    attribute: "subscription_id"
    all-foreign-keys:
      - table: "events"
      - table: "invoices"
        subattribute: "charges"
      - table: "invoices"
        subattribute: "payments_and_credits"
      - table: "invoices"
      - table: "statements"
        subattribute: "events.event"
      - table: "statements"
      - table: "statements"
        subattribute: "transactions"
      - table: "subscriptions"
        join-on: "id"
      - table: "transactions"

  - id: "transaction-id"
    table: "transactions"
    attribute: "transaction-id"
    all-foreign-keys:
      - table: "events"
        subattribute: "event_specific_data"
        join-on: "account_transaction_id"
      - table: "invoices"
        subattribute: "charges"
        join-on: "payment_id"
      - table: "invoices"
        subattribute: "payments_and_credits"
        join-on: "payment_id"
      - table: "statements"
        subattribute: "transactions"
        join-on: "id"
      - table: "subscriptions"
        join-on: "signup_payment_id"
      - table: "subscriptions"
        join-on: "stored_credential_transaction_id"
      - table: "transactions"
        join-on: "id"
      - table: "transactions"
        join-on: "parent_id"
      - table: "transactions"
        join-on: "payment_id"
---