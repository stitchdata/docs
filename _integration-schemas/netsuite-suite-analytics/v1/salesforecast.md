---
tap: "netsuite-suite-analytics"
version: "1"
key: "sales-forecast"

name: "salesforecast"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/salesforecast.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "calculated_amount"
    type: "number"
    description: ""

  - name: "date_entered"
    type: "date-time"
    description: ""

  - name: "forecast_amount"
    type: "number"
    description: ""

  - name: "forecast_date"
    type: "date-time"
    description: ""

  - name: "forecast_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "high_calculated_amount"
    type: "number"
    description: ""

  - name: "high_forecasted_amount"
    type: "number"
    description: ""

  - name: "is_alt_sales"
    type: "string"
    description: ""

  - name: "low_calculated_amount"
    type: "number"
    description: ""

  - name: "low_forecasted_amount"
    type: "number"
    description: ""

  - name: "manager_override"
    type: "string"
    description: ""

  - name: "modified_by_id"
    type: "integer"
    description: ""

  - name: "pipeline_amount"
    type: "number"
    description: ""

  - name: "salesrep_id"
    type: "integer"
    description: ""

  - name: "subsidiary"
    type: "integer"
    description: ""

  - name: "team_forecast"
    type: "string"
    description: ""
---