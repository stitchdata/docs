---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "source-types"
key: "get-a-source-type"
version: "4"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Get a source type"
method: "get"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}/{source_type}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.source-types.get.short }}"
description: "{{ api.core-objects.source-types.get.description | flatify }}"


# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

arguments:
  - name: "source_type"
    required: true
    type: "string"
    description: |
      {{ connect.common.attributes.type-argument | replace: "[TYPE]","source" | replace: "[TYPE-1]","platform.hubspot" | replace: "[TYPE-2]","platform.marketo" }}


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and a [Source Report Card object]({{ api.data-structures.report-cards.source.section }}) corresponding to `type`.


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    language: "json"
    code: |
      {% assign right-bracket = "}" %}
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | remove: right-bracket | replace:"{source_type","platform.hubspot" | strip_newlines }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json"

  - type: "Response"
    language: "json"
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
          "default_start_date": "-30 days",
          "protocol": "platform.hubspot",
          "access": true
        }
      }
---
