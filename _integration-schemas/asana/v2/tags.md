---
tap: "asana"
version: "2"
key: "tag"

name: "tags"
doc-link: "https://asana.com/developers/api-reference/tags"
singer-schema: "https://github.com/singer-io/tap-asana/blob/master/tap_asana/schemas/tags.json"
description: |
  The `{{ table.name }}` table contains info about the tags in your {{ integration.display_name }} account. A tag is a label that can be attached to any task in Asana.

replication-method: "Key-based Incremental"

attributes:
  - name: "color"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""
    replication-key: true

  - name: "followers"
    type: "array"
    description: ""
    subattributes:
    - name: "gid"
      type: "string"
      description: ""

    - name: "resource_type"
      type: "string"
      description: ""

    - name: "name"
      type: "string"
      description: ""


  - name: "gid"
    type: "string"
    description: ""
    primary-key: true

  - name: "name"
    type: "string"
    description: ""

  - name: "notes"
    type: "string"
    description: ""

  - name: "permalink_url"
    type: "string"
    description: ""

  - name: "resource_type"
    type: "string"
    description: ""

  - name: "workspace"
    type: "object"
    description: ""
    subattributes:
    - name: "gid"
      type: "string"
      description: ""

    - name: "resource_type"
      type: "string"
      description: ""

    - name: "name"
      type: "string"
      description: ""



---