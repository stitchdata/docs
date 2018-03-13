---
content-type: "api-endpoint"
endpoint: "destinations"
key: "list-destinations"
version: "3"
order: 3


title: "List destinations"
method: "get"
short-url: |
  /v{{ object.version }}{{ object.endpoint-url }}
full-url: |
  {{ page.api-base-url }}{{ endpoint.short-url | flatify }}
description: |
  List the destination currently in use. Only a single data warehouse is supported per Stitch client account.


returns: "An array (of length zero or one) of destinations."


examples:
  - type: "request"
    language: "curl"
    code: |
      curl -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json" 
           -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip_newlines }}
  - type: "response"
    language: "json"
    code: |
      [
        {  
          "id":"<DESTINATION_ID>",
          "type":"redshift",
          "created_at":"2018-02-06T15:36:36Z",
          "updated_at":"2018-02-06T15:36:36Z",
          "connection": {  
              "host":"<HOST>",
              "port":5439,
              "username":"<USERNAME>",
              "database":"<DATABASE>",
              "password":"<PASSWORD>",
              "ssl":false
          },
          "last_check":{
            "error": false,
            "started_at":"2018-02-06T16:15:19Z",
            "completed_at":"2018-02-06T16:16:21Z"
          }
        }
      ]
---

