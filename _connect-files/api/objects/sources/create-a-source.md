---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

content-type: "api-endpoint"
endpoint: "sources"
key: "create-a-source"
version: "4"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Create a source"
method: "post"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}

short: "{{ api.core-objects.sources.create.short }}"
description: "{{ api.core-objects.sources.create.description | flatify }}"


# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

arguments:
  - name: "display_name"
    required: true
    type: "string"
    description: "{{ connect.common.attributes.display-name }}"
    example-value: |
      "HubSpot"

  - name: "type"
    required: true
    type: "string"
    description: "The source type. For example: `platform.marketo` or `platform.hubspot`."
    example-value: |
      "platform.hubspot"

  - name: "properties"
    required: false
    type: "object"
    description: "{{ connect.common.attributes.properties | flatify }}"


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and a [Source object]({{ api.core-objects.sources.object }}) with a `report_card` property. 

  The `report_card` property contains the [Source Report Card object]({{ api.data-structures.report-cards.source.section }}) for the source's configuration status.


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
           -d "{
                   "type":"platform.shopify",
                   "display_name":"Shopify",
                   "properties":{
                      "start_date":"2017-01-01T00:00:00Z",
                      "frequency_in_minutes":"30"
                   }
                }"
  - type: "Response"
    language: "json"
    code: |
      {
         "properties":{
            "anchor_time":"2019-01-30T18:16:37.205Z",
            "cron_expression":null,
            "frequency_in_minutes":"30",
            "image_version":"1.latest",
            "product":"pipeline",
            "shop":"stitchdatawearhouse",
            "start_date":"2017-01-01T00:00:00Z"
         },
         "updated_at":"2019-05-28T13:52:23Z",
         "schedule":null,
         "name":"shopify",
         "type":"platform.shopify",
         "deleted_at":null,
         "system_paused_at":null,
         "stitch_client_id":116078,
         "paused_at":null,
         "id":86741,
         "display_name":"Shopify",
         "created_at":"2019-01-10T19:38:18Z",
         "report_card":{
            "type":"platform.shopify",
            "current_step":1,
            "current_step_type":"fully_configured",
            "steps":[
               {
                  "type":"form",
                  "properties":[
                     {
                        "name":"anchor_time",
                        "is_required":false,
                        "is_credential":false,
                        "system_provided":false,
                        "property_type":"user_provided",
                        "json_schema":{
                           "type":"string",
                           "format":"date-time"
                        },
                        "provided":true,
                        "tap_mutable":false
                     },
                     {
                        "name":"cron_expression",
                        "is_required":false,
                        "is_credential":false,
                        "system_provided":false,
                        "property_type":"user_provided",
                        "json_schema":null,
                        "provided":false,
                        "tap_mutable":false
                     },
                     {
                        "name":"date_window_size",
                        "is_required":false,
                        "is_credential":false,
                        "system_provided":false,
                        "property_type":"user_provided",
                        "json_schema":{
                           "type":"integer"
                        },
                        "provided":false,
                        "tap_mutable":false
                     },
                     {
                        "name":"frequency_in_minutes",
                        "is_required":false,
                        "is_credential":false,
                        "system_provided":false,
                        "property_type":"user_provided",
                        "json_schema":{
                           "type":"string",
                           "pattern":"^1$|^30$|^60$|^360$|^720$|^1440$"
                        },
                        "provided":true,
                        "tap_mutable":false
                     },
                     {
                        "name":"image_version",
                        "is_required":true,
                        "is_credential":false,
                        "system_provided":true,
                        "property_type":"read_only",
                        "json_schema":null,
                        "provided":true,
                        "tap_mutable":false
                     },
                     {
                        "name":"shop",
                        "is_required":true,
                        "is_credential":false,
                        "system_provided":false,
                        "property_type":"user_provided",
                        "json_schema":{
                           "type":"string"
                        },
                        "provided":true,
                        "tap_mutable":false
                     },
                     {
                        "name":"start_date",
                        "is_required":true,
                        "is_credential":false,
                        "system_provided":false,
                        "property_type":"user_provided",
                        "json_schema":{
                           "type":"string",
                           "pattern":"^\\d{4}-\\d{2}-\\d{2}T00:00:00Z$"
                        },
                        "provided":true,
                        "tap_mutable":false
                     }
                  ]
               },
               {
                  "type":"oauth",
                  "properties":[
                     {
                        "name":"api_key",
                        "is_required":true,
                        "is_credential":true,
                        "system_provided":true,
                        "property_type":"system_provided_by_default",
                        "json_schema":{
                           "type":"string"
                        },
                        "provided":false,
                        "tap_mutable":false
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

  - type: "Errors"
---