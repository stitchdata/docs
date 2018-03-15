---
content-type: "api-endpoint"
endpoint: "sources"
key: "update-a-source"
version: "4"
order: 2


title: "Update a source"
method: "put"
short-url: |
  /v{{ object.version }}{{ object.endpoint-url }}/{id}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.sources.update.description }}"
description: "{{ api.core-objects.sources.update.description }}"


arguments:
  - name: "id"
    required: true
    type: "string"
    description: "A path parameter corresponding to the unique ID of the source to be updated."

  - name: "display_name"
    required: false
    type: "string"
    description: "{{ connect.common.attributes.display-name }}"

  - name: "properties"
    required: false
    type: "object"
    description: "{{ connect.common.attributes.properties | flatify }}"


returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and a [Source object]({{ api.core-objects.sources.object }}).

examples:
  - type: "request"
    language: "json"
    code: |
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip_newlines }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json"
           -d "{
                   "display_name":"Salesforce",
                   "properties":{
                      "frequency_in_minutes":"60"
                   }
               }"

  - type: "response"
    language: "json"
    code: |
      HTTP/1.1 200 OK
      Content-Type: application/json;charset=ISO-8859-1

      {
         "properties":{
            "frequency_in_minutes":"60",
            "image_version":"1.latest",
            "start_date":"2017-01-01T00:00:00Z"
         },
         "updated_at":"2018-02-06T17:37:14Z",
         "check_job_name":null,
         "name":"salesforce",
         "type":"platform.salesforce",
         "deleted_at":null,
         "system_paused_at":null,
         "stitch_client_id":<ACCOUNT_ID>,
         "paused_at":null,
         "id":<SOURCE_ID>,
         "display_name":"Salesforce",
         "created_at":"2018-02-06T17:36:02Z",
         "report_card":{
            "type":"platform.salesforce",
            "current_step":1,
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
                        "name":"api_type",
                        "is_required":true,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{
                           "type":"string",
                           "pattern":"^(REST|BULK)$"
                        }
                     },
                     {
                        "name":"is_sandbox",
                        "is_required":false,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{
                           "type":"string",
                           "pattern":"^(true|false)$"
                        }
                     },
                     {
                        "name":"quota_percent_per_run",
                        "is_required":false,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{
                           "type":"string",
                           "pattern":"^\\d+$"
                        }
                     },
                     {
                        "name":"quota_percent_total",
                        "is_required":false,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{
                           "type":"string",
                           "pattern":"^\\d+$"
                        }
                     },
                     {
                        "name":"select_fields_by_default",
                        "is_required":true,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{
                           "type":"string",
                           "pattern":"^(true|false)$"
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
                        "system_provided":false,
                        "json_schema":{
                           "type":"string"
                        }
                     },
                     {
                        "name":"client_secret",
                        "is_required":true,
                        "provided":false,
                        "is_credential":true,
                        "system_provided":false,
                        "json_schema":{
                           "type":"string"
                        }
                     },
                     {
                        "name":"instance_url",
                        "is_required":true,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{
                           "type":"string",
                           "format":"uri"
                        }
                     },
                     {
                        "name":"orgid",
                        "is_required":false,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{
                           "type":"string"
                        }
                     },
                     {
                        "name":"refresh_token",
                        "is_required":true,
                        "provided":false,
                        "is_credential":true,
                        "system_provided":false,
                        "json_schema":{
                           "type":"string"
                        }
                     }
                  ]
               },
               {
                  "type":"discover_schema",
                  "properties":[  ]
               },
               {
                  "type":"field_selection",
                  "properties":[  ]
               },
               {
                  "type":"fully_configured",
                  "properties":[  ]
               }
            ],
            "current_step_hints":{
               "api":{
                  "method":"PUT",
                  "url":"{{ endpoint.short-url | flatify | strip_newlines }}"
               }
            }
         }
      }
  - type: "errors"
---