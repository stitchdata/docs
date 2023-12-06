---
tap: "netsuite-suite-analytics"
version: "1"
key: "accounting-period"

name: "accounting_periods"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/accountingperiod.html"
description: |
  The `{{ table.name }}` table contains info about accounting periods.

replication-method: "Key-based Incremental"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: "The time the accounting period was last modified."

  - name: "accounting_period_id"
    type: "integer"
    netsuite-primary-key: true
    description: "The accounting period ID. {{ integration.netsuite-primary-key-description | flatify }}"
    foreign-key-id: "accounting-period-id"

  - name: "closed"
    type: "string"
    description: "Indicates whether the period is closed."

  - name: "closed_accounts_payable"
    type: "string"
    description: "Whether the period is closed for accounts payable."

  - name: "closed_accounts_receivable"
    type: "string"
    description: "Whether the period is closed for accounts receivable."

  - name: "closed_all"
    type: "string"
    description: "Whether the period is closed for all."

  - name: "closed_on"
    type: "date-time"
    description: "The date the period was closed."

  - name: "closed_payroll"
    type: "string"
    description: "Whether the period is closed for payroll."

  - name: "ending"
    type: "date-time"
    description: "The end date for the period."

  - name: "fiscal_calendar_id"
    type: "integer"
    description: "The fiscal calendar for the period."

  - name: "full_name"
    type: "string"
    description: "The full name of the period."

  - name: "is_adjustment"
    type: "string"
    description: "Whether the period is an adjustment period."

  - name: "isinactive"
    type: "string"
    description: "Whether the period is inactive."

  - name: "locked_accounts_payable"
    type: "string"
    description: "Whether accounts payable is locked for the period."

  - name: "locked_accounts_receivable"
    type: "string"
    description: "Whether accounts receivable is locked for the period."

  - name: "locked_all"
    type: "string"
    description: "Whether all are locked for the period."

  - name: "locked_payroll"
    type: "string"
    description: "Whether payroll is locked for the period."

  - name: "name"
    type: "string"
    description: "The name of the period."

  - name: "parent_id"
    type: "integer"
    description: "The parent accounting period."
    foreign-key-id: "accounting-period-id"

  - name: "quarter"
    type: "string"
    description: "Whether the period is a quarter."
  
  - name: "starting"
    type: "date-time"
    description: "The start date of the period."

  - name: "year_0"
    type: "string"
    description: ""

  - name: "year_id"
    type: "integer"
    description: "The year of the accounting period."
    foreign-key-id: "accounting-period-id"
---