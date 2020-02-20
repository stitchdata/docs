---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "destination-types"
key: "list-destination-types"
version: "4"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "List destination types"
method: "get"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.destination-types.list.short }}"
description: |
  {{ api.core-objects.destination-types.list.description | flatify }}

  Refer to the [Destination and source API availability reference]({{ link.connect.guides.connection-reference | prepend: site.baseurl | append: "#destinations-api-availability" }}) for info on the destinations that are available in the API.


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and an array of [Destination Report Card objects]({{ api.data-structures.report-cards.destination.section }}), one for each supported destination `type`.


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    language: "json"
    code: |
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip_newlines }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json"

  - type: "Response"
    language: "json"
    code: |
      [
        {
          "type": "azure_sqldw",
          "current_step": 1,
          "current_step_type": "form",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "host",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
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
                  },
                  "provided": false
                },
                {
                  "name": "port",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+$"
                  },
                  "provided": false
                },
                {
                  "name": "username",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                },
                {
                  "name": "password",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                },
                {
                  "name": "azure_storage_account_token",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                },
                {
                  "name": "azure_storage_sas_url",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "format": "uri"
                  },
                  "provided": false
                },
                {
                  "name": "database",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                },
                {
                  "name": "encryption_type",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(ssh|none)$"
                  },
                  "provided": false
                },
                {
                  "name": "encryption_host",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
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
                  },
                  "provided": false
                },
                {
                  "name": "encryption_port",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+$"
                  },
                  "provided": false
                },
                {
                  "name": "encryption_username",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                }
              ]
            },
            {
              "type": "fully_configured",
              "properties": []
            }
          ],
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "beta",
            "protocol": "azure_sqldw",
            "access": true
          }
        },
        {
          "type": "redshift",
          "current_step": 1,
          "current_step_type": "form",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "database",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                },
                {
                  "name": "encryption_host",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
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
                  },
                  "provided": false
                },
                {
                  "name": "encryption_port",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+$"
                  },
                  "provided": false
                },
                {
                  "name": "encryption_type",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(ssh|none)$"
                  },
                  "provided": false
                },
                {
                  "name": "encryption_username",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                },
                {
                  "name": "host",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
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
                  },
                  "provided": false
                },
                {
                  "name": "password",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                },
                {
                  "name": "port",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+$"
                  },
                  "provided": false
                },
                {
                  "name": "username",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                }
              ]
            },
            {
              "type": "fully_configured",
              "properties": []
            }
          ],
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "released",
            "protocol": "redshift",
            "access": true
          }
        },
        {
          "type": "postgres",
          "current_step": 1,
          "current_step_type": "form",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "database",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                },
                {
                  "name": "encryption_host",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
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
                  },
                  "provided": false
                },
                {
                  "name": "encryption_port",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+$"
                  },
                  "provided": false
                },
                {
                  "name": "encryption_type",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(ssh|none)$"
                  },
                  "provided": false
                },
                {
                  "name": "encryption_username",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                },
                {
                  "name": "host",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
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
                  },
                  "provided": false
                },
                {
                  "name": "password",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                },
                {
                  "name": "port",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+$"
                  },
                  "provided": false
                },
                {
                  "name": "ssl",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "boolean"
                  },
                  "provided": false
                },
                {
                  "name": "sslrootcert",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                },
                {
                  "name": "username",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                }
              ]
            },
            {
              "type": "fully_configured",
              "properties": []
            }
          ],
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "released",
            "protocol": "postgres",
            "access": true
          }
        },
        {
          "type": "snowflake",
          "current_step": 1,
          "current_step_type": "form",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "database",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                },
                {
                  "name": "host",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
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
                  },
                  "provided": false
                },
                {
                  "name": "password",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                },
                {
                  "name": "port",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+$"
                  },
                  "provided": false
                },
                {
                  "name": "role",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                },
                {
                  "name": "username",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                },
                {
                  "name": "warehouse",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                }
              ]
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
        },
        {
          "type": "s3",
          "current_step": 1,
          "current_step_type": "form",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "csv_delimiter",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                },
                {
                  "name": "csv_force_quote",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(true|false)$"
                  },
                  "provided": false
                },
                {
                  "name": "output_file_format",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(csv|jsonl)$"
                  },
                  "provided": false
                },
                {
                  "name": "s3_bucket",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                },
                {
                  "name": "s3_key_format_string",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                },
                {
                  "name": "sentinel_key",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "system_provided_by_default",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^stitch-challenge-file-.*$"
                  },
                  "provided": false
                }
              ]
            },
            {
              "type": "fully_configured",
              "properties": []
            }
          ],
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "released",
            "protocol": "s3",
            "access": true
          }
        },
        {
          "type": "storagegrid",
          "current_step": 1,
          "current_step_type": "form",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "access_key_id",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                },
                {
                  "name": "csv_delimiter",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                },
                {
                  "name": "csv_force_quote",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(true|false)$"
                  },
                  "provided": false
                },
                {
                  "name": "endpoint",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
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
                  },
                  "provided": false
                },
                {
                  "name": "output_file_format",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(csv|jsonl)$"
                  },
                  "provided": false
                },
                {
                  "name": "port",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+$"
                  },
                  "provided": false
                },
                {
                  "name": "s3_bucket",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                },
                {
                  "name": "s3_key_format_string",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                },
                {
                  "name": "secret_access_key",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                },
                {
                  "name": "sentinel_key",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "system_provided_by_default",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^stitch-challenge-file-.*$"
                  },
                  "provided": false
                }
              ]
            },
            {
              "type": "fully_configured",
              "properties": []
            }
          ],
          "details": {
            "pricing_tier": "enterprise",
            "pipeline_state": "alpha",
            "protocol": "storagegrid",
            "access": false
          }
        }
      ]
---