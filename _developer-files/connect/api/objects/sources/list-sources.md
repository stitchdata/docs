---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "sources"
key: "list-sources"
version: "4"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "List sources"
method: "get"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ site.data.connect.core-objects.sources.list.description }}"
description: |
  {{ site.data.connect.core-objects.sources.list.description }}

  **Note**: This endpoint retrieves specific configuration information about the sources connected to a single account. To retrieve general configuration information about all supported data source types, use the [List all source types]({{ site.data.connect.core-objects.source-types.list.anchor }}) endpoint.


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and an array of [Source Objects]({{ site.data.connect.core-objects.sources.object }}), one for each source connected to the account.

  
# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    request-url: "{{ endpoint.short-url | flatify | strip_newlines }}"
    header: "{{ site.data.connect.request-headers.get | flatify }}"
    code: ""

  - type: "Response"
    code: |
      [
        {
          "properties": {
            "anchor_time": "2019-01-07T23:23:08.116Z",
            "cron_expression": null,
            "customer_ids": "1585293495,4224806558,6668731595",
            "frequency_in_minutes": "30",
            "image_version": "1.latest",
            "product": "pipeline",
            "start_date": "2018-01-01T00:00:00Z",
            "user_id": "100551921296891141132"
          },
          "updated_at": "2019-04-12T19:03:13Z",
          "schedule": null,
          "name": "adwords",
          "type": "platform.adwords",
          "deleted_at": "2019-01-09T17:28:57Z",
          "system_paused_at": null,
          "stitch_client_id": 116078,
          "paused_at": null,
          "id": 119945,
          "display_name": "AdWords2",
          "created_at": "2019-01-07T23:20:22Z",
          "report_card": {
            "type": "platform.adwords",
            "current_step": 5,
            "current_step_type": "fully_configured",
            "steps": [
              {
                "type": "form",
                "properties": [
                  {
                    "name": "anchor_time",
                    "is_required": false,
                    "is_credential": false,
                    "system_provided": false,
                    "property_type": "user_provided",
                    "json_schema": {
                      "type": "string",
                      "format": "date-time"
                    },
                    "provided": true,
                    "tap_mutable": false
                  },
                  {
                    "name": "cron_expression",
                    "is_required": false,
                    "is_credential": false,
                    "system_provided": false,
                    "property_type": "user_provided",
                    "json_schema": null,
                    "provided": false,
                    "tap_mutable": false
                  },
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
                    "provided": true,
                    "tap_mutable": false
                  },
                  {
                    "name": "image_version",
                    "is_required": true,
                    "is_credential": false,
                    "system_provided": true,
                    "property_type": "read_only",
                    "json_schema": null,
                    "provided": true,
                    "tap_mutable": false
                  },
                  {
                    "name": "start_date",
                    "is_required": true,
                    "is_credential": false,
                    "system_provided": false,
                    "property_type": "user_provided",
                    "json_schema": {
                      "type": "string",
                      "pattern": "^\\d{4}-\\d{2}-\\d{2}T00:00:00Z$"
                    },
                    "provided": true,
                    "tap_mutable": false
                  }
                ]
              },
              {
                "type": "oauth",
                "properties": [
                  {
                    "name": "customer_ids",
                    "is_required": true,
                    "is_credential": false,
                    "system_provided": false,
                    "property_type": "user_provided",
                    "json_schema": {
                      "type": "string"
                    },
                    "provided": true,
                    "tap_mutable": false
                  },
                  {
                    "name": "developer_token",
                    "is_required": true,
                    "is_credential": true,
                    "system_provided": true,
                    "property_type": "system_provided_by_default",
                    "json_schema": {
                      "type": "string"
                    },
                    "provided": true,
                    "tap_mutable": false
                  },
                  {
                    "name": "oauth_client_id",
                    "is_required": true,
                    "is_credential": true,
                    "system_provided": true,
                    "property_type": "system_provided_by_default",
                    "json_schema": {
                      "type": "string"
                    },
                    "provided": true,
                    "tap_mutable": false
                  },
                  {
                    "name": "oauth_client_secret",
                    "is_required": true,
                    "is_credential": true,
                    "system_provided": true,
                    "property_type": "system_provided_by_default",
                    "json_schema": {
                      "type": "string"
                    },
                    "provided": true,
                    "tap_mutable": false
                  },
                  {
                    "name": "refresh_token",
                    "is_required": true,
                    "is_credential": true,
                    "system_provided": true,
                    "property_type": "system_provided_by_default",
                    "json_schema": {
                      "type": "string"
                    },
                    "provided": true,
                    "tap_mutable": false
                  },
                  {
                    "name": "user_id",
                    "is_required": true,
                    "is_credential": false,
                    "system_provided": true,
                    "property_type": "system_provided_by_default",
                    "json_schema": {
                      "type": "string"
                    },
                    "provided": true,
                    "tap_mutable": false
                  }
                ]
              },
              {
                "type": "discover_schema",
                "properties": []
              },
              {
                "type": "field_selection",
                "properties": []
              },
              {
                "type": "fully_configured",
                "properties": []
              }
            ]
          }
        },
        {
          "properties": {
            "anchor_time": "2019-01-09T19:30:00.000Z",
            "user_agent": "Stitch-c7ad6999-c6d8-4504-9ae6-b153717fdd3e",
            "oauth_s3_path": "116078-120407-xero",
            "organization_name": "Stitch Xero",
            "frequency_in_minutes": "60",
            "product": "pipeline",
            "oauth_s3_bucket": "com-stitchdata-prod-platform-oauth-creds",
            "start_date": "2018-01-09T19:15:49Z",
            "cron_expression": null,
            "image_version": "1.latest"
          },
          "updated_at": "2019-05-24T16:21:57Z",
          "schedule": null,
          "name": "xero",
          "type": "platform.xero",
          "deleted_at": null,
          "system_paused_at": null,
          "stitch_client_id": 116078,
          "paused_at": "2019-01-22T18:04:48Z",
          "id": 120407,
          "display_name": "Xero",
          "created_at": "2019-01-09T19:16:03Z",
          "report_card": {
            "type": "platform.xero",
            "current_step": 4,
            "current_step_type": "field_selection",
            "steps": [
              {
                "type": "form",
                "properties": [
                  {
                    "name": "anchor_time",
                    "is_required": false,
                    "is_credential": false,
                    "system_provided": false,
                    "property_type": "user_provided",
                    "json_schema": {
                      "type": "string",
                      "format": "date-time"
                    },
                    "provided": true,
                    "tap_mutable": false
                  },
                  {
                    "name": "cron_expression",
                    "is_required": false,
                    "is_credential": false,
                    "system_provided": false,
                    "property_type": "user_provided",
                    "json_schema": null,
                    "provided": false,
                    "tap_mutable": false
                  },
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
                    "provided": true,
                    "tap_mutable": false
                  },
                  {
                    "name": "image_version",
                    "is_required": true,
                    "is_credential": false,
                    "system_provided": true,
                    "property_type": "read_only",
                    "json_schema": null,
                    "provided": true,
                    "tap_mutable": false
                  },
                  {
                    "name": "start_date",
                    "is_required": true,
                    "is_credential": false,
                    "system_provided": false,
                    "property_type": "user_provided",
                    "json_schema": {
                      "type": "string",
                      "pattern": "^\\d{4}-\\d{2}-\\d{2}T00:00:00Z$"
                    },
                    "provided": true,
                    "tap_mutable": false
                  }
                ]
              },
              {
                "type": "oauth",
                "properties": [
                  {
                    "name": "consumer_key",
                    "is_required": true,
                    "is_credential": true,
                    "system_provided": true,
                    "property_type": "system_provided_by_default",
                    "json_schema": null,
                    "provided": true,
                    "tap_mutable": false
                  },
                  {
                    "name": "consumer_secret",
                    "is_required": true,
                    "is_credential": true,
                    "system_provided": true,
                    "property_type": "system_provided_by_default",
                    "json_schema": null,
                    "provided": true,
                    "tap_mutable": false
                  },
                  {
                    "name": "oauth_s3_bucket",
                    "is_required": true,
                    "is_credential": false,
                    "system_provided": true,
                    "property_type": "read_only",
                    "json_schema": null,
                    "provided": true,
                    "tap_mutable": false
                  },
                  {
                    "name": "oauth_s3_path",
                    "is_required": true,
                    "is_credential": false,
                    "system_provided": true,
                    "property_type": "read_only",
                    "json_schema": null,
                    "provided": true,
                    "tap_mutable": false
                  },
                  {
                    "name": "oauth_session_handle",
                    "is_required": true,
                    "is_credential": true,
                    "system_provided": true,
                    "property_type": "system_provided_by_default",
                    "json_schema": null,
                    "provided": true,
                    "tap_mutable": false
                  },
                  {
                    "name": "oauth_token",
                    "is_required": true,
                    "is_credential": true,
                    "system_provided": true,
                    "property_type": "system_provided_by_default",
                    "json_schema": null,
                    "provided": true,
                    "tap_mutable": false
                  },
                  {
                    "name": "oauth_token_secret",
                    "is_required": true,
                    "is_credential": true,
                    "system_provided": true,
                    "property_type": "system_provided_by_default",
                    "json_schema": null,
                    "provided": true,
                    "tap_mutable": false
                  },
                  {
                    "name": "organization_name",
                    "is_required": false,
                    "is_credential": false,
                    "system_provided": true,
                    "property_type": "system_provided_by_default",
                    "json_schema": {
                      "type": "string"
                    },
                    "provided": true,
                    "tap_mutable": false
                  },
                  {
                    "name": "rsa_key",
                    "is_required": true,
                    "is_credential": true,
                    "system_provided": true,
                    "property_type": "system_provided_by_default",
                    "json_schema": null,
                    "provided": true,
                    "tap_mutable": false
                  },
                  {
                    "name": "user_agent",
                    "is_required": true,
                    "is_credential": false,
                    "system_provided": true,
                    "property_type": "read_only",
                    "json_schema": {
                      "type": "string"
                    },
                    "provided": true,
                    "tap_mutable": false
                  }
                ]
              },
              {
                "type": "discover_schema",
                "properties": []
              },
              {
                "type": "field_selection",
                "properties": []
              },
              {
                "type": "fully_configured",
                "properties": []
              }
            ]
          }
        },
        {
          "properties": {
            "ssl": "true",
            "anchor_time": "2019-01-10T19:39:17.724Z",
            "frequency_in_minutes": "60",
            "port": "5432",
            "dbname": "demni2mf59dt10",
            "host": "<HOST>",
            "product": "pipeline",
            "cron_expression": null,
            "image_version": "0.latest",
            "user": "nxucqufdolmwxr"
          },
          "updated_at": "2019-05-24T19:54:43Z",
          "schedule": null,
          "name": "heroku",
          "type": "platform.heroku_pg",
          "deleted_at": "2019-05-24T19:54:43Z",
          "system_paused_at": null,
          "stitch_client_id": 116078,
          "paused_at": null,
          "id": 120643,
          "display_name": "Heroku",
          "created_at": "2019-01-10T19:36:13Z",
          "report_card": {
            "type": "platform.heroku_pg",
            "current_step": 4,
            "current_step_type": "fully_configured",
            "steps": [
              {
                "type": "form",
                "properties": [
                  {
                    "name": "anchor_time",
                    "is_required": false,
                    "is_credential": false,
                    "system_provided": false,
                    "property_type": "user_provided",
                    "json_schema": {
                      "type": "string",
                      "format": "date-time"
                    },
                    "provided": true,
                    "tap_mutable": false
                  },
                  {
                    "name": "cron_expression",
                    "is_required": false,
                    "is_credential": false,
                    "system_provided": false,
                    "property_type": "user_provided",
                    "json_schema": null,
                    "provided": false,
                    "tap_mutable": false
                  },
                  {
                    "name": "dbname",
                    "is_required": true,
                    "is_credential": false,
                    "system_provided": false,
                    "property_type": "user_provided",
                    "json_schema": {
                      "type": "string"
                    },
                    "provided": true,
                    "tap_mutable": false
                  },
                  {
                    "name": "default_replication_method",
                    "is_required": false,
                    "is_credential": false,
                    "system_provided": false,
                    "property_type": "user_provided",
                    "json_schema": {
                      "type": "string",
                      "pattern": "^(true|false)$"
                    },
                    "provided": false,
                    "tap_mutable": false
                  },
                  {
                    "name": "filter_dbs",
                    "is_required": false,
                    "is_credential": false,
                    "system_provided": false,
                    "property_type": "user_provided",
                    "json_schema": {
                      "type": "string"
                    },
                    "provided": false,
                    "tap_mutable": false
                  },
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
                    "provided": true,
                    "tap_mutable": false
                  },
                  {
                    "name": "host",
                    "is_required": true,
                    "is_credential": false,
                    "system_provided": false,
                    "property_type": "user_provided",
                    "json_schema": {
                      "type": "string",
                      "anyOf": [
                        {
                          "format": "hostname"
                        },
                        {
                          "format": "ipv4"
                        }
                      ]
                    },
                    "provided": true,
                    "tap_mutable": false
                  },
                  {
                    "name": "image_version",
                    "is_required": true,
                    "is_credential": false,
                    "system_provided": true,
                    "property_type": "read_only",
                    "json_schema": null,
                    "provided": true,
                    "tap_mutable": false
                  },
                  {
                    "name": "include_schemas_in_destination_stream_name",
                    "is_required": false,
                    "is_credential": false,
                    "system_provided": false,
                    "property_type": "user_provided",
                    "json_schema": {
                      "type": "string"
                    },
                    "provided": false,
                    "tap_mutable": false
                  },
                  {
                    "name": "itersize",
                    "is_required": false,
                    "is_credential": false,
                    "system_provided": false,
                    "property_type": "user_provided",
                    "json_schema": {
                      "type": "string",
                      "pattern": "^\\d+"
                    },
                    "provided": false,
                    "tap_mutable": false
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
                    "provided": true,
                    "tap_mutable": false
                  },
                  {
                    "name": "port",
                    "is_required": true,
                    "is_credential": false,
                    "system_provided": false,
                    "property_type": "user_provided",
                    "json_schema": {
                      "type": "integer"
                    },
                    "provided": true,
                    "tap_mutable": false
                  },
                  {
                    "name": "ssh",
                    "is_required": false,
                    "is_credential": false,
                    "system_provided": false,
                    "property_type": "user_provided",
                    "json_schema": {
                      "type": "string",
                      "pattern": "^(true|false)$"
                    },
                    "provided": false,
                    "tap_mutable": false
                  },
                  {
                    "name": "ssh_host",
                    "is_required": false,
                    "is_credential": false,
                    "system_provided": false,
                    "property_type": "user_provided",
                    "json_schema": {
                      "type": "string",
                      "anyOf": [
                        {
                          "format": "hostname"
                        },
                        {
                          "format": "ipv4"
                        }
                      ]
                    },
                    "provided": false,
                    "tap_mutable": false
                  },
                  {
                    "name": "ssh_port",
                    "is_required": false,
                    "is_credential": false,
                    "system_provided": false,
                    "property_type": "user_provided",
                    "json_schema": {
                      "type": "string",
                      "pattern": "^\\d+"
                    },
                    "provided": false,
                    "tap_mutable": false
                  },
                  {
                    "name": "ssh_user",
                    "is_required": false,
                    "is_credential": false,
                    "system_provided": false,
                    "property_type": "user_provided",
                    "json_schema": {
                      "type": "string"
                    },
                    "provided": false,
                    "tap_mutable": false
                  },
                  {
                    "name": "ssl",
                    "is_required": false,
                    "is_credential": false,
                    "system_provided": false,
                    "property_type": "user_provided",
                    "json_schema": {
                      "type": "string",
                      "pattern": "^(true|false)$"
                    },
                    "provided": true,
                    "tap_mutable": false
                  },
                  {
                    "name": "user",
                    "is_required": true,
                    "is_credential": false,
                    "system_provided": false,
                    "property_type": "user_provided",
                    "json_schema": {
                      "type": "string"
                    },
                    "provided": true,
                    "tap_mutable": false
                  }
                ]
              },
              {
                "type": "discover_schema",
                "properties": []
              },
              {
                "type": "field_selection",
                "properties": []
              },
              {
                "type": "fully_configured",
                "properties": []
              }
            ]
          }
        }
---