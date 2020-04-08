---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "streams"
key: "update-a-streams-metadata"
version: "4"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Update a stream's metadata"
method: "put"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}/metadata
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.streams.update.short }}"
description: |
  {% include misc/data-files.html %}
  {{ api.core-objects.streams.update.description | flatify }}

  Refer to the [Select streams and fields guide]({{ link.connect.guides.select-streams-and-fields | prepend: site.baseurl }}) for instructions on selecting streams and fields.


# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

arguments:
  - name: "source_id"
    required: true
    type: "path parameter"
    description: |
      A path parameter corresponding to the [unique ID of the source]({{ api.core-objects.sources.object }}) containing the stream(s).
    example-value: |
      120643

  - name: "streams"
    required: true
    type: "array"
    description: |
      An array of [Stream objects]({{ api.core-objects.streams.object }}), with each object corresponding to a stream to be updated.

      Each object is required to have the following properties:
    subarguments:
      - name: "tap_stream_id"
        required: true
        type: "string"
        description: "The `tap_stream_id` of the [stream]({{ api.data-structures.stream-schemas.section }}) to be updated."

      - name: "metadata"
        required: true
        type: "array"
        description: |
          An array of [Metadata objects]({{ api.data-structures.metadata.top-level.section }}) with each object corresponding to a field in the stream to be updated. More than one field may be included in a single request.

          Each object is required to have the following properties:
        sub-subarguments:
          - name: "breadcrumb"
            required: true
            type: "array"
            description: |
              An array of strings describing a path into the schema:

              - To refer to the stream itself, this value should be `[]`, or an empty array. The associated `metadata` object should include modifable [Stream-level Metadata object properties]({{ api.data-structures.metadata.stream-level.section }}).

              - To refer to a specific field, the value should be `["properties", "<FIELD_NAME>"]`, where `<FIELD_NAME>` represents the name of an included field. For example: `["properties", "first_name"]` refers to a field named `first_name`. The associated `metadata` object should include modifable [Field-level Metadata object properties]({{ api.data-structures.metadata.field-level.section }}).

              **Note**: To select fields, the stream must also be selected. To select a stream, one `metadata` object for the stream should have a `breadcrumb` that is an empty array (`[]`). this is only required to initially select the stream. See the **Request** tab below for an example.

          - name: "metadata"
            required: true
            type: "object"
            description: |
              The properties in the stream's [Stream Schema object]({{ api.data-structures.stream-schemas.section }})
              `non-discoverable-metadata-keys` property:

              - If `breadcrumb` refers to the stream, modifiable properties in a [Stream-level Metadata object]({{ api.data-structures.metadata.stream-level.section }})
              - If `breadcrumb` refers to a field, modifiable properties in a [Field-level Metadata object]({{ api.data-structures.metadata.field-level.section }})


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and a JSON body of:

  ```json
  {
    "status": 200
  }
  ```


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    language: "json"
    subexamples: 
      - type: "Selecting a single stream"
        code: |
          {% capture request-header %}{% assign right-bracket = "}" %}curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | replace: "{source_id","120645" | remove: right-bracket | strip_newlines }} \
               -H "Authorization: Bearer <ACCESS_TOKEN>" \
               -H "Content-Type: application/json" \
               -d "{
          {% endcapture %}{{ request-header | flatify | rstrip }}
                     "streams": [
                       {
                         "tap_stream_id": "custom_collections",
                         "metadata": [
                           {
                             "breadcrumb": [],
                             "metadata": {
                               "selected": true
                             }
                           }
                         ]
                       }
                     ]
                   }"

      - type: "Selecting a single stream and multiple fields"
        code: |
          {{ request-header | flatify | rstrip }}
                     "streams": [
                       {
                         "tap_stream_id": "custom_collections",
                         "metadata": [
                           {
                             "breadcrumb": [],
                             "metadata": {
                               "selected": true
                             }
                           },
                           {
                             "breadcrumb": [
                               "properties",
                               "title"
                             ],
                             "metadata": {
                               "selected": true
                             }
                           },
                           {
                             "breadcrumb": [
                               "properties",
                               "published_at"
                             ],
                             "metadata": {
                               "selected": true
                             }
                           }
                         ]
                       }
                     ]
                   }"

      - type: "Selecting multiple streams and fields"
        code: |
          {{ request-header | flatify | rstrip }}
                     "streams": [
                        {
                          "tap_stream_id": "custom_collections",
                          "metadata": [
                            {
                              "breadcrumb": [],
                              "metadata": {
                                "selected": true
                              }
                            },
                            {
                              "breadcrumb": [
                                "properties",
                                "title"
                              ],
                              "metadata": {
                                "selected": true
                              }
                            },
                            {
                              "breadcrumb": [
                                "properties",
                                "published_at"
                              ],
                              "metadata": {
                                "selected": true
                              }
                            }
                          ]
                        },
                        {
                          "tap_stream_id": "customers",
                          "metadata": [
                            {
                              "breadcrumb": [],
                              "metadata": {
                                "selected": true
                              }
                            },
                            {
                              "breadcrumb": [
                                "properties",
                                "first_name"
                              ],
                              "metadata": {
                                "selected": true
                              }
                            },
                            {
                              "breadcrumb": [
                                "properties",
                                "last_name"
                              ],
                              "metadata": {
                                "selected": true
                              }
                            }
                          ]
                        }
                      ]
                    }'

      - type: "Selecting a database table and defining replication"
        code: |
          {{ request-header | flatify | rstrip }}
                     "streams": [
                       {
                         "tap_stream_id": "demni2mf59dt10-public-customers",
                         "metadata": [
                           {
                             "breadcrumb": [],
                             "metadata": {
                               "selected": true,
                               "replication-method": "INCREMENTAL",
                               "replication-key": "updated_at"
                             }
                           },
                           {
                             "breadcrumb": [
                               "properties",
                               "name"
                             ],
                             "metadata": {
                               "selected": true
                             }
                           },
                           {
                             "breadcrumb": [
                               "properties",
                               "has_magic"
                             ],
                             "metadata": {
                               "selected": true
                             }
                           }
                         ]
                       }
                     ]
                   }"

      - type: "Selecting a database view and defining replication"
        code: |
          {{ request-header | flatify | rstrip }}
                     "streams": [
                         {
                           "tap_stream_id": "demni2mf59dt10-public-customer_view",
                           "metadata": [
                             {
                               "breadcrumb": [],
                               "metadata": {
                                 "replication-key": "updated_at",
                                 "view-key-properties": [
                                   "id"
                                 ],
                                 "replication-method": "INCREMENTAL",
                                 "selected": true
                               }
                             },
                             {
                               "breadcrumb": [
                                 "properties",
                                 "name"
                               ],
                               "metadata": {
                                 "selected": true
                               }
                             },
                             {
                               "breadcrumb": [
                                 "properties",
                                 "has_magic"
                               ],
                               "metadata": {
                                 "selected": true
                               }
                             }
                           ]
                         }
                       ]
                     }"

  - type: "Response"
    subexamples:
      - type: "Applicable to all requests"
        code: |
            {
              "status": 200
            }

  - type: "Errors"
    # The errors live in: _data/connect/response-codes/streams.yml
---
