---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-structure"
key: "report-card-object--source"

title: "Source Report Card"
description: "{{ api.data-structures.report-cards.source.description }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "current_step"
    type: "integer"
    description: "The index (in the `steps` array) of the current step needed to configure the data source."

  - name: "steps"
    type: "array"
    description: "A sequential list of [Connection Step objects]({{ api.data-structures.connection-steps.section }}) required to complete configuration for the connection type."

  - name: "type"
    type: "string"
    description: "The connection type. Ex: `platform.mysql` or `platform.hubspot`"


# -------------------------- #
#          EXAMPLES          #
# -------------------------- #

examples:
  - type: "Database source"
    code: |
      {
        "type": "platform.mysql",
        "current_step": 1,
        "steps": [
          {
            "type": "form",
            "properties": [
              {
                "name": "image_version",
                "is_required": true,
                "provided": false,
                "is_credential": false,
                "system_provided": true,
                "tap_mutable": false,
                "json_schema": null
              },
              {
                "name": "frequency_in_minutes",
                "is_required": true,
                "provided": false,
                "is_credential": false,
                "system_provided": false,
                "tap_mutable": false,
                "json_schema": {
                  "type": "string",
                  "pattern": "^1$|^30$|^60$|^360$|^720$|^1440$"
                }
              },
              {
                "name": "anchor_time",
                "is_required": false,
                "provided": false,
                "is_credential": false,
                "system_provided": false,
                "tap_mutable": false,
                "json_schema": {
                  "type": "string",
                  "format": "date-time"
                }
              },
              {
                "name": "database",
                "is_required": false,
                "provided": false,
                "is_credential": false,
                "system_provided": false,
                "tap_mutable": false,
                "json_schema": {
                  "type": "string"
                }
              },
              {
                "name": "filter_dbs",
                "is_required": false,
                "provided": false,
                "is_credential": false,
                "system_provided": false,
                "tap_mutable": false,
                "json_schema": {
                  "type": "string"
                }
              },
              {
                "name": "host",
                "is_required": true,
                "provided": false,
                "is_credential": false,
                "system_provided": false,
                "tap_mutable": false,
                "json_schema": {
                  "type": "string",
                  "format": "uri"
                }
              },
              {
                "name": "password",
                "is_required": true,
                "provided": false,
                "is_credential": true,
                "system_provided": false,
                "tap_mutable": false,
                "json_schema": {
                  "type": "string"
                }
              },
              {
                "name": "port",
                "is_required": true,
                "provided": false,
                "is_credential": false,
                "system_provided": false,
                "tap_mutable": false,
                "json_schema": {
                  "type": "string",
                  "pattern": "^\\d+"
                }
              },
              {
                "name": "server_id",
                "is_required": false,
                "provided": false,
                "is_credential": false,
                "system_provided": false,
                "tap_mutable": false,
                "json_schema": {
                  "type": "string",
                  "pattern": "^\\d+$"
                }
              },
              {
                "name": "ssh",
                "is_required": false,
                "provided": false,
                "is_credential": false,
                "system_provided": false,
                "tap_mutable": false,
                "json_schema": {
                  "type": "string",
                  "pattern": "^(true|false)"
                }
              },
              {
                "name": "ssh_host",
                "is_required": false,
                "provided": false,
                "is_credential": false,
                "system_provided": false,
                "tap_mutable": false,
                "json_schema": {
                  "type": "string",
                  "format": "uri"
                }
              },
              {
                "name": "ssh_port",
                "is_required": false,
                "provided": false,
                "is_credential": false,
                "system_provided": false,
                "tap_mutable": false,
                "json_schema": {
                  "type": "string",
                  "pattern": "^\\d+"
                }
              },
              {
                "name": "ssh_user",
                "is_required": false,
                "provided": false,
                "is_credential": false,
                "system_provided": false,
                "tap_mutable": false,
                "json_schema": {
                  "type": "string"
                }
              },
              {
                "name": "ssl",
                "is_required": false,
                "provided": false,
                "is_credential": false,
                "system_provided": false,
                "tap_mutable": false,
                "json_schema": {
                  "type": "string",
                  "pattern": "^(true|false)"
                }
              },
              {
                "name": "user",
                "is_required": true,
                "provided": false,
                "is_credential": false,
                "system_provided": false,
                "tap_mutable": false,
                "json_schema": {
                  "type": "string"
                }
              },
              {
                "name": "use_log_based_replication",
                "is_required": false,
                "provided": false,
                "is_credential": false,
                "system_provided": false,
                "tap_mutable": false,
                "json_schema": {
                  "type": "string",
                  "pattern": "^(true|false)$"
                }
              }
            ]
          },
          {
            "type": "discover_schema",
            "properties": []
          },
          {
            "type": "field_selection",
            "properties": []
          },
          {
            "type": "fully_configured",
            "properties": []
          }
        ]
      }


  - type: "SaaS source"
    code: |
      {
         "report_card":{
            "type":"platform.hubspot",
            "current_step":2,
            "steps":[
               {
                  "type":"form",
                  "properties":[
                     {
                        "name":"image_version",
                        "is_required":true,
                        "provided":true,
                        "is_credential":false,
                        "system_provided":true,
                        "json_schema":null
                     },
                     {
                        "name":"frequency_in_minutes",
                        "is_required":true,
                        "provided":true,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{
                           "type":"string",
                           "pattern":"^\\d+$"
                        }
                     },
                     {
                        "name":"start_date",
                        "is_required":true,
                        "provided":true,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{
                           "type":"string",
                           "pattern":"^\\d{4}-\\d{2}-\\d{2}T00:00:00Z$"
                        }
                     }
                  ]
               },
               {
                  "type":"oauth",
                  "properties":[
                     {
                        "name":"client_id",
                        "is_required":true,
                        "provided":false,
                        "is_credential":true,
                        "system_provided":true,
                        "json_schema":{
                           "type":"string"
                        }
                     },
                     {
                        "name":"client_secret",
                        "is_required":true,
                        "provided":false,
                        "is_credential":true,
                        "system_provided":true,
                        "json_schema":{
                           "type":"string"
                        }
                     },
                     {
                        "name":"redirect_uri",
                        "is_required":true,
                        "provided":false,
                        "is_credential":true,
                        "system_provided":true,
                        "json_schema":{
                           "type":"string",
                           "format":"uri"
                        }
                     },
                     {
                        "name":"refresh_token",
                        "is_required":true,
                        "provided":false,
                        "is_credential":true,
                        "system_provided":true,
                        "json_schema":{
                           "type":"string"
                        }
                     }
                  ]
               },
               {
                  "type":"discover_schema",
                  "properties":[

                  ]
               },
               {
                  "type":"field_selection",
                  "properties":[

                  ]
               },
               {
                  "type":"fully_configured",
                  "properties":[

                  ]
               }
            ]
         }
      }
---