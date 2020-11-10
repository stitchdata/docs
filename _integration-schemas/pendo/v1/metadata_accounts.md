---
tap: "pendo"
version: "1"
key: "metadata-account"

name: "metadata_accounts"
doc-link: "https://developers.pendo.io/docs/?bash#metadata"
singer-schema: "https://github.com/singer-io/tap-pendo/blob/master/tap_pendo/schemas/metadata_accounts.json"
description: |
  The `{{ table.name }}` table contains info about the metadata schema used for account objects in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "Get a metadata schema (account)"
  doc-link: "https://developers.pendo.io/docs/?bash#get-a-metadata-schema"

attributes:
  - name: "auto"
    type: "object"
    description: ""
    subattributes:
      - name: "firstvisit"
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

      - name: "id"
        type: "object"
        description: ""
        subattributes: *attributes

      - name: "lastvisit"
        type: "object"
        description: ""
        subattributes: *attributes
---