---
tap: "netsuite-suite-analytics"
version: "1"
key: "consolidated-exchange-rate"

name: "consolidated_exchange_rates"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/consolidatedexchangerate.html"
description: |
  The `{{ table.name }}` table contains info about consolidated exchange rates. This is used in {{ integration.display_name }} OneWorld for consolidation purposes, ensuring currency amounts correctly roll up from child to parent subsidiaries.

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "consolidated_exchange_rate_id"
    type: "integer"
    netsuite-primary-key: true
    description: "The consolidated exchange rate ID. {{ integration.netsuite-primary-key-description | flatify }}"
    foreign-key-id: "consolidated-exchange-rate-id"

  - name: "accounting_book_id"
    type: "integer"
    description: ""


  - name: "accounting_period_id"
    type: "integer"
    description: "The accounting period."
    foreign-key-id: "accounting-period-id"

  - name: "average_budget_rate"
    type: "number"
    description: "The average budget exchange rate."

  - name: "average_rate"
    type: "number"
    description: "The average actual exchange rate."

  - name: "current_budget_rate"
    type: "number"
    description: "The current budget exchange rate."

  - name: "current_rate"
    type: "number"
    description: "The current actual exchange rate."

  - name: "from_subsidiary_id"
    type: "integer"
    description: "The originating subsidiary."
    foreign-key-id: "subsidiary-id"

  - name: "historical_budget_rate"
    type: "number"
    description: "The historical budget rate."

  - name: "historical_rate"
    type: "number"
    description: "The historical actual exchange rate."

  - name: "to_subsidiary_id"
    type: "integer"
    description: "The receiving subsidiary."
    foreign-key-id: "subsidiary-id"
---