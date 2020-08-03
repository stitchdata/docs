---
tap: "harvest"
version: "2"

name: "invoice_line_items"
doc-link: https://help.getharvest.com/api-v2/invoices-api/invoices/invoices#the-invoice-line-item-object
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/invoice_line_items.json
description: |
  The `{{ table.name }}` table contains info about the line items contained in invoices.

  **Note**: This table is updated based on new and updated `invoices`. This means that when an invoice is updated, this table will also be updated.

replication-method: "Key-based Incremental"

replication-key:
  name: "updated_at"
  ## This is replicated as part of the parent table, invoices

api-method:
  name: List all invoices
  doc-link: https://help.getharvest.com/api-v2/invoices-api/invoices/invoices#list-all-invoices

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The invoice line item ID."
    # foreign-key-id: "invoice-line-item-id"

  - name: "amount"
    type: "number"
    description: "The line item subtotal, calculated as `quantity * unit_price`."

  - name: "description"
    type: "string"
    description: "The description of the line item."

  - name: "invoice_id"
    type: "integer"
    description: "The ID of the invoice containing the line item."
    foreign-key-id: "invoice-id"

  - name: "kind"
    type: "string"
    description: "The name of the invoice item category associated with the item."

  - name: "project_id"
    type: "integer"
    description: "The ID of the project associated with the item."
    foreign-key-id: "project-id"

  - name: "quantity"
    type: "integer"
    description: "The unit quantity of the item."

  - name: "taxed"
    type: "boolean"
    description: "If `true`, the invoice's `tax` percentage applies to this line item."

  - name: "taxed2"
    type: "boolean"
    description: "If `true`, the invoice's `tax2` percentage applies to this line item."

  - name: "unit_price"
    type: "number"
    description: "The individual price per unit."
---