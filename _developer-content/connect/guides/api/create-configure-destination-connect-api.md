---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Create a Destination with the Connect API
permalink: /developers/stitch-connect/guides/create-destination-with-stitch-connect
summary: "Create a destination using the Stitch Connect API."

product-type: "connect"
content-type: "guide"
content-id: "create-destination"
topics: "destination, connect api"

key: "create-destination-connect-api"

layout: tutorial


# -------------------------- #
#      GUIDE PAGE INFO       #
# -------------------------- #

## This is used only on the /stitch-connect/guides page.
doc-type: "tutorial"
icon: destination
order: 3

description: "Create and configure a destination using the Connect API."


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Destination and destination API availability"
    link: "{{ link.connect.guides.connection-reference | prepend: site.baseurl }}"

  - title: "Create a data source with the Connect API"
    link: "{{ link.connect.guides.create-configure-a-source | prepend: site.baseurl }}"

  - title: "Replication scheduling for destinations using the Connect API"
    link: "{{ link.connect.guides.replication-scheduling-for-destinations | prepend: site.baseurl }}"

  - title: "Connect API reference"
    link: "{{ link.connect.api | prepend: site.baseurl }}"

# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}
  {% assign api = site.data.connect.api %}

  {{ page.summary }}


# -------------------------- #
#     GUIDE REQUIREMENTS     #
# -------------------------- #

requirements:
  - item: |
      **Access to Stitch Connect and valid Connect API credentials.** Connect access is a Stitch {{ site.data.stitch.subscription-plans.unlimited.name }} or {{ site.data.stitch.subscription-plans.unlimited-plus.name }} feature. Refer to the [Connect API reference]({{ link.connect.api | flatify | prepend: site.baseurl }}#authentication) for more info on obtaining API credentials.
  - item: |
      **A Stitch account.**


# -------------------------- #
#       TUTORIAL STEPS       #
# -------------------------- #

steps:
  - title: "Get the destination's API type"
    anchor: "get-destination-api-type"
    content: |
      {% assign right-bracket = "}" %}

      {% assign form-property = site.developer-files | find:"key","destination-form-properties-postgresql-object" %}

      To get started, you'll need to identify the API type of the destination you want to create. Every destination available in the Connect API has a `type` which is unique to that destination.

      For example: The API type for an {{ form-property.display-name }} destination is `{{ form-property.api-type }}`.

      Refer to the [Connection Property Reference]({{ link.connect.guides.connection-reference | prepend: site.baseurl | append: "#destinations-api-availability" }}) to locate the API type for your destination.

  - title: "Get the destination's report card"
    anchor: "get-destination-report-card"
    content: |
      {% assign destination-types = site.data.connect.core-objects.destination-types %}

      When preparing for destination creation, the next step is to get the report card for the destination you want to create. The report card contains information about the steps required to fully configure the connection.

      Use the [{{ destination-types.get.method | upcase }} {{ destination-types.get.name | flatify }} endpoint]({{ link.connect.api | append: destination-types.get.anchor | prepend: site.baseurl }}) to get the report card for the destination. In this example, we're retrieving the report card for a `{{ form-property.api-type }}` destination:

      {% assign example-url = destination-types.get.name %}
      {% assign request-url = example-url | flatify | remove: right-bracket | replace:"{destination_type",form-property.api-type | strip_newlines %}
      {% assign description = "GET " | append: example-url %}
      {% include developers/api-request-examples.html code-description=description header=site.data.connect.request-headers.get.without-body request-url=request-url %}

      The response will be a [destination object]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.core-objects.destinations.object }}) with a [Connection step object]({{ link.connect.api | append: site.data.connect.data-structures.connection-steps.section | prepend: site.baseurl }}):

      {% capture code %}
      {
        "type": "postgres",
        "current_step": 1,
        "current_step_type": "form",
        "steps": [
          {
            "type": "form",
            "properties": [
              {
                "name": "database",
                "is_required": true,
                "is_credential": false,
                "system_provided": false,
                "property_type": "user_provided",
                "json_schema": {
                  "type": "string"
                },
                "provided": false
              },
              {
                "name": "encryption_host",
                "is_required": false,
                "is_credential": false,
                "system_provided": false,
                "property_type": "user_provided",
                "json_schema": {
                  "type": "string"
                },
                "provided": false
              },
              {
                "name": "encryption_port",
                "is_required": false,
                "is_credential": false,
                "system_provided": false,
                "property_type": "user_provided",
                "json_schema": {
                  "type": "string",
                  "pattern": "^\\d+$"
                },
                "provided": false
              },
              {
                "name": "encryption_type",
                "is_required": true,
                "is_credential": false,
                "system_provided": false,
                "property_type": "user_provided",
                "json_schema": {
                  "type": "string",
                  "pattern": "^(ssh|none)$"
                },
                "provided": false
              },
              {
                "name": "encryption_username",
                "is_required": false,
                "is_credential": false,
                "system_provided": false,
                "property_type": "user_provided",
                "json_schema": {
                  "type": "string"
                },
                "provided": false
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
                "provided": false
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
                "provided": false
              },
              {
                "name": "port",
                "is_required": true,
                "is_credential": false,
                "system_provided": false,
                "property_type": "user_provided",
                "json_schema": {
                  "type": "string",
                  "pattern": "^\\d+$"
                },
                "provided": false
              },
              {
                "name": "ssl",
                "is_required": true,
                "is_credential": false,
                "system_provided": false,
                "property_type": "user_provided",
                "json_schema": {
                  "type": "string",
                  "pattern": "^(true|false)$"
                },
                "provided": false
              },
              {
                "name": "sslrootcert",
                "is_required": false,
                "is_credential": false,
                "system_provided": false,
                "property_type": "user_provided",
                "json_schema": {
                  "type": "string"
                },
                "provided": false
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
                "provided": false
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
      }
      {% endcapture %}
      {% assign description = "Response for GET " | append: example-url %}
      {% include layout/code-snippet.html code-description=description code=code %}

      **Note**: To create the destination in your account, the `details.access` property must be `true`. This indicates that the plan your Stitch account is using has access to the destination.

      For {{ form-property.display-name }} destinations, only the `form` step must be completed to fully configure the destination. To complete the step, you'll need to provide values for all required user-provided properties. These properties will have a `is_required: true` value and a `property_type: user_provided` value. Refer to the [{{ form-property.title }} documentation]({{ TODO }}) for more info about these properties.

  - title: "Create the destination and complete the form step"
    anchor: "create-destination-complete-form-step"
    content: |
      {% assign destinations = site.data.connect.core-objects.destinations %}

      Use the [{{ destinations.create.method | upcase }} {{ destinations.create.name | flatify }} endpoint]({{ link.connect.api | prepend: site.baseurl | append: destinations.create.anchor }}) to create the {{ form-property.display-name }} destination. The request body must include the following properties:

      {% include developers/api-form-property-fields-logic.html content="destination" %}

      - `type`: The API type of the destination. In this example, this value will be `{{ form-property.api-type }}`.
      - `properties`: A [Properties object]({{ site.data.connect.data-structures.properties.section | prepend: link.connect.api | prepend: site.baseurl }}) containing the properties required to configure the destination. Refer to the [destination connection property documentation]({{ TODO }}) for your destination for more info about the required properties.

         For `{{ form-property.api-type }}`, the required properties are:

         {% assign required-attributes = all-form-attributes | where:"required",true %}

         {% for attribute in required-attributes %}
         - `{{ attribute.name }}`
         {% endfor %}

      This request will complete the `form` step outlined in the destination's report card, which you retrieved in [Step 2](#get-destination-report-card):

      {% assign request-url = destinations.create.name %}
      {% assign description = "POST " | append: request-url %}
      {% capture code %}'{
        "type": "postgres",
        "name": "Staging",
        "description": "Postgres database for the staging environment.",
        "properties": {
          "database": "[DATABASE]",
          "encryption_type": "none",
          "host": "[HOST_ADDRESS]",
          "password": "[PASSWORD]",
          "port": "5432",
          "ssl": "false",
          "username": "[USERNAME]"
        }
      }'
      {% endcapture %}
      {% include developers/api-request-examples.html code-description=description header=site.data.connect.request-headers.post.with-body request-url=request-url code=code %}
 
      The response will be a [destination object]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.core-objects.destinations.object }}) containing the destination's ID, [report card]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.data-structures.report-cards.destination.section }}), and current configuration status (`report_card.current_step_type`):

      {% capture code %}
      {
        "description": "Postgres database for the staging environment.",
        "properties": {
          "database": "[DATABASE]",
          "encryption_type": "none",
          "host": "[HOST_ADDRESS]",
          "port": "5432",
          "ssl": "false",
          "username": "[USERNAME]"
        },
        "updated_at": "2021-06-03T16:11:03Z",
        "check_job_name": "116078.337658.check.8934a4cd-4d60-48c9-85e4-e95cab6d4cae",
        "name": "Staging",
        "type": "postgres",
        "deleted_at": null,
        "system_paused_at": null,
        "stitch_client_id": 116078,
        "paused_at": null,
        "id": 337658,
        "display_name": null,
        "created_at": "2021-06-03T16:11:03Z",
        "report_card": {
          "type": "postgres",
          "current_step": 2,
          "current_step_type": "fully_configured",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "database",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": true
                },
                {
                  "name": "encryption_host",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                },
                {
                  "name": "encryption_port",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+$"
                  },
                  "provided": false
                },
                {
                  "name": "encryption_type",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(ssh|none)$"
                  },
                  "provided": true
                },
                {
                  "name": "encryption_username",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
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
                  "provided": true
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
                  "provided": true
                },
                {
                  "name": "port",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+$"
                  },
                  "provided": true
                },
                {
                  "name": "ssl",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(true|false)$"
                  },
                  "provided": true
                },
                {
                  "name": "sslrootcert",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
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
                  "provided": true
                }
              ]
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

  - title: "Check the destination's configuration status"
    anchor: "check-destination-configuration-status"
    content: |
      After the destination is created, Stitch will automatically perform a connection check using the details provided in the `properties` object. If the check is successful, Sttich will advance to the next `step` in the destination's configuration.

      In this example, the only step required for our {{ form-property.display-name }} is the `form` step. The destination's configuration status should be `fully_configured` if the connection check was successful, meaning Stitch can begin loading replicated data into the destination.

      You can verify the destination's configuration status by sending a request to [{{ destinations.list.method | upcase }} {{ destinations.list.name | flatify }}]({{ link.connect.api | prepend: site.baseurl | append: destinations.list.anchor }}):

      {% assign example-url = destinations.list.name %}
      {% assign request-url = example-url | flatify | strip_newlines %}
      {% assign description = "GET " | append: example-url %}

      {% include developers/api-request-examples.html code-description=description header=site.data.connect.request-headers.get.without-body request-url=request-url %}

      The response will be a [destination object]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.core-objects.destinations.object }}) containing the destination's current configuration status (`report_card.current_step_type`):

      {% capture code %}
      {
        "description": "Postgres database for the staging environment.",
        "properties": {
          "database": "[DATABASE]",
          "encryption_type": "none",
          "host": "[HOST_ADDRESS]",
          "port": "5432",
          "ssl": "false",
          "username": "[USERNAME]"
        },
        "updated_at": "2021-06-03T16:11:03Z",
        "check_job_name": "116078.337658.check.8934a4cd-4d60-48c9-85e4-e95cab6d4cae",
        "name": "Staging",
        "type": "postgres",
        "deleted_at": null,
        "system_paused_at": null,
        "stitch_client_id": 116078,
        "paused_at": null,
        "id": 337658,
        "display_name": null,
        "created_at": "2021-06-03T16:11:03Z",
        "report_card": {
          "type": "postgres",
          "current_step": 2,
          "current_step_type": "fully_configured",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "database",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": true
                },
                {
                  "name": "encryption_host",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
                },
                {
                  "name": "encryption_port",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+$"
                  },
                  "provided": false
                },
                {
                  "name": "encryption_type",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(ssh|none)$"
                  },
                  "provided": true
                },
                {
                  "name": "encryption_username",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
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
                  "provided": true
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
                  "provided": true
                },
                {
                  "name": "port",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d+$"
                  },
                  "provided": true
                },
                {
                  "name": "ssl",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^(true|false)$"
                  },
                  "provided": true
                },
                {
                  "name": "sslrootcert",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": false
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
                  "provided": true
                }
              ]
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


# -------------------------- #
#        NEXT STEPS          #
# -------------------------- #

next-steps: |
  Congratulations on configuring a destination using the Connect API! Now that you've got a destination, start [creating data sources and get your data flowing]({{ link.connect.guides.create-configure-a-source | prepend: site.baseurl }}).

  Check out the [Tutorials and resources]({{ link.connect.guides.category | prepend: site.baseurl }}) to see what else you can do with Stitch Connect.
---