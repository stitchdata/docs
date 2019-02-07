---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-structure"
key: "details-object"

# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Details"
description: "{{ api.data-structures.details.description | flatify }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "access"
    type: "boolean"
    description: "If `true`, the connection can be used for the Stitch client account being accessed."
    value: |
      true

  - name: "pricing_tier"
    type: "string"
    description: |
      Indicates the type of Stitch plan required to use the connection. Possible values are:

      - `standard` - Any Stitch plan can use the connection.
      - `premium` - A paid Stitch plan is required to use the connection.
      - `enterprise` - An Enterprise Stitch plan is required to use the connection.
    value: |
      "standard"

  - name: "pipeline_state"
    type: "string"
    description: |
      The connection `type`'s release status in Stitch. Possible values are:

      - `alpha` - The connection is in development.
      - `beta` - The connection is in open or closed beta.
      - `released` - The connection is in general release.
      - `deprecated` - The connection has been deprecated.
    value: |
      "released"

  - name: "protocol"
    type: "string"
    description: "The `type` of the connection. For example: `snowflake` or `redshift`"
    value: |
      "snowflake"

examples:
  - code: |
      {
        "type": "snowflake",
        "current_step": 1,
        "steps": [
          {
            "type": "form",
            "properties": []
          },
          {
            "type": "fully_configured",
            "properties": []
          }
        ],
        "details": {
          "pricing_tier": "standard",
          "pipeline_state": "released",
          "protocol": "snowflake",
          "access": true
        }
      }
---