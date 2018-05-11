---
content-type: "api-structure"
key: "properties-object"

title: "Properties"
description: "{{ api.data-structures.properties.description | flatify }}"

object-attributes:
  - name: "name"
    type: "string"
    description: "The name of the property."

  - name: "required_to_be_fully_configured"
    type: "boolean"
    description: "If `true`, the property is required for complete configuration."

  - name: "provided"
    type: "boolean"
    description: "If `true`, the property has been provided."

  - name: "is_credential"
    type: "boolean"
    description: "If `true`, the property is a credential or otherwise sensitive data."

  - name: "system_provided"
    type: "boolean"
    description: "If `true`, the system provides this property."

  - name: "json_schema"
    type: "array"
    description: |
      An array containing:

      - `type` - The expected data type of the property's value. For example: `string`
      - `pattern` - The expected pattern of the property's value. For example: `^\\d+$`

      Data will only be returned for this array if `system_provided: false`.

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