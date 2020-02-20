---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-sub-structure"
key: "field-level-metadata-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Field-level Metadata"
description: |
  {% include misc/data-files.html %}
  {{ api.data-structures.metadata.field-level.description | flatify }}

  Refer to the [Field selection and compatibility rules guide]({{ link.connect.guides.field-selection-compatibility-rules | prepend: site.baseurl }}) for info about selection and compatibility rules.


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "inclusion"
    type: "string"
    description: |
      Indicates when a field will be included. Possible values are:

      - `automatic` - The field is included all the time, regardless of `selected-by-default` and `selected` values
      - `available` - The field is available for selection. The field will be included if `selected-by-default` or `selected` is `true`.
      - `unsupported` - The field is unsupported and will not be included, regardless of `selected-by-default` and `selected` values

      If a field is `unsupported`, the `unsupported-description` attribute may provide additonal information.
    modifiable: false
    applies-to: "all"
    value: |
      automatic

  - name: "selected"
    type: "boolean"
    description: |
      Indicates whether a field should be included in a stream's field selection list. This value will be present only if the [stream containing the field]({{ api.data-structures.metadata.stream-level.section }}) is selected (`selected: true`).

      - `null` - The value has not been set
      - `true` - The field is selected
      - `false` - The field is not selected
    modifiable: true
    applies-to: "all"
    value: |
      true

  - name: "selected-by-default"
    type: "boolean"
    description: |
      Indicates if a field will be selected by default. Possible values are:

      - `null` - The value has not been set
      - `true` - The field is selected by default and is included regardless of the `selected` value
      - `false` - The field is not selected by default. The field will be included if the `selected` value is `true`.
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

  - name: "fieldExclusions"
    type: "array"
    description: |
      A list of arrays, each array containing an array of strings that correspond to fields that are incompatible when the current field is selected.

      For example: If the metadata for a `DeviceOS` field contains a `fieldExclusion` of `["properties":"ImpressionLostToBidPercent"]`, then the `DeviceOS` and `ImpressionLostToBidPercent` fields cannot be selected together in the stream.

      Refer to the example tabs below for an example of this property.
    modifiable: false
    value: |
      "fieldExclusions": [
        [
          "properties",
          "BidMatchType"
        ],
        [
          "properties",
          "DeviceOS"
        ],
        [
          "properties",
          "TopVsOther"
        ]
      ]

  - name: "unsupported-description"
    type: "string"
    description: |
      The reason a field is unsupported (`inclusion: unsupported`). **Note**: This is not available for all sources.
    modifiable: false
    applies-to: "salesforce"
    value: |
      this field is unsupported by the Bulk API.

examples:
  - type: "Database source"
    code: |
      {
        "metadata": {
          "sql-datatype": "double precision",
          "selected-by-default": true,
          "inclusion": "available"
        }

  - type: "SaaS source"
    code: |
      {
        "metadata": {
          "selected": false,
          "inclusion": "available"
        }

  - type: "Field exclusions"
    code: |
      {{ site.data.connect.code-examples.field-metadata.field-exclusion }}

  - type: "Unsupported field"
    code: |
      {{ site.data.connect.code-examples.field-metadata.unsupported-field }}
---