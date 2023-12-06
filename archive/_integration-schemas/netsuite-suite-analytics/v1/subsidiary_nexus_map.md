---
tap: "netsuite-suite-analytics"
version: "1"
key: "subsidiary-nexus-map"

name: "subsidiary_nexus_map"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/subsidiary_nexus_map.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "nexus_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    # foreign-key-id: "nexus-id"

  - name: "subsidiary_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    # foreign-key-id: "subsidiary-id"
---