---
tap: "netsuite-suite-analytics"
version: "1"
key: "country"

name: "countries"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/countries.html"
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
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "country-id"

  - name: "name"
    type: "string"
    description: ""

  - name: "short_name"
    type: "string"
    description: ""
---