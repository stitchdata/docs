---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-structure"
key: "report-card-object--destination"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Destination Report Card"
description: "{{ api.data-structures.report-cards.destination.description }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "current_step"
    type: "integer"
    description: "The index (in the `steps` array) of the current step needed to configure the destination."

  - name: "details"
    type: "object"
    sub-type: "details"
    url: "{{ api.data-structures.details.section }}"
    description: |
      {{ api.data-structures.details.short | flatify }}

  - name: "steps"
    type: "array"
    description: "A sequential list of [Connection Step objects]({{ api.data-structures.connection-steps.section }}) required to complete configuration for the connection type."

  - name: "type"
    type: "string"
    description: "The destination connection type. Ex: `postgres` or `redshift`"


# -------------------------- #
#          EXAMPLES          #
# -------------------------- #

examples:
  - code: |
      {
        "type": "snowflake",
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
                "name": "role",
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
                "is_credential": true,
                "system_provided": false,
                "property_type": "user_provided",
                "json_schema": {
                  "type": "string"
                },
                "provided": false
              },
              {
                "name": "warehouse",
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
          "protocol": "snowflake",
          "access": true
        }
      }
---