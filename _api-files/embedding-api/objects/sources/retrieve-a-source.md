---
content-type: "embed-endpoint"
endpoint: "sources"
key: "retrieve-a-source"
version: "4"
order: 4


title: "Retrieve a source"
method: "get"
short-url: |
  /v{{ object.version }}{{ object.endpoint-url }}/{id}
full-url: |
  {{ page.api-base-url }}{{ endpoint.short-url | flatify }}
description: "Retrieves a previously created data source by its unique identifier."


arguments:
  - name: "id"
    required: true
    description: "A path parameter corresponding to the unique ID of the data source to be retrieved."


returns: "A single data source if a valid identifier was provided."


examples:
  - type: "request"
    language: "curl"
    code: |
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip_newlines }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json"
  # - type: "response"
  #   language: ""
  #   code: |

---