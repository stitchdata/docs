---
tap: "ringcentral"
version: "1.0"
key: ""

name: "company_call_log"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-ringcentral/blob/master/tap_ringcentral/schemas/company_call_log.json"
description: |
  The `{{ table.name }}` contains info about 

replication-method: "Key-based Incremental"

replication-key:
  name: "dateFrom : dateTo"

api-method:
    name: "Get Company Call Log Records"
    doc-link: "https://developers.ringcentral.com/api-reference#Call-Log-loadCompanyCallLog"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""

  - name: "_contact_id"
    type: "integer"
    description: ""

  - name: "action"
    type: "string"
    description: ""

  - name: "deleted"
    type: "anything"
    description: ""

  - name: "direction"
    type: "string"
    description: ""

  - name: "duration"
    type: "integer"
    description: ""

  - name: "extension"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""

      - name: "uri"
        type: "string"
        description: ""

  - name: "from"
    type: "object"
    description: ""
    subattributes:
      - name: "location"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "phoneNumber"
        type: "string"
        description: ""

  - name: "message"
    type: "anything"
    description: ""

  - name: "reason"
    type: "anything"
    description: ""

  - name: "reasonDescription"
    type: "anything"
    description: ""

  - name: "result"
    type: "string"
    description: ""

  - name: "sessionId"
    type: "string"
    description: ""

  - name: "startTime"
    type: "date-time"
    description: ""

  - name: "to"
    type: "object"
    description: ""
    subattributes:
      - name: "location"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "phoneNumber"
        type: "string"
        description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "uri"
    type: "string"
    description: ""
---