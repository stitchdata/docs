---
tap: "impact"
version: "1"
key: "phone-number"

name: "phone_numbers"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-impact/blob/master/tap_impact/schemas/phone_numbers.json"
description: |
  The `{{ table.name }}` table contains info about phone numbers.

replication-method: "Full Table"

api-method:
  name: "Get phone numbers"
  doc-link: "https://developer.impact.com/default#operations-Phone_Numbers-GetPhoneNumbers"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "phone-number-id"

  - name: "country"
    type: "string"
    description: ""

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "international_number"
    type: "string"
    description: ""

  - name: "last_date_assigned"
    type: "date-time"
    description: ""

  - name: "last_date_released"
    type: "date-time"
    description: ""

  - name: "number"
    type: "string"
    description: ""

  - name: "uri"
    type: "string"
    description: ""
---