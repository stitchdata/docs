---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Create a Data Source with the Connect API
permalink: /developers/stitch-connect/guides/create-data-source-with-stitch-connect
summary: "Create a data source using the Stitch Connect API."

product-type: "connect"
content-type: "guide"
content-id: "create-data-source"
topics: "sources, connect api"

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

      {% assign example-url = source-types.get.name %}
      {% assign request-url = example-url | flatify | remove: right-bracket | replace:"{source_type","platform.recurly" | strip_newlines %}
      {% assign description = "GET " | append: example-url %}
      {% include developers/api-request-examples.html code-description=description header=site.data.connect.request-headers.get.without-body request-url=request-url %}

      The response will be a [Source object]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.core-objects.sources.object }}) with a [Connection step object]({{ link.connect.api | append: site.data.connect.data-structures.connection-steps.section | prepend: site.baseurl }}):

      {% capture code %}
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
          "access": true
        }
      }
      {% endcapture %}
      {% assign description = "Response for GET " | append: example-url %}
      {% include layout/code-snippet.html code-description=description code=code %}

      **Note**: To create the source in your account, the `details.access` property must be `true`. This indicates that the plan your Stitch account is using has access to the source.

      {% assign form-property = site.developer-files | where:"key","source-form-properties-recurly-object" | first %}

      For Recurly sources, the following steps are required to fully configure the source:

      1. **The `form` step**. Provide values for all required user-provided properties. These properties will have a `is_required: true` value and a `property_type: user_provided` value. Refer to the [{{ form-property.title }} documentation]({{ link.connect.api | prepend: site.baseurl | append: "#" | append: form-property.key }}) for more info about these properties.

      2. **The `discover_schema` step.** Stitch runs a [connection check]({{ site.data.connect.core-objects.connection-checks.section | prepend: link.connect.api | prepend: site.baseurl }}) to test the provided `form` properties and detects the streams and fields available in the source. If all `form` properties are valid, including credentials, Stitch will automatically advance to the next step without any action required on your part.

         If the connection check fails, the source will remain on this step until a successful connection check completes.

      3. **The `field_selection` step**. Select the streams and fields you want to replicate.

  - title: "Create the source and complete the form step"
    anchor: "create-source-complete-form-step"
    content: |
      {% assign sources = site.data.connect.core-objects.sources %}

      Use the [{{ sources.create.method | upcase }} {{ sources.create.name | flatify }} endpoint]({{ link.connect.api | prepend: site.baseurl | append: sources.create.anchor }}) to create the Recurly source. The request body must include the following properties:

      {% include developers/api-form-property-fields-logic.html content="source" %}

      - `type`: The API type of the source. In this example, this value will be `platform.recurly`.
      - `display_name`: {{ site.data.connect.general.common.attributes.display-name }}

         For example:  A display name of `Recurly` will create a destination schema named `recurly`. **Note**: The schema name can't be changed after the source has been created.
      - `properties`: A [Properties object]({{ site.data.connect.data-structures.properties.section | prepend: link.connect.api | prepend: site.baseurl }}) containing the properties required to configure the source. Refer to the [Source form property documentation]({{ site.data.connect.data-structures.source-form-properties.section | prepend: link.connect.api | prepend: site.baseurl }}) for your source for more info about the required properties.

         For `platform.recurly`, the properties are:

         {% for attribute in all-form-attributes %}
         - `{{ attribute.name }}`{% if attribute.required == false %}*{% endif %}
         {% endfor %}

         <strong>*</strong> While these properties have a `is_required: false` value, you must provide a replication schedule for the source. Refer to the [Replication Scheduling for Sources Using the Connect API guide]({{ link.connect.guides.replication-scheduling-for-sources | prepend: site.baseurl }}) for more info and examples.

      This request will complete the `form` step outlined in the source's report card, which you retrieved in [Step 2](#get-source-report-card):

      {% assign request-url = sources.create.name %}
      {% assign description = "POST " | append: request-url %}
      {% capture code %}'{
         "type":"platform.recurly",
         "display_name":"Recurly",
         "properties":{
            "start_date":"2018-01-10T00:00:00Z",
            "api_key":"<RECURLY_API_KEY>",
            "frequency_in_minutes":"60",
            "quota_limit":"30",
            "subdomain":"stitchdata"
         }
      }'
      {% endcapture %}
      {% include developers/api-request-examples.html code-description=description header=site.data.connect.request-headers.post.with-body request-url=request-url code=code %}
 
      The response will be a [Source object]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.core-objects.sources.object }}) containing the source's ID, [report card]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.data-structures.report-cards.source.section }}), and current configuration status (`report_card.current_step_type`):

      {% capture code %}
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
      {% endcapture %}
      {% assign description = "Response for POST " | append: request-url %}
      {% include layout/code-snippet.html code-description=description code=code request-url=request-url %}

  # - title: "Wait for a successful connection check"
  #   anchor: "wait-successful-connection-check"
  #   content: |
  #     If all required `form` properties for the source have been provided, the source will automatically progress to `discover_schema` step. During this step, Stitch will perform a connection check using the `form` properties provided for the source.

  #     After a successful connection check completes, the source will automatically progress to [the `field_selection` step](#complete-field-selection-step). 

  #     If you notice that the source hasn't progressed past `discover_schema`, use the source's last connection check results to pinpoint the problem. Retrieve this info using the [GET {{ site.data.connect.core-objects.connection-checks.get-source.name | flatify }} endpoint](), replacing `{source_id}` with the source's ID:

  #     {% assign example-url = site.data.connect.core-objects.connection-checks.get-source.name %}
  #     {% assign request-url = example-url | flatify | remove: right-bracket | replace:"{source_id","233312" | strip_newlines %}
  #     {% assign description = "GET " | append: example-url %}

  #     {% include developers/api-request-examples.html code-description=description header=site.data.connect.request-headers.get.without-body request-url=request-url %}

  #     {{ site.data.connect.code-examples.connection-checks.failed | lstrip }}


  - title: "Complete the field selection step"
    anchor: "complete-field-selection-step"
    content: |
      Next, you'll select the streams and fields you want to replicate from the source. The source will automatically progress from `discover_schema` to `field_selection` after a successful connection check completes. 

      Locate the source's ID in the source's report card - in this example, it's `233312` - and follow the steps in the [Select Streams and Fields with the Connect API guide]({{ link.connect.guides.select-streams-and-fields | prepend: site.baseurl }}).

      To complete field selection, at least one stream and one field in the stream must be selected. This includes fields that are automatically selected. For example: If a stream uses an `id` field as a Primary Key, this field will be automatically included when the stream is selected.

      **Note**: Stream and field selection may occur any time when a source's `current_step` is `field_selection` or `fully_configured`, as long as the source's report card has a `field_selection` step.

  - title: "Check the source's configuration status"
    anchor: "check-source-configuration-status"
    content: |
      After field selection, the source's configuration status should be `fully_configured`. When `fully_configured`, Stitch can begin replication for the source using the schedule and stream/field selection data you provided.

      You can verify the source's configuration status by sending a request to [{{ sources.retrieve.method | upcase }} {{ sources.retrieve.name | flatify }}]({{ link.connect.api | prepend: site.baseurl | append: sources.retrieve.anchor }}), replacing `{source_id}` with the source's ID:

      {% assign example-url = sources.retrieve.name %}
      {% assign request-url = example-url | flatify | remove: right-bracket | replace:"{source_id","233312" | strip_newlines %}
      {% assign description = "GET " | append: example-url %}

      {% include developers/api-request-examples.html code-description=description header=site.data.connect.request-headers.get.without-body request-url=request-url %}

      The response will be a [Source object]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.core-objects.sources.object }}) containing the source's current configuration status (`report_card.current_step_type`):

      {% capture code %}
      {
        "properties": {
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
      {% endcapture %}

      {% assign description = "Response for GET " | append: example-url %}
      {% include layout/code-snippet.html code-description=description code=code request-url=request-url %}

  - title: "Start a replication job"
    anchor: "start-a-replication-job"
    content: |
      {% include note.html type="single-line" content="**Note**: This step is optional." %}
      
      {% assign replication-jobs = site.data.connect.core-objects.replication-jobs %}

      Now that the source is `fully_configured`, you can start extracting data.

      Stitch will automatically schedule a replication job based on the [schedule you set](#create-source-complete-form-step). To see when the next replication job will begin, check the  `schedule.next_fire_time` value in the Source object:

      {% capture code %}
      {
         "properties": {...},
         "updated_at": "2020-03-20T19:09:03Z",
         "schedule":{
            "type":"interval",
            "unit":"minute",
            "interval":60.0,
            "next_fire_time":"2020-03-20T19:09:38Z"
         },
         [...]
      }
      {% endcapture %}

      {% assign description = "Example schedule in a Source object" %}
      {% include layout/code-snippet.html code-description=description code=code %}

      If you want to start a replication job sooner than the `next_fire_time`, you can send a request to [POST {{ replication-jobs.post.name | flatify }}]({{ link.connect.api | prepend: site.baseurl | append: replication-jobs.post.anchor }}), replacing `{source_id}` with the source's ID:

      {% assign example-url = replication-jobs.post.name %}
      {% assign request-url = example-url | flatify | remove: right-bracket | replace:"{source_id","233312" | strip_newlines %}
      {% assign description = "POST " | append: example-url %}
      {% include developers/api-request-examples.html code-description=description header=site.data.connect.request-headers.post.without-body request-url=request-url %}

      **Note**: Stitch allows only one replication job to run at a time. The response to the above request may be either of the following:

      - **If the job started successfully**, the response will be a single [Replication Job object]({{ link.connect.api | prepend: site.baseurl | append: replication-jobs.object }}):

      {% capture code %}
      {
         "job_name":"116078.233312.sync.c12fb0a7-7e4a-11e9-abdc-0edc2c318fba"
      }
      {% endcapture %}
      {% assign description = "Response for POST " | append: example-url | append: " indicating a job was started" %}
         {% include layout/code-snippet.html use-code-block=false language="json" code-description=description code=code %}

         ```json
      {{ code | lstrip | rstrip }}
         ```

      - **If a job was already in progress**, the response will be a single error object similar to:

      {% capture code %}
      {
         "error":{
            "type":"already_running",
            "message":"Did not create job for client-id: 116078; connection-id: 233312 because one already exists"
         }
      }
      {% endcapture %}
      {% assign description = "Response for POST " | append: example-url | append: " indicating a job is already running" %}
         {% include layout/code-snippet.html use-code-block=false language="json" code-description=description code=code %}

         ```json
      {{ code | lstrip | rstrip }}
         ```

# -------------------------- #
#        NEXT STEPS          #
# -------------------------- #

next-steps: |
  Congratulations on configuring a data source using the Connect API! Check out the [Tutorials and resources]({{ link.connect.guides.category | prepend: site.baseurl }}) to see what else you can do with Stitch Connect.
---