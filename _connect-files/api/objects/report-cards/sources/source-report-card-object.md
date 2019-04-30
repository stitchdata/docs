---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-structure"
key: "report-card-object--source"

title: "Source Report Card"
description: "{{ api.data-structures.report-cards.source.description }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "current_step"
    type: "integer"
    description: "The index (in the `steps` array) of the current step needed to configure the data source."

  - name: "details"
    type: "object"
    sub-type: "details"
    url: "{{ api.data-structures.details.section }}"
    description: |
      {{ api.data-structures.details.short | flatify }}

  - name: "steps"
    type: "array"
    description: "A sequential list of [Connection Step objects]({{ api.data-structures.connection-steps.section }}) required to complete configuration for the connection type."

  - name: "type"
    type: "string"
    description: "The connection type. Ex: `platform.mysql` or `platform.hubspot`"


# -------------------------- #
#          EXAMPLES          #
# -------------------------- #

examples:
  - type: "Database source"
    code: |
      {
        "type": "platform.mysql",
        "current_step": 1,
        "current_step_type": "form",
        "steps": [
          {
            "type": "form",
            "properties": [
              {
                "name": "allow_non_auto_increment_pks",
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
                "name": "anchor_time",
                "is_required": false,
                "is_credential": false,
                "system_provided": false,
                "property_type": "user_provided",
                "json_schema": {
                  "type": "string",
                  "format": "date-time"
                },
                "provided": false,
                "tap_mutable": false
              },
              {
                "name": "check_hostname",
                "is_required": false,
                "is_credential": false,
                "system_provided": false,
                "property_type": "user_provided",
                "json_schema": {
                  "type": "string",
                  "pattern": "^(true|false)"
                },
                "provided": false,
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
                "name": "database",
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
                "provided": false,
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
                "provided": false,
                "tap_mutable": false
              },
              {
                "name": "image_version",
                "is_required": true,
                "is_credential": false,
                "system_provided": true,
                "property_type": "read_only",
                "json_schema": null,
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
                "provided": false,
                "tap_mutable": false
              },
              {
                "name": "port",
                "is_required": true,
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
                "name": "server_id",
                "is_required": false,
                "is_credential": false,
                "system_provided": false,
                "property_type": "user_provided",
                "json_schema": {
                  "type": "string",
                  "pattern": "^\\d+$"
                },
                "provided": false,
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
                  "pattern": "^(true|false)"
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
                  "pattern": "^(true|false)"
                },
                "provided": false,
                "tap_mutable": false
              },
              {
                "name": "ssl_ca",
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
                "name": "ssl_cert",
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
                "name": "ssl_client_auth_enabled",
                "is_required": false,
                "is_credential": false,
                "system_provided": false,
                "property_type": "user_provided",
                "json_schema": {
                  "type": "string",
                  "pattern": "^(true|false)"
                },
                "provided": false,
                "tap_mutable": false
              },
              {
                "name": "ssl_key",
                "is_required": false,
                "is_credential": true,
                "system_provided": false,
                "property_type": "user_provided",
                "json_schema": {
                  "type": "string"
                },
                "provided": false,
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
                "provided": false,
                "tap_mutable": false
              },
              {
                "name": "use_log_based_replication",
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
                "name": "verify_mode",
                "is_required": false,
                "is_credential": false,
                "system_provided": false,
                "property_type": "user_provided",
                "json_schema": {
                  "type": "string",
                  "pattern": "^(true|false)"
                },
                "provided": false,
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
        ],
        "details": {
          "pricing_tier": "standard",
          "pipeline_state": "released",
          "default_scheduling_interval": 30,
          "protocol": "platform.mysql",
          "access": true
        }
      }


  - type: "SaaS source"
    code: |
      {
        "type": "platform.hubspot",
        "current_step": 1,
        "current_step_type": "form",
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
                "provided": false,
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
                "provided": false,
                "tap_mutable": false
              },
              {
                "name": "image_version",
                "is_required": true,
                "is_credential": false,
                "system_provided": true,
                "property_type": "read_only",
                "json_schema": null,
                "provided": false,
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
                "provided": false,
                "tap_mutable": false
              }
            ]
          },
          {
            "type": "oauth",
            "properties": [
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
              },
              {
                "name": "client_secret",
                "is_required": true,
                "is_credential": true,
                "system_provided": true,
                "property_type": "system_provided_by_default",
                "json_schema": {
                  "type": "string"
                },
                "provided": false,
                "tap_mutable": false
              },
              {
                "name": "redirect_uri",
                "is_required": true,
                "is_credential": true,
                "system_provided": true,
                "property_type": "system_provided_by_default",
                "json_schema": {
                  "type": "string",
                  "format": "uri"
                },
                "provided": false,
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
                "provided": false,
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
        ],
        "details": {
          "pricing_tier": "premium",
          "pipeline_state": "released",
          "default_scheduling_interval": 30,
          "protocol": "platform.hubspot",
          "access": true
        }
      }
---