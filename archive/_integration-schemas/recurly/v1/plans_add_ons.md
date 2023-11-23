---
tap: "recurly"
version: "1"

name: "plans_add_ons"
key: "plan-add-on"

doc-link: ""
singer-schema: "https://github.com/singer-io/tap-recurly/blob/master/tap_recurly/schemas/plans_add_ons.json"
description: |
  The `{{ table.name }}` table contains info about the add-ons in your {{ integration.display_name }} account. An add-on is a charge billed each billing period in addition to a subscription's base charge.

  **Note**: To replicate this table, you must also have the [`plans`](#plans) table set to replicate.

replication-method: "Key-based Incremental"
api-method:
    name: "List a plan's add-ons"
    doc-link: "https://partner-docs.recurly.com/v2018-08-09#operation/list_plan_add_ons"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The plan add-on ID."
    foreign-key-id: "plan-add-on-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The date and time the add-on was last updated."

  - name: "accounting_code"
    type: "string"
    description: "The accounting code for invoice line items for this add-on."

  - name: "code"
    type: "string"
    description: "The unique identifier for the add-on within its plan."

  - name: "created_at"
    type: "date-time"
    description: "The date and time the add-on was created."

  - name: "currencies"
    type: "array"
    description: "The currencies associated with the add-on."
    subattributes:
      - name: "currency"
        type: "string"
        description: "The three-letter ISO 4217 currency code."

      - name: "unit_amount"
        type: "number"
        description: "The unit price."

  - name: "default_quantity"
    type: "integer"
    description: "The default quantity for the hosted pages."

  - name: "deleted_at"
    type: "date-time"
    description: "The date and time the add-on was deleted."

  - name: "display_quantity"
    type: "boolean"
    description: "Determines if the quantity field is displayed on the hosted pages for the add-on."

  - name: "name"
    type: "string"
    description: "The add-on name."

  - name: "object"
    type: "string"
    description: ""

  - name: "plan_id"
    type: "string"
    description: "The ID of the plan the add-on is associated with."
    foreign-key-id: "plan-id"

  - name: "state"
    type: "string"
    description: |
      The state of the add-on. Possible values are:

      - `active`
      - `inactive`

  - name: "tax_code"
    type: "string"
    description: |
      Used by Avalara, Vertex, and Recurly’s EU VAT tax feature. The tax code values are specific to each tax system. If you are using Recurly’s EU VAT feature:

      - `P0000000` - Physical
      - `D0000000` - Digital
      - Empty string - Unknown
---