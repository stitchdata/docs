---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "destinations"
key: "list-destinations"
version: "4"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "List destinations"
method: "get"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.destinations.list.short }}"
description: "{{ api.core-objects.destinations.list.description | flatify }}"


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of `200 OK` and an array of [Destination objects]({{ api.core-objects.destinations.object }}), one for each destination connected to the account.

  **Note**: Stitch currently supports only one destination per account.

# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    language: "json"
    code: |
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip_newlines }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json" 
  - type: "Response"
    language: "json"
    code: |
      [
         {
            "properties":{
               "database":"demni2mf59dt10",
               "encryption_type":"none",
               "host":"<HOST>",
               "port":"5432",
               "ssl":"true",
               "status":"1",
               "username":"stitch"
            },
            "updated_at":"2019-05-24T18:04:08Z",
            "name":"Default Warehouse",
            "type":"postgres",
            "deleted_at":null,
            "system_paused_at":null,
            "stitch_client_id":116078,
            "paused_at":null,
            "id":155582,
            "display_name":null,
            "created_at":"2019-05-24T18:03:50Z",
            "report_card":{
               "type":"postgres",
               "current_step":2,
               "current_step_type":"fully_configured",
               "steps":[
                  {
                     "type":"form",
                     "properties":[
                        {
                           "name":"database",
                           "is_required":true,
                           "is_credential":false,
                           "system_provided":false,
                           "property_type":"user_provided",
                           "json_schema":{
                              "type":"string"
                           },
                           "provided":true
                        },
                        {
                           "name":"encryption_host",
                           "is_required":false,
                           "is_credential":false,
                           "system_provided":false,
                           "property_type":"user_provided",
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
                           },
                           "provided":false
                        },
                        {
                           "name":"encryption_port",
                           "is_required":false,
                           "is_credential":false,
                           "system_provided":false,
                           "property_type":"user_provided",
                           "json_schema":{
                              "type":"string",
                              "pattern":"^\\d+$"
                           },
                           "provided":false
                        },
                        {
                           "name":"encryption_type",
                           "is_required":true,
                           "is_credential":false,
                           "system_provided":false,
                           "property_type":"user_provided",
                           "json_schema":{
                              "type":"string",
                              "pattern":"^(ssh|none)$"
                           },
                           "provided":true
                        },
                        {
                           "name":"encryption_username",
                           "is_required":false,
                           "is_credential":false,
                           "system_provided":false,
                           "property_type":"user_provided",
                           "json_schema":{
                              "type":"string"
                           },
                           "provided":false
                        },
                        {
                           "name":"host",
                           "is_required":true,
                           "is_credential":false,
                           "system_provided":false,
                           "property_type":"user_provided",
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
                           },
                           "provided":true
                        },
                        {
                           "name":"password",
                           "is_required":true,
                           "is_credential":true,
                           "system_provided":false,
                           "property_type":"user_provided",
                           "json_schema":{
                              "type":"string"
                           },
                           "provided":true
                        },
                        {
                           "name":"port",
                           "is_required":true,
                           "is_credential":false,
                           "system_provided":false,
                           "property_type":"user_provided",
                           "json_schema":{
                              "type":"string",
                              "pattern":"^\\d+$"
                           },
                           "provided":true
                        },
                        {
                           "name":"ssl",
                           "is_required":true,
                           "is_credential":false,
                           "system_provided":false,
                           "property_type":"user_provided",
                           "json_schema":{
                              "type":"boolean"
                           },
                           "provided":true
                        },
                        {
                           "name":"sslrootcert",
                           "is_required":false,
                           "is_credential":false,
                           "system_provided":false,
                           "property_type":"user_provided",
                           "json_schema":{
                              "type":"string"
                           },
                           "provided":false
                        },
                        {
                           "name":"username",
                           "is_required":true,
                           "is_credential":false,
                           "system_provided":false,
                           "property_type":"user_provided",
                           "json_schema":{
                              "type":"string"
                           },
                           "provided":true
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
      ]
---