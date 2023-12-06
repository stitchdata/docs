---
tap: "netsuite-suite-analytics"
version: "1"
key: "campaign-vertical"

name: "campaign_verticals"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/campaignvertical.html"
description: ""

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
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.

  - name: "campaignvertical_extid"
    type: "string"
    description: ""

  - name: "campaignvertical_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "campaign-vertical-id"

  - name: "description"
    type: "string"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""
---