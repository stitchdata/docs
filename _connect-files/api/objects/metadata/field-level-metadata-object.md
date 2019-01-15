---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-structure"
key: "field-level-metadata-object"

# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Field-level Metadata"
description: "{{ api.data-structures.metadata.field-level.description | flatify }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
      # - If `automatic`, then `selected` will be `true`
      # - If `unsupported`, then `selected` will be `false`
      # - If `available`, then `selected` will be `false` until the field is selected

  - name: "inclusion"
    type: "string"
    description: |
      Indicates whether a field will be included all the time (`automatic`), none of the time (`unsupported`), or selected to be included or not (`available`).

      If a field is `unsupported`, the `unsupported-description` attribute may provide additonal information. **Note**: This is not available for all sources.
    modifiable: false
    applies-to: "all"
    value: |
      automatic

  - name: "selected"
    type: "boolean"
    description: |
      Indicates whether a field should be included in a stream's field selection list. This value will be present only if the [stream containing the field]({{ api.data-structures.metadata.stream-level.section }}) is selected (`selected: true`).

      Accepted values are:

      - `true` - The field is selected and data for the field will be replicated
      - `false` - The field is not selected and data for this field will not be replicated
    modifiable: true
    applies-to: "all"
    value: |
      true

  - name: "selected-by-default"
    type: "boolean"
    description: |
      Indicates whether a field will be included in a stream's field selection list if `selected` is not defined.
    modifiable: false
    applies-to: ""
    value: |
      true

  - name: "sql-datatype"
    type: "string"
    description: |
      **For database sources only.** The data type of a column from a database.
    modifiable: false
    applies-to: "db2, mysql, oracle, postgres"
    value: |
      text

  - name: "unsupported-description"
    type: "string"
    description: |
      The reason a field is unsupported (`inclusion: unsupported`).
    modifiable: false
    applies-to: "salesforce"
    value: |
      this field is unsupported by the Bulk API.

examples:
  - title: "Database source"
    code: |
      {
        "metadata": {
          "sql-datatype": "double precision",
          "selected-by-default": true,
          "inclusion": "available"
        }

  - title: "SaaS source"
    code: |
      {
        "metadata": {
          "selected": false,
          "inclusion": "available"
        }

  - title: "Unsupported field"
    code: |
      {
        "metadata": {
          "unsupported-description": "this field is unsupported by the Bulk API.",
          "selected": false,
          "inclusion": "unsupported"
        }
---