---
tap: "kustomer"
version: "1"

name: "tags"
doc-link: "https://dev.kustomer.com/v1/tags/"
singer-schema: "https://github.com/singer-io/tap-kustomer/blob/master/tap_kustomer/schemas/tags.json"
description: |
  The {{ table.name }} contains information about tags in the {{ integration.name }} app.

replication-method: "Key-based Incremental"

api-method:
    name: "getTags"
    doc-link: "https://dev.kustomer.com/v1/tags/NWydnz3xaPBWCePQp"
    
attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The tag ID."
    #foreign-key-id: "tag-id"

  - name: "updated_at"
    type: "date-time"
    description: "The last time the tag was updated."

  - name: "color"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "created_by"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "string"
        description: ""
      - name: "type"
        type: "string"
        description: ""

  - name: "deleted"
    type: "boolean"
    description: ""

  - name: "links"
    type: "object"
    description: ""
    subattributes:
      - name: "self"
        type: "string"
        description: ""

  - name: "modified_at"
    type: "string"
    description: ""

  - name: "modified_by"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "string"
        description: ""
      - name: "type"
        type: "string"
        description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "org"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "string"
        description: ""
      - name: "type"
        type: "string"
        description: ""

  - name: "type"
    type: "string"
    description: ""
---
