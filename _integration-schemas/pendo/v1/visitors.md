---
tap: "pendo"
version: "1"
key: "visitor"

name: "visitors"
doc-link: "https://developers.pendo.io/docs/?bash#visitor"
singer-schema: "https://github.com/singer-io/tap-pendo/blob/master/tap_pendo/schemas/visitors.json"
description: |
  The `{{ table.name }}` table contains info about the visitors recorded in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Aggregation"
  doc-link: "https://api/v1/aggregation"

attributes:
  - name: "visitor_id"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "visitor-id"

  - name: "lastupdated"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "metadata_agent"
    type: "object"
    description: ""
    subattributes:
      - name: "email"
        type: "string"
        description: ""

      - name: "ipaddress"
        type: "string"
        description: ""

      - name: "language"
        type: "string"
        description: ""

  - name: "metadata_auto"
    type: "object"
    description: ""
    subattributes:
      - name: "accountid"
        type: "string"
        description: ""
        foreign-key-id: "account-id"

      - name: "accountids"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""
            foreign-key-id: "account-id"

      - name: "firstvisit"
        type: "date-time"
        description: ""

      - name: "id"
        type: "string"
        description: ""

      - name: "idhash"
        type: "integer"
        description: ""

      - name: "lastbrowsername"
        type: "string"
        description: ""

      - name: "lastbrowserversion"
        type: "string"
        description: ""

      - name: "lastoperatingsystem"
        type: "string"
        description: ""

      - name: "lastservername"
        type: "string"
        description: ""

      - name: "lastupdated"
        type: "date-time"
        description: ""

      - name: "lastuseragent"
        type: "string"
        description: ""

      - name: "lastvisit"
        type: "date-time"
        description: ""

      - name: "nid"
        type: "integer"
        description: ""
---