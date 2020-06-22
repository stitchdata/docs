---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-object"
endpoint: "destination-types"
order: 3


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Destination Type"
endpoint-url: "/destination-types"

description: "{{ api.core-objects.destination-types.description }}"
intro-short: "Retrieve configuration info for destinations" # Used in the API functionality section of the docs

# -------------------------- #
#        VERSION INFO        #
# -------------------------- #

latest-version: "4"
versions:
  - number: "4"
    deprecated: false


# -------------------------- #
#      AVAILABLE METHODS     #
# -------------------------- #

available-methods:
  - id: "get-a-destination-type"
    title: "Get a destination type"
    method: "get"
    short: "{{ api.core-objects.destination-types.get.short | flatify }}"

  - id: "list-destination-types"
    title: "List all destination types"
    method: "get"
    short: "{{ api.core-objects.destination-types.list.short | flatify }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "report_card"
    type: "object"
    sub-type: "destination report card"
    url: "{{ api.data-structures.report-cards.destination.section }}"
    description: "The Destination Report Card object corresponding to the destination's `type`. For example: `s3` or `snowflake`."


# -------------------------- #
#           EXAMPLES         #
# -------------------------- #

examples:
  - code: |
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