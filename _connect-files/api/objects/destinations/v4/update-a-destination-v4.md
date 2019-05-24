---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

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


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    language: "json"
    code: |
      {% assign right-bracket = "}" %}
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | replace: "{destination_id","86741" | remove: right-bracket | strip_newlines }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json"
           -d "{
                "type":"postgres",
                "properties": {
                  "host": "<HOST>",
                  "port": 5432,
                  "username": "<USERNAME>",
                  "database": "<DATABASE>",
                  "password": "<PASSWORD>",
                  "ssl": false
                  }
              }"

  - type: "Response"
    language: "json"
    code: |
      HTTP/1.1 200 OK
      Content-Type: application/json;charset=ISO-8859-1
      
      [
        {
          "properties": {
            "database": "<DATABASE>",
            "host": "<HOST>",
            "port": "5432",
            "username": "<USERNAME>"
          },
          "updated_at": "2019-01-10T16:46:50Z",
          "name": "Default Warehouse",
          "type": "postgres",
          "deleted_at": null,
          "system_paused_at": null,
          "stitch_client_id": <CLIENT_ID>,
          "paused_at": null,
          "id": 120603,
          "created_at": "2019-01-10T16:46:50Z",
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
      ]

  - type: "Errors"
---