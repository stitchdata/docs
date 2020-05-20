---
tap: "pepperjam"
version: "1"
key: "transaction_history"

name: "transaction_history"
doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#TransactionHistory"
singer-schema: "https://github.com/singer-io/tap-pepperjam/blob/master/tap_pepperjam/schemas/transaction_history.json"
description: |
  The {{ table.name }} table contains all historical publisher transactions, within a 28-day time frame from the date of the last table replication, in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"
attribution-window: true

api-method:
    name: "getTransactionHistory"
    doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#TransactionHistory"
    
attributes:
  - name: "transaction_id"
    type: "integer"
    primary-key: true
    description: "The transaction ID."
    #foreign-key-id: "transaction-id"

  - name: "process_date"
    type: "date-time"
    primary-key: true
    description: "The date the transaction was processed."
    #foreign-key-id: "process-date-id"
    
  - name: "sale_date"
    type: "date-time"
    primary-key: true
    description: "The date the sale was made."
    replication-key: true
    #foreign-key-id: "sale-date-id"

  - name: "commission"
    type: "null"
    description: ""
  - name: "company"
    type: "string"
    description: ""
  - name: "group_id"
    type: "integer"
    description: ""
  - name: "item_id"
    type: "string"
    description: ""
  - name: "link_type"
    type: "string"
    description: ""
  - name: "order_id"
    type: "string"
    description: ""
  - name: "publisher"
    type: "string"
    description: ""
  - name: "publisher_commission"
    type: "null"
    description: ""
  - name: "publisher_id"
    type: "integer"
    description: ""
  - name: "publisher_type"
    type: "string"
    description: ""
  - name: "revision"
    type: "string"
    description: ""
  - name: "sale_amount"
    type: "null"
    description: ""
  - name: "site_commission"
    type: "null"
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
