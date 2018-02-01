---
content-type: "embed-endpoint"
endpoint: "source-types"
key: "list-source-types"
version: "4"
order: 2


title: "List source types"
method: "get"
short-url: |
  /v{{ object.version }}{{ object.endpoint-url }}
full-url: |
  {{ page.api-base-url }}{{ endpoint.short-url | flatify }}
description: "Retrieves information about data sources' configurations."


returns: "An array of report card objects."


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