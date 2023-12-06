---
tap: "netsuite-suite-analytics"
version: "1"
key: "state"

name: "states"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/state.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "country_id"
    type: "integer"
    description: ""
    foreign-key-id: "country-id"

  - name: "name"
    type: "string"
    description: ""

  - name: "short_name"
    type: "string"
    description: ""

  - name: "state_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
---