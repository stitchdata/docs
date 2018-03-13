---
content-type: "api-endpoint"
endpoint: "sources"
key: "create-a-source"
version: "4"
order: 1


title: "Create a source"
method: "post"
short-url: |
  /v{{ object.version }}{{ object.endpoint-url }}
full-url: |
  {{ page.api-base-url }}{{ endpoint.short-url | flatify }}
description: |
  Creates a source object, which is the first step in setting up a new data source. After the source object is created, additional configuration steps must be completed.

  The configuration process is unique for each type of source. Use the source's `report_card` object's `current_step` attribute to identify the current `step` in configuring the source.

  The `report_card` object's `current_step_hints` attribute will assist you in guiding the user to [Stitch.js]({{ page.anchors.stitch-js.section }}) to complete the current step.


arguments:
  - name: "display_name"
    required: true
    description: "A descriptive name for the source. This will be used to dynamically generate the name corresponding to the schema name or dataset name that the data from this source will be loaded into."

  - name: "type"
    required: true
    description: "The source type. For example: `platform.marketo` or `platform.hubspot`."

  - name: "properties"
    required: false
    description: "A source [Properties object]({{ page.anchors.data-structures.properties }}) corresponding to the value of `type`."


returns: "A [Source object]({{ page.anchors.core-objects.sources.object }}) with a `report_card` property, which contains the [Report Card object]({{ page.anchors.data-structures.report-cards }}) for the source's configuration status."


examples:
  - type: "request"
    language: "curl"
    code: |
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip_newlines }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json"
           -d "{
                   "type":"platform.hubspot",
                   "display_name":"HubSpot",
                   "properties":{
                      "start_date":"2017-01-01T00:00:00Z",
                      "frequency_in_minutes":"30"
                   }
                }"
  - type: "response"
    language: "json"
    code: |
      {
         "properties":{
            "frequency_in_minutes":"30",
            "image_version":"1.latest",
            "start_date":"2017-01-01T00:00:00Z"
         },
         "updated_at":"2018-02-06T16:25:06Z",
         "check_job_name":null,
         "name":"hubspot",
         "type":"platform.hubspot",
         "deleted_at":null,
         "system_paused_at":null,
         "stitch_client_id":<ACCOUNT_ID>,
         "paused_at":null,
         "id":<SOURCE_ID>,
         "display_name":"HubSpot",
         "created_at":"2018-02-06T16:25:06Z",
         "report_card":{
            "type":"platform.hubspot",
            "current_step":2,
            "steps":[
               {
                  "type":"form",
                  "properties":[
                     {
                        "name":"image_version",
                        "is_required":true,
                        "provided":true,
                        "is_credential":false,
                        "system_provided":true,
                        "json_schema":null
                     },
                     {
                        "name":"frequency_in_minutes",
                        "is_required":true,
                        "provided":true,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{
                           "type":"string",
                           "pattern":"^\\d+$"
                        }
                     },
                     {
                        "name":"start_date",
                        "is_required":true,
                        "provided":true,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{
                           "type":"string",
                           "pattern":"^\\d{4}-\\d{2}-\\d{2}T00:00:00Z$"
                        }
                     }
                  ]
               },
               {
                  "type":"oauth",
                  "properties":[
                     {
                        "name":"client_id",
                        "is_required":true,
                        "provided":false,
                        "is_credential":true,
                        "system_provided":true,
                        "json_schema":{
                           "type":"string"
                        }
                     },
                     {
                        "name":"client_secret",
                        "is_required":true,
                        "provided":false,
                        "is_credential":true,
                        "system_provided":true,
                        "json_schema":{
                           "type":"string"
                        }
                     },
                     {
                        "name":"redirect_uri",
                        "is_required":true,
                        "provided":false,
                        "is_credential":true,
                        "system_provided":true,
                        "json_schema":{
                           "type":"string",
                           "format":"uri"
                        }
                     },
                     {
                        "name":"refresh_token",
                        "is_required":true,
                        "provided":false,
                        "is_credential":true,
                        "system_provided":true,
                        "json_schema":{
                           "type":"string"
                        }
                     }
                  ]
               },
               {
                  "type":"discover_schema",
                  "properties":[ ]
               },
               {
                  "type":"field_selection",
                  "properties":[ ]
               },
               {
                  "type":"fully_configured",
                  "properties":[ ]
               }
            ],
            "current_step_hints":{
               "js":{
                  "function":"authorizeSource",
                  "options":{
                     "id":<SOURCE_ID>
                  }
               }
            }
         }
      }

  - type: "errors"
    language: "json"
    errors:
      - name: "Existing integration"
        type: &400 "400 Bad Request"
        fix-it: |
          Occurs when the source's `display_name` is already in use. Stitch uses the `display_name` attribute to dynamically generate a corresponding schema name - the `name` attribute in the [Source Object](#source-object) - in the connected destination for the integration.

          As schema names must be unique to prevent collisions, sources created through the API must have unique `display_name` values upon creation. A source's `display_name` attribute can be changed after creation by using the [Update a Source](#) endpoint.

          For example: If you create an integration with a `display_name` of `HubSpot` and then attempt to create a second integration with `display_name: HubSpot`, you'll receive the response below. To resolve the error, use a unique `display_name` value to create the source.
        code: |
            "a source of name <NAME> already exists"

      - name: "Prohibited arguments"
        type: *400
        fix-it: |
          Occurs when arguments other than `display_name`, `type`, and `properties` are included in the request.

        code: |
            "POST body may only include a type, a display_name and map of string properties"

      - name: "Bad properties"
        type: *400
        fix-it: |
          Occurs when the `properties` argument is included and contains invalid data. The response will include `bad_properties`, which is an array containing the names of the properties deemed to be incorrect for the source `type`.

          Possible reasons for this include:

          - Incorrectly formatted data
          - Incorrectly typed data - all properties must be sent as strings
          - A property is included but doesn't have a value, or is an empty string

          For example: The value of `start_date` is an empty string or sent in a format other than `YYYY-MM-DDTHH:MM:SSZ`. If the following request were sent:

          ```curl
          curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip_newlines }}
               -H "Authorization: Bearer <ACCESS_TOKEN>" 
               -H "Content-Type: application/json"
               -d "{
                       "type":"platform.hubspot",
                       "display_name":"HubSpot",
                       "properties":{
                          "start_date":"2017-01-01 00:00:00",
                          "frequency_in_minutes":""
                       }
                    }"
          ```

          It would result in the following response:
        code: |
          {
             "bad_properties":[
                "start_date",
                "frequency_in_minutes"
             ],
             ...
          }

---