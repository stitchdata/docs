---
content-type: "api-endpoint"
endpoint: "destinations"
key: "create-a-destination"
version: "3"
order: 1


title: "Create a destination"
method: "post"
short-url: |
  /v{{ object.version }}{{ object.endpoint-url }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.destinations.create.short }}"
description: "{{ api.core-objects.destinations.create.description | flatify }}"


arguments:
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
  - type: "request"
    language: "json"
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
      HTTP/1.1 200 OK
      Content-Type: application/json;charset=ISO-8859-1

      {
        "id":"<DESTINATION_ID>",
        "type":"redshift",
        "created_at":"2018-02-06T15:36:36Z",
        "updated_at":"2018-02-06T15:36:36Z",
        "connection": {
            "host":"<HOST>",
            "port":5439,
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