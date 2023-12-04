---
tap: "asana"
version: "2"
key: "user"

name: "users"
doc-link: "https://asana.com/developers/api-reference/users"
singer-schema: "https://github.com/singer-io/tap-asana/blob/master/tap_asana/schemas/users.json"
description: |
  The `{{ table.name }}` table contains info about the users in your {{ integration.display_name }} account.

replication-method: "Full Table"

attributes:
  - name: "email"
    type: "string"
    description: ""

  - name: "gid"
    type: "string"
    description: ""
    primary-key: true

  - name: "name"
    type: "string"
    description: ""

  - name: "photo"
    type: "object"
    description: ""
    subattributes:
    - name: "image_21x21"
      type: "string"
      description: ""

    - name: "image_27x27"
      type: "string"
      description: ""

    - name: "image_36x36"
      type: "string"
      description: ""

    - name: "image_60x60"
      type: "string"
      description: ""

    - name: "image_128x128"
      type: "string"
      description: ""

    - name: "image_1024x1024"
      type: "string"
      description: ""


  - name: "resource_type"
    type: "string"
    description: ""

  - name: "workspaces"
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



---