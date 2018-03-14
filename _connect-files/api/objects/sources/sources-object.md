---
content-type: "api-object"
endpoint: "sources"

title: "Source"
description: "{{ api.core-objects.sources.description }}"
endpoint-url: "/sources"
version: "4"

object-attributes:
  - name: "id"
    type: "integer"
    description: "The unique identifier for this source."

  - name: "created_at"
    type: "timestamp"
    description: "The time at which the source object was created."

  - name: "deleted_at"
    type: "timestamp"
    description: "The time at which the source object was deleted."

  - name: "display_name"
    type: "string"
    description: "The display name of the source connection."

  - name: "name"
    type: "string"
    description: "{{ connect.common.attributes.name }}"

  - name: "paused_at"
    type: "timestamp"
    description: "If the connection was paused by the user, the time the pause began. Otherwise, or if the connection is active, this will be null."

  - name: "properties"
    type: "object"
    sub-type: "properties"
    url: "{{ api.data-structures.properties.section }}"
    description: "{{ connect.common.attributes.properties | flatify }}"

  - name: "report_card"
    type: "object"
    sub-type: "report card"
    url: "{{ api.data-structures.report-cards.section }}"
    description: "A description of the source's configuration state."

  - name: "stitch_client_id"
    type: "integer"
    description: "The ID of the Stitch client account."

  - name: "system_paused_at"
    type: "timestamp"
    description: "If the connection was paused by the system, the time the pause began. Otherwise, or if the connection is active, this will be null."

  - name: "type"
    type: "string"
    description: "The source type."

  - name: "updated_at"
    type: "timestamp"
    description: "The time at which the object was last updated."
---