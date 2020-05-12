---
tap: "pepperjam"
version: "1"
key: "publisher"

name: "publisher"
doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#Publisher"
singer-schema: "https://github.com/singer-io/tap-pepperjam/blob/master/tap_pepperjam/schemas/publisher.json"
description: |
  The `{{ table.name }}` table contains information about the publishers, the publishers' status, and the publishers' term in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "getPublisher"
  doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#Publisher"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The publisher ID."
    #foreign-key-id: "publisher-id"

  - name: "category"
    type: "array"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""

      - name: "name"
        type: "string"
        description: ""
  - name: "company"
    type: "string"
    description: ""
  - name: "country"
    type: "string"
    description: ""
  - name: "first_name"
    type: "string"
    description: ""
  - name: "group"
    type: "array"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""
        foreign-key-id: "group-id"

      - name: "name"
        type: "string"
        description: ""
  - name: "join_date"
    type: "date-time"
    description: ""
  - name: "last_name"
    type: "string"
    description: ""
  - name: "promotional_method"
    type: "array"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""

      - name: "name"
        type: "string"
        description: ""
  - name: "request_date"
    type: "date-time"
    description: ""
  - name: "state"
    type: "string"
    description: ""
  - name: "status"
    type: "string"
    description: ""
  - name: "term"
    type: "array"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""
        foreign-key-id: "term-id"

      - name: "name"
        type: "string"
        description: ""
  - name: "transparency"
    type: "integer"
    description: ""
  - name: "website"
    type: "string"
    description: ""
---