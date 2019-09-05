---
content-type: "api-endpoint"
endpoint: "sources"
key: "pause-a-source"
version: "4"


title: "Pause a source"
method: "put"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}/{source_id}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.sources.pause.description }}"
description: |
  {{ api.core-objects.sources.pause.description }} When a source is paused, Stitch will not automatically start replication jobs for the source. Manual replication jobs can still be started using the [Start a replication job endpoint](#start-a-job), however.

  **Note**: This endpoint behaves identically to [Update a source](#update-a-source).

arguments:
  - name: "source_id"
    required: true
    type: "path parameter"
    description: "A path parameter corresponding to the unique ID of the source to be paused."
    example-value: |
      86741

  - name: "paused_at"
    required: false
    type: "timestamp"
    description: |
      The time the source was paused. This field must contain an [ISO 8601-compliant](https://en.wikipedia.org/wiki/ISO_8601){:target="new"} date.

      **Note**: Providing any value - past, present, or future - for this property will pause the source immediately if the request is successful.
    example-value: |
      "2019-06-01T00:00:00Z"


returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and a [Source object]({{ api.core-objects.sources.object }}) with a populated `paused_at` value.

examples:
  - type: "Request"
    language: "json"
    code: |
      {% assign right-bracket = "}" %}
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | replace: "{source_id","86741" | remove: right-bracket | strip_newlines }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json"
           -d "{
                 "paused_at":"2019-06-01T00:00:00Z"
               }"

  - type: "Response"
    language: "json"
    code: |
      {
         "properties":{
            "anchor_time":"2019-01-30T18:16:37.205Z",
            "cron_expression":null,
            "frequency_in_minutes":"60",
            "image_version":"1.latest",
            "product":"pipeline",
            "shop":"stitchdatawearhouse",
            "start_date":"2017-01-01T00:00:00Z"
         },
         "updated_at":"2019-05-28T13:52:23Z",
         "schedule":null,
         "name":"shopify",
         "type":"platform.shopify",
         "deleted_at":null,
         "system_paused_at":null,
         "stitch_client_id":116078,
         "paused_at":"2019-06-01T00:00:00Z",
         "id":86741,
         "display_name":"Shopify",
         "created_at":"2019-01-10T19:38:18Z",
         "report_card":{
            "type":"platform.shopify",
            "current_step":1,
            "current_step_type":"fully_configured",
            "steps":[
               {
                  "type":"form",
                  "properties":[
                     {
                        "name":"anchor_time",
                        "is_required":false,
                        "is_credential":false,
                        "system_provided":false,
                        "property_type":"user_provided",
                        "json_schema":{
                           "type":"string",
                           "format":"date-time"
                        },
                        "provided":true,
                        "tap_mutable":false
                     },
                     {
                        "name":"cron_expression",
                        "is_required":false,
                        "is_credential":false,
                        "system_provided":false,
                        "property_type":"user_provided",
                        "json_schema":null,
                        "provided":false,
                        "tap_mutable":false
                     },
                     {
                        "name":"date_window_size",
                        "is_required":false,
                        "is_credential":false,
                        "system_provided":false,
                        "property_type":"user_provided",
                        "json_schema":{
                           "type":"integer"
                        },
                        "provided":false,
                        "tap_mutable":false
                     },
                     {
                        "name":"frequency_in_minutes",
                        "is_required":false,
                        "is_credential":false,
                        "system_provided":false,
                        "property_type":"user_provided",
                        "json_schema":{
                           "type":"string",
                           "pattern":"^1$|^30$|^60$|^360$|^720$|^1440$"
                        },
                        "provided":true,
                        "tap_mutable":false
                     },
                     {
                        "name":"image_version",
                        "is_required":true,
                        "is_credential":false,
                        "system_provided":true,
                        "property_type":"read_only",
                        "json_schema":null,
                        "provided":true,
                        "tap_mutable":false
                     },
                     {
                        "name":"shop",
                        "is_required":true,
                        "is_credential":false,
                        "system_provided":false,
                        "property_type":"user_provided",
                        "json_schema":{
                           "type":"string"
                        },
                        "provided":true,
                        "tap_mutable":false
                     },
                     {
                        "name":"start_date",
                        "is_required":true,
                        "is_credential":false,
                        "system_provided":false,
                        "property_type":"user_provided",
                        "json_schema":{
                           "type":"string",
                           "pattern":"^\\d{4}-\\d{2}-\\d{2}T00:00:00Z$"
                        },
                        "provided":true,
                        "tap_mutable":false
                     }
                  ]
               },
               {
                  "type":"oauth",
                  "properties":[
                     {
                        "name":"api_key",
                        "is_required":true,
                        "is_credential":true,
                        "system_provided":true,
                        "property_type":"system_provided_by_default",
                        "json_schema":{
                           "type":"string"
                        },
                        "provided":false,
                        "tap_mutable":false
                     }
                  ]
               },
               {
                  "type":"discover_schema",
                  "properties":[

                  ]
               },
               {
                  "type":"field_selection",
                  "properties":[

                  ]
               },
               {
                  "type":"fully_configured",
                  "properties":[

                  ]
               }
            ]
         }
      }
---