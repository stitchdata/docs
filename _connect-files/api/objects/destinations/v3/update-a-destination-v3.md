---
content-type: "api-endpoint"
endpoint: "destinations"
key: "update-a-destination"
version: "3"


title: "Update a destination"
method: "put"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}/{destination_id}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.destinations.update.short }}"
description: "{{ api.core-objects.destinations.update.description | flatify }}"


arguments:
  - name: "destination_id"
    required: true
    type: "path parameter"
    description: "A path parameter corresponding to the unique ID of the destination to be updated."

  - name: "type"
    required: true
    type: "string"
    description: "{{ connect.common.attributes.destination-type | flatify }}"

  - name: "connection"
    required: true
    type: "object"
    description: "A [Destination Form Properties object]({{ api.form-properties.destination-forms.section }}) corresponding to the value of `type`."


returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and a [Destination object]({{ api.core-objects.destinations.object }}).


examples:
  - type: "Request"
    language: "json"
    code: |
      {% assign right-bracket = "}" %}
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | replace: "{destination_id","86741" | remove: right-bracket | strip_newlines }}
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

  - type: "Response"
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

  - type: "Errors"
---