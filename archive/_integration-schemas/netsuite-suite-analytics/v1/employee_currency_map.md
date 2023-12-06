---
tap: "netsuite-suite-analytics"
version: "1"
key: "employee-currency-map"

name: "employee_currency_map"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/employee_currency_map.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "currency_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "currency-id"

  - name: "employee_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "employee-id"
---