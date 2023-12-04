---
tap: "netsuite-suite-analytics"
version: "1"
key: "campaign-offer"

name: "campaignoffer"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/campaignoffer.html"
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

  - name: "campaign_offer_extid"
    type: "string"
    description: ""

  - name: "campaign_offer_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "campaign-offer-id"

  - name: "description"
    type: "string"
    description: ""

  - name: "is_inactive"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""
---