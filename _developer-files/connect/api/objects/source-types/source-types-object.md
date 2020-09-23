---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-object"
endpoint: "source-types"
order: 5


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Source Type"
endpoint-url: "/source-types"

description: "{{ api.core-objects.source-types.description }}"
intro-short: "Retrieve configuration info for data sources" # Used in the API functionality section of the docs

# -------------------------- #
#        VERSION INFO        #
# -------------------------- #

latest-version: "4"
versions:
  - number: "4"
    deprecated: false


# -------------------------- #
#      AVAILABLE METHODS     #
# -------------------------- #

available-methods:
  - id: "get-a-source-type"
    title: "Get a source type"
    method: "get"
    short: "{{ api.core-objects.source-types.get.short | flatify }}"

  - id: "list-source-types"
    title: "List all source types"
    method: "get"
    short: "{{ api.core-objects.source-types.list.short | flatify }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "report_card"
    type: "object"
    sub-type: "source report card"
    url: "{{ api.data-structures.report-cards.source.section }}"
    description: "The Source Report Card object corresponding to the source's `type`. For example: `platform.marketo` or `platform.hubspot`."


# -------------------------- #
#           EXAMPLES         #
# -------------------------- #

examples:
  - code: |
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
                "name": "email_chunk_size",
                "is_required": false,
                "is_credential": false,
                "system_provided": false,
                "property_type": "user_provided",
                "json_schema": {
                  "anyOf": [
                    {
                      "type": "integer"
                    },
                    {
                      "type": "string",
                      "pattern": "^\\d+"
                    }
                  ]
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
                "name": "include_inactives",
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
                "name": "require_content_scope",
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
              },
              {
                "name": "subscription_chunk_size",
                "is_required": false,
                "is_credential": false,
                "system_provided": false,
                "property_type": "user_provided",
                "json_schema": {
                  "anyOf": [
                    {
                      "type": "integer"
                    },
                    {
                      "type": "string",
                      "pattern": "^\\d+"
                    }
                  ]
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
          "pricing_tier": "standard",
          "pipeline_state": "released",
          "default_start_date": "-30 days",
          "default_scheduling_interval": 30,
          "protocol": "platform.hubspot",
          "access": true
        }
      }
---