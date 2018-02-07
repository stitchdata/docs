---
content-type: "embed-endpoint"
endpoint: "destinations"
key: "update-a-destination"
version: "3"
order: 2


title: "Update a destination"
method: "put"
short-url: |
  /v{{ object.version }}{{ object.endpoint-url }}/{id}
full-url: |
  {{ page.api-base-url }}{{ endpoint.short-url | flatify }}
description: "Updates a destination. Modifications to the `type` attribute are not supported."


arguments:
  - name: "id"
    required: true
    description: "A path parameter corresponding to the unique ID of the destination to be updated."

  - name: "type"
    required: true
    description: |
      The destination type, which is one of: 

      - `redshift`
      - `postgres`
      - `snowflake`

  - name: "connection"
    required: true
    description: "A [Destination Form Properties object]({{ page.anchors.form-properties.destination-forms.section }}) corresponding to the value of `type`."


returns: "A [Destination object]({{ page.anchors.core-objects.destinations.object }})."


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

  - type: "response"
    language: "json"
    code: |
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
    language: "json"
    errors:
      - name: "Invalid destination ID"
        type: &400 "400 Bad Request"
        fix-it: |
          Occurs when the ID passed in the request URL is invalid.
        code: |
          "invalid connection id"

      - name: "Incorrect type"
        type: *400
        fix-it: |
          Occurs when the value of `type` doesn't match the existing value.

          For example: If the destination was created with a `type` of `redshift` and you attempt to update it with `type: postgres`.
        code: |
          "this API endpoint does not support modifying destination type"

      - name: "Prohibited arguments"
        type: *400
        fix-it: |
          Occurs when:

          - Arguments other than `type` and `connection` are included in the request
          - Properties in the `connection` argument are incorrectly typed. For example: `port` is sent as a `string` instead of an `integer`

        code: |
            "body must be a map with type = redshift, postgres, or snowflake. required-keys = type, connection"
---