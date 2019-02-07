---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "sources"
key: "retrieve-a-source"
version: "4"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Retrieve a source"
method: "get"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}/{id}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.sources.retrieve.description }}"
description: "{{ api.core-objects.sources.retrieve.description }}"


# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

arguments:
  - name: "id"
    required: true
    type: "path parameter"
    description: "A path parameter corresponding to the unique ID of the data source to be retrieved."
    example-value: |
      86741

# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful and a valid identifier was provided, the API will return a status of <code class="api success">200 OK</code> and a single [Source Object]({{ api.core-objects.sources.object }}).


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    language: "json"
    code: |
      {% assign right-bracket = "}" %}
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | replace: "{id","86741" | remove: right-bracket | strip_newlines }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json"
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
         "updated_at":"2018-02-06T18:04:59Z",
         "name":"hubspot",
         "type":"platform.hubspot",
         "deleted_at":"2018-02-06T18:04:58Z",
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
                  "properties":[  

                  ]
               },
               {
                  "type":"field_selection",
                  "properties":[ ]
               },
               {
                  "type":"fully_configured",
                  "properties":[  ]
               }
            ]
         }
      }
---