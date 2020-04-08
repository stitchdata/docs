---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
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
description: |
  {{ api.core-objects.destinations.create.description | flatify }}

  Refer to the [Destination and source API availability reference]({{ link.connect.guides.connection-reference | prepend: site.baseurl | append: "#destinations-api-availability" }}) for info on the destinations that are available in the API.


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
    description: "A [Destination Form Property object]({{ api.form-properties.destination-forms.section }}) corresponding to the value of `type`."


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
    code: |
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip_newlines }} \
           -H "Authorization: Bearer <ACCESS_TOKEN>" \
           -H "Content-Type: application/json" \
           -d "{
                "type":"postgres",
                "properties": {
                  "host":"<HOST>",
                  "port":"5432",
                  "username":"stitch",
                  "database":"demni2mf59dt10",
                  "password":"<PASSWORD>",
                  "ssl":false
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

  - type: "Errors"
---