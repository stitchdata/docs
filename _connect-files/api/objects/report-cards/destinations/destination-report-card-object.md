---
content-type: "api-structure"
key: "report-card-object--destination"

title: "Destination Report Card"
description: "{{ api.data-structures.report-cards.destination.description }}"

object-attributes:
  - name: "current_step"
    type: "integer"
    description: "The index (in the `steps` array) of the current step needed to configure the destination."

  - name: "steps"
    type: "array"
    description: "A sequential list of [Connection Step objects]({{ api.data-structures.connection-steps.section }}) required to complete configuration for the connection type."

  - name: "type"
    type: "string"
    description: "The destination connection type. Ex: `postgres` or `redshift`"

examples:
  - code: |
      {
         "report_card":{
            "type":"postgres",
            "current_step":1,
            "steps":[
               {
                  "type":"form",
                  "properties":[
                     {
                        "name":"database",
                        "is_required":true,
                        "provided":true,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{
                           "type":"string"
                        }
                     },
                     {
                        "name":"encryption_host",
                        "is_required":false,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{
                           "anyOf":[
                              {
                                 "type":"string",
                                 "format":"ipv4"
                              },
                              {
                                 "type":"string",
                                 "format":"ipv6"
                              },
                              {
                                 "type":"string",
                                 "format":"hostname"
                              }
                           ]
                        }
                     },
                     {
                        "name":"encryption_port",
                        "is_required":false,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{
                           "type":"integer"
                        }
                     },
                     {
                        "name":"encryption_type",
                        "is_required":true,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{
                           "type":"string",
                           "pattern":"^(ssh|none)$"
                        }
                     },
                     {
                        "name":"encryption_username",
                        "is_required":false,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{
                           "type":"string"
                        }
                     },
                     {
                        "name":"host",
                        "is_required":true,
                        "provided":true,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{
                           "anyOf":[
                              {
                                 "type":"string",
                                 "format":"ipv4"
                              },
                              {
                                 "type":"string",
                                 "format":"ipv6"
                              },
                              {
                                 "type":"string",
                                 "format":"hostname"
                              }
                           ]
                        }
                     },
                     {
                        "name":"password",
                        "is_required":true,
                        "provided":true,
                        "is_credential":true,
                        "system_provided":false,
                        "json_schema":{
                           "type":"string"
                        }
                     },
                     {
                        "name":"port",
                        "is_required":true,
                        "provided":true,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{
                           "type":"integer"
                        }
                     },
                     {
                        "name":"ssl",
                        "is_required":false,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{
                           "type":"boolean"
                        }
                     },
                     {
                        "name":"sslrootcert",
                        "is_required":false,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{
                           "type":"string"
                        }
                     },
                     {
                        "name":"username",
                        "is_required":true,
                        "provided":true,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{
                           "type":"string",
                           "pattern":"^[a-z][-a-z0-9_]*$"
                        }
                     }
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