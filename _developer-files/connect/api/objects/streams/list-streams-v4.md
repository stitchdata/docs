---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "streams"
key: "list-streams"
version: "4"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "List streams for a source"
method: "get"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ site.data.connect.core-objects.streams.list.description }}"
description: "{{ site.data.connect.core-objects.streams.list.description }}"


# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

arguments:
  - name: "source_id"
    required: true
    type: "path parameter"
    description: |
      A path parameter corresponding to the [unique ID of the source]({{ site.data.connect.core-objects.sources.object }}) containing the streams.
    example-value: |
      120643


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and an array of [Stream objects]({{ site.data.connect.core-objects.streams.object }}), one for each available stream in the source.


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    request-url: |
      {% assign right-bracket = "}" %}{{ endpoint.short-url | flatify | replace: "{source_id","120643" | remove: right-bracket | strip_newlines }}
    header: "{{ site.data.connect.request-headers.get.without-body | flatify }}"
    code: ""

  - type: "Response"
    subexamples:
      - title: "Streams for a database source"
        code: |
          [
            {
              "selected": null,
              "stream_id": 2289176,
              "tap_stream_id": "demni2mf59dt10-heroku-orders",
              "stream_name": "orders",
              "metadata": {
                "database-name": "demni2mf59dt10",
                "selected": null,
                "is-view": false,
                "row-count": 447,
                "schema-name": "heroku",
                "table-key-properties": [
                  "id"
                ]
              }
            },
            {
              "selected": null,
              "stream_id": 2343457,
              "tap_stream_id": "demni2mf59dt10-public-customers",
              "stream_name": "customers",
              "metadata": {
                "database-name": "demni2mf59dt10",
                "selected": null,
                "is-view": false,
                "row-count": 0,
                "schema-name": "public",
                "table-key-properties": [
                  "id"
                ]
              }
            },
            {
              "selected": true,
              "stream_id": 2288740,
              "tap_stream_id": "demni2mf59dt10-public-zapier_table",
              "stream_name": "addresses",
              "metadata": {
                "database-name": "demni2mf59dt10",
                "selected": true,
                "is-view": false,
                "replication-method": "FULL_TABLE",
                "row-count": 0,
                "schema-name": "public",
                "table-key-properties": [
                  "id"
                ]
              }
            },
            {
              "selected": false,
              "stream_id": 2375830,
              "tap_stream_id": "demni2mf59dt10-public-customer_view",
              "stream_name": "customer_view",
              "metadata": {
                "database-name": "demni2mf59dt10",
                "selected": false,
                "is-view": true,
                "replication-key": "id",
                "replication-method": "INCREMENTAL",
                "row-count": 0,
                "schema-name": "public",
                "table-key-properties": [],
                "view-key-properties": [
                  "id"
                ]
              }
            }
          ]

      - title: "Streams for a SaaS source"
        code: |
          [
            {
              "selected": true,
              "stream_id": 2288757,
              "tap_stream_id": "abandoned_checkouts",
              "stream_name": "abandoned_checkouts",
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
              "selected": true,
              "stream_id": 2288759,
              "tap_stream_id": "collects",
              "stream_name": "collects",
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
              "selected": null,
              "stream_id": 2288758,
              "tap_stream_id": "custom_collections",
              "stream_name": "custom_collections",
              "metadata": {
                "forced-replication-method": "INCREMENTAL",
                "selected": null,
                "table-key-properties": [
                  "id"
                ],
                "valid-replication-keys": [
                  "updated_at"
                ]
              }
            },
            {
              "selected": null,
              "stream_id": 2288756,
              "tap_stream_id": "customers",
              "stream_name": "customers",
              "metadata": {
                "forced-replication-method": "INCREMENTAL",
                "selected": null,
                "table-key-properties": [
                  "id"
                ],
                "valid-replication-keys": [
                  "updated_at"
                ]
              }
            },
            {
              "selected": null,
              "stream_id": 2288754,
              "tap_stream_id": "metafields",
              "stream_name": "metafields",
              "metadata": {
                "forced-replication-method": "INCREMENTAL",
                "selected": null,
                "table-key-properties": [
                  "id"
                ],
                "valid-replication-keys": [
                  "updated_at"
                ]
              }
            },
            {
              "selected": null,
              "stream_id": 2288751,
              "tap_stream_id": "order_refunds",
              "stream_name": "order_refunds",
              "metadata": {
                "forced-replication-method": "INCREMENTAL",
                "selected": null,
                "table-key-properties": [
                  "id"
                ],
                "valid-replication-keys": [
                  "created_at"
                ]
              }
            },
            {
              "selected": null,
              "stream_id": 2288753,
              "tap_stream_id": "orders",
              "stream_name": "orders",
              "metadata": {
                "forced-replication-method": "INCREMENTAL",
                "selected": null,
                "table-key-properties": [
                  "id"
                ],
                "valid-replication-keys": [
                  "updated_at"
                ]
              }
            },
            {
              "selected": null,
              "stream_id": 2288755,
              "tap_stream_id": "products",
              "stream_name": "products",
              "metadata": {
                "forced-replication-method": "INCREMENTAL",
                "selected": null,
                "table-key-properties": [
                  "id"
                ],
                "valid-replication-keys": [
                  "updated_at"
                ]
              }
            },
            {
              "selected": null,
              "stream_id": 2288752,
              "tap_stream_id": "transactions",
              "stream_name": "transactions",
              "metadata": {
                "forced-replication-method": "INCREMENTAL",
                "selected": null,
                "table-key-properties": [
                  "id"
                ],
                "valid-replication-keys": [
                  "created_at"
                ]
              }
            }
          ]  
---