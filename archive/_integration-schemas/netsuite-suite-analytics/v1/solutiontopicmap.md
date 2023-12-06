---
tap: "netsuite-suite-analytics"
version: "1"
key: "solution-topic-map"

name: "solutiontopicmap"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/solutiontopicmap.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "solution_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "topic_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
---