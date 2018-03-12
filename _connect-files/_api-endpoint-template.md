---
content-type: "embed-endpoint"
endpoint: ""
key: ""
order: 


title: ""
method: ""
short-url: |
  /v{{ object.version }}{{ object.endpoint-url }}
full-url: |
  {{ page.api-base-url }}{{ endpoint.short-url | flatify }}
description: ""


arguments:
  - name: ""
    required: 
    description: ""


returns: ""

examples:
  - type: "request"
    language: ""
    code: |
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip_newlines }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json"
           -d ""
  - type: "response"
    language: ""
    code: |
      
---