---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
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

  - name: "display_name"
    type: "string"
    description: "The display name of the destination."
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
      Parameters for connecting to the destination, excluding any sensitive credentials. The parameters must adhere to the `type` of destination.

      **Note**: When included in responses, this object will contain the current values for the destination's form properties. If an optional property (`is_required: false`) has not been provided, it will not be present in this object.

  - name: "report_card"
    type: "object"
    sub-type: "destination report card"
    url: "{{ api.data-structures.report-cards.destination.section }}"
    description: |
      The Report Card object corresponding to the destination's `type`. For example: `postgres` or `redshift`.

  - name: "stitch_client_id"
    type: "integer"
    description: "The ID of the Stitch client account associated with the destination."
    example-value: |
      7723

  - name: "system_paused_at"
    type: "timestamp"
    description: "If the connection was paused by the system, the time the pause began. Otherwise, or if the connection is active, this will be null."
    example-value: |
      null


# -------------------------- #
#           EXAMPLES         #
# -------------------------- #

examples:
  - code: |
      {
        "properties": {
          "database": "demni2mf59dt10",
          "encryption_type": "none",
          "host": "<HOST>",
          "port": "5432",
          "ssl": "true",
          "status": "1",
          "username": "stitch"
        },
        "updated_at": "2019-05-24T18:04:08Z",
        "name": "Default Warehouse",
        "type": "postgres",
        "deleted_at": null,
        "system_paused_at": null,
        "stitch_client_id": 116078,
        "paused_at": null,
        "id": 155582,
        "display_name": null,
        "created_at": "2019-05-24T18:03:50Z",
        "report_card": {
          "type": "postgres",
          "current_step": 2,
          "current_step_type": "fully_configured",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "database",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": true
                },
                {
                  "name": "encryption_host",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "anyOf": [
                      {
                        "type": "string",
                        "format": "ipv4"
                      },
                      {
                        "type": "string",
                        "format": "ipv6"
                      },
                      {
                        "type": "string",
                        "format": "hostname"
                      }
                    ]
                  },
                  "provided": false
                },
                {
                  "name": "encryption_port",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+$"
                  },
                  "provided": false
                },
                {
                  "name": "encryption_type",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(ssh|none)$"
                  },
                  "provided": true
                },
                {
                  "name": "encryption_username",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                },
                {
                  "name": "host",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "anyOf": [
                      {
                        "type": "string",
                        "format": "ipv4"
                      },
                      {
                        "type": "string",
                        "format": "ipv6"
                      },
                      {
                        "type": "string",
                        "format": "hostname"
                      }
                    ]
                  },
                  "provided": true
                },
                {
                  "name": "password",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": true
                },
                {
                  "name": "port",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+$"
                  },
                  "provided": true
                },
                {
                  "name": "ssl",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "boolean"
                  },
                  "provided": true
                },
                {
                  "name": "sslrootcert",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                },
                {
                  "name": "username",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": true
                }
              ]
            },
            {
              "type": "fully_configured",
              "properties": []
            }
          ]
        }
      }
---