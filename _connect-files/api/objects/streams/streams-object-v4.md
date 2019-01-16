---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

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

  - id: "update-a-stream"
    title: "Select a stream"
    method: "put"
    short: "{{ api.core-objects.streams.update.description | flatify }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "stream_id"
    type: "integer"
    description: "The stream ID."

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
      Details about the stream.
---