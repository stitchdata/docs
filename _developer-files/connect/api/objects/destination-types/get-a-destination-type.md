---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "destination-types"
key: "get-a-destination-type"
version: "4"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Get a destination type"
method: "get"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}/{destination_type}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: |
  {{ api.core-objects.destination-types.get.short }}
description: |
  {{ api.core-objects.destination-types.get.description | flatify }}

  Refer to the [Destination and source API availability reference]({{ link.connect.guides.connection-reference | prepend: site.baseurl | append: "#destinations-api-availability" }}) for info on the destinations that are available in the API.


# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

arguments:
  - name: "destination_type"
    required: true
    type: "string"
    description: |
      {{ connect.common.attributes.type-argument | replace: "[TYPE]","destination" | replace: "[TYPE-1]","s3" | replace: "[TYPE-2]","redshift" }}
    example-value:
      "snowflake"


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and a [Destination Report Card object]({{ api.data-structures.report-cards.destination.section }}) corresponding to `type`.


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    language: "json"
    code: |
      {% assign right-bracket = "}" %}curl {{ endpoint.full-url | flatify | remove: right-bracket | replace:"{destination_type","redshift" | strip_newlines }} \
           -H "Authorization: Bearer <ACCESS_TOKEN>" \
           -H "Content-Type: application/json"


  - type: "Response"
    language: "json"
    code: |
      {
        "type": "redshift",
        "current_step": 1,
        "current_step_type": "form",
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
                "provided": false
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
                "provided": false
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
                "provided": false
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
                "provided": false
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
                "provided": false
              }
            ]
          },
          {
            "type": "fully_configured",
            "properties": []
          }
        ],
        "details": {
          "pricing_tier": "standard",
          "pipeline_state": "released",
          "protocol": "redshift",
          "access": true
        }
      }
---