---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-object"
endpoint: "stream-schemas"
order: 9


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Stream Schema"
description: "{{ api.core-objects.stream-schemas.description }}"
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
  - id: "retrieve-a-streams-schema"
    title: "Retrieve a stream's schema"
    method: "get"
    short: "{{ api.core-objects.stream-schemas.retrieve.description | flatify }}"

  - id: "update-a-streams-schema"
    title: "Select fields in a stream"
    method: "put"
    short: "{{ api.core-objects.stream-schemas.update.description | flatify }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "schema"
    type: "object"
    description: "The JSON schema describing the stream's fields."

  - name: "metadata"
    type: "array"
    description: |
      An array containing objects with the following properties:
    subattributes:
      - name: "breadcrumbs"
        type: "array"
        description: |
          An array of strings describing a path into the schema. For example:

          - A value of `[]` refers to the entire schema, or stream
          - A value of `["properties", "id"]` refers to the `properties.id` portion of the schema, or a field named `id`

      - name: "metadata"
        type: "object"
        description: |
          An object containing metadata associated with the `breadcrumb`. The type of metadata object depends on the `breadcrumb`:

           - For the entire schema (`breadcrumb: []`), this will be a [Stream-level Metadata object]({{ api.data-structures.metadata.stream-level.section }})
           - For an individual field (`breadcrumb: ["properties", "{field_name}"]`), this will be a [Field-level Metadata object]({{ api.data-structures.metadata.field-level.section }})

  - name: "non-discoverable-metadata-keys"
    type: "array"
    description: |
      An array of strings corresponding to `metadata` keys that can be modified.
    value: |
      "selected",
      "replication-method",
      "replication-key"
---