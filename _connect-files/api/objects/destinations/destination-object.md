---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-object"
endpoint: "destinations"
order: 3


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Destination"
description: "{{ api.core-objects.destinations.description }}"
endpoint-url: "/destinations"


# -------------------------- #
#        VERSION INFO        #
# -------------------------- #

latest-version: "4"
versions:
  - number: "4"
    deprecated: false

  - number: "3"
    deprecated: false


# -------------------------- #
#      AVAILABLE METHODS     #
# -------------------------- #

available-methods:
  - id: "create-a-destination"
    title: "Create a destination"
    method: "post"
    short: "{{ api.core-objects.destinations.create.description | flatify }}"

  - id: "update-a-destination"
    title: "Update a destination"
    method: "put"
    short: "{{ api.core-objects.destinations.update.description | flatify }}"

  - id: "list-destinations"
    title: "List destinations"
    method: "get"
    short: "{{ api.core-objects.destinations.list.description | flatify }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "id"
    type: "integer"
    first-appeared-in: "3"
    description: "A unique identifier for this destination."

  - name: "connection"
    type: "object"
    sub-type: "destination form properties"
    url: "{{ api.form-properties.destination-forms.section }}"
    first-appeared-in: "3"
    deprecated-in: "4"
    description: |
      **Renamed in v4 of the Destinations endpoint.** Use `properties` instead.

  - name: "created_at"
    type: "timestamp"
    first-appeared-in: "3"
    description: "The time at which the destination object was created."

  - name: "deleted_at"
    type: "timestamp"
    first-appeared-in: "4"
    description: "The time at which the destination object was deleted."

  - name: "last_check"
    type: "object"
    sub-type: "connection check"
    url: "{{ api.data-structures.connection-checks.section }}"
    first-appeared-in: "3"
    deprecated-in: "4"
    description: |
      The status and results of the most recent check run for this destination connection.

      **Note**: This field has been deprecated in v4 of the Destinations endpoint. It will be removed at a future date.

  - name: "name"
    type: "string"
    first-appeared-in: "4"
    description: "The name for the destination."

  - name: "paused_at"
    type: "timestamp"
    first-appeared-in: "4"
    description: "If the connection was paused by the user, the time the pause began. Otherwise, or if the connection is active, this will be null."

  - name: "properties"
    type: "object"
    sub-type: "destination form properties"
    url: "{{ api.form-properties.destination-forms.section }}"
    first-appeared-in: "4"
    description: |
      Parameters for connecting to the destination, excluding any sensitive credentials.

      The parameters must adhere to the `type` of destination.

  - name: "report_card"
    type: "object"
    sub-type: "destination report card"
    url: "{{ api.data-structures.report-cards.destination.section }}"
    first-appeared-in: "4"
    description: |
      The Report Card object corresponding to the destination's `type`. For example: `postgres` or `redshift`.

  - name: "stitch_client_id"
    type: "integer"
    first-appeared-in: "4"
    description: "The ID of the Stitch client account."

  - name: "system_paused_at"
    type: "timestamp"
    first-appeared-in: "4"
    description: "If the connection was paused by the system, the time the pause began. Otherwise, or if the connection is active, this will be null."

  - name: "type"
    type: "string"
    description: "{{ connect.common.attributes.destination-type | flatify }}"

  - name: "updated_at"
    type: "timestamp"
    description: "The time at which the destination object was last updated."
---