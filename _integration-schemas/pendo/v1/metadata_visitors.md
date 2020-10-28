---
tap: "pendo"
version: "1"
key: "metadata-visitor"

name: "metadata_visitors"
doc-link: "https://developers.pendo.io/docs/?bash#metadata"
singer-schema: "https://github.com/singer-io/tap-pendo/blob/master/tap_pendo/schemas/metadata_visitors.json"
description: |
  The `{{ table.name }}` table contains info about the metadata schema used for visitor objects in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "Get a metadata schema (visitor)"
  doc-link: "https://developers.pendo.io/docs/?bash#get-a-metadata-schema"

attributes:
  - name: "agent"
    type: "null"
    description: ""

  - name: "auto"
    type: "object"
    description: ""
    subattributes:
      - name: "accountid"
        type: "object"
        description: ""
        subattributes: &attributes
          - name: "dirty"
            type: "boolean"
            description: ""

          - name: "display_name"
            type: "string"
            description: ""

          - name: "element_format"
            type: "string"
            description: ""

          - name: "element_type"
            type: "string"
            description: ""

          - name: "is_calculated"
            type: "boolean"
            description: ""

          - name: "is_deleted"
            type: "boolean"
            description: ""

          - name: "is_hidden"
            type: "boolean"
            description: ""

          - name: "is_per_app"
            type: "boolean"
            description: ""

          - name: "never_index"
            type: "boolean"
            description: ""

          - name: "type"
            type: "string"
            description: ""

      - name: "accountids"
        type: "object"
        description: ""
        subattributes: *attributes

      - name: "firstvisit"
        type: "object"
        description: ""
        subattributes: *attributes

      - name: "id"
        type: "object"
        description: ""
        subattributes: *attributes

      - name: "lastbrowsername"
        type: "object"
        description: ""
        subattributes: *attributes

      - name: "lastbrowserversion"
        type: "object"
        description: ""
        subattributes: *attributes

      - name: "lastoperatingsystem"
        type: "object"
        description: ""
        subattributes: *attributes

      - name: "lastservername"
        type: "object"
        description: ""
        subattributes: *attributes

      - name: "lastvisit"
        type: "object"
        description: ""
        subattributes: *attributes

  - name: "pendo"
    type: "object"
    description: ""
    subattributes:
      - name: "designerenabled"
        type: "object"
        description: ""
        subattributes: *attributes
---