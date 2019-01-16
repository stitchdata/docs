---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

content-type: "api-endpoint"
endpoint: "stream-schemas"
key: "update-a-streams-schema"
version: "4"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Select fields in a stream"
method: "put"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}/metadata
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.stream-schemas.update.short }}"
description: "{{ api.core-objects.stream-schemas.update.description | flatify }}"


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

  - name: "streams"
    required: true
    type: "array"
    description: |
      An array of objects corresponding to streams to be updated. More than one stream may be included in a single request. Every stream to be updated must be its own object.

      Objects are required to have the following properties:
    subarguments:
      - name: "stream_id"
        required: true
        type: "integer"
        description: "The [unique ID of the stream]({{ api.core-objects.stream-schemas.object }}) to be updated."

      - name: "metadata"
        required: true
        type: "array"
        description: |
          An array of [Field-level Metadata objects]({{ api.data-structures.metadata.field-level.section }}) corresponding to fields in the stream to be updated. More than one field must be included in a single request. Every field to be updated must be its own object.

  - name: "stream_id"
    required: true
    type: "path parameter"
    description: "A path parameter corresponding to the [unique ID of the stream]({{ api.core-objects.streams.object }}) to be updated."
    example-value: |
      2339248


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful and valid identifiers were provided, the API will return a status of <code class="api success">200 OK</code> and a single [Stream Schema Object]({{ api.core-objects.stream-schemas.object }}).


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    language: "json"
    subexamples: 
      - title: ""
        code: 

  - type: "Response"
    language: "json"
    code: 

  - type: "Errors"
    # The errors live in: _data/connect/response-codes/stream-schemas.yml
---