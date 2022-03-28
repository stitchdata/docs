---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
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
description: |
  {{ site.data.connect.core-objects.source-types.list.description | flatify }}

  Refer to the [Destination and source API availability reference]({{ link.connect.guides.connection-reference | prepend: site.baseurl | append: "#sources-api-availability" }}) for info on the sources that are available in the API.


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and an array of [Source Report Card objects]({{ site.data.connect.data-structures.report-cards.source.section }}), one for each supported source `type`.


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    request-url: "{{ endpoint.short-url | flatify | strip_newlines }}"
    header: "{{ site.data.connect.request-headers.get.without-body | flatify }}"
    code: ""

  - type: "Response"
    code: |
      [
        {
          "type": "platform.closeio",
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
                  "name": "api_key",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "platform.closeio",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.freshdesk",
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
                },
                {
                  "name": "domain",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": null,
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "api_key",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": null,
                  "provided": false,
                  "tap_mutable": false
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "platform.freshdesk",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
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
            "access": true,
            "image_version": "2.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.referral-saasquatch",
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
                  "name": "api_key",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": null,
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
                },
                {
                  "name": "tenant_alias",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": null,
                  "provided": false,
                  "tap_mutable": false
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "platform.referral-saasquatch",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.braintree",
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
                  "name": "merchant_id",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": null,
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "private_key",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": null,
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "public_key",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
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
              "type": "fully_configured",
              "properties": []
            }
          ],
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "released",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "platform.braintree",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.gitlab",
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
                },
                {
                  "name": "api_url",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "format": "uri"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "private_token",
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
                  "name": "projects",
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
                  "name": "groups",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": false
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "platform.gitlab",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.outbrain",
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
                },
                {
                  "name": "account_id",
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
                  "name": "username",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "platform.outbrain",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.wootric",
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
                },
                {
                  "name": "client_id",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": null,
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "client_secret",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": null,
                  "provided": false,
                  "tap_mutable": false
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "platform.wootric",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.marketo",
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
                  "name": "client_id",
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
                  "name": "client_secret",
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
                  "name": "endpoint",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "format": "uri"
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
                  "name": "identity",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "format": "uri"
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
                  "name": "max_daily_calls",
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
              "type": "fully_configured",
              "properties": []
            }
          ],
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "platform.marketo",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": {
            "type": "platform.marketobulk"
          }
        },
        {
          "type": "platform.urban-airship",
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
                  "name": "app_key",
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
                  "name": "app_secret",
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
              "type": "fully_configured",
              "properties": []
            }
          ],
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "released",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "platform.urban-airship",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.shippo",
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
                },
                {
                  "name": "token",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": false
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "platform.shippo",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.facebook",
          "current_step": 1,
          "current_step_type": "form",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "aggregate_level",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": null,
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
                  "name": "include_deleted",
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
                  "name": "insights_buffer_days",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
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
                  "name": "access_token",
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
                  "name": "account_id",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "platform.facebook",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.harvest",
          "current_step": 1,
          "current_step_type": "form",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "account_name",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": null,
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
                  "system_provided": false,
                  "property_type": "system_provided_by_default",
                  "json_schema": null,
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "client_secret",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "system_provided_by_default",
                  "json_schema": null,
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "refresh_token",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "system_provided_by_default",
                  "json_schema": null,
                  "provided": false,
                  "tap_mutable": false
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "platform.harvest",
            "access": true,
            "image_version": "2.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.taboola",
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
                  "name": "account_id",
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
                  "name": "client_id",
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
                  "name": "client_secret",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": false
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "platform.taboola",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.adwords",
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
                  "name": "customer_ids",
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
                  "name": "developer_token",
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
                  "name": "oauth_client_id",
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
                  "name": "oauth_client_secret",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 1440,
            "protocol": "platform.adwords",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.zuora",
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
                  "name": "api_type",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(AQUA|REST)$"
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
                  "name": "european",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_immutable",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(true|false)$"
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
                  "name": "partner_id",
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
                  "name": "sandbox",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_immutable",
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
                  "name": "username",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "platform.zuora",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
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
                  "name": "incremental_limit",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "type": "string"
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
                  "property_type": "user_provided_advanced",
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
            "pipeline_state": "deprecated",
            "default_start_date": null,
            "default_scheduling_interval": 30,
            "protocol": "platform.mysql",
            "access": false,
            "image_version": "1.latest"
          },
          "upgrade_available": {
            "type": "platform.hp-mysql"
          }
        },
        {
          "type": "platform.fullstory",
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
                  "name": "api_key",
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
              "type": "fully_configured",
              "properties": []
            }
          ],
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "released",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "platform.fullstory",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.appsflyer",
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
                  "name": "api_token",
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
                  "name": "app_id",
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
              "type": "fully_configured",
              "properties": []
            }
          ],
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "released",
            "default_start_date": "-60 days",
            "default_scheduling_interval": 30,
            "protocol": "platform.appsflyer",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.selligent",
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
                },
                {
                  "name": "organization",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": null,
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "base_url",
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
                  "name": "api_key",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": null,
                  "provided": false,
                  "tap_mutable": false
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "platform.selligent",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.autopilot",
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
                  "name": "api_key",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": null,
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.autopilot",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.aurora",
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
                  "name": "incremental_limit",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "type": "string"
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
                  "name": "port",
                  "is_required": true,
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
            "pipeline_state": "deprecated",
            "default_start_date": null,
            "default_scheduling_interval": 30,
            "protocol": "platform.mysql",
            "access": false,
            "image_version": "1.latest"
          },
          "upgrade_available": {
            "type": "platform.hp-aurora"
          }
        },
        {
          "type": "platform.mariadb",
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
                  "name": "incremental_limit",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "type": "string"
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
            "pipeline_state": "deprecated",
            "default_start_date": null,
            "default_scheduling_interval": 30,
            "protocol": "platform.mysql",
            "access": false,
            "image_version": "1.latest"
          },
          "upgrade_available": {
            "type": "platform.hp-mariadb"
          }
        },
        {
          "type": "platform.cloudsql",
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
                  "name": "incremental_limit",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "internal_hostname",
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
                  "property_type": "user_provided_advanced",
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
            "pipeline_state": "deprecated",
            "default_start_date": null,
            "default_scheduling_interval": 30,
            "protocol": "platform.mysql",
            "access": false,
            "image_version": "1.latest"
          },
          "upgrade_available": {
            "type": "platform.hp-cloudsql"
          }
        },
        {
          "type": "platform.xero",
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
                  "name": "include_archived_contacts",
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
                  "name": "oauth_s3_bucket",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": true,
                  "property_type": "read_only",
                  "json_schema": null,
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "oauth_s3_path",
                  "is_required": false,
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
                },
                {
                  "name": "user_agent",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": true,
                  "property_type": "read_only",
                  "json_schema": {
                    "type": "string"
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
                  "name": "access_token",
                  "is_required": false,
                  "is_credential": true,
                  "system_provided": true,
                  "property_type": "system_provided_by_default",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": true
                },
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
                  "name": "consumer_key",
                  "is_required": false,
                  "is_credential": true,
                  "system_provided": true,
                  "property_type": "system_provided_by_default",
                  "json_schema": null,
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "consumer_secret",
                  "is_required": false,
                  "is_credential": true,
                  "system_provided": true,
                  "property_type": "system_provided_by_default",
                  "json_schema": null,
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "oauth_session_handle",
                  "is_required": false,
                  "is_credential": true,
                  "system_provided": true,
                  "property_type": "system_provided_by_default",
                  "json_schema": null,
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "oauth_token",
                  "is_required": false,
                  "is_credential": true,
                  "system_provided": true,
                  "property_type": "system_provided_by_default",
                  "json_schema": null,
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "oauth_token_secret",
                  "is_required": false,
                  "is_credential": true,
                  "system_provided": true,
                  "property_type": "system_provided_by_default",
                  "json_schema": null,
                  "provided": false,
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
                  "tap_mutable": true
                },
                {
                  "name": "rsa_key",
                  "is_required": false,
                  "is_credential": true,
                  "system_provided": true,
                  "property_type": "system_provided_by_default",
                  "json_schema": null,
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "tenant_id",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": true,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "xero_user_id",
                  "is_required": true,
                  "is_credential": false,
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.xero",
            "access": true,
            "image_version": "2.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.zendesk-chat",
          "current_step": 1,
          "current_step_type": "form",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "agents_page_limit",
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
                  "name": "chats_full_sync_days",
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
                  "name": "chat_search_interval_days",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": null,
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
                },
                {
                  "name": "subdomain",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": null,
                  "provided": false,
                  "tap_mutable": false
                }
              ]
            },
            {
              "type": "oauth",
              "properties": [
                {
                  "name": "access_token",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "system_provided_by_default",
                  "json_schema": null,
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "platform.zendesk-chat",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.klaviyo",
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
                  "name": "api_key",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": null,
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.klaviyo",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.jira",
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
                  "name": "groups",
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
                },
                {
                  "name": "base_url",
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
                  "name": "username",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.jira",
            "access": true,
            "image_version": "2.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.salesforce",
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
                  "name": "api_type",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_immutable",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(REST|BULK)$"
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
                  "name": "is_sandbox",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_immutable",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(true|false)$"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "quota_percent_per_run",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(\\d|[1-9]\\d|100)$"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "quota_percent_total",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(\\d|[1-9]\\d|100)$"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "select_fields_by_default",
                  "is_required": true,
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
                  "system_provided": false,
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
                  "system_provided": false,
                  "property_type": "system_provided_by_default",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "instance_url",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "system_provided_by_default",
                  "json_schema": {
                    "type": "string",
                    "format": "uri"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "orgid",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "system_provided_by_default",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "refresh_token",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.salesforce",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.pipedrive",
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
                  "name": "api_token",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "platform.pipedrive",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.marketobulk",
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
                  "name": "max_export_days",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+$"
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
                  "name": "endpoint",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": null,
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "client_id",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": null,
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "client_secret",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": null,
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "max_daily_calls",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 720,
            "protocol": "platform.marketo",
            "access": true,
            "image_version": "2.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.codat",
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
                  "name": "api_key",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": null,
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
                },
                {
                  "name": "uat_urls",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_immutable",
                  "json_schema": null,
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.codat",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.exacttarget",
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
                  "name": "batch_size",
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
                  "name": "refresh_token",
                  "is_required": false,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": true
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
                  "name": "client_id",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": null,
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "client_secret",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": null,
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "tenant_subdomain",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.exacttarget",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.db2",
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
                  "name": "filter_schemas",
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
                  "name": "user",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": null,
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
            "default_start_date": null,
            "default_scheduling_interval": 60,
            "protocol": "platform.db2",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.listrak",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.listrak",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.bing-ads",
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
                  "name": "account_ids",
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
                  "name": "customer_id",
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
                  "name": "developer_token",
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
                  "name": "oauth_client_id",
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
                  "name": "oauth_client_secret",
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
                },
                {
                  "name": "user_id",
                  "is_required": false,
                  "is_credential": false,
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 1440,
            "protocol": "platform.bing-ads",
            "access": true,
            "image_version": "2.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.yotpo",
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
                  "name": "api_key",
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
                  "name": "api_secret",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.yotpo",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.sendgrid",
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
                  "name": "api_key",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.sendgrid",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.quickbase",
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
                  "name": "qb_appid",
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
                  "name": "qb_url",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "format": "uri"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "qb_user_token",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.quickbase",
            "access": true,
            "image_version": "2.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.oracle",
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
                  "name": "default_replication_method",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(LOG_BASED|FULL_TABLE)$"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "filter_schemas",
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
                  "name": "scn_window_size",
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
                  "name": "sid",
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
            "pricing_tier": "enterprise",
            "pipeline_state": "released",
            "default_start_date": null,
            "default_scheduling_interval": 60,
            "protocol": "platform.oracle",
            "access": false,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.bronto",
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
                },
                {
                  "name": "token",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.bronto",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.postgres",
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
                  "name": "dbname",
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
                  "name": "debug_lsn",
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
                  "name": "default_replication_method",
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
                  "name": "include_schemas_in_destination_stream_name",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_immutable",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(true|false)$"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "itersize",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "logical_poll_total_seconds",
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
                  "name": "wal2json_message_format",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^1|2$"
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
            "pipeline_state": "deprecated",
            "default_start_date": null,
            "default_scheduling_interval": 60,
            "protocol": "platform.postgres",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": {
            "type": "platform.hp-postgres"
          }
        },
        {
          "type": "platform.github",
          "current_step": 1,
          "current_step_type": "form",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "access_token",
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
                  "name": "repository",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.github",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.zendesk",
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
                  "name": "search_window_size",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "type": "string"
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
                  "name": "subdomain",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
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
                  "name": "access_token",
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
                  "name": "marketplace_app_id",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": true,
                  "property_type": "system_provided_by_default",
                  "json_schema": {
                    "type": "integer"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "marketplace_name",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": true,
                  "property_type": "system_provided_by_default",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "marketplace_organization_id",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": true,
                  "property_type": "system_provided_by_default",
                  "json_schema": {
                    "type": "integer"
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.zendesk",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.s3-csv",
          "current_step": 1,
          "current_step_type": "form",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "account_id",
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
                  "name": "bucket",
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
                  "name": "external_id",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": true,
                  "property_type": "read_only",
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
                  "name": "role_name",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": true,
                  "property_type": "read_only",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "search_prefix",
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
                  "name": "tables",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.s3-csv",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.doubleclick-campaign-manager",
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
                  "name": "profile_id",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
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
                },
                {
                  "name": "user_id",
                  "is_required": false,
                  "is_credential": false,
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "platform.doubleclick-campaign-manager",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.amplitude",
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
                  "name": "username",
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
                  "name": "account",
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
                  "name": "warehouse",
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
                  "name": "database",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "default_start_date": null,
            "default_scheduling_interval": 60,
            "protocol": "platform.amplitude",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.uservoice",
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
                },
                {
                  "name": "subdomain",
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
                  "name": "api_key",
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
                  "name": "api_secret",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.uservoice",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.intacct",
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
                  "name": "external_id",
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
                  "name": "role_name",
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
                  "name": "company_id",
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
                  "name": "bucket",
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
                  "name": "account_id",
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
                  "name": "path",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.intacct",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.heroku_pg",
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
                  "name": "dbname",
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
                  "property_type": "user_provided_advanced",
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
            "pipeline_state": "deprecated",
            "default_start_date": null,
            "default_scheduling_interval": 60,
            "protocol": "platform.postgres",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": {
            "type": "platform.hp-heroku-pg"
          }
        },
        {
          "type": "platform.cloudsql_pg",
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
                  "name": "dbname",
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
                  "property_type": "user_provided_advanced",
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
            "pipeline_state": "deprecated",
            "default_start_date": null,
            "default_scheduling_interval": 60,
            "protocol": "platform.postgres",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": {
            "type": "platform.hp-cloudsql-pg"
          }
        },
        {
          "type": "platform.harvest-forecast",
          "current_step": 1,
          "current_step_type": "form",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "account_id",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.harvest-forecast",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.campaign-monitor",
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
                  "name": "client_id",
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
                  "name": "access_token",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.campaign-monitor",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.liveperson",
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
                },
                {
                  "name": "app_key",
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
                  "name": "app_secret",
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
                  "name": "access_token",
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
                  "name": "access_token_secret",
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
                  "name": "account_id",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.liveperson",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.platformpurple",
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
                  "name": "api_key",
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
                  "name": "environment",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.platformpurple",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.clubspeed",
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
                  "name": "private_key",
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
                  "name": "subdomain",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.clubspeed",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.shopify",
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
                  "name": "date_window_size",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
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
                  "name": "results_per_page",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "shop",
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
                  "name": "api_key",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.shopify",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "import_api",
          "current_step": 2,
          "current_step_type": "fully_configured",
          "steps": [
            {
              "type": "form",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "import_api",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.responsys",
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
                  "name": "host",
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
                  "name": "path",
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
                  "name": "port",
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
                  "name": "username",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.responsys",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.stripe",
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
                  "name": "date_window_size",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
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
                  "name": "whitelist_map",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
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
                  "name": "account_id",
                  "is_required": true,
                  "is_credential": false,
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "platform.stripe",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.heap",
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
                  "name": "external_id",
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
                  "name": "role_name",
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
                  "name": "bucket",
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
                  "name": "account_id",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^[0-9]{12}$"
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.heap",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.frontapp",
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
                },
                {
                  "name": "token",
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
                  "name": "incremental_range",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.frontapp",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.revinate",
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
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "api_key",
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
                  "name": "api_secret",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": false
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.revinate",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.typeform",
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
                },
                {
                  "name": "token",
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
                  "name": "forms",
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
                  "name": "incremental_range",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.typeform",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.toggl",
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
                  "name": "api_token",
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
                  "name": "detailed_report_trailing_days",
                  "is_required": true,
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.toggl",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.eloqua",
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
                  "name": "bulk_page_size",
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
                  "is_credential": false,
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
                  "is_credential": false,
                  "system_provided": true,
                  "property_type": "system_provided_by_default",
                  "json_schema": {
                    "type": "string"
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
                  "tap_mutable": true
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.eloqua",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.shiphero",
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
                },
                {
                  "name": "token",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.shiphero",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.jira-cloud",
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
                  "name": "groups",
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
                  "name": "access_token",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "system_provided_by_default",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "cloud_id",
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
                  "name": "oauth_client_id",
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
                  "name": "oauth_client_secret",
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
                  "name": "refresh_token",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.jira",
            "access": false,
            "image_version": "2.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.netsuite",
          "current_step": 1,
          "current_step_type": "form",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "account",
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
                  "name": "body_fields_only",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": null,
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "consumer_key",
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
                  "name": "consumer_secret",
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
                  "name": "page_size",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "return_search_columns",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": null,
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "search_window_size",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+.?\\d*$"
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
                  "name": "token_id",
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
                  "name": "token_secret",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.netsuite",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.bigcommerce",
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
                },
                {
                  "name": "client_id",
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
                  "name": "access_token",
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
                  "name": "store_hash",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.bigcommerce",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.toast",
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
                },
                {
                  "name": "client_id",
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
                  "name": "client_secret",
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
                  "name": "location_guid",
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
                  "name": "management_group_guid",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.toast",
            "access": false,
            "image_version": "pr-alpha-117193.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.freshsales",
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
                },
                {
                  "name": "domain",
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
                  "name": "api_key",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.freshsales",
            "access": false,
            "image_version": "pr-alpha-119739.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.onfleet",
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
                  "name": "api_key",
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
                  "name": "quota_limit",
                  "is_required": true,
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.onfleet",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.invoiced",
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
                  "name": "api_key",
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
                  "name": "sandbox",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.invoiced",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.exchangeratesapi",
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
                  "name": "base",
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
              "type": "fully_configured",
              "properties": []
            }
          ],
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.exchangeratesapi",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.recurly",
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
                },
                {
                  "name": "api_key",
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
                  "name": "subdomain",
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
                  "name": "quota_limit",
                  "is_required": true,
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.recurly",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.asana",
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
                  "name": "access_token",
                  "is_required": false,
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
                  "name": "client_id",
                  "is_required": true,
                  "is_credential": false,
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
                  "is_credential": false,
                  "system_provided": true,
                  "property_type": "system_provided_by_default",
                  "json_schema": {
                    "type": "string"
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.asana",
            "access": true,
            "image_version": "2.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.chargebee",
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
                  "name": "api_key",
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
                  "name": "include_deleted",
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
                  "name": "site",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.chargebee",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.mailchimp",
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
                  "name": "page_size",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
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
                  "name": "access_token",
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
                  "name": "client_id",
                  "is_required": true,
                  "is_credential": false,
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.mailchimp",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.mssql",
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
                    "type": "string"
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
                  "name": "include_schemas_in_destination_stream_name",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "platform.mssql",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.redshift",
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
                },
                {
                  "name": "host",
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
                  "name": "port",
                  "is_required": true,
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
                        "pattern": "^\\d+$"
                      }
                    ]
                  },
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
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "schema",
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
                  "name": "ssl",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.redshift",
            "access": false,
            "image_version": "pr-alpha-100608.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.gemini",
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
                  "name": "refresh_token",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.gemini",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.appfigures",
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
                },
                {
                  "name": "api_key",
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
                  "name": "username",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.appfigures",
            "access": false,
            "image_version": "pr-alpha-100608.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.lever",
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
                },
                {
                  "name": "token",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.lever",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.ebay",
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
                },
                {
                  "name": "scope",
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
            "pipeline_state": "beta",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.ebay",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.ringcentral",
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
                },
                {
                  "name": "api_url",
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
                  "name": "client_id",
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
                  "name": "client_secret",
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
                  "name": "username",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.ringcentral",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.helpscout",
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
                  "system_provided": false,
                  "property_type": "user_provided",
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
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "refresh_token",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": true
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.helpscout",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.iterable",
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
                },
                {
                  "name": "api_key",
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
                  "name": "api_window_in_days",
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
                        "pattern": "^\\d+$"
                      }
                    ]
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.iterable",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.linkedin-ads",
          "current_step": 1,
          "current_step_type": "form",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "accounts",
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
                  "name": "page_size",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
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
                  "name": "access_token",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.linkedin-ads",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.deputy",
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
                  "is_credential": false,
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
                  "name": "domain",
                  "is_required": true,
                  "is_credential": false,
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
                  "is_credential": false,
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
                  "tap_mutable": true
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.deputy",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.pardot",
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
                  "name": "email",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "format": "email"
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
                  "name": "pardot_business_unit_id",
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
                  "name": "password",
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
                  "name": "user_key",
                  "is_required": false,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
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
                  "is_required": false,
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
                  "is_required": false,
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
                  "name": "refresh_token",
                  "is_required": false,
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.pardot",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.ga360",
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
                  "name": "dataset_id",
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
                  "name": "page_size",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "project_id",
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
                  "name": "service_account_json",
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
            "pricing_tier": "enterprise",
            "pipeline_state": "beta",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.ga360",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.mongodb",
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
                  "name": "database",
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
                  "name": "include_schemas_in_destination_stream_name",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_immutable",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(true|false)$"
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
                  "name": "replica_set",
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
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(true|false)$"
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "platform.mongodb",
            "access": true,
            "image_version": "2.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.mambu",
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
                  "name": "apikey_audit",
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
                  "name": "lookback_window",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "page_size",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
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
                  "name": "subdomain",
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
                  "name": "username",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.mambu",
            "access": true,
            "image_version": "2.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.outreach",
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
                  "name": "page_size",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "quota_limit",
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
                  "is_credential": false,
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
                  "is_credential": false,
                  "system_provided": true,
                  "property_type": "system_provided_by_default",
                  "json_schema": {
                    "type": "string"
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
            "pipeline_state": "beta",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.outreach",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.3plcentral",
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
                  "name": "base_url",
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
                  "name": "client_id",
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
                  "name": "client_secret",
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
                  "name": "customer_id",
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
                  "name": "facility_id",
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
                },
                {
                  "name": "tpl_key",
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
                  "name": "user_login_id",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.3plcentral",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.google-search-console",
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
                  "name": "site_urls",
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
                  "property_type": "user_provided",
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
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "refresh_token",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": true,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "user_id",
                  "is_required": false,
                  "is_credential": false,
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
            "pipeline_state": "beta",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.google-search-console",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.saasoptics",
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
                },
                {
                  "name": "account_name",
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
                  "name": "server_subdomain",
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
                  "name": "token",
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
                  "name": "date_window_size",
                  "is_required": true,
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.saasoptics",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.mavenlink",
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
                },
                {
                  "name": "token",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.mavenlink",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.recharge",
          "current_step": 1,
          "current_step_type": "form",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "access_token",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.recharge",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.satismeter",
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
                  "name": "api_key",
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
                  "name": "project_id",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.satismeter",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.intercom",
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
                  "name": "access_token",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.intercom",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.impact",
          "current_step": 1,
          "current_step_type": "form",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "account_sid",
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
                  "name": "api_catalog",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "enum": [
                      "Advertisers",
                      "Agencies",
                      "Partners"
                    ]
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "auth_token",
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
                  "name": "model_id",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.impact",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.darksky",
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
                },
                {
                  "name": "secret_key",
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
                  "name": "language",
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
                  "name": "units",
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
                  "name": "location_list",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.darksky",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.chargify",
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
                  "name": "api_key",
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
                },
                {
                  "name": "subdomain",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "pipeline_state": "beta",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.chargify",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.azure",
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
                    "type": "string"
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
                  "name": "include_schemas_in_destination_stream_name",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "platform.mssql",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.sftp",
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
                  "name": "port",
                  "is_required": true,
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
                  "name": "tables",
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
                  "name": "username",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.sftp",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.google-analytics",
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
                  "name": "cached_profile_lookup",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": true,
                  "property_type": "system_provided_by_default",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": true
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
                  "name": "quota_user",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": true,
                  "property_type": "read_only",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "report_definitions",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "name": {
                          "type": "string"
                        },
                        "id": {
                          "type": "string"
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "name",
                        "id"
                      ]
                    }
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
                },
                {
                  "name": "user_id",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": true,
                  "property_type": "system_provided_by_default",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "view_id",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.google-analytics",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.copper",
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
                  "name": "email",
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
                },
                {
                  "name": "token",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.copper",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.google-sheets",
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
                  "name": "spreadsheet_id",
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
                },
                {
                  "name": "user_id",
                  "is_required": false,
                  "is_credential": false,
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.google-sheets",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.dynamodb",
          "current_step": 1,
          "current_step_type": "form",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "account_id",
                  "is_required": true,
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
                  "name": "external_id",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": true,
                  "property_type": "read_only",
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
                  "name": "region_name",
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
                  "name": "role_name",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": true,
                  "property_type": "read_only",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "use_local_dynamo",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_immutable",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(true|false)$"
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.dynamodb",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.ujet",
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
                  "name": "company_key",
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
                  "name": "company_secret",
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
                  "name": "date_window_size",
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
                  "name": "domain",
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
                },
                {
                  "name": "subdomain",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.ujet",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.surveymonkey",
          "current_step": 1,
          "current_step_type": "form",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "access_token",
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
                  "name": "page_size",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "type": "string"
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
                  "name": "survey_id",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.surveymonkey",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.slack",
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
                  "name": "date_window_size",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
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
                  "name": "lookback_window",
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
                  "name": "token",
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
                  "name": "join_public_channels",
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
                  "name": "private_channels",
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
                  "name": "exclude_archived",
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
            "pipeline_state": "beta",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.slack",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.lookml",
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
                  "name": "api_token",
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
                  "name": "git_owner",
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
                  "name": "git_repositories",
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
            "pipeline_state": "beta",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.lookml",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.dayforce",
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
                  "name": "client_namespace",
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
                  "name": "username",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.dayforce",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.pagerduty",
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
                  "name": "email",
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
                },
                {
                  "name": "token",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.pagerduty",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.looker",
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
                },
                {
                  "name": "api_port",
                  "is_required": true,
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
                  "name": "client_id",
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
                  "name": "client_secret",
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
                  "name": "subdomain",
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
                  "name": "domain",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "pipeline_state": "beta",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.looker",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.criteo",
          "current_step": 1,
          "current_step_type": "form",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "advertiser_ids",
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
                  "name": "client_id",
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
                  "name": "client_secret",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.criteo",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.pinterest-ads",
          "current_step": 1,
          "current_step_type": "form",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "advertisers",
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
                  "name": "attribution_window",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "type": "string"
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
                  "name": "date_window_size",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
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
                  "name": "access_token",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": true,
                  "property_type": "user_provided",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.pinterest-ads",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.kustomer",
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
                  "name": "api_token",
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
                  "name": "date_window_size",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
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
                  "name": "page_size_limit",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.kustomer",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.swellrewards",
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
                  "name": "api_guid",
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
                  "name": "api_key",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.swellrewards",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.workday-raas",
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
                  "name": "reports",
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
                  "name": "username",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "pricing_tier": "enterprise",
            "pipeline_state": "released",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.workday-raas",
            "access": false,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.mixpanel",
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
                  "name": "api_secret",
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
                  "name": "attribution_window",
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
                  "name": "date_window_size",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "end_date",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d{4}-\\d{2}-\\d{2}T00:00:00Z$"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "eu_residency",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_immutable",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(true|false)$"
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
                  "name": "project_timezone",
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
                  "name": "select_properties_by_default",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.mixpanel",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.circle-ci",
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
                  "name": "project_slugs",
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
                  "name": "token",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.circle-ci",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.covid-19",
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
                  "name": "api_token",
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
            "pipeline_state": "beta",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 720,
            "protocol": "platform.covid-19",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.mailshake",
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
                  "name": "api_key",
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
            "pipeline_state": "beta",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.mailshake",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.pepperjam",
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
                  "name": "api_key",
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
            "pipeline_state": "beta",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.pepperjam",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.netsuite-suite-analytics",
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
                },
                {
                  "name": "host",
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
                  "name": "account_id",
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
                  "name": "role_id",
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
                  "name": "username",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.netsuite-suite-analytics",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.zoom",
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
                  "name": "client_id",
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
                  "name": "client_secret",
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
                  "name": "jwt",
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
                  "name": "refresh_token",
                  "is_required": false,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "pipeline_state": "beta",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.zoom",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.trello",
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
                  "name": "access_token",
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
                  "name": "access_token_secret",
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
                  "name": "consumer_key",
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
                  "name": "consumer_secret",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.trello",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.typo",
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
                  "name": "api_key",
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
                  "name": "api_secret",
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
                  "name": "audit_id",
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
                  "name": "cluster_api_endpoint",
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
                  "name": "dataset",
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
                  "name": "records_per_page",
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
                  "name": "record_limit",
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
                  "name": "repository",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.typo",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.twitter-ads",
          "current_step": 1,
          "current_step_type": "form",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "account_ids",
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
                  "name": "attribution_window",
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
                  "name": "country_codes",
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
                  "name": "reports",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "name": {
                          "type": "string"
                        },
                        "entity": {
                          "type": "string"
                        },
                        "segment": {
                          "type": "string"
                        },
                        "granularity": {
                          "type": "string"
                        }
                      },
                      "additionalProperties": false
                    }
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
                  "name": "with_deleted",
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
                }
              ]
            },
            {
              "type": "oauth",
              "properties": [
                {
                  "name": "access_token",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": true,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "access_token_secret",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": true,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "consumer_key",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": true,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "consumer_secret",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": true,
                  "property_type": "user_provided",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.twitter-ads",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.adroll",
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
                  "name": "end_date",
                  "is_required": false,
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
                  "name": "lookback_window",
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
                        "pattern": "^\\d+$"
                      }
                    ]
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
                }
              ]
            },
            {
              "type": "oauth",
              "properties": [
                {
                  "name": "access_token",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": true,
                  "property_type": "system_provided_by_default",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": true
                },
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
                  "name": "refresh_token",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": true,
                  "property_type": "system_provided_by_default",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": true
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.adroll",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.twilio",
          "current_step": 1,
          "current_step_type": "form",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "account_sid",
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
                  "name": "auth_token",
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
                  "name": "date_window_days",
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
                  "name": "lock_period_days",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.twilio",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.square",
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
                  "name": "sandbox",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_immutable",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.square",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.snapchat-ads",
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
                  "name": "omit_empty",
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
                  "name": "swipe_up_attribution_window",
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
                  "name": "targeting_country_codes",
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
                  "name": "view_attribution_window",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.snapchat-ads",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.amazon-ads-dsp",
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
                },
                {
                  "name": "client_id",
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
                  "name": "client_secret",
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
                  "name": "refresh_token",
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
                  "name": "redirect_uri",
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
                  "name": "profiles",
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
                  "name": "reports",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.amazon-ads-dsp",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.ilevel",
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
                  "name": "is_sandbox",
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
            "pipeline_state": "beta",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.ilevel",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.quickbooks",
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
                  "name": "max_results",
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
                  "name": "sandbox",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_immutable",
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
                  "name": "realm_id",
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
                  "name": "refresh_token",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": true,
                  "property_type": "system_provided_by_default",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": true
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.quickbooks",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.activecampaign",
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
                  "name": "api_token",
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
                  "name": "api_url",
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
            "pipeline_state": "beta",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.activecampaign",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.ms-teams",
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
                  "is_credential": false,
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
                  "name": "tenant_id",
                  "is_required": true,
                  "is_credential": false,
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
            "pipeline_state": "beta",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.ms-teams",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.autodesk-bim-360",
          "current_step": 1,
          "current_step_type": "form",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "account_id",
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
                  "name": "client_id",
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
                  "name": "client_secret",
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
                  "name": "refresh_token",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": true
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.autodesk-bim-360",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.sling",
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
                  "name": "api_key",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.sling",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.x-y",
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
                  "name": "api_user",
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
                  "name": "customer",
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
                  "name": "inventory",
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
                  "name": "inventory_movement",
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
                  "name": "invoice",
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
                  "name": "item",
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
                  "name": "sales_order_line",
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
                  "name": "space_uri",
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
                  "name": "stock_transfer",
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
                  "name": "token",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.x-y",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.pendo",
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
                  "name": "include_anonymous_visitors",
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
                  "name": "lookback_window",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
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
                  "name": "period",
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
                  "name": "request_timeout",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "type": "string"
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
                  "name": "x_pendo_integration_key",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "pipeline_state": "beta",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.pendo",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.insided",
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
                  "name": "client_id",
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
                  "name": "client_secret",
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
                  "name": "refresh_token",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.insided",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.signonsite",
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
                  "name": "api_key",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.signonsite",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.nikabot",
          "current_step": 1,
          "current_step_type": "form",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "access_token",
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
                  "name": "end_date",
                  "is_required": false,
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
                  "name": "page_size",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "type": "string"
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.nikabot",
            "access": false,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.hp-postgres",
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
                  "name": "dbname",
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
                  "name": "default_replication_method",
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
                  "property_type": "user_provided_advanced",
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
                  "name": "include_schemas_in_destination_stream_name",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_immutable",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(true|false)$"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "incremental_limit",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
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
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "logical_poll_total_seconds",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+$"
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
                  "name": "replication_slot_name",
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
                  "name": "socket_timeout",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
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
            "default_start_date": null,
            "default_scheduling_interval": 60,
            "protocol": "platform.hp-postgres",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "hp.rando",
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
                  "name": "streams",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": null,
                  "provided": false,
                  "tap_mutable": false
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "hp.rando",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.skubana",
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
                },
                {
                  "name": "token",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.skubana",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.hp-mysql",
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
                  "name": "dbname",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
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
                    "anyOf": [
                      {
                        "type": "string"
                      },
                      {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
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
                  "name": "include_schemas_in_destination_stream_name",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_immutable",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(true|false)$"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "incremental_limit",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+$"
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
                  "name": "server_id",
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
                    "pattern": "^(true|false)$"
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
            "default_start_date": null,
            "default_scheduling_interval": 60,
            "protocol": "platform.hp-mysql",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.ordway",
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
                  "name": "api_key",
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
                  "name": "company",
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
                },
                {
                  "name": "user_email",
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
                  "name": "user_token",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.ordway",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.youtube-analytics",
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
                  "name": "channel_ids",
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
                  "name": "client_id",
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
                  "name": "client_secret",
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
                  "name": "refresh_token",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.youtube-analytics",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.crossbeam",
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
                  "name": "auth_base_url",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "base_url",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "type": "string"
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
                  "name": "organization_uuid",
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
                  "is_credential": false,
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
            "pipeline_state": "beta",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.crossbeam",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.hp-cloudsql-pg",
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
                  "name": "dbname",
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
                  "name": "default_replication_method",
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
                  "property_type": "user_provided_advanced",
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
                  "name": "include_schemas_in_destination_stream_name",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_immutable",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(true|false)$"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "itersize",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "anyOf": [
                      {
                        "type": "integer"
                      },
                      {
                        "type": "string",
                        "pattern": "^\\d+$"
                      }
                    ]
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "logical_poll_total_seconds",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "anyOf": [
                      {
                        "type": "integer"
                      },
                      {
                        "type": "string",
                        "pattern": "^\\d+$"
                      }
                    ]
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
                    "anyOf": [
                      {
                        "type": "integer"
                      },
                      {
                        "type": "string",
                        "pattern": "^\\d+$"
                      }
                    ]
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "replication_slot_name",
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
                    "anyOf": [
                      {
                        "type": "integer"
                      },
                      {
                        "type": "string",
                        "pattern": "^\\d+$"
                      }
                    ]
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
            "default_start_date": null,
            "default_scheduling_interval": 60,
            "protocol": "platform.hp-postgres",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.hp-heroku-pg",
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
                  "name": "dbname",
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
                  "name": "default_replication_method",
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
                  "property_type": "user_provided_advanced",
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
                  "name": "include_schemas_in_destination_stream_name",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_immutable",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(true|false)$"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "itersize",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "anyOf": [
                      {
                        "type": "integer"
                      },
                      {
                        "type": "string",
                        "pattern": "^\\d+$"
                      }
                    ]
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "logical_poll_total_seconds",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "anyOf": [
                      {
                        "type": "integer"
                      },
                      {
                        "type": "string",
                        "pattern": "^\\d+$"
                      }
                    ]
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
                    "anyOf": [
                      {
                        "type": "integer"
                      },
                      {
                        "type": "string",
                        "pattern": "^\\d+$"
                      }
                    ]
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
                    "anyOf": [
                      {
                        "type": "integer"
                      },
                      {
                        "type": "string",
                        "pattern": "^\\d+$"
                      }
                    ]
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
            "default_start_date": null,
            "default_scheduling_interval": 60,
            "protocol": "platform.hp-postgres",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "webhook.particleio",
          "current_step": 2,
          "current_step_type": "fully_configured",
          "steps": [
            {
              "type": "form",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "incoming-webhook",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "webhook.aftership",
          "current_step": 2,
          "current_step_type": "fully_configured",
          "steps": [
            {
              "type": "form",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "incoming-webhook",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "webhook.branch",
          "current_step": 2,
          "current_step_type": "fully_configured",
          "steps": [
            {
              "type": "form",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "incoming-webhook",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "webhook.contentful",
          "current_step": 2,
          "current_step_type": "fully_configured",
          "steps": [
            {
              "type": "form",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "incoming-webhook",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "webhook.customerio",
          "current_step": 1,
          "current_step_type": "form",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "webhookz_primary_key",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": true,
                  "property_type": "read_only",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": false
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "incoming-webhook",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "webhook.delighted",
          "current_step": 2,
          "current_step_type": "fully_configured",
          "steps": [
            {
              "type": "form",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "incoming-webhook",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "webhook.drip",
          "current_step": 2,
          "current_step_type": "fully_configured",
          "steps": [
            {
              "type": "form",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "incoming-webhook",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "webhook.formkeep",
          "current_step": 2,
          "current_step_type": "fully_configured",
          "steps": [
            {
              "type": "form",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "incoming-webhook",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "webhook.iterable",
          "current_step": 2,
          "current_step_type": "fully_configured",
          "steps": [
            {
              "type": "form",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "incoming-webhook",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "webhook.mailjet",
          "current_step": 2,
          "current_step_type": "fully_configured",
          "steps": [
            {
              "type": "form",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "incoming-webhook",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "webhook.sendgrid",
          "current_step": 2,
          "current_step_type": "fully_configured",
          "steps": [
            {
              "type": "form",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "sendgrid",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "webhook.sendwithus",
          "current_step": 2,
          "current_step_type": "fully_configured",
          "steps": [
            {
              "type": "form",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "incoming-webhook",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "webhook.sparkpost",
          "current_step": 2,
          "current_step_type": "fully_configured",
          "steps": [
            {
              "type": "form",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "incoming-webhook",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "webhook.vero",
          "current_step": 2,
          "current_step_type": "fully_configured",
          "steps": [
            {
              "type": "form",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "incoming-webhook",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "webhook.zapier",
          "current_step": 2,
          "current_step_type": "fully_configured",
          "steps": [
            {
              "type": "form",
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "incoming-webhook",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "webhook.incoming-webhook",
          "current_step": 2,
          "current_step_type": "fully_configured",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "webhookz_primary_key",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_immutable",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": false
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
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "incoming-webhook",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.sailthru",
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
                  "name": "api_key",
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
                  "name": "api_secret",
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
            "pipeline_state": "beta",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.sailthru",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "webhook.segment",
          "current_step": 2,
          "current_step_type": "oauth",
          "steps": [
            {
              "type": "form",
              "properties": []
            },
            {
              "type": "oauth",
              "properties": [
                {
                  "name": "scope",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": true,
                  "property_type": "system_provided_by_default",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "source_names",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": true,
                  "property_type": "system_provided_by_default",
                  "json_schema": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "workspace_names",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": true,
                  "property_type": "system_provided_by_default",
                  "json_schema": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  },
                  "provided": false,
                  "tap_mutable": false
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
            "default_start_date": null,
            "default_scheduling_interval": null,
            "protocol": "segment_webhooks",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.amazon-sp",
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
                  "name": "aws_access_key",
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
                  "name": "aws_secret_key",
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
                  "name": "client_id",
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
                  "name": "client_secret",
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
                  "name": "marketplaces",
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
                  "name": "refresh_token",
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
                  "name": "role_arn",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.amazon-sp",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.dixa",
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
                  "name": "api_token",
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
                  "name": "interval",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.dixa",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.ms-dynamics",
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
                  "name": "api_version",
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
                  "name": "client_id",
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
                  "name": "client_secret",
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
                  "name": "max_pagesize",
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
                  "name": "organization_uri",
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
                  "name": "redirect_uri",
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
                  "name": "refresh_token",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.ms-dynamics",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.nice-incontact",
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
                  "name": "api_cluster",
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
                  "name": "api_key",
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
                  "name": "api_secret",
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
                  "name": "api_version",
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
                  "name": "auth_domain",
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
                  "name": "periods",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.nice-incontact",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.calendly",
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
                  "name": "calendly_api_token",
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
                  "name": "mode",
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
            "pipeline_state": "alpha",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.calendly",
            "access": false,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.google-ads",
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
                  "name": "conversion_window",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^([1-9]|[12][0-9]|30|60|90)$"
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
                  "name": "customer_ids",
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
                  "name": "developer_token",
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
                  "name": "login_customer_ids",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "customerId": {
                          "type": "string"
                        },
                        "loginCustomerId": {
                          "type": "string"
                        }
                      },
                      "additionalProperties": false
                    }
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "oauth_client_id",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": true,
                  "property_type": "system_provided_by_default",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false,
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
            "pipeline_state": "beta",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 60,
            "protocol": "platform.google-ads",
            "access": true,
            "image_version": "0.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.hp-mariadb",
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
                  "name": "dbname",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
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
                    "anyOf": [
                      {
                        "type": "string"
                      },
                      {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
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
                  "name": "include_schemas_in_destination_stream_name",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_immutable",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(true|false)$"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "incremental_limit",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+$"
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
                  "name": "server_id",
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
                    "pattern": "^(true|false)$"
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
            "default_start_date": null,
            "default_scheduling_interval": 60,
            "protocol": "platform.hp-mysql",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.hp-aurora",
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
                  "name": "dbname",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
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
                    "anyOf": [
                      {
                        "type": "string"
                      },
                      {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
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
                  "name": "include_schemas_in_destination_stream_name",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_immutable",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(true|false)$"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "incremental_limit",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+$"
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
                  "name": "server_id",
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
                    "pattern": "^(true|false)$"
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
            "default_start_date": null,
            "default_scheduling_interval": 60,
            "protocol": "platform.hp-mysql",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "platform.hp-cloudsql",
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
                  "name": "dbname",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
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
                    "anyOf": [
                      {
                        "type": "string"
                      },
                      {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
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
                  "name": "include_schemas_in_destination_stream_name",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_immutable",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(true|false)$"
                  },
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "incremental_limit",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided_advanced",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+$"
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
                  "name": "server_id",
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
                    "pattern": "^(true|false)$"
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
            "default_start_date": null,
            "default_scheduling_interval": 60,
            "protocol": "platform.hp-mysql",
            "access": true,
            "image_version": "1.latest"
          },
          "upgrade_available": null
        },
        {
          "type": "adroll",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "adroll",
            "access": false,
            "image_version": null
          },
          "upgrade_available": {
            "type": "platform.adroll"
          }
        },
        {
          "type": "ad-words",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": "-30 days",
            "default_scheduling_interval": 30,
            "protocol": "ad-words",
            "access": false,
            "image_version": null
          },
          "upgrade_available": {
            "type": "platform.google-ads"
          }
        },
        {
          "type": "azure_sqldw",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "released",
            "default_start_date": null,
            "default_scheduling_interval": null,
            "protocol": "azure_sqldw",
            "access": true,
            "image_version": null
          },
          "upgrade_available": null
        },
        {
          "type": "google-analytics-reporting",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": "-30 days",
            "default_scheduling_interval": 360,
            "protocol": "google-analytics-reporting",
            "access": false,
            "image_version": null
          },
          "upgrade_available": {
            "type": "platform.google-analytics"
          }
        },
        {
          "type": "autopilothq",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "autopilothq",
            "access": false,
            "image_version": null
          },
          "upgrade_available": {
            "type": "platform.autopilot"
          }
        },
        {
          "type": "bigquery",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "alpha",
            "default_start_date": null,
            "default_scheduling_interval": null,
            "protocol": "bigquery",
            "access": false,
            "image_version": null
          },
          "upgrade_available": null
        },
        {
          "type": "bigquery_v2",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "released",
            "default_start_date": null,
            "default_scheduling_interval": null,
            "protocol": "bigquery_v2",
            "access": true,
            "image_version": null
          },
          "upgrade_available": null
        },
        {
          "type": "bingads",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "bingads",
            "access": false,
            "image_version": null
          },
          "upgrade_available": {
            "type": "platform.bing-ads"
          }
        },
        {
          "type": "closeio",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "closeio",
            "access": false,
            "image_version": null
          },
          "upgrade_available": {
            "type": "platform.closeio"
          }
        },
        {
          "type": "databricks_delta",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "released",
            "default_start_date": null,
            "default_scheduling_interval": null,
            "protocol": "databricks_delta",
            "access": true,
            "image_version": null
          },
          "upgrade_available": null
        },
        {
          "type": "deskdotcom",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "released",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "deskdotcom",
            "access": true,
            "image_version": null
          },
          "upgrade_available": null
        },
        {
          "type": "square",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "square",
            "access": false,
            "image_version": null
          },
          "upgrade_available": {
            "type": "platform.square"
          }
        },
        {
          "type": "facebook",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "facebook",
            "access": false,
            "image_version": null
          },
          "upgrade_available": {
            "type": "platform.facebook"
          }
        },
        {
          "type": "googleanalytics",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "released",
            "default_start_date": null,
            "default_scheduling_interval": 30,
            "protocol": "googleanalytics",
            "access": true,
            "image_version": null
          },
          "upgrade_available": {
            "type": "platform.adwords"
          }
        },
        {
          "type": "google-ecommerce",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": null,
            "default_scheduling_interval": 30,
            "protocol": "google-ecommerce",
            "access": false,
            "image_version": null
          },
          "upgrade_available": null
        },
        {
          "type": "hubspot",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "hubspot",
            "access": false,
            "image_version": null
          },
          "upgrade_available": {
            "type": "platform.hubspot"
          }
        },
        {
          "type": "intercom",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "intercom",
            "access": false,
            "image_version": null
          },
          "upgrade_available": {
            "type": "platform.intercom"
          }
        },
        {
          "type": "jira",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "jira",
            "access": false,
            "image_version": null
          },
          "upgrade_available": {
            "type": "platform.jira"
          }
        },
        {
          "type": "mailchimp",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 1440,
            "protocol": "mailchimp",
            "access": false,
            "image_version": null
          },
          "upgrade_available": {
            "type": "platform.mailchimp"
          }
        },
        {
          "type": "marketo",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "marketo",
            "access": false,
            "image_version": null
          },
          "upgrade_available": {
            "type": "platform.marketo"
          }
        },
        {
          "type": "mixpanel",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": "-60 days",
            "default_scheduling_interval": 30,
            "protocol": "mixpanel",
            "access": false,
            "image_version": null
          },
          "upgrade_available": {
            "type": "platform.mixpanel"
          }
        },
        {
          "type": "mssql_server",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "released",
            "default_start_date": null,
            "default_scheduling_interval": null,
            "protocol": "mssql_server",
            "access": true,
            "image_version": null
          },
          "upgrade_available": null
        },
        {
          "type": "mysql_destination",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "beta",
            "default_start_date": null,
            "default_scheduling_interval": null,
            "protocol": "mysql_destination",
            "access": true,
            "image_version": null
          },
          "upgrade_available": null
        },
        {
          "type": "netsuite",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "netsuite",
            "access": false,
            "image_version": null
          },
          "upgrade_available": {
            "type": "platform.netsuite"
          }
        },
        {
          "type": "pardot",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": "-4 weeks",
            "default_scheduling_interval": 30,
            "protocol": "pardot",
            "access": false,
            "image_version": null
          },
          "upgrade_available": {
            "type": "platform.pardot"
          }
        },
        {
          "type": "pipedrive",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "pipedrive",
            "access": false,
            "image_version": null
          },
          "upgrade_available": {
            "type": "platform.pipedrive"
          }
        },
        {
          "type": "pipeline_iapi",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": null,
            "default_scheduling_interval": null,
            "protocol": "pipeline_iapi",
            "access": false,
            "image_version": null
          },
          "upgrade_available": null
        },
        {
          "type": "postgres",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": null,
            "default_scheduling_interval": null,
            "protocol": "postgres",
            "access": false,
            "image_version": null
          },
          "upgrade_available": {
            "type": "platform.hp-postgres"
          }
        },
        {
          "type": "quickbooks",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "quickbooks",
            "access": false,
            "image_version": null
          },
          "upgrade_available": {
            "type": "platform.quickbooks"
          }
        },
        {
          "type": "recurly",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "recurly",
            "access": false,
            "image_version": null
          },
          "upgrade_available": {
            "type": "platform.recurly"
          }
        },
        {
          "type": "panoply",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "released",
            "default_start_date": null,
            "default_scheduling_interval": null,
            "protocol": "redshift",
            "access": true,
            "image_version": null
          },
          "upgrade_available": null
        },
        {
          "type": "redshift",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "released",
            "default_start_date": null,
            "default_scheduling_interval": null,
            "protocol": "redshift",
            "access": true,
            "image_version": null
          },
          "upgrade_available": null
        },
        {
          "type": "snowflake",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "released",
            "default_start_date": null,
            "default_scheduling_interval": null,
            "protocol": "snowflake",
            "access": true,
            "image_version": null
          },
          "upgrade_available": null
        },
        {
          "type": "s3",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "released",
            "default_start_date": null,
            "default_scheduling_interval": null,
            "protocol": "s3",
            "access": true,
            "image_version": null
          },
          "upgrade_available": null
        },
        {
          "type": "dataworld",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "released",
            "default_start_date": null,
            "default_scheduling_interval": null,
            "protocol": "s3",
            "access": true,
            "image_version": null
          },
          "upgrade_available": null
        },
        {
          "type": "storagegrid",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "alpha",
            "default_start_date": null,
            "default_scheduling_interval": null,
            "protocol": "s3",
            "access": false,
            "image_version": null
          },
          "upgrade_available": null
        },
        {
          "type": "salesforce",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "salesforce",
            "access": false,
            "image_version": null
          },
          "upgrade_available": {
            "type": "platform.salesforce"
          }
        },
        {
          "type": "stripe",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "stripe",
            "access": false,
            "image_version": null
          },
          "upgrade_available": {
            "type": "platform.stripe"
          }
        },
        {
          "type": "trello",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "trello",
            "access": false,
            "image_version": null
          },
          "upgrade_available": {
            "type": "platform.trello"
          }
        },
        {
          "type": "twitter",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": null,
            "default_scheduling_interval": 30,
            "protocol": "twitter",
            "access": false,
            "image_version": null
          },
          "upgrade_available": null
        },
        {
          "type": "xero",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 360,
            "protocol": "xero",
            "access": false,
            "image_version": null
          },
          "upgrade_available": {
            "type": "platform.xero"
          }
        },
        {
          "type": "zendesk",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "zendesk",
            "access": false,
            "image_version": null
          },
          "upgrade_available": {
            "type": "platform.zendesk"
          }
        },
        {
          "type": "zopim",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "zopim",
            "access": false,
            "image_version": null
          },
          "upgrade_available": {
            "type": "webhook.incoming-webhook"
          }
        },
        {
          "type": "zuora",
          "details": {
            "pricing_tier": "standard",
            "pipeline_state": "deprecated",
            "default_start_date": "-1 year",
            "default_scheduling_interval": 30,
            "protocol": "zuora",
            "access": false,
            "image_version": null
          },
          "upgrade_available": {
            "type": "platform.zuora"
          }
        }
      ]
---