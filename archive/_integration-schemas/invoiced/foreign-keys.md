---
tap-reference: "invoiced"

version: "1"

foreign-keys:
  - id: "credit-note-id"
    attribute: "id"
    table: "credit_notes"
    all-foreign-keys:
      - table: "credit_notes"
        join-on: "id"
      - table: "transactions"

  - id: "customer-id"
    attribute: "customer"
    table: "customers"
    all-foreign-keys:
      - table: "credit_notes"
      - table: "customers"
        join-on: "id"
      - table: "estimates"
      - table: "invoices"
      - table: "subscriptions"
      - table: "transactions"

  - id: "discount-id"
    attribute: "id"
    table: "credit_notes"
    all-foreign-keys:
      - table: "credit_notes"
        subtable: "discounts"
        join-on: "id"

      - table: "credit_notes"
        subtable: "items__discounts"
        join-on: "id"

      - table: "estimates"
        subtable: "discounts"
        join-on: "id"

      - table: "estimates"
        subtable: "items__discounts"
        join-on: "id"

      - table: "invoices"
        subtable: "discounts"
        join-on: "id"

      - table: "invoices"
        subtable: "items__discounts"
        join-on: "id"

      - table: "subscriptions"
        subtable: "discounts"
        join-on: "id"

  - id: "estimate-id"
    attribute: "id"
    table: "estimates"
    all-foreign-keys:
      - table: "estimates"
        join-on: "id"

  - id: "invoice-id"
    attribute: "id"
    table: "invoices"
    all-foreign-keys:
      - table: "credit_notes"
      - table: "estimates"
      - table: "invoices"
        join-on: "id"
      - table: "transactions"

  - id: "line-item-id"
    attribute: "id"
    table: "credit_notes"
    all-foreign-keys:
      - table: "credit_notes"
        subtable: "items"
        join-on: "id"
      - table: "estimates"
        subtable: "items"
        join-on: "id"
      - table: "invoices"
        subtable: "items"
        join-on: "id"

  - id: "plan-id"
    attribute: "plan"
    table: ""
    all-foreign-keys:
      - table: "subscriptions"
      - table: "subscriptions"
        subtable: "addons"

  - id: "subscription-id"
    attribute: "subscription"
    table: "subscriptions"
    all-foreign-keys:
      - table: "invoices"
      - table: "subscriptions"
        join-on: "id"

  - id: "tax-id"
    attribute: "id"
    table: "credit_notes"
    all-foreign-keys:
      - table: "credit_notes"
        subtable: "items__taxes"
        join-on: "id"

      - table: "credit_notes"
        subtable: "taxes"
        join-on: "id"

      - table: "customers"
        subtable: "taxes"
        join-on: "id"

      - table: "estimates"
        subtable: "taxes"
        join-on: "id"

      - table: "estimates"
        subtable: "items__taxes"
        join-on: "id"

      - table: "subscriptions"
        subtable: "taxes"
        join-on: "id"

  - id: "transaction-id"
    attribute: "id"
    table: "transactions"
    all-foreign-keys:
      - table: "transactions"
        join-on: "id"
      - table: "transactions"
        join-on: "parent_transaction"
---