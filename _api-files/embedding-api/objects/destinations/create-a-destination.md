---
content-type: "embed-endpoint"
endpoint: "destinations"
key: "create-a-destination"
version: "3"
order: 1


title: "Create a destination"
method: "post"
short-url: |
  /v{{ object.version }}{{ object.endpoint-url }}
full-url: |
  {{ page.api-base-url }}{{ endpoint.short-url | flatify }}
description: "Create a new destination. Only a single destination is supported per Stitch client account."


arguments:
  - name: "type"
    required: true
    description: "The destination type, either `redshift` or `postgres`."

  - name: "connection"
    required: true
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
                "type":"redshift",
                "connection": {
                  "host": "<HOST>",
                  "port": 5439,
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
        "type":"redshift",
        "created_at":"TIME",
        "updated_at":"TIME",
        "connection": {  
            "host":"<HOST>",
            "port":5439,
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