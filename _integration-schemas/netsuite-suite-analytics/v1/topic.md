---
tap: "netsuite-suite-analytics"
version: "1"
key: "topic"

name: "topic"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/topic.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "description"
    type: "string"
    description: ""

  - name: "is_inactive"
    type: "string"
    description: ""

  - name: "long_description"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "parent_topic_id"
    type: "integer"
    description: ""

  - name: "topic_extid"
    type: "string"
    description: ""

  - name: "topic_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
---