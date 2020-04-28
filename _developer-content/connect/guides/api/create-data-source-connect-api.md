---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Create a Data Source with the Connect API
#permalink: /developers/stitch-connect/guides/create-data-source-with-stitch-connect
summary: "Create a data source using the Stitch Connect API."

# product-type: "connect"
# content-type: "guide"
# content-id: "create-data-source"
# topics: "sources, connect api"

key: "create-source-connect-api"

layout: tutorial


# -------------------------- #
#      GUIDE PAGE INFO       #
# -------------------------- #

## This is used only on the /stitch-connect/guides page.
doc-type: "tutorial"
icon: source
order: 3

description: "Create and configure a data source using the Connect API."


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Destination and source API availability"
    link: "{{ link.connect.guides.connection-reference | prepend: site.baseurl }}"

  - title: "Replication scheduling for sources using the Connect API"
    link: "{{ link.connect.guides.replication-scheduling-for-sources | prepend: site.baseurl }}"

  - title: "Select streams and fields with the Connect API"
    link: "{{ link.connect.guides.select-streams-and-fields | prepend: site.baseurl }}"

  - title: "Field selection and compatibility rules"
    link: "{{ link.connect.guides.field-selection-compatibility-rules | prepend: site.baseurl }}"

  - title: "Connect API reference"
    link: "{{ link.connect.api | prepend: site.baseurl }}"

# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}

  {{ page.summary }}


# -------------------------- #
#     GUIDE REQUIREMENTS     #
# -------------------------- #

requirements:
  - item: |
      **Access to Stitch Connect and valid Connect API credentials.** Connect access is a Stitch Enterprise feature. Refer to the [Connect API reference]({{ link.connect.api | flatify | prepend: site.baseurl }}#authentication) for more info on obtaining API credentials.


# -------------------------- #
#       TUTORIAL STEPS       #
# -------------------------- #

steps:
  - title: "Get the source's API type"
    anchor: "get-source-api-type"
    content: |
      {% assign api = site.data.connect.api %}
      {% assign right-bracket = "}" %}

      To get started, you'll need to identify the API type of the data source you want to create. Every data source available in the Connect API has a `type`, and is typically similar to `platform.<source-type>`.

      For example: The API type for a Recurly source is `platform.recurly`.

      Refer to the [Destination and Source API Availability Reference]({{ link.connect.guides.connection-reference | prepend: site.baseurl | append: "#sources-api-availability" }}) to locate the API type for your data source.

  - title: "Get the source's report card"
    anchor: "get-source-report-card"
    content: |
      {% assign source-types = site.data.connect.core-objects.source-types %}

      When preparing for source creation, the next step is to get the report card for the source you want to create. The report card contains information about the steps required to fully configure a source.

      Use the [{{ source-types.get.method | upcase }} {{ source-types.get.name | flatify }} endpoint]({{ link.connect.api | append: source-types.get.anchor | prepend: site.baseurl }}) to get the report card for the source. In this example, we're retrieving the report card for a `platform.recurly` source:

      {% assign request-url = source-types.get.name %}

      {% assign description = "GET " | append: request-url %}

      {% include developers/api-request-examples.html code-description=description header=site.data.connect.request-headers.get.without-body request-url=request-url %}

      The response will be a [Source object]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.core-objects.sources.object }}) with a [Connection step object]({{ link.connect.api | append: site.data.connect.data-structures.connection-steps.section | prepend: site.baseurl }}):

      ```json
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
          "pricing_tier": "premium",
          "pipeline_state": "released",
          "default_start_date": "-1 year",
          "default_scheduling_interval": 60,
          "protocol": "platform.recurly",
          "access": true
        }
      }
      ```

      **Note**: To create the source in your account, the `details.access` property must be `true`. This indicates that the plan your Stitch account is using has access to the source.

      For Recurly sources, the following steps are required to fully configure the source:

      1. **The `form` step**. Provide values for all required user-provided properties. These properties will have a `is_required: true` value and a `property_type: user_provided` value. Refer to the [{{ form-property.title }} documentation]({{ | append: "#" | append: form-property.key }}) for more info about these properties.

      2. **The `discover_schema` step.** Stitch runs a [connection check]({{ site.data.connect.core-objects.connection-checks.section | prepend: link.connect.api | prepend: site.baseurl }}) to test the provided `form` properties and detects the streams and fields available in the source. If all `form` properties are valid, including credentials, Stitch will automatically advance to the next step without any action required on your part.

         If the connection check fails, the source will remain on this step until a successful connection check completes.

      3. **The `field_selection` step**. Select the streams and fields you want to replicate.

  - title: "Create the source and complete the form step"
    anchor: "create-source-complete-form-step"
    content: |
      {% assign sources = site.data.connect.core-objects.sources %}

      Use the [{{ sources.create.method | upcase }} {{ sources.create.name | flatify }} endpoint]({{ link.connect.api | prepend: site.baseurl | append: sources.create.anchor }}) to create the Recurly source. The request body must include the following properties:

      {% assign form-property = site.developer-files | where:"key","source-form-properties-recurly-object" | first %}

      {% include developers/api-form-property-fields-logic.html content="source" %}

      - `type`: The API type of the source. In this example, this value will be `platform.recurly`.
      - `display_name`: {{ site.data.connect.general.common.attributes.display-name }}

         For example:  A display name of `Recurly` will create a destination schema named `recurly`.
      - `properties`: A [Properties object]({{ site.data.connect.data-structures.properties.section | prepend: link.connect.api | prepend: site.baseurl }}) containing the properties required to configure the source. Refer to the [Source form property documentation]({{ site.data.connect.data-structures.source-form-properties.section | prepend: link.connect.api | prepend: site.baseurl }}) for your source for more info about the required properties.

         For `platform.recurly`, the properties are:

         {% for attribute in all-form-attributes %}
         - `{{ attribute.name }}`{% if attribute.required == false %}*{% endif %}
         {% endfor %}

         <strong>*</strong> While these properties have a `is_required: false` value, you must provide a replication schedule for the source. Refer to the [Replication Scheduling for Sources Using the Connect API guide]({{ link.connect.guides.replication-scheduling-for-sources | prepend: site.baseurl }}) for more info and examples.

      This request will complete the `form` step outlined in the source's report card, which you retrieved in [Step 2](#get-source-report-card):

      ```json
      curl -X POST {{ site.data.connect.api.base-url | strip_newlines }}{{ site.data.connect.core-objects.sources.create.name | flatify | strip_newlines }} \
           -H 'Content-Type: application/json' \
           -H 'Authorization: Bearer <CONNECT_API_TOKEN>' \
           -d $'{
                  "type": "platform.recurly",
                  "display_name": "Recurly",
                  "properties": {
                    "start_date": "2018-01-10T00:00:00Z",
                    "api_key": "<RECURLY_API_KEY>",
                    "frequency_in_minutes": "60",
                    "quota_limit": "30",
                    "subdomain": "stitchdata"
                  }
                }'
      ```

      The response will be a [Source object]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.core-objects.sources.object }}) containing the source's ID, [report card]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.data-structures.report-cards.source.section }}), and current configuration status (`report_card.current_step_type`):

      ```json
      {
        "properties": {
          "frequency_in_minutes": "60",
          "image_version": "1.latest",
          "quota_limit": "30",
          "start_date": "2018-01-10T00:00:00Z",
          "subdomain": "stitchdata"
        },
        "updated_at": "2020-03-20T16:06:19Z",
        "schedule": null,
        "check_job_name": "116078.233312.check.bc876980-6ac4-11ea-9197-0ee6b2399f9b",
        "name": "recurly",
        "type": "platform.recurly",
        "deleted_at": null,
        "system_paused_at": null,
        "stitch_client_id": 116078,
        "paused_at": null,
        "id": 233312,                                   /* Source ID */
        "display_name": "Recurly",
        "created_at": "2020-03-20T16:03:16Z",
        "report_card": {
          "type": "platform.recurly",
          "current_step": 3,
          "current_step_type": "field_selection",       /* Configuration status */
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
                  "provided": true,
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
                  "provided": true,
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
      ```

  - title: "Complete the field selection step"
    anchor: "complete-field-selection-step"
    content: |
      Next, you'll select the streams and fields you want to replicate from the source. Locate the source's ID in the source's report card - in this example, it's `233312` - and follow the steps in the [Select Streams and Fields with the Connect API guide]({{ link.connect.guides.select-streams-and-fields | prepend: site.baseurl }}).

      To complete field selection, at least one stream and one field in the stream must be selected. This includes fields that are automatically selected. For example: If a stream uses an `id` field as a Primary Key, this field will be automatically included when the stream is selected.

  - title: "Check the source's configuration status"
    anchor: "check-source-configuration-status"
    content: |
      After field selection, the source's configuration status should be `fully_configured`. When `fully_configured`, Stitch can begin replication for the source using the schedule and stream/field selection data you provided.

      You can verify the source's configuration status by sending a request to [{{ sources.retrieve.method | upcase }} {{ sources.retrieve.name | flatify }}]({{ link.connect.api | prepend: site.baseurl | append: sources.retrieve.anchor }}), replacing `{source_id}` with the source's ID:

      ```json
      curl {{ site.data.connect.api.base-url | strip_newlines }}{{ sources.retrieve.name | flatify | remove: right-bracket | replace:"{source_id","233312" | strip_newlines }} \
           -H 'Content-Type: application/json' \
           -H 'Authorization: Bearer <CONNECT_API_TOKEN>'
      ```

      The response will be a [Source object]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.core-objects.sources.object }}) containing the source's current configuration status (`report_card.current_step_type`):

      ```json
      {
        "properties": {
          "anchor_time": "2020-03-20T19:09:38.509Z",
          "frequency_in_minutes": "60",
          "image_version": "1.latest",
          "quota_limit": "30",
          "start_date": "2018-01-10T00:00:00Z",
          "subdomain": "stitchdata"
        },
        "updated_at": "2020-03-20T19:09:03Z",
        "schedule": {
          "type": "interval",
          "unit": "minute",
          "interval": 60.0,
          "next_fire_time": "2020-03-20T19:09:38Z"
        },
        "name": "recurly",
        "type": "platform.recurly",
        "deleted_at": null,
        "system_paused_at": null,
        "stitch_client_id": 116078,
        "paused_at": null,
        "id": 233312,
        "display_name": "Recurly",
        "created_at": "2020-03-20T16:03:16Z",
        "report_card": {
          "type": "platform.recurly",
          "current_step": 4,
          "current_step_type": "fully_configured",       /* Configuration status */
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
                  "provided": true,
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
                  "provided": true,
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
      ```

      TODO- FINISH THIS SECTION



# -------------------------- #
#        NEXT STEPS          #
# -------------------------- #

next-steps: |
  Congratulations on configuring a data source using the Connect API!

  TODO- Add links to other Connect stuff
---