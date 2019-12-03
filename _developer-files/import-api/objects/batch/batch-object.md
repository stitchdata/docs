---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "import-api"
content-type: "api-object"
endpoint: "batch"
version: "2"
order: 2


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Batch"
description: "{{ site.data.import-api.core-objects.batch.object | flatify }}"
endpoint-url: "/import/batch"


# -------------------------- #
#        VERSION INFO        #
# -------------------------- #

latest-version: "2"
versions:
  - number: "2"
    deprecated: false

# -------------------------- #
#      AVAILABLE METHODS     #
# -------------------------- #

available-methods:
  - id: "batch-data"
    title: "Create a batch"
    method: "post"
    short: "{{ site.data.import-api.core-objects.batch.description | flatify }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

## The copy for these attributes lives in:
## _data/import-api/general.yml

object-attributes:
  - name: "table_name"
    type: "string"
    description: |
      {{ general.attributes.table-name | remove: "A single request can push data to multiple tables." }}
    value: "customers"

  # - name: "table_version"
  #   type: "integer"
  #   description: "{{ general.attributes.table-version | flatify }}"
  #   value: "1"

  - name: "schema"
    type: "object"
    sub-type: "schema"
    url: "{{ site.data.import-api.data-structures.schema.section }}"
    description: |
      A [Schema object]({{ site.data.import-api.data-structures.schema.section }}) containing the JSON schema describing the record(s) in the [Message object's]({{ site.data.import-api.data-structures.message.section }}) `data` property.

      Records must conform to this schema or an error will be returned when the request is sent.
    value: ""

  - name: "messages"
    type: "array"
    sub-type: "message"
    url: "{{ site.data.import-api.data-structures.message.section }}"
    description: |
      An array of [Message]({{ site.data.import-api.data-structures.message.section }}) objects, each representing a record to be upserted into the table.

  - name: "key_names"
    type: "array"
    description: |
      An array of strings representing the Primary Key fields in the source table. **Note**: A value must be provided, but it may be an empty list to indicate that the source table doesn't have a Primary Key.

      If fields are provided, they must comply with the following:

      1. Each field in the list must be the name of a top-level property defined in the [Schema object]({{ site.data.import-api.data-structures.schema.section }}). Primary Key fields cannot be contained in an object or an array.
      2. Fields in the list may not be `null` in the source.
      3. If a field is a string, its value must be less than 256 characters.

      All fields included in `key_names` must be present in the [Schema object]({{ site.data.import-api.data-structures.schema.section }}) and every [Message object]({{ site.data.import-api.data-structures.message.section }}) in the request.
    value: "id"
---