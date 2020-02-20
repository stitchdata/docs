---
tap: "deputy"
version: "1"
key: "kiosk"

name: "kiosks"
doc-link: "https://www.deputy.com/api-doc/Resources/Kiosk"

description: |
  The `{{ table.name }}` table contains info about kiosks.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The kiosk ID."
    #foreign-key-id: "kiosk-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the kiosk was last modified."

  - name: "Name"
    type: "string"
    description: ""

  - name: "InstallationId"
    type: "string"
    description: ""

  - name: "Company"
    type: "integer"
    description: ""
    foreign-key-id: "company-id"

  - name: "ConnectionMode"
    type: "integer"
    description: ""

  - name: "SubnetRestriction"
    type: "string"
    description: ""

  - name: "AuthenticationMode"
    type: "integer"
    description: ""

  - name: "UseBiometric"
    type: "boolean"
    description: ""

  - name: "LastActivity"
    type: "string"
    description: ""

  - name: "IpAddress"
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