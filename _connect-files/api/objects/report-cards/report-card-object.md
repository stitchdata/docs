---
content-type: "api-structure"
key: "report-card-object"

title: "Report Card"
description: "{{ api.data-structures.report-cards.description }}"

object-attributes:
  - name: "current_step"
    type: "integer"
    description: "The index (in the `steps` array) of the current step needed to configure the data source."

  - name: "current_step_hints"
    type: "object"
    sub-type: "current step hints "
    url: "{{ api.data-structures.current-step-hints.section }}"
    description: |
      If the current step requires the user to interact with the Stitch interface, this object will provide the function to call and properties to pass to [Stitch.js]({{ js.section | flatify | prepend: site.baseurl }}).

      Otherwise, this object will provide information about the next call to make to the API.

  - name: "steps"
    type: "array"
    description: "A sequential list of [Connection Step objects]({{ api.data-structures.connection-steps.section }}) required to complete configuration for the connection type."

  - name: "type"
    type: "string"
    description: "The connection type. Ex: `platform.salesforce` or `platform.hubspot`"

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
               },
               {
                  "type":"oauth",
                  "properties":[
                     {
                        "name":"client_id",
                        "is_required":true,
                        "provided":false,
                        "is_credential":true,
                        "system_provided":true,
                        "json_schema":{
                           "type":"string"
                        }
                     },
                     {
                        "name":"client_secret",
                        "is_required":true,
                        "provided":false,
                        "is_credential":true,
                        "system_provided":true,
                        "json_schema":{
                           "type":"string"
                        }
                     },
                     {
                        "name":"redirect_uri",
                        "is_required":true,
                        "provided":false,
                        "is_credential":true,
                        "system_provided":true,
                        "json_schema":{
                           "type":"string",
                           "format":"uri"
                        }
                     },
                     {
                        "name":"refresh_token",
                        "is_required":true,
                        "provided":false,
                        "is_credential":true,
                        "system_provided":true,
                        "json_schema":{
                           "type":"string"
                        }
                     }
                  ]
               },
               {
                  "type":"discover_schema",
                  "properties":[

                  ]
               },
               {
                  "type":"field_selection",
                  "properties":[

                  ]
               },
               {
                  "type":"fully_configured",
                  "properties":[

                  ]
               }
            ],
            "current_step_hints":{
               "js":{
                  "function":"authorizeSource",
                  "options":{
                     "id":<SOURCE_ID>
                  }
               }
            }
         }
      }
---