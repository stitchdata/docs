---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

content-type: "api-endpoint"
endpoint: "source-types"
key: "list-source-types"
version: "4"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "List source types"
method: "get"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.source-types.list.short }}"
description: "{{ api.core-objects.source-types.list.description | flatify }}"


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and an array of [Source Report Card objects]({{ api.data-structures.report-cards.source.section }}), one for each supported source `type`.


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "request"
    language: "json"
    code: |
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip_newlines }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json"

  - type: "response"
    language: "json"
    code: |
      HTTP/1.1 200 OK
      Content-Type: application/json;charset=ISO-8859-1

      [  
         {  
            "type":"platform.hubspot",                                /* HubSpot source */
            "current_step":1,
            "steps":[  
               {  
                  "type":"form",
                  "properties":[  
                     {  
                        "name":"image_version",
                        "is_required":true,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":true,
                        "json_schema":null
                     },
                     {  
                        "name":"frequency_in_minutes",
                        "is_required":true,
                        "provided":false,
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
                        "provided":false,
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
                  "properties":[  ]
               },
               {  
                  "type":"field_selection",
                  "properties":[  ]
               },
               {  
                  "type":"fully_configured",
                  "properties":[  ]
               }
            ]
         },
         {  
            "type":"platform.marketo",                                /* Marketo source */
            "current_step":1,
            "steps":[  
               {  
                  "type":"form",
                  "properties":[  
                     {  
                        "name":"image_version",
                        "is_required":true,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":true,
                        "json_schema":null
                     },
                     {  
                        "name":"frequency_in_minutes",
                        "is_required":true,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{  
                           "type":"string",
                           "pattern":"^\\d+$"
                        }
                     },
                     {  
                        "name":"client_id",
                        "is_required":true,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{  
                           "type":"string"
                        }
                     },
                     {  
                        "name":"client_secret",
                        "is_required":true,
                        "provided":false,
                        "is_credential":true,
                        "system_provided":false,
                        "json_schema":{  
                           "type":"string"
                        }
                     },
                     {  
                        "name":"endpoint",
                        "is_required":true,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{  
                           "type":"string",
                           "format":"uri"
                        }
                     },
                     {  
                        "name":"identity",
                        "is_required":true,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{  
                           "type":"string",
                           "format":"uri"
                        }
                     },
                     {  
                        "name":"max_daily_calls",
                        "is_required":false,
                        "provided":false,
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
                        "provided":false,
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
                  "type":"fully_configured",
                  "properties":[  ]
               }
            ]
         },
         {  
            "type":"platform.zuora",                                  /* Zuora source */
            "current_step":1,
            "steps":[  
               {  
                  "type":"form",
                  "properties":[  
                     {  
                        "name":"image_version",
                        "is_required":true,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":true,
                        "json_schema":null
                     },
                     {  
                        "name":"frequency_in_minutes",
                        "is_required":true,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{  
                           "type":"string",
                           "pattern":"^\\d+$"
                        }
                     },
                     {  
                        "name":"european",
                        "is_required":false,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{  
                           "type":"string",
                           "pattern":"^(true|false)$"
                        }
                     },
                     {  
                        "name":"password",
                        "is_required":true,
                        "provided":false,
                        "is_credential":true,
                        "system_provided":false,
                        "json_schema":{  
                           "type":"string"
                        }
                     },
                     {  
                        "name":"sandbox",
                        "is_required":false,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{  
                           "type":"string",
                           "pattern":"^(true|false)$"
                        }
                     },
                     {  
                        "name":"start_date",
                        "is_required":true,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{  
                           "type":"string",
                           "pattern":"^\\d{4}-\\d{2}-\\d{2}T00:00:00Z$"
                        }
                     },
                     {  
                        "name":"username",
                        "is_required":true,
                        "provided":false,
                        "is_credential":true,
                        "system_provided":false,
                        "json_schema":{  
                           "type":"string"
                        }
                     }
                  ]
               },
               {  
                  "type":"discover_schema",
                  "properties":[  ]
               },
               {  
                  "type":"field_selection",
                  "properties":[  ]
               },
               {  
                  "type":"fully_configured",
                  "properties":[  ]
               }
            ]
         },
         {  
            "type":"platform.salesforce",                             /* Salesforce source */
            "current_step":1,
            "steps":[  
               {  
                  "type":"form",
                  "properties":[  
                     {  
                        "name":"image_version",
                        "is_required":true,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":true,
                        "json_schema":null
                     },
                     {  
                        "name":"frequency_in_minutes",
                        "is_required":true,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{  
                           "type":"string",
                           "pattern":"^\\d+$"
                        }
                     },
                     {  
                        "name":"api_type",
                        "is_required":true,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{  
                           "type":"string",
                           "pattern":"^(REST|BULK)$"
                        }
                     },
                     {  
                        "name":"is_sandbox",
                        "is_required":false,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{  
                           "type":"string",
                           "pattern":"^(true|false)$"
                        }
                     },
                     {  
                        "name":"quota_percent_per_run",
                        "is_required":false,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{  
                           "type":"string",
                           "pattern":"^\\d+$"
                        }
                     },
                     {  
                        "name":"quota_percent_total",
                        "is_required":false,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{  
                           "type":"string",
                           "pattern":"^\\d+$"
                        }
                     },
                     {  
                        "name":"select_fields_by_default",
                        "is_required":true,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{  
                           "type":"string",
                           "pattern":"^(true|false)$"
                        }
                     },
                     {  
                        "name":"start_date",
                        "is_required":true,
                        "provided":false,
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
                        "system_provided":false,
                        "json_schema":{  
                           "type":"string"
                        }
                     },
                     {  
                        "name":"client_secret",
                        "is_required":true,
                        "provided":false,
                        "is_credential":true,
                        "system_provided":false,
                        "json_schema":{  
                           "type":"string"
                        }
                     },
                     {  
                        "name":"instance_url",
                        "is_required":true,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{  
                           "type":"string",
                           "format":"uri"
                        }
                     },
                     {  
                        "name":"orgid",
                        "is_required":false,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{  
                           "type":"string"
                        }
                     },
                     {  
                        "name":"refresh_token",
                        "is_required":true,
                        "provided":false,
                        "is_credential":true,
                        "system_provided":false,
                        "json_schema":{  
                           "type":"string"
                        }
                     }
                  ]
               },
               {  
                  "type":"discover_schema",
                  "properties":[  ]
               },
               {  
                  "type":"field_selection",
                  "properties":[  ]
               },
               {  
                  "type":"fully_configured",
                  "properties":[  ]
               }
            ]
         },
         {  
            "type":"platform.yotpo",                                  /* Yotpo source */
            "current_step":1,
            "steps":[  
               {  
                  "type":"form",
                  "properties":[  
                     {  
                        "name":"image_version",
                        "is_required":true,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":true,
                        "json_schema":null
                     },
                     {  
                        "name":"frequency_in_minutes",
                        "is_required":true,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{  
                           "type":"string",
                           "pattern":"^\\d+$"
                        }
                     },
                     {  
                        "name":"api_key",
                        "is_required":true,
                        "provided":false,
                        "is_credential":true,
                        "system_provided":false,
                        "json_schema":{  
                           "type":"string"
                        }
                     },
                     {  
                        "name":"api_secret",
                        "is_required":true,
                        "provided":false,
                        "is_credential":true,
                        "system_provided":false,
                        "json_schema":{  
                           "type":"string"
                        }
                     },
                     {  
                        "name":"start_date",
                        "is_required":true,
                        "provided":false,
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
                  "type":"discover_schema",
                  "properties":[  ]
               },
               {  
                  "type":"field_selection",
                  "properties":[  ]
               },
               {  
                  "type":"fully_configured",
                  "properties":[  ]
               }
            ]
         },
         {  
            "type":"platform.sendgrid",                               /* SendGrid source */
            "current_step":1,
            "steps":[  
               {  
                  "type":"form",
                  "properties":[  
                     {  
                        "name":"image_version",
                        "is_required":true,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":true,
                        "json_schema":null
                     },
                     {  
                        "name":"frequency_in_minutes",
                        "is_required":true,
                        "provided":false,
                        "is_credential":false,
                        "system_provided":false,
                        "json_schema":{  
                           "type":"string",
                           "pattern":"^\\d+$"
                        }
                     },
                     {  
                        "name":"api_key",
                        "is_required":true,
                        "provided":false,
                        "is_credential":true,
                        "system_provided":false,
                        "json_schema":{  
                           "type":"string"
                        }
                     },
                     {  
                        "name":"start_date",
                        "is_required":true,
                        "provided":false,
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
                  "type":"discover_schema",
                  "properties":[  ]
               },
               {  
                  "type":"field_selection",
                  "properties":[  ]
               },
               {  
                  "type":"fully_configured",
                  "properties":[  ]
               }
            ]
         }
      ]
---