---
content-type: "embed-endpoint"
endpoint: "destinations"
key: "update-a-destination"
order: 2


title: "Update a destination"
method: "put"
short-url: |
  /v{{ object.version }}{{ object.endpoint-url }}/[id]
full-url: |
  {{ page.api-base-url }}{{ endpoint.short-url | flatify }}
description: "Update a destination. Modifications to the `type` attribute are not supported."


arguments:
  - name: "type"
    required: false
    description: "The destination type, either `redshift` or `postgres`."

  - name: "connection"
    required: false
    description: "A destination form properties object corresponding to the value of `type`."

returns: "A destination object."


examples:
  - type: "request"
    language: "curl"
    code: |
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip_newlines }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json"
           -d "{
                "type":"postgres",
                "connection": {
                  "host": "<HOST>",
                  "port": 5432,
                  "username": "<USERNAME>",
                  "database": "<DATABASE>",
                  "password": "<PASSWORD>",
                  "ssl": false
                  }
              }"

  - type: "response"
    language: "json"
    code: |
      {  
        "id":"<ID>",
        "type":"postgres",
        "created_at":"TIME",
        "updated_at":"TIME",
        "connection": {
            "host":"<HOST>",
            "port":5432,
            "username":"<USERNAME>",
            "database":"<DATABASE>",
            "password":"<PASSWORD>",
            "ssl":false
        },
        "last_check":{
            "updated_at":"TIME",
            "status":"OK",
            "message":""
        }
      }
---