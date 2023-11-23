---
tap: "asana"
version: "2"
key: "workspace"

name: "workspaces"
doc-link: "https://asana.com/developers/api-reference/workspaces"
singer-schema: "https://github.com/singer-io/tap-asana/blob/master/tap_asana/schemas/workspaces.json"
description: |
  The `{{ table.name }}` table contains info about the workspaces associated with your {{ integration.display_name }} account.

replication-method: "Full Table"

attributes:
  - name: "email_domains"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""


  - name: "email_domains"
    type: "null"
    description: ""


  - name: "gid"
    type: "string"
    description: ""
    primary-key: true

  - name: "is_organization"
    type: "boolean"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "resource_type"
    type: "string"
    description: ""


---