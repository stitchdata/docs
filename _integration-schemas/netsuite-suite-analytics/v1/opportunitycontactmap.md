---
tap: "netsuite-suite-analytics"
version: "1"
key: "opportunity-contact-map"

name: "opportunitycontactmap"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/opportunitycontactmap.html"
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

  - name: "contact_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "contactrole_id"
    type: "integer"
    description: ""

  - name: "opportunity_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
---