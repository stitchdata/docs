---
content-type: "api-endpoint"
endpoint: "sources"
key: "list-sources"
version: "4"
order: 3


title: "List sources"
method: "get"
short-url: |
  /v{{ object.version }}{{ object.endpoint-url }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.sources.list.description }}"
description: "{{ api.core-objects.sources.list.description }}"


returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and an array of [Source Objects]({{ api.core-objects.sources.object }}), including paused and deleted sources.


examples:
  - type: "request"
    language: "json"
    code: |
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip_newlines }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json"
  - type: "response"
    language: "json"
    code: |
      HTTP/1.1 200 OK
      Content-Type: application/json;charset=ISO-8859-1
      
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
               ]
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
               ]
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
               ]
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
               ]
            }
         }
      ]

---