---
content-type: "embed-endpoint"
endpoint: "sources"
key: "list-sources"
version: "4"
order: 3


title: "List sources"
method: "get"
short-url: |
  /v{{ object.version }}{{ object.endpoint-url }}
full-url: |
  {{ page.api-base-url }}{{ endpoint.short-url | flatify }}
description: |
  List the sources for an account.

  **Note**: The response will include active, paused, and deleted sources.


returns: "An array of [sources]({{ page.anchors.core-objects.sources.object }}), including paused and deleted sources."


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
      [
         {
            "properties":{
               "frequency_in_minutes":"30",
               "image_version":"1.latest",
               "start_date":"2017-01-01T00:00:00Z"
            },
            "updated_at":"2018-02-06T18:04:59Z",
            "name":"hubspot_api_test",
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
                     "properties":[ ... ]
                  },
                  {
                     "type":"oauth",
                     "properties":[ ... ]
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
                  "js":{
                     "function":"authorizeSource",
                     "options":{  
                        "id":<SOURCE_ID>
                     }
                  }
               }
            }
         },
         {  
            "properties":{
               "frequency_in_minutes":"30",
               "image_version":"1.latest",
               "start_date":"2017-01-01T00:00:00Z"
            },
            "updated_at":"2018-02-06T18:12:41Z",
            "name":"hubspot",
            "type":"platform.hubspot",
            "deleted_at":null,
            "system_paused_at":null,
            "stitch_client_id":<ACCOUNT_ID>,
            "paused_at":null,
            "id":<SOURCE_ID>,
            "display_name":"HubSpot",
            "created_at":"2018-02-06T18:12:41Z",
            "report_card":{
               "type":"platform.hubspot",
               "current_step":2,
               "steps":[  
                  {
                     "type":"form",
                     "properties":[ ... ]
                  },
                  {
                     "type":"oauth",
                     "properties":[ ... ]
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
                  "js":{
                     "function":"authorizeSource",
                     "options":{  
                        "id":<SOURCE_ID>
                     }
                  }
               }
            }
         },
         {  
            "properties":{
               "frequency_in_minutes":"30",
               "image_version":"1.latest",
               "start_date":"2017-01-01T00:00:00Z"
            },
            "updated_at":"2018-02-06T18:10:44Z",
            "name":"salesforce_api_test",
            "type":"platform.salesforce",
            "deleted_at":"2018-02-06T18:05:06Z",
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
                     "properties":[ ... ]
                  },
                  {  
                     "type":"oauth",
                     "properties":[ ... ]
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
                     "url":"{{ endpoint.short-url | flatify | strip_newlines }}{id}"
                  }
               }
            }
         },
         {  
            "properties":{
               "frequency_in_minutes":"30",
               "image_version":"1.latest",
               "start_date":"2017-01-01T00:00:00Z"
            },
            "updated_at":"2018-02-06T18:05:30Z",
            "name":"salesforce_api_test",
            "type":"platform.salesforce",
            "deleted_at":null,
            "system_paused_at":null,
            "stitch_client_id":<ACCOUNT_ID>,
            "paused_at":null,
            "id":<SOURCE_ID>,
            "display_name":"Salesforce",
            "created_at":"2018-02-06T18:05:30Z",
            "report_card":{
               "type":"platform.salesforce",
               "current_step":1,
               "steps":[
                  {
                     "type":"form",
                     "properties":[ ... ]
                  },
                  {
                     "type":"oauth",
                     "properties":[ ... ]
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
                     "url":"{{ endpoint.short-url | flatify | strip_newlines }}{id}"
                  }
               }
            }
         }
      ]

---