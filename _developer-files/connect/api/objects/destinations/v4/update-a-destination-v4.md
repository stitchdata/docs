---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "destinations"
key: "update-a-destination"
version: "4"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Update a destination"
method: "put"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}/{destination_id}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.destinations.update.short }}"
description: "{{ api.core-objects.destinations.update.description | flatify }}"


# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

arguments:
  - name: "destination_id"
    required: true
    type: "path parameter"
    description: "A path parameter corresponding to the unique ID of the destination to be updated."

  - name: "properties"
    required: true
    type: "object"
    description: "A [Destination Form Properties object]({{ api.form-properties.destination-forms.section }}) corresponding to the value of `type`."


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of `200 OK` and a [Destination object]({{ api.core-objects.destinations.object }}) with a `report_card` property.


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    language: "json"
    code: |
      {% assign right-bracket = "}" %}
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | replace: "{destination_id","155582" | remove: right-bracket | strip_newlines }} \
           -H "Authorization: Bearer <ACCESS_TOKEN>" \
           -H "Content-Type: application/json" \
           -d "{
                "properties": {
                  "username": "stitch_admin"
                  }
              }"

  - type: "Response"
    language: "json"
    code: |
      {
        "properties": {
          "database": "demni2mf59dt10",
          "encryption_type": "none",
          "host": "<HOST>",
          "port": "5432",
          "ssl": "true",
          "status": "1",
          "username": "stitch_admin"
        },
        "updated_at": "2019-05-28T15:37:37Z",
        "check_job_name": "116078.155582.check.859f4746-815e-11e9-bb8e-0693226a5168",
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

  - type: "Errors"
---