---
tap: "deputy"
version: "1"
key: "sms-log"

name: "sms_logs"
doc-link: "https://www.deputy.com/api-doc/Resources/SmsLog"

description: |
  The `{{ table.name }}` table contains info about SMS logs.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The SMS log ID."
    #foreign-key-id: "sms-log-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the SMS log was last modified."

  - name: "Destination"
    type: "string"
    description: ""

  - name: "Message"
    type: "string"
    description: ""

  - name: "Count"
    type: "integer"
    description: ""

  - name: "SmsId"
    type: "string"
    description: ""

  - name: "DeliveryReport"
    type: "string"
    description: ""

  - name: "Creator"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Created"
    type: "date-time"
    description: ""
---