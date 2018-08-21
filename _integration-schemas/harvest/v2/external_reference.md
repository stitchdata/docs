---
tap: "harvest"
version: "2.0"

name: "external_references"
doc-link: 
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/external_reference.json
description: |
  The `{{ table.name }}` table contains info about external references.

replication-method: "Key-based Incremental"

api-method:
  name: 
  doc-link: 

attributes:
  - name: "id"
    type: "integer"
    description: "The ID of the external reference."
    foreign-key-id: "external-reference-id"

  - name: "task_id"
    type: "integer"
    description: "The ID of the task associated with the reference."
    foreign-key-id: "task-id"

  - name: "group_id"
    type: "integer"
    description: "The ID of the group associated with the reference."

  - name: "permalink"
    type: "string"
    description: "The permalink value associated with the reference."

  - name: "service"
    type: "string"
    description: "The name of the service associated with the reference."

  - name: "service_icon_url"
    type: "string"
    description: "The URL of the associated service's icon."
---