---
tap: "netsuite-suite-analytics"
version: "1"
key: "nexus"

name: "nexus"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/nexus.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "country"
    type: "string"
    description: ""

  - name: "date_valid_since"
    type: "date-time"
    description: ""

  - name: "date_valid_until"
    type: "date-time"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "hierarchy_level"
    type: "integer"
    description: ""

  - name: "is_inactive"
    type: "string"
    description: ""

  - name: "is_tax_date_from_fulfillment"
    type: "string"
    description: ""

  - name: "nexus_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "parent_id"
    type: "integer"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "tax_agency_id"
    type: "integer"
    description: ""

  - name: "taxcode_id"
    type: "integer"
    description: ""

  - name: "vendtax1_id"
    type: "integer"
    description: ""

  - name: "vendtax2_id"
    type: "integer"
    description: ""
---