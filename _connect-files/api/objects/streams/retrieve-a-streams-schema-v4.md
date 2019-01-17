---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

content-type: "api-endpoint"
endpoint: "streams"
key: "retrieve-a-streams-schema"
version: "4"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Retrieve a stream's schema"
method: "get"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}/{stream_id}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.streams.retrieve-schema.short }}"
description: "{{ api.core-objects.streams.retrieve-schema.description | flatify }}"


# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

arguments:
  - name: "source_id"
    required: true
    type: "path parameter"
    description: |
      A path parameter corresponding to the [unique ID of the source]({{ api.core-objects.sources.object }}) containing the stream.
    example-value: |
      120643

  - name: "stream_id"
    required: true
    type: "path parameter"
    description: "A path parameter corresponding to the [unique ID of the stream]({{ api.core-objects.streams.object }}) to be retrieved."
    example-value: |
      2339248


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful and valid identifiers were provided, the API will return a status of <code class="api success">200 OK</code> and a single [Stream Schema Object]({{ api.data-structures.stream-schemas.section }}).


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    code: |
      {% assign right-bracket = "}" %}
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | replace: "{source_id","120643" | replace:"{stream_id","2339248" | remove: right-bracket | strip_newlines }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json"

  - type: "Response"
    code: |
      {
        "schema": "{\"properties\":{\"position\":{\"type\":[\"null\",\"integer\"]},\"created_at\":{\"type\":[\"null\",\"string\"],\"format\":\"date-time\"},\"sort_value\":{\"type\":[\"null\",\"string\"]},\"collection_id\":{\"type\":[\"null\",\"integer\"]},\"id\":{\"type\":[\"null\",\"integer\"]},\"product_id\":{\"type\":[\"null\",\"integer\"]},\"updated_at\":{\"type\":[\"null\",\"string\"],\"format\":\"date-time\"},\"featured\":{\"type\":[\"null\",\"boolean\"]}},\"type\":\"object\"}",
        "metadata": [
          {
            "breadcrumb": [],
            "metadata": {
              "forced-replication-method": "INCREMENTAL",
              "selected": true,
              "table-key-properties": [
                "id"
              ],
              "valid-replication-keys": [
                "updated_at"
              ]
            }
          },
          {
            "breadcrumb": [
              "properties",
              "collection_id"
            ],
            "metadata": {
              "inclusion": "available",
              "selected": true
            }
          },
          {
            "breadcrumb": [
              "properties",
              "created_at"
            ],
            "metadata": {
              "inclusion": "available",
              "selected": false
            }
          },
          {
            "breadcrumb": [
              "properties",
              "featured"
            ],
            "metadata": {
              "inclusion": "available",
              "selected": false
            }
          },
          {
            "breadcrumb": [
              "properties",
              "id"
            ],
            "metadata": {
              "inclusion": "automatic",
              "selected": false
            }
          },
          {
            "breadcrumb": [
              "properties",
              "position"
            ],
            "metadata": {
              "inclusion": "available",
              "selected": false
            }
          },
          {
            "breadcrumb": [
              "properties",
              "product_id"
            ],
            "metadata": {
              "inclusion": "available",
              "selected": false
            }
          },
          {
            "breadcrumb": [
              "properties",
              "sort_value"
            ],
            "metadata": {
              "inclusion": "available",
              "selected": false
            }
          },
          {
            "breadcrumb": [
              "properties",
              "updated_at"
            ],
            "metadata": {
              "inclusion": "automatic",
              "selected": false
            }
          }
        ],
        "non-discoverable-metadata-keys": [
          "selected",
          "replication-method",
          "replication-key",
          "view-key-properties"
        ]
      }

  - type: "Errors"
    # The errors live in: _data/connect/response-codes/streams.yml
---