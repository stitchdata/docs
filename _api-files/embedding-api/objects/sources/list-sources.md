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
description: "List the data sources for an account."


returns: "An array of sources."


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