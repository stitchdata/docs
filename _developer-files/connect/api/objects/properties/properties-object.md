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
    description: "The name of the property."
    value: |
      "frequency_in_minutes"

  - name: "required_to_be_fully_configured"
    type: "boolean"
    description: "If `true`, the property is required for complete configuration."
    value: |
      true

  - name: "provided"
    type: "boolean"
    description: "If `true`, the property has been provided."
    value: |
      true

  - name: "is_credential"
    type: "boolean"
    description: "If `true`, the property is a credential or otherwise sensitive data."
    value: |
      false

  - name: "system_provided"
    type: "boolean"
    description: "If `true`, the system provides this property."
    value: |
      false

  - name: "tap_mutable"
    type: "boolean"
    description: "**This is an internal field and is for Stitch use only.**"
    value: |
      false

  - name: "json_schema"
    type: "array"
    description: |
      **Note**: Data will only be returned for this array if `system_provided: false`.
      
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

examples:
  - code: |
      {
        "report_card":{  
            "type":"platform.hubspot",
            "current_step":2,
            "steps":[  
               {  
                  "type":"form",
                  "properties":[  
                     {  
                        "name":"image_version",
                        "is_required":true,
                        "provided":true,
                        "is_credential":false,
                        "system_provided":true,
                        "json_schema":null
                     },
                     {  
                        "name":"frequency_in_minutes",
                        "is_required":true,
                        "provided":true,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{  
                           "type":"string",
                           "pattern":"^\\d+$"
                        }
                     },
                     {  
                        "name":"start_date",
                        "is_required":true,
                        "provided":true,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{  
                           "type":"string",
                           "pattern":"^\\d{4}-\\d{2}-\\d{2}T00:00:00Z$"
                        }
                     }
                  ]
               }
            ]
         }
      }
---