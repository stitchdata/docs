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
    description: |
      Indicates whether the Stitch client who made the request has access to the connection.

      This value is based on the connection's `pricing_tier` and `pipeline_state`. If the Stitch client is using a plan that doesn’t meet the `pricing_tier` requirement, the `access` value will be `false`. For example: If `pricing_tier: enterprise`,the Stitch client must be on an Enterprise plan to access the source.

      All connections with a `pipeline_state` value of `deprecated` will also have an `access` value of `false`.
    value: |
      true

  - name: "default_scheduling_interval"
    type: "integer"
    description: |
      **Applicable only to source report cards.** The default `frequency_in_minutes` value for the source.
    value: |
      30

  - name: "pricing_tier"
    type: "string"
    description: |
      Indicates the type of Stitch plan required to use the connection. Possible values are:

      - `standard` - Any Stitch plan can use the connection.
      - `enterprise` - An Enterprise Stitch plan is required to use the connection.
    value: |
      "standard"

  - name: "default_start_date"
    type: "string"
    description: |
      **Applicable only to source report cards.** The default `start_date` value for the source.
    value: |
      "-1 year"

  - name: "pipeline_state"
    type: "string"
    description: |
      The connection `type`'s release status in Stitch. Possible values are:

      - `alpha` - The connection is in development and is not available in Stitch.
      - `beta` - The connection is in open or closed beta and is available in Stitch.
      - `released` - The connection is in general release and available in Stitch.
      - `deprecated` - The connection has been deprecated and is no longer available in Stitch.
    value: |
      "released"

  - name: "protocol"
    type: "string"
    description: "The `type` of the connection. For example: `snowflake` or `platform.facebook`"
    value: |
      "snowflake"

examples:
  - type: "Destination connection"
    code: |
      {  
         "details":{  
            "pricing_tier":"standard",
            "pipeline_state":"released",
            "protocol":"snowflake",
            "access":true
         }
      }

  - type: "Source connection"
    code: |
      {
         "details":{
            "pricing_tier":"enterprise",
            "pipeline_state":"released",
            "default_scheduling_interval":60,
            "default_start_date": null,
            "protocol":"platform.oracle",
            "access":false
         }
      }
---