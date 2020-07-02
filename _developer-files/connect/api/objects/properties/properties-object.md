---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-structure"
key: "properties-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Properties"
description: "{{ api.data-structures.properties.description | flatify }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "name"
    type: "string"
    description: &name-desc "The name of the property."
    oauth-description: *name-desc
    value: |
      "frequency_in_minutes"

  - name: "is_required"
    type: "boolean"
    description: "If `true`, the property is required for complete configuration."
    oauth-description: "If `true`, the property is required for OAuth configuration."
    value: |
      true

  - name: "is_credential"
    type: "boolean"
    description: &credential-desc "If `true`, the property is a credential or otherwise sensitive data. **Note**: Values for this property won't be returned by the API."
    oauth-description: *credential-desc
    value: |
      false

  - name: "system_provided"
    type: "boolean"
    deprecated: true
    description: |
      **This property has been deprecated.** Use the `property_type` property instead.
    value: |
      false

  - name: "property_type"
    type: "string"
    description: |
      Indicates the type of the property. Possible values are:

      - `user_provided` - Indicates the property must be set by the user.
      - `read_only` - Indicates the property is read-only and is not settable by the API. Generally, this is an internal field set inside of Stitch.
      - `system_provided_by_default` - Indicates the property used to be `system_provided: true`, but can now be set by the API consumer. These are generally properties associated with OAuth for generating refresh and access tokens.

         **Note**: Use caution when setting these properties, as using incorrect values can put the source into a non-functioning state.
    oauth-description: |
      Indicates the type of the property. For OAuth properties, possible values are:

      - `user_provided` - Indicates the property must be set by you.
      - `system_provided_by_default` - Indicates that the property is provided by Stitch by default, but can be set by you. **Note**: Use caution when setting these properties, as incorrect values may put the source into a non-functioning state.
    value: "user_provided"

  - name: "json_schema"
    type: "array"
    description: |
      **Note**: Data will only be returned for this array if `property_type: user_provided` or `property_type: system_provided_by_default`. If `property_type: read_only`, this property will be `null`.
      
      An array containing:

      - `type` - A `string` indicating the expected data type of the property's value. For example: `boolean`
      - `pattern` - A `string` indicating the expected pattern of the property's value. For example: `^\\d+$`
      - `anyOf` - A series of arrays containing key-value pairs for the `type` and `format` combinations Stitch will accept as the property's value. For example:

          ```json
          "anyOf": [
              {
                  "type": "string",
                  "format": "ipv4"
              },
              {
                  "type": "string",
                  "format": "ipv6"
              },
              {
                  "type": "string",
                  "format": "hostname"
              }
          ]
          ```
    oauth-description: |
      An array containing:

      - `type` - A `string` indicating the expected data type of the property's value. For example: `boolean`
      - `pattern` - A `string` indicating the expected pattern of the property's value. For example: `^\\d+$`
      - `anyOf` - A series of arrays containing key-value pairs for the `type` and `format` combinations Stitch will accept as the property's value.

  - name: "provided"
    type: "boolean"
    description: &provided-desc "If `true`, the property has been provided. For properties where `property_type: user_provided`, this indicates that the user has provided the property."
    oauth-description: "If `true`, the property has been provided. For properties where `property_type: user_provided`, this indicates that you have provided the property."
    value: |
      true

  - name: "tap_mutable"
    type: "boolean"
    description: "**This is an internal field and is for Stitch use only.**"
    value: |
      false

examples:
  - type: "User-provided property"
    code: |
        {
          "name": "frequency_in_minutes",
          "is_required": false,
          "is_credential": false,
          "system_provided": false,
          "property_type": "user_provided",
          "json_schema": {
            "type": "string",
            "pattern": "^1$|^30$|^60$|^360$|^720$|^1440$"
          },
          "provided": false,
          "tap_mutable": false
        }

  - type: "Read-only property"
    code: |
      {
        "name": "image_version",
        "is_required": true,
        "is_credential": false,
        "system_provided": true,
        "property_type": "read_only",
        "json_schema": null,
        "provided": false,
        "tap_mutable": false
      }

  - type: "System provided by default property"
    code: |
      {
        "name": "client_id",
        "is_required": true,
        "is_credential": true,
        "system_provided": true,
        "property_type": "system_provided_by_default",
        "json_schema": {
          "type": "string"
        },
        "provided": false,
        "tap_mutable": false
      }
---