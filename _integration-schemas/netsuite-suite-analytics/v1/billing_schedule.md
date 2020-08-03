---
tap: "netsuite-suite-analytics"
version: "1"
key: "billing-schedule"

name: "billing_schedule"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/billingschedule.html"
description: |
  The `{{ table.name }}` table contains info about the billing schedules in your NetSuite account.

replication-method: "Full Table"
loading-behavior: "Append-Only"

attributes:
  - name: "bill_amount"
    type: "number"
    description: "The bill amount."

  - name: "bill_amount_foreign"
    type: "number"
    description: "The foreign currency bill amount."

  - name: "bill_count"
    type: "number"
    description: "The bill count."

  - name: "bill_date"
    type: "date-time"
    description: "The date of the bill."

  - name: "bill_net_amount"
    type: "integer"
    description: "The bill net amount."

  - name: "bill_net_amount_foreign"
    type: "integer"
    description: "The bill net amount in foreign currency."

  - name: "milestone_id"
    type: "integer"
    description: "The milestone ID."

  - name: "payment_terms_id"
    type: "integer"
    description: "The payment term ID."
    # foreign-key-id: "payment-term-id"

  - name: "rev_rec_end_date"
    type: "date-time"
    description: "The rev rec end date."

  - name: "rev_rec_start_date"
    type: "date-time"
    description: "The rev rec start date."

  - name: "transaction_id"
    type: "integer"
    description: "The transaction ID."
    # foreign-key-id: "transaction-id"

  - name: "transaction_line_id"
    type: "integer"
    description: "The transaction line ID."
---