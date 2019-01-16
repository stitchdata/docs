---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

content-type: "api-endpoint"
endpoint: "destinations"
key: "create-a-destination"
version: "4"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Create a destination"
method: "post"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.destinations.create.short }}"
description: "{{ api.core-objects.destinations.create.description | flatify }}"


# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

arguments:
  - name: "type"
    required: true
    type: "string"
    description: "{{ connect.common.attributes.destination-type | flatify }}"

  - name: "properties"
    required: true
    type: "object"
    description: "A [Destination Form Properties object]({{ api.form-properties.destination-forms.section }}) corresponding to the value of `type`."


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of `200 OK` and a [Destination object]({{ api.core-objects.destinations.object }}) with a `report_card` property.

  The `report_card` property contains the [Destination Report Card object]({{ api.data-structures.report-cards.destination.section }}) for the destination's configuration status.


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    language: "json"
    subexamples:
      - title: "Create a PostgreSQL destination"
        code: |
          curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip_newlines }}
               -H "Authorization: Bearer <ACCESS_TOKEN>" 
               -H "Content-Type: application/json"
               -d "{
                    "type":"postgres",
                    "properties": {
                      "host":"<HOST>",
                      "port":5432,
                      "username":"<USERNAME>",
                      "database":"<DATABASE>",
                      "password":"<PASSWORD>",
                      "ssl":false
                      }
                   }"


  - type: "Response"
    language: "json"
    subexamples:
      - title: "PostgreSQL destination response"
        code: |
          {
            "properties": {
              "database": "<DATABASE>",
              "host": "<HOST>",
              "port": "5432",
              "username": "<USERNAME>"
            },
            "updated_at": "2019-01-09T22:16:23Z",
            "check_job_name": null,
            "name": "Default Warehouse",
            "type": "postgres",
            "deleted_at": null,
            "system_paused_at": null,
            "stitch_client_id": <CLIENT_ID>,
            "paused_at": null,
            "id": <DESTINATION_ID>,
            "created_at": "2019-01-09T22:16:23Z",
            "report_card": {
              "type": "postgres",
              "current_step": 1,
              "steps": [
                {
                  "type": "form",
                  "properties": [
                    {
                      "name": "database",
                      "is_required": true,
                      "provided": true,
                      "is_credential": false,
                      "system_provided": false,
                      "json_schema": {
                        "type": "string"
                      }
                    },
                    {
                      "name": "encryption_host",
                      "is_required": false,
                      "provided": false,
                      "is_credential": false,
                      "system_provided": false,
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
                      }
                    },
                    {
                      "name": "encryption_port",
                      "is_required": false,
                      "provided": false,
                      "is_credential": false,
                      "system_provided": false,
                      "json_schema": {
                        "type": "string",
                        "pattern": "^\\d+$"
                      }
                    },
                    {
                      "name": "encryption_type",
                      "is_required": true,
                      "provided": false,
                      "is_credential": false,
                      "system_provided": false,
                      "json_schema": {
                        "type": "string",
                        "pattern": "^(ssh|none)$"
                      }
                    },
                    {
                      "name": "encryption_username",
                      "is_required": false,
                      "provided": false,
                      "is_credential": false,
                      "system_provided": false,
                      "json_schema": {
                        "type": "string"
                      }
                    },
                    {
                      "name": "host",
                      "is_required": true,
                      "provided": true,
                      "is_credential": false,
                      "system_provided": false,
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
                      }
                    },
                    {
                      "name": "password",
                      "is_required": true,
                      "provided": true,
                      "is_credential": true,
                      "system_provided": false,
                      "json_schema": {
                        "type": "string"
                      }
                    },
                    {
                      "name": "port",
                      "is_required": true,
                      "provided": true,
                      "is_credential": false,
                      "system_provided": false,
                      "json_schema": {
                        "type": "string",
                        "pattern": "^\\d+$"
                      }
                    },
                    {
                      "name": "ssl",
                      "is_required": true,
                      "provided": false,
                      "is_credential": false,
                      "system_provided": false,
                      "json_schema": {
                        "type": "boolean"
                      }
                    },
                    {
                      "name": "sslrootcert",
                      "is_required": false,
                      "provided": false,
                      "is_credential": false,
                      "system_provided": false,
                      "json_schema": {
                        "type": "string"
                      }
                    },
                    {
                      "name": "username",
                      "is_required": true,
                      "provided": true,
                      "is_credential": false,
                      "system_provided": false,
                      "json_schema": {
                        "type": "string"
                      }
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
  - type: "Errors"
---