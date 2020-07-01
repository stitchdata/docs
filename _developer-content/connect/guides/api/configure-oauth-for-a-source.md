---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Configure OAuth for a Data Source with the Connect API
permalink: /developers/stitch-connect/guides/configure-oauth-for-a-source-with-stitch-connect
summary: "Configure OAuth for a data source using your own OAuth client credentials and the Connect API."
keywords: connect oauth, oauth, whitelabel, white label

product-type: "connect"
content-type: "guide"
content-id: "configure-oauth-source"
topics: "sources, connect api"

key: "configure-oauth-source-connect-api"

layout: tutorial


# -------------------------- #
#      GUIDE PAGE INFO       #
# -------------------------- #

## This is used only on the /stitch-connect/guides page.
doc-type: "tutorial"
icon: lock
order: 4

description: "Configure OAuth for a data source using your own OAuth credentials and the Connect API."


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Destination and source API availability"
    link: "{{ link.connect.guides.connection-reference | prepend: site.baseurl }}"

  - title: "Connect API reference"
    link: "{{ link.connect.api | prepend: site.baseurl }}"

# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro-sections:
  - content: |
      {% include misc/data-files.html %}

      Configuring OAuth yourself is required only if you want to use your own OAuth client credentials. Otherwise, Stitch will use its managed credentials to perform the OAuth handshake.

      Configuring OAuth allows you to completely white label the source setup process, ensuring your end users have a seamless experience. At a glance, the process will look like this:

      1. Your application handles the OAuth handshake and redirects
      2. Your application provides the required OAuth source properties to the Connect API
      3. Stitch manages OAuth and refresh tokens on an ongoing basis for sources that utilze them

      You can configure OAuth for any source with an `oauth` connection step.


# -------------------------- #
#     GUIDE REQUIREMENTS     #
# -------------------------- #

requirements:
  - item: |
      **Access to Stitch Connect and valid Connect API credentials.** Connect access is a Stitch Enterprise feature. Refer to the [Connect API reference]({{ link.connect.api | flatify | prepend: site.baseurl }}#authentication) for more info on obtaining API credentials.

  - item: |
      **Access to a source with an `oauth` connection step**. This guide will use a [Google Analytics SaaS source]({{ site.data.connect.api.section | flatify | prepend: site.baseurl | append: site.data.connect.data-structures.source-form-properties.section |  append: "-google-analytics-object" }}) as an example, but any source type with an `oauth` connection step will work.

      To determine if a source has an `oauth` connection step, [retrieve its Report Card]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.core-objects.source-types.get.anchor | flatify }}).


# -------------------------- #
#       TUTORIAL STEPS       #
# -------------------------- #

steps:
  - title: "Create and configure the source"
    anchor: "configure-the-source"
    endpoint: "POST {{ site.data.connect.core-objects.sources.create.name | flatify }}"
    content: |
      {% assign api = site.data.connect.api %}
      {% assign right-bracket = "}" %}
      {% assign source-id = "122635" %}

      Create and configure a source. Refer to steps 1-3 of the [Create and configure a source using the Connect API guide]({{ link.connect.guides.create-configure-a-source | flatify | prepend: site.baseurl }}) for instructions.

      **Note**: OAuth properties may be provided in the same request that creates the source, or in a subsequent request to update the source, which is the approach this guide takes.

  - title: "Get the source's OAuth properties"
    anchor: "get-source-oauth-properties"
    content: |
      {% include developers/api-tutorial-step-table.html item=step item-list=step.substeps %}

    substeps:
      - title: "Get the source's report card"
        anchor: "get-source-report-card"
        endpoint: "GET {{ site.data.connect.core-objects.source-types.get.name | flatify }}"
        content: |
          {% assign example-url = site.data.connect.core-objects.source-types.get.name %}

          The OAuth properties that a source uses are found in the `oauth` step of the source’s report card. Like the `form` step, these properties will vary from source to source.

          To retrieve the source's OAuth properties, make a request to [{{ substep.endpoint | flatify }}]({{ link.connect.api | append: site.data.connect.core-objects.source-types.get.anchor | prepend: site.baseurl }}), replacing `{source_type}` with the type of the source:
          
          {% assign request-url = example-url | flatify | replace: "{source_type","platform.google-analytics" | remove: right-bracket | strip_newlines %}

          {% assign description = substep.endpoint %}

          {% include developers/api-request-examples.html code-description=description header=site.data.connect.request-headers.get.without-body request-url=request-url %}

          The response will be a [Report card object]({{ link.connect.api | append: site.data.connect.data-structures.report-cards.source.section | prepend: site.baseurl }}) corresponding to the `source_type`. Locate the OAuth connection step (`steps.oauth`) property object:

          {% capture code %}
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
              "pipeline_state": "beta",
              "default_start_date": "-1 year",
              "default_scheduling_interval": 60,
              "protocol": "platform.google-analytics",
              "access": true
            }
          }
          {% endcapture %}

          {% assign description = "Response for " | append: substep.endpoint %}

          {% include layout/code-snippet.html code-description=description language="json" code=code %}

          For `platform.google-analytics` sources, the properties required for OAuth are:

          {% assign google-analytics-object = site.developer-files | where:"key","source-form-properties-google-analytics-object" | first %}
          {% assign google-analytics-oauth = google-analytics-object.oauth-attributes %}

          {% for attribute in google-analytics-oauth %}
          - `{{ attribute.name }}`
          {% endfor %}

      - title: "Understand OAuth property metadata"
        anchor: "understand-oauth-property-metadata"
        content: |
          Next, we'll touch on the properties an OAuth connection step property contains. You'll use this data to determine what information you need to provide to successfully configure OAuth for the source.

          For OAuth properties, we'll look at the following metadata:

          {% assign details-object = site.developer-files | where:"key","properties-object" | first %}
          {% assign details-attributes = details-object.object-attributes | sort_natural:"name" %}

          <table class="attribute-list table-hover">
          {% for attribute in details-attributes %}
          {% if attribute.oauth-description %}
          <tr>
          <td align="right" width="20%; fixed">
          <strong>{{ attribute.name }}</strong><br>
          {{ attribute.type | upcase }}
          </td>
          <td>
          {{ attribute.oauth-description | flatify | markdownify }}
          </td>
          </tr>
          {% endif %}
          {% endfor %}
          </table>

          If a property has an `is_required: true` value, it must be provided to successfully configure OAuth for the source.

          Additionally, consider the property's `property_type` value. To configure OAuth using your own OAuth client credentials, you'll need to provide values for properties where `property_type` is either `user_provided` or `system_provided_by_default`. If you don't provide a value for properties where `property_type: system_provided_by_default`, Stitch will use its own OAuth client credentials to perform the OAuth handshake. 

          Consider the OAuth properties for `platform.google-analytics`:

          {% capture code %}
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
          }
          {% endcapture %}

          {% include layout/code-snippet.html code-description="OAuth properties for platform.google-analytics" language="json" code=code %}

          As all the properties have an `is_required: true` value, we'll need to provide values for every property to configure OAuth.

  - title: "Perform an OAuth handshake with the source"
    anchor: "perform-oauth-handshake-with-source"
    content: |
      Now that you know what information you need to provide to the Connect API to configure OAuth, you can perform an OAuth handshake with the source.

      How you do this is up to you, as implementing an OAuth flow is outside the scope of this guide. We recommend referring to the source's OAuth documentation, which is included in every source's [connection property reference]({{ link.connect.api | append: site.data.connect.data-structures.source-form-properties.section | prepend: site.baseurl }}) (if available), for help.

  - title: "Update the source with the OAuth properties"
    anchor: "update-source-with-oauth-properties"
    endpoint: "PUT {{ site.data.connect.core-objects.sources.update.name | flatify }}"
    content: |
      {% include note.html type="single-line" content="**Note**: OAuth properties may be provided in the same request that creates the source, or in a subsequent request to update the source, which is the approach this section uses." %}

      After the OAuth handshake is successfully performed, you can provide the Connect API with the required OAuth properties.

      Make a request to [{{ step.endpoint | flatify }}]({{ link.connect.api | append: site.data.connect.core-objects.sources.update.anchor | prepend: site.baseurl }}), replacing `{source_id}` with the ID of the source.

      The request body should contain a `properties` object with the required OAuth properties and their values:

      {% assign example-url = site.data.connect.core-objects.sources.update.name %}
      {% assign request-url = example-url | flatify | replace: "{source_id",source-id | remove: right-bracket | strip_newlines %}

      {% assign description = step.endpoint %}
      {% capture code %}'{
         "properties":{
            "client_id":"<GOOGLE_ANALYTICS_CLIENT_ID>",
            "client_secret":"<GOOGLE_ANALYTICS_CLIENT_SECRET>",
            "refresh_token": "<GOOGLE_ANALYTICS_CLIENT_REFRESH_TOKEN>",
            "view_id": "143355753"
         }
      }'
      {% endcapture %}

      {% include developers/api-request-examples.html code-description=description header=site.data.connect.request-headers.put.with-body request-url=request-url code=code %}

      The response will be a [Source object]({{ link.connect.api | append: site.data.connect.core-objects.sources.object | flatify | prepend: site.baseurl }}). If provided, OAuth properties with an `is_credential: false` value will be included in the `properties` object. You can also check the OAuth property's `provided` value in the OAuth connection step (`steps.oauth`) property object:

      {% capture code %}
      {
        "properties": {
          "cron_expression": null,
          "frequency_in_minutes": "60",
          "image_version": "0.latest",
          "product": "pipeline",
          "quota_user": "234588",
          "report_definitions": [
            {
              "name": "Visitor Traffic",
              "id": "a53305a5-d6c8-42d3-9c5d-65a524f217c1"
            }
          ],
          "start_date": "2019-03-25T00:00:00Z",
          "view_id": "143355753"
        },
        "updated_at": "2020-06-26T18:06:12Z",
        "schedule": null,
        "name": "tap_google",
        "type": "platform.google-analytics",
        "deleted_at": null,
        "system_paused_at": null,
        "stitch_client_id": 116078,
        "paused_at": "2020-06-23T01:29:17Z",
        "id": 122635,
        "display_name": "Google Analytics",
        "created_at": "2020-03-25T20:23:29Z",
        "report_card": {
          "type": "platform.google-analytics",
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
                  "name": "quota_user",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": true,
                  "property_type": "read_only",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": true,
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
                  "name": "client_id",
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
                  "name": "client_secret",
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
                  "name": "view_id",
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
      {% endcapture %}

      {% assign description = "Response for " | append: step.endpoint %}

      {% include layout/code-snippet.html code-description=description language="json" code=code %}

      If all form and OAuth connection properties have been provided, the source will advance to the next step in the configuration process. This will typically be `field_selection` or `fully_configured`.
      

# -------------------------- #
#        NEXT STEPS          #
# -------------------------- #

next-steps: |
  Congratulations on configuring OAuth for a source! To fully configure a souce, you might also need to [select streams and fields]({{ link.connect.guides.select-streams-and-fields | prepend: site.baseurl }}) to replicate.

  Check out the [Tutorials and resources]({{ link.connect.guides.category | prepend: site.baseurl }}) to see what else you can do with Stitch Connect.
---