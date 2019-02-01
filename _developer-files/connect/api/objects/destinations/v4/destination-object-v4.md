---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

type: "connect"
content-type: "api-version-object"
endpoint: "destinations"

# -------------------------- #
#        VERSION INFO        #
# -------------------------- #

version: "4"

# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "deleted_at"
    type: "timestamp"
    description: "The time at which the destination object was deleted."
    example-value: |
      null

  - name: "name"
    type: "string"
    description: "The name for the destination."
    example-value: |
      "Default Warehouse"

  - name: "paused_at"
    type: "timestamp"
    description: "If the connection was paused by the user, the time the pause began. Otherwise, or if the connection is active, this will be null."
    example-value: |
      null

  - name: "properties"
    type: "object"
    sub-type: "destination form properties"
    url: "{{ api.form-properties.destination-forms.section }}"
    description: |
      Parameters for connecting to the destination, excluding any sensitive credentials.

      The parameters must adhere to the `type` of destination.

  - name: "report_card"
    type: "object"
    sub-type: "destination report card"
    url: "{{ api.data-structures.report-cards.destination.section }}"
    description: |
      The Report Card object corresponding to the destination's `type`. For example: `postgres` or `redshift`.

  - name: "stitch_client_id"
    type: "integer"
    description: "The ID of the Stitch client account."
    example-value: |
      7723

  - name: "system_paused_at"
    type: "timestamp"
    description: "If the connection was paused by the system, the time the pause began. Otherwise, or if the connection is active, this will be null."
    example-value: |
      null
---