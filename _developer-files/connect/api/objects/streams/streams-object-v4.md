---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

type: "connect"
content-type: "api-object"
endpoint: "streams"
order: 8


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Stream"
description: "{{ api.core-objects.streams.description }}"
endpoint-url: "/sources/{source_id}/streams"


# -------------------------- #
#        VERSION INFO        #
# -------------------------- #

latest-version: "4"
versions:
  - number: "4"
    deprecated: false


# -------------------------- #
#      AVAILABLE METHODS     #
# -------------------------- #

available-methods:
  - id: "list-streams"
    title: "List streams for a source"
    method: "get"
    short: "{{ api.core-objects.streams.list.description | flatify }}"

  - id: "retrieve-a-streams-schema"
    title: "Retrieve a stream's schema"
    method: "get"
    short: "{{ api.core-objects.streams.retrieve-schema.description | flatify }}"

  - id: "update-a-streams-metadata"
    title: "Update a stream's metadata"
    method: "put"
    short: "{{ api.core-objects.streams.update.description | flatify }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "stream_id"
    type: "integer"
    description: "The stream ID."
    
  - name: "selected"
    type: "boolean"
    description: |
      Indicates if the stream is selected for replication. Possible values are:

      - `null` - Only present if a stream has never been selected. Otherwise, this value will be `true` if selected, and `false` if de-selected.
      - `true` - The stream is selected and data will be replicated for all selected fields
      - `false` - The stream is not selected and data for this stream will not be replicated

  - name: "stream_name"
    type: "string"
    description: "The name of the stream. This value may not be unique. For example: A database with multiple schemas can have the same stream name in multiple schemas."

  - name: "tap_stream_id"
    type: "string"
    description: |
      The unique version of the stream name.

      For database sources, this value will be the database name, schema name, and table name, combined.

  - name: "metadata"
    type: "object"
    sub-type: "stream level metadata"
    url: "{{ api.data-structures.metadata.stream-level.section }}"
    description: |
      {{ api.data-structures.metadata.stream-level.short }}


# -------------------------- #
#      OBJECT EXAMPLES       #
# -------------------------- #

examples:
  - type: "Database source (non view)"
    code: |
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
      }

  - type: "Database source (view)"
    code: |
      {
        "selected": true,
        "stream_id": 2375830,
        "tap_stream_id": "demni2mf59dt10-public-customer_view",
        "stream_name": "customer_view",
        "metadata": {
          "database-name": "demni2mf59dt10",
          "selected": true,
          "is-view": true,
          "replication-key": "id",
          "replication-method": "INCREMENTAL",
          "row-count": 125,
          "schema-name": "public",
          "table-key-properties": [],
          "view-key-properties": [
            "id"
          ]
        }
      }

  - type: "SaaS source"
    code: |
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
      }
---