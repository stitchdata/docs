---
content-type: "embed-endpoint"
endpoint: "sources"
key: "update-a-source"
version: "4"
order: 2


title: "Update a source"
method: "put"
short-url: |
  /v{{ object.version }}{{ object.endpoint-url }}/{id}
full-url: |
  {{ page.api-base-url }}{{ endpoint.short-url | flatify }}
description: "Updates a data source object."


arguments:
  - name: "id"
    required: true
    description: "A path parameter corresponding to the unique ID of the data source to be updated."

  - name: "display_name"
    required: false
    description: "A descriptive name for the source. This will be used to dynamically generate the name corresponding to the schema name or dataset name that the data from this source will be loaded into."

  - name: "properties"
    required: false
    description: "A source properties object corresponding to the value of `type`."


returns: "A source object."

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
  # - type: "response"
  #   language: ""
  #   code: |

---