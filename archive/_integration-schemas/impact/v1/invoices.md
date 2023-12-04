---
tap: "impact"
version: "1"
key: "invoice"

name: "invoices"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-impact/blob/master/tap_impact/schemas/invoices.json"
description: |
  The `{{ table.name }}` table contains info about the invoices in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get invoices"
  doc-link: "https://developer.impact.com/default#operations-Invoices-GetInvoices"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "invoice-id"

  - name: "created_date"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "currency"
    type: "string"
    description: ""

  - name: "line_items"
    type: "array"
    description: ""
    subattributes:
      - name: "actions"
        type: "integer"
        description: ""

      - name: "campaign_id"
        type: "integer"
        description: ""
        foreign-key-id: "campaign-id"

      - name: "campaign_name"
        type: "string"
        description: ""

      - name: "description"
        type: "string"
        description: ""

      - name: "due_date"
        type: "date-time"
        description: ""

      - name: "event_month_year"
        type: "string"
        description: ""

      - name: "net_item_amount"
        type: "number"
        description: ""

      - name: "paid_date"
        type: "date-time"
        description: ""

      - name: "status"
        type: "string"
        description: ""

      - name: "total_item_amount"
        type: "number"
        description: ""

      - name: "vat_item_amount"
        type: "number"
        description: ""

  - name: "media_id"
    type: "integer"
    description: ""
    foreign-key-id: "media-id"

  - name: "media_name"
    type: "string"
    description: ""

  - name: "pdf"
    type: "string"
    description: ""

  - name: "total_amount"
    type: "number"
    description: ""

  - name: "total_vat_amount"
    type: "number"
    description: ""
---