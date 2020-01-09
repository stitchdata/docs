---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "sources"
key: "retrieve-a-source"
version: "4"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Retrieve a source"
method: "get"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}/{source_id}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.sources.retrieve.description }}"
description: |
  {{ api.core-objects.sources.retrieve.description }} This endpoint can be used to retrieve an active, paused, or deleted source.


# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

arguments:
  - name: "source_id"
    required: true
    type: "path parameter"
    description: "A path parameter corresponding to the unique ID of the data source to be retrieved."
    example-value: |
      86741

# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful and a valid identifier was provided, the API will return a status of <code class="api success">200 OK</code> and a single [Source Object]({{ api.core-objects.sources.object }}).


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    language: "json"
    code: |
      {% assign right-bracket = "}" %}
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | replace: "{source_id","120643" | remove: right-bracket | strip_newlines }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json"
  - type: "Response"
    language: "json"
    code: |
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
        "id": 120643,
        "display_name": "AdWords",
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
      }
---