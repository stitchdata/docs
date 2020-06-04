---
tap: "netsuite-suite-analytics"
version: "1"
key: "campaign-subscription-status"

name: "campaign_subscription_statuses"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/campaign_subscription_statuses.html"
description: |
  {{ integration.netsuite-replication-keys | flatify }}

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

  - name: "last_modified_date"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.

  - name: "entity_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "entity-id"

  - name: "subscription_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "campaign-subscription-id"

  - name: "unsubscribed"
    type: "string"
    description: ""
---