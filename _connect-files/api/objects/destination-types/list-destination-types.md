---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

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
description: "{{ api.core-objects.destination-types.list.description | flatify }}"


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and an array of [Destination Report Card objects]({{ api.data-structures.report-cards.destination.section }}), one for each supported destination `type`.


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
      [
        {
          "type": "azure_sqldw",
          "current_step": 1,
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "host",
                  "is_required": true,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
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
                  }
                },
                {
                  "name": "port",
                  "is_required": true,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+$"
                  }
                },
                {
                  "name": "username",
                  "is_required": true,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string"
                  }
                },
                {
                  "name": "password",
                  "is_required": true,
                  "provided": false,
                  "is_credential": true,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string"
                  }
                },
                {
                  "name": "azure_storage_account_token",
                  "is_required": true,
                  "provided": false,
                  "is_credential": true,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string"
                  }
                },
                {
                  "name": "azure_storage_sas_url",
                  "is_required": true,
                  "provided": false,
                  "is_credential": true,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string"
                  }
                },
                {
                  "name": "database",
                  "is_required": true,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string"
                  }
                },
                {
                  "name": "encryption_type",
                  "is_required": true,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(ssh|none)$"
                  }
                },
                {
                  "name": "encryption_host",
                  "is_required": false,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
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
                  }
                },
                {
                  "name": "encryption_port",
                  "is_required": false,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+$"
                  }
                },
                {
                  "name": "encryption_username",
                  "is_required": false,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string"
                  }
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
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "database",
                  "is_required": true,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string"
                  }
                },
                {
                  "name": "encryption_host",
                  "is_required": false,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
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
                  }
                },
                {
                  "name": "encryption_port",
                  "is_required": false,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+$"
                  }
                },
                {
                  "name": "encryption_type",
                  "is_required": true,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(ssh|none)$"
                  }
                },
                {
                  "name": "encryption_username",
                  "is_required": false,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string"
                  }
                },
                {
                  "name": "host",
                  "is_required": true,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
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
                  }
                },
                {
                  "name": "password",
                  "is_required": true,
                  "provided": false,
                  "is_credential": true,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string"
                  }
                },
                {
                  "name": "port",
                  "is_required": true,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+$"
                  }
                },
                {
                  "name": "username",
                  "is_required": true,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string"
                  }
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
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "database",
                  "is_required": true,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string"
                  }
                },
                {
                  "name": "encryption_host",
                  "is_required": false,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
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
                  }
                },
                {
                  "name": "encryption_port",
                  "is_required": false,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+$"
                  }
                },
                {
                  "name": "encryption_type",
                  "is_required": true,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(ssh|none)$"
                  }
                },
                {
                  "name": "encryption_username",
                  "is_required": false,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string"
                  }
                },
                {
                  "name": "host",
                  "is_required": true,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
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
                  }
                },
                {
                  "name": "password",
                  "is_required": true,
                  "provided": false,
                  "is_credential": true,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string"
                  }
                },
                {
                  "name": "port",
                  "is_required": true,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+$"
                  }
                },
                {
                  "name": "ssl",
                  "is_required": true,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "boolean"
                  }
                },
                {
                  "name": "sslrootcert",
                  "is_required": false,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string"
                  }
                },
                {
                  "name": "username",
                  "is_required": true,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string"
                  }
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
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "database",
                  "is_required": true,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string"
                  }
                },
                {
                  "name": "host",
                  "is_required": true,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
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
                  }
                },
                {
                  "name": "password",
                  "is_required": true,
                  "provided": false,
                  "is_credential": true,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string"
                  }
                },
                {
                  "name": "port",
                  "is_required": true,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+$"
                  }
                },
                {
                  "name": "role",
                  "is_required": false,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string"
                  }
                },
                {
                  "name": "username",
                  "is_required": true,
                  "provided": false,
                  "is_credential": true,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string"
                  }
                },
                {
                  "name": "warehouse",
                  "is_required": true,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string"
                  }
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
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "csv_delimiter",
                  "is_required": false,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string"
                  }
                },
                {
                  "name": "csv_force_quote",
                  "is_required": false,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(true|false)$"
                  }
                },
                {
                  "name": "output_file_format",
                  "is_required": true,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(csv|jsonl)$"
                  }
                },
                {
                  "name": "s3_bucket",
                  "is_required": true,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string"
                  }
                },
                {
                  "name": "s3_key_format_string",
                  "is_required": true,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string"
                  }
                },
                {
                  "name": "sentinel_key",
                  "is_required": true,
                  "provided": false,
                  "is_credential": true,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string",
                    "pattern": "^stitch-challenge-file-.*$"
                  }
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
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "access_key_id",
                  "is_required": true,
                  "provided": false,
                  "is_credential": true,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string"
                  }
                },
                {
                  "name": "csv_delimiter",
                  "is_required": false,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string"
                  }
                },
                {
                  "name": "csv_force_quote",
                  "is_required": false,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(true|false)$"
                  }
                },
                {
                  "name": "endpoint",
                  "is_required": true,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
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
                  }
                },
                {
                  "name": "output_file_format",
                  "is_required": true,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(csv|jsonl)$"
                  }
                },
                {
                  "name": "port",
                  "is_required": true,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+$"
                  }
                },
                {
                  "name": "s3_bucket",
                  "is_required": true,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string"
                  }
                },
                {
                  "name": "s3_key_format_string",
                  "is_required": true,
                  "provided": false,
                  "is_credential": false,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string"
                  }
                },
                {
                  "name": "secret_access_key",
                  "is_required": true,
                  "provided": false,
                  "is_credential": true,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string"
                  }
                },
                {
                  "name": "sentinel_key",
                  "is_required": true,
                  "provided": false,
                  "is_credential": true,
                  "system_provided": false,
                  "json_schema": {
                    "type": "string",
                    "pattern": "^stitch-challenge-file-.*$"
                  }
                }
              ]
            },
            {
              "type": "fully_configured",
              "properties": []
            }
          ],
          "details": {
            "pricing_tier": "default",
            "pipeline_state": "alpha",
            "protocol": "storagegrid",
            "access": false
          }
        }
      ]
---