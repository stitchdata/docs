---
content-type: "embed-endpoint"
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
description: "Retrieves information about a data source's configuration."


arguments:
  - name: "type"
    required: true
    description: "A path parameter indicating the `type` of source to retrieve, such as `platform.marketo` or `platform.hubspot`."


returns: "A report card object corresponding to `type`."

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