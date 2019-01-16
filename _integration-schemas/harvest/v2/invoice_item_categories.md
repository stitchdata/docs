---
tap: "harvest"
version: "2.0"

name: "invoice_item_categories"
doc-link: https://help.getharvest.com/api-v2/invoices-api/invoices/invoice-item-categories/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/invoice_item_categories.json
description: |
  The `{{ table.name }}` table contains info about the various categories that can be applied to invoice line items.

  **Note**: Harvest includes two non-removable categories by default for the hours and expenses you bill.

replication-method: "Key-based Incremental"
api-method:
  name: List all invoice item categories
  doc-link: http://help.getharvest.com/api-v1/invoices-api/invoices/invoice-messages-payments/#show-all-categories

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the invoice item category."
    # foreign-key-id: "invoice-item-categories"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The last time the invoice item category was updated."

  - name: "name"
    type: "string"
    description: "The name of the invoice item category."

  - name: "created_at"
    type: "date-time"
    description: "The time the invoice item category was created."

  - name: "use_as_service"
    type: "boolean"
    description: "Indicates if the invoice item category is used as a service."

  - name: "use_as_expense"
    type: "boolean"
    description: "Indicates if the invoice item category is used as an expense."
---