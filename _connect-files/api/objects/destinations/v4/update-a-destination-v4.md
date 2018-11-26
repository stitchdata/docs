---
content-type: "api-endpoint"
endpoint: "destinations"
key: "update-a-destination"
version: "4"


title: "Update a destination"
method: "put"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}/{id}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.destinations.update.short }}"
description: "{{ api.core-objects.destinations.update.description | flatify }}"


arguments:
  - name: "id"
    required: true
    type: "path parameter"
    description: "A path parameter corresponding to the unique ID of the destination to be updated."

  - name: "type"
    required: true
    type: "string"
    description: "{{ connect.common.attributes.destination-type | flatify }}"

  - name: "properties"
    required: true
    type: "object"
    description: "A [Destination Form Properties object]({{ api.form-properties.destination-forms.section }}) corresponding to the value of `type`."


returns: |
  If successful, the API will return a status of `200 OK` and a [Destination object]({{ api.core-objects.destinations.object }}) with a `report_card` property.


examples:
  - type: "request"
    language: "json"
    code: |
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip_newlines }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json"
           -d "{
                "type":"postgres",
                "properties": {
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
      HTTP/1.1 200 OK
      Content-Type: application/json;charset=ISO-8859-1

      {
        "id":"<DESTINATION_ID>",
        "type":"postgres",
        "created_at":"2018-02-06T15:36:36Z",
        "updated_at":"2018-02-06T18:55:43Z",
        "connection": {
            "host":"<HOST>",
            "port":5432,
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

  - type: "errors"
---