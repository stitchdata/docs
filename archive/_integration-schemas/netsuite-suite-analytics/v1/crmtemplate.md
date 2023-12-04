---
tap: "netsuite-suite-analytics"
version: "1"
key: "crm-template"

name: "crmtemplate"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/crmtemplate.html"
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

  - name: "crmtemplate_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "crm-template-id"

  - name: "crmtemplate_modified_by"
    type: "integer"
    description: ""

  - name: "crmtemplate_record_type"
    type: "string"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "from_email"
    type: "string"
    description: ""

  - name: "is_inactive"
    type: "string"
    description: ""

  - name: "is_private"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "owner_id"
    type: "integer"
    description: ""

  - name: "reply_email_address"
    type: "string"
    description: ""

  - name: "subject"
    type: "string"
    description: ""
---