---
content-type: "api-object"
endpoint: "destinations"
order: 3

title: "Destination"
description: "{{ api.core-objects.destinations.description }}"
endpoint-url: "/destinations"
version: "3"

object-attributes:
  - name: "id"
    type: "integer"
    description: "A unique identifier for this destination."

  - name: "connection"
    type: "object"
    sub-type: "destination form properties"
    url: "{{ api.form-properties.destination-forms.section }}"
    description: |
      Parameters for connecting to the destination, excluding any sensitive credentials.

      The parameters must adhere to the `type` of destination.

  - name: "created_at"
    type: "timestamp"
    description: "The time at which the destination object was created."

  - name: "last_check"
    type: "object"
    sub-type: "connection check"
    url: "{{ api.data-structures.connection-checks.section }}"
    description: "The status and results of the most recent check run for this destination connection."

  - name: "type"
    type: "string"
    description: "{{ connect.common.attributes.destination-type }}"

  - name: "updated_at"
    type: "timestamp"
    description: "The time at which the destination object was last updated."
---