---
tap: "pepperjam"
version: "1"
key: "transaction_history"

name: "transaction_history"
doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#TransactionHistory"
singer-schema: "https://github.com/singer-io/tap-pepperjam/blob/master/tap_pepperjam/schemas/transaction_history.json"
description: |
  The `{{ table.name }}` table contains all historical publisher transactions, within a given year, in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "getTransactionHistory"
  doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#TransactionHistory"
    
attributes:
  - name: "transaction_id"
    type: "integer"
    primary-key: true
    description: "The transaction ID."
    foreign-key-id: "transaction-id"

  - name: "process_date"
    type: "date-time"
    primary-key: true
    description: "The date the transaction was processed."
    
  - name: "sale_date"
    type: "date-time"
    primary-key: true
    description: "The date the sale was made."
    replication-key: true

  - name: "commission"
    type: "number"
    description: ""
  - name: "company"
    type: "string"
    description: ""
  - name: "group_id"
    type: "integer"
    description: ""
    foreign-key-id: "group-id"
  - name: "item_id"
    type: "string"
    description: ""
  - name: "link_type"
    type: "string"
    description: ""
  - name: "order_id"
    type: "string"
    description: ""
    foreign-key-id: "order-id"
  - name: "publisher"
    type: "string"
    description: ""
  - name: "publisher_commission"
    type: "number"
    description: ""
  - name: "publisher_id"
    type: "integer"
    description: ""
    foreign-key-id: "publisher-id"
  - name: "publisher_type"
    type: "string"
    description: ""
  - name: "revision"
    type: "string"
    description: ""
  - name: "sale_amount"
    type: "number"
    description: ""
  - name: "site_commission"
    type: "number"
    description: ""
  - name: "status"
    type: "string"
    description: ""
  - name: "transaction_type"
    type: "string"
    description: ""
  - name: "website_url"
    type: "string"
    description: ""
---