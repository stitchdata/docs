---
tap-reference: "xero"
version: "1.0"

name: "allocations"
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/allocations.json

attributes:
  - name: "Date"
    type: "date-time"
    description: |
      The date the {{ table.name | append: " " | remove: "s " | replace: "_", " " }} was applied.

  - name: "Amount"
    type: "number"
    description: "The amount being applied to the invoice."

  - name: "Invoice"
    type: "object"
    description: |
      Details about the invoices the {{ table.name | append: " " | remove: "s " | replace: "_", " " }} has been allocated against.
    object-attributes:
      - name: "InvoiceID"
        type: "string"
        description: |
          The ID of the invoice the {{ table.name | append: " " | remove: "s " | replace: "_", " " }} is being allocated against.
        foreign-key: true
---