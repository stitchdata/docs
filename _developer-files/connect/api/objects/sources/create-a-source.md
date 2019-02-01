---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

type: "connect"
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
                   "type":"platform.hubspot",
                   "display_name":"HubSpot",
                   "properties":{
                      "start_date":"2017-01-01T00:00:00Z",
                      "frequency_in_minutes":"30"
                   }
                }"
  - type: "Response"
    language: "json"
    code: |
      HTTP/1.1 200 OK
      Content-Type: application/json;charset=ISO-8859-1

      {
         "properties":{
            "frequency_in_minutes":"30",
            "image_version":"1.latest",
            "start_date":"2017-01-01T00:00:00Z"
         },
         "updated_at":"2018-02-06T16:25:06Z",
         "check_job_name":null,
         "name":"hubspot",
         "type":"platform.hubspot",
         "deleted_at":null,
         "system_paused_at":null,
         "stitch_client_id":<ACCOUNT_ID>,
         "paused_at":null,
         "id":<SOURCE_ID>,
         "display_name":"HubSpot",
         "created_at":"2018-02-06T16:25:06Z",
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
                  "properties":[ ]
               },
               {
                  "type":"field_selection",
                  "properties":[ ]
               },
               {
                  "type":"fully_configured",
                  "properties":[ ]
               }
            ]
         }
      }

  - type: "Errors"
---