---
content-type: "api-endpoint"
endpoint: "source-types"
key: "get-a-source-type"
version: "4"
order: 1


title: "Get a source type"
method: "get"
short-url: |
  /v{{ object.version }}{{ object.endpoint-url }}/{type}
full-url: |
  {{ page.api-base-url }}{{ endpoint.short-url | flatify }}
description: |
  Retrieves information about a data source's configuration. 

  **Note**: This endpoint doesn't retrieve information about the specific configuration of sources in a single account. Instead, it will return general configuration information for the specified `type`.


arguments:
  - name: "type"
    required: true
    description: "A path parameter indicating the `type` of source to retrieve, such as `platform.marketo` or `platform.hubspot`."


returns: "A [Report Card object]({{ page.anchors.data-structures.report-cards }}) corresponding to `type`."

examples:
  - type: "request"
    language: "curl"
    code: |
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip_newlines }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json"

  - type: "response"
    language: "json"
    code: |
      {  
         "type":"platform.hubspot",
         "current_step":1,
         "current_step_hints":{  
            "api":{  
               "method":"POST",
               "url":"/v4/sources"
            },
            "js":{  
               "function":"addSource",
               "options":{  
                  "type":"platform.hubspot"
               }
            }
         },
         "steps":[  
            {  
               "type":"form",
               "properties":[  
                  {  
                     "name":"image_version",
                     "is_required":true,
                     "provided":false,
                     "is_credential":false,
                     "system_provided":true,
                     "json_schema":null
                  },
                  {  
                     "name":"frequency_in_minutes",
                     "is_required":true,
                     "provided":false,
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
                     "provided":false,
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
         ]
      }

---