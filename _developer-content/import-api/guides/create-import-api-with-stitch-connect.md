---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Create and configure an Import API source with Stitch Connect
doc-type: "tutorial"

product-type: "import-api"
content-type: "guide"
content-id: "create-import-api-with-stitch-connect"
layout: tutorial

permalink: /developers/import-api/guides/create-import-api-integration-with-stitch-connect
icon: 
order: 1

summary: "Using the Stitch Connect API, create a new Import API integration and generate an access token. You'll also learn how to push data to the Import API after the source has been configured."
## This is used only on the /import-api/guides page.
description: "Create an Import API integration using the Stitch Connect API."


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Generate and Revoke Import API Access Tokens in the Stitch App"
    link: "{{ link.import-api.guides.generate-revoke-access-tokens | prepend: site.baseurl }}"

  - title: "Structuring Data for the Import API"
    link: "{{ link.import-api.guides.structure-data | prepend: site.baseurl }}"

  - title: "Import API reference"
    link: "{{ link.import-api.api | prepend: site.baseurl }}"

  - title: "Connect API reference"
    link: "{{ link.connect.api | prepend: site.baseurl }}"

# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}

  {% capture import-api-notice %}
  **Note**: This guide focuses on creating an Import API source using Stitch Connect. For help creating Import API integrations using the Stitch web app, refer to the [Generate and Revoke Import API access tokens in the Stitch app guide]({{ link.import-api.guides.generate-revoke-access-tokens | prepend: site.baseurl }}).
  {% endcapture %}

  {% include note.html type="single-line" content=import-api-notice %}

  {{ page.summary }}


# -------------------------- #
#     EXAMPLE TABLE DATA     #
# -------------------------- #

example-table:
  - name: "{{ system-column.batched-at }}"
    value: "2019-02-02 00:44:38.988+00"
  - name: "{{ system-column.received-at }}"
    value: "2019-02-02 00:43:53.75+00"
  - name: "{{ system-column.sequence }}"
    value: "100"
  - name: "{{ system-column.table-version }}"
    value: "0"
  - name: "id"
    value: "1"
  - name: "name"
    value: "Finn"
  - name: "updated_at"
    value: "2019-02-02T00:38:33+00:00"


# -------------------------- #
#     GUIDE REQUIREMENTS     #
# -------------------------- #

requirements:
  - item: |
      **Access to Stitch Connect.** To request access to Stitch Connect, fill out [this form]({{ site.data.connect.api.interest-form }}){:target="new"}.
  - item: |
      **An active Stitch client account and an account access token.** Account access tokens are obtained when creating a Stitch client account or performing OAuth for an existing Stitch account. Refer to the [Connect authentication guide]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.api.authentication }}) for more info.


steps:
  - title: "Get the Import API source report card"
    anchor: "get-import-api-source-report-card"
    content: |
      {% assign right-bracket = "}" %}
      {% assign source-type = "import_api" %}

      First, you'll need to retrieve the Import API's report card. {{ site.data.connect.data-structures.report-cards.source.description }}

      To retrieve the report card for the Import API, make a request to `GET {{ site.data.connect.core-objects.source-types.get.name | flatify }}`, replacing `{type}` with `import_api`. The `<API_TOKEN>` in the request [must be the account access token associated with the Stitch account](#prerequisites):

      ```json
      curl GET {{ site.data.connect.api.base-url | strip_newlines }}{{ site.data.connect.core-objects.source-types.get.name | flatify | replace: "{type",source-type | remove: right-bracket | strip_newlines }}
           -H 'Content-Type: application/json' \
           -H 'Authorization: Bearer <CONNECT_API_TOKEN>'
      ```

      The response will be a single object containing the Import API's report card:

      ```json
      {{ site.data.connect.code-examples.source-report-cards.import-api | rstrip }}
      ```

      Report cards contain [connection steps]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.data-structures.connection-steps.section }}), which are the steps necessary to configure a data source.

      In this case, the Import API has only one step (the `form`) step to be considered `fully_configured`.

  - title: "Create the Import API source"
    anchor: "create-import-api-source"
    content: |
      Now that you have the properties required to configure an Import API source, you can create it using the [Create a Source endpoint]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.core-objects.sources.create.anchor }}).

      To create the Import API source, make a request to `POST {{ site.data.connect.core-objects.sources.create.name | flatify }}` with a request body that includes the following properties:

      - `type`: This should be `import_api`.
      - `display_name`: {{ site.data.connect.general.common.attributes.display-name }}

         For example: A display name of `Import API` would create a destination schema named `import_api`.

      This request will complete the `form` step outlined in the source's report card:

      ```json
      curl -X POST {{ site.data.connect.api.base-url | strip_newlines }}{{ site.data.connect.core-objects.sources.create.name | flatify | strip_newlines }}
           -H 'Content-Type: application/json' \
           -H 'Authorization: Bearer <CONNECT_API_TOKEN>' \
           -d $'{
                  "type": "import_api",
                  "display_name": "Import API"
                }
      ```

      The response will be a [source object]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.core-objects.sources.object }}) with a report card property. Take note of the following:

      - The `token` property in the `properties` object.  The key in this object is the `token_id`, and the value is the access token associated with this Import API source.
      - The `current_step` in the `report_card` object is now `2`, which corresponds to the `fully_configured` step. This indicates that the source has been fully configured and you can now push data to it.

      ```json
      {{ site.data.connect.code-examples.sources.import-api.full-object | rstrip }}
      ```

  - title: "Push data to the Import API"
    anchor: "push-data-import-api"
    content: |
      {% capture out-of-scope-notice %}
      **Note**: Instructions for structuring the data in request bodies for the Import API is outside the scope of this guide. Refer to the [Structuring data for the Import API guide]({{ link.import-api.guides.structure-data | prepend: site.baseurl }}) for instructions and examples.
      {% endcapture %}

      {% include note.html type="single-line" content=out-of-scope-notice %}

      Now that the Import API is `fully_configured`, you start pushing data to it.

      While you used the Connect API to create the Import API source, to actually push data, you'll need to use the [Import API]({{ link.import-api.api | prepend: site.baseurl }}). 

      {% for substep in step.substeps %}
      - [Step 3.{{ forloop.index }}: {{ substep.title }}](#{{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Get the Import API access token"
        anchor: "get-import-api-access-token"
        content: |
          Requests made to the Import API should include the access token associated with the Import API integration. This is the `token` property contained in the response of [Step 2](#create-import-api-source):

          ```json
          {{ site.data.connect.code-examples.sources.import-api.access-token | rstrip }}
          ```

      - title: "Build the request header"
        anchor: "build-import-api-request-header"
        content: |
          Pushing data to the Import API is accomplished by making a request to `POST {{ site.data.import-api.api.core-objects.push.url }}`. The request header must include the Import API access token and a supported media type (`application/json` or `application/transit+json`):

          ```json
          curl -X POST {{ site.data.import-api.api.base-url | strip_newlines }}{{ site.data.import-api.api.core-objects.push.url | flatify | strip_newlines }}
               -H 'Content-Type: application/json' \
               -H 'Authorization: Bearer <IMPORT_API_TOKEN>' \
          ```

      - title: "Submit the request"
        anchor: "submit-request-to-import-api"
        content: |
          Lastly, you'll submit the request and push data to the Import API. Request bodies sent to the Import API must be valid JSON or Transit. Refer to the [Push endpoint documentation]({{ link.import-api.api | prepend: site.baseurl | append: site.data.import-api.api.core-objects.push.anchor }}) for descriptions of the arguments required to successfully use this endpoint.

          While structuring the request body data is outside the scope of this guide, you can refer to the [Structuring data for the Import API guide]({{ link.import-api.guides.structure-data | prepend: site.baseurl }}) for instructions and examples.

          For this example, we'll use a single record for a table named `customers`:

          ```json
          curl -X POST {{ site.data.import-api.api.base-url | strip_newlines }}{{ site.data.import-api.api.core-objects.push.url | flatify | strip_newlines }}
               -H 'Content-Type: application/json' \
               -H 'Authorization: Bearer <IMPORT_API_TOKEN>' \
               -d $'[
                      {
                        "client_id": 116078,
                        "table_name": "customers",
                        "sequence": 100,
                        "data": {
                          "id": "1",
                          "name": "Finn",
                          "updated_at": "2019-02-02T00:38:33+00:00"
                        },
                        "key_names": [
                          "id"
                        ],
                        "action": "upsert"
                      }
                    ]'
          ```

          If successful, the Import API will return a status of `201 Created` and the following response:

          ```json
          {
            "status": "OK",
            "message": "Batch Accepted!"
          }
          ```

          **Note**: Due to the structure of Stitch's replication process, data pushed to the Import API will not immediately be available in the destination. The successful response in this section refers only to Stitch **accepting** the data, not it being loaded.

  - title: "Verify the data in the destination"
    anchor: "verify-data-destination"
    content: |
      After Stitch loads the pushed data, you can expect to see a table in the schema associated with the integration that contains the data. In this example, the schema would be `import_api` and the table would be `customers`.

      The table will contain the attributes included in the request, along with [Stitch's system columns]({{ link.destinations.storage.sdc-columns | prepend: site.baseurl }}):

      {% assign table-rows = "name|value" | split: "|" %}

      <table>
      {% for row in table-rows %}
      <tr>
      {% for column in page.example-table %}
      <td>
      {{ column[row] | flatify }}
      </td>
      {% endfor %}
      </tr>
      {% endfor %}
      </table>

      **Note**: The structure of the table will be determined by the data loading rules for the specific destination being used. Refer to the [Destination data loading guides]({{ link.destinations.storage.loading-data | prepend: site.baseurl }}) for more info and examples.

  - title: "Rotate Import API access tokens"
    anchor: "rotate-import-api-access-tokens"
    content: |
      {% capture rotate-tokens-notice %}
      **Note**: This step isn't required to create an Import API source. This is only required if you wish to generate and replace an access token. For example: If your token is lost or compromised.
      {% endcapture %}

      {% include note.html content=rotate-tokens-notice %}

      Each Import API source is allowed a maximum of two active access tokens at a time.

      If you need to revoke a token, we recommend first creating a replacement and updating your application with it to prevent interruptions. **Note**: Any requests you attempt to send to Stitch during the time an invalid token is in use must be re-sent once a valid token is in place.

      In the following steps, you'll use the Connect API and your Connect API token to generate and revoke the Import API source's access tokens.

    substeps:
      - title: "Generate a replacement access token"
        anchor: "generate-replacement-access-token"
        content: |
          {% assign source-id = "126890" %}
          {% assign original-token-id = "544973525" %}

          To generate a new Import API access token, make a request to `POST {{ site.data.connect.core-objects.sources.create-iapi-token.name | flatify }}`, replacing `{source_id}` with the Import API source's `source_id`. In the [report card in Step 2](#create-import-api-source), you'll see the source ID is `{{ source-id }}`.

          ```json
          curl -X POST {{ site.data.connect.api.base-url | strip_newlines }}{{ site.data.connect.core-objects.sources.create-iapi-token.name | flatify | replace: "{source_id",source-id | remove: right-bracket | strip_newlines }}
               -H 'Content-Type: application/json' \
               -H 'Authorization: Bearer <CONNECT_API_TOKEN>'
          ```

          The response will be a source object with access token, connection, and report card properties:

          - `access_token` - The value of this property is the newly generated Import API access token.
          - `connection` - The `properties.token` object contains key-value pairs indicating the access tokens currently in use for the Import API source. The key is the `token_id`, and the value is the access token.
             - `545799083` is the `token_id` for the newly generated Import API access token
             - `{{ original-token-id }}` is the `token_id` for the original Import API access token. Keep this handy, as you'll need it in the next step to revoke the token.
          - `report_card` - The source's current configuration status.

          ```json
          {
            "access_token": "<NEW_IMPORT_API_ACCESS_TOKEN>",
            "connection": {
              "properties": {
                "token": {
                  "{{ original-token-id }}": "<ORIGINAL_IMPORT_API_ACCESS_TOKEN>",
                  "545799083": "<NEW_IMPORT_API_ACCESS_TOKEN>"
                }
              },
              "updated_at": "2019-02-06T14:22:53Z",
              "name": "import_api",
              "type": "import_api",
              "deleted_at": null,
              "system_paused_at": null,
              "stitch_client_id": 116078,
              "paused_at": null,
              "id": 126890,
              "display_name": "Import API",
              "created_at": "2019-02-05T16:44:55Z",
              "report_card": {
                "type": "import_api",
                "current_step": 2,
                "steps": [
                  {
                    "type": "form",
                    "properties": [
                      {
                        "name": "token",
                        "is_required": true,
                        "provided": true,
                        "is_credential": false,
                        "system_provided": true,
                        "json_schema": {
                          "type": "string"
                        },
                        "tap_mutable": false
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
          }
          ```

      - title: "Revoke the original access token"
        anchor: "revoke-original-access-token"
        content: |
          After you've replaced the access token in your application, you should revoke the original access token.

          To revoke the token, make a request to `DELETE {{ site.data.connect.core-objects.sources.revoke-iapi-token.name | flatify }}`, replacing `{source_id}` with the source ID and `{token_id}` with the token ID. In this example, that would be:

          - **Source ID** - {{ source-id }}
          - **Token ID** - {{ original-token-id }}

          ```json
          curl -X DELETE {{ site.data.connect.api.base-url | strip_newlines }}{{ site.data.connect.core-objects.sources.revoke-iapi-token.name | flatify | replace: "{source_id",source-id | replace:"{token_id",original-token-id | remove: right-bracket | strip_newlines }}
               -H 'Content-Type: application/json' \
               -H 'Authorization: Bearer <CONNECT_API_TOKEN>'
          ```

          The response will be a source object with report card and properties objects. In the example respose below, note that the `properties.token` object no longer contains the original Import API access token:

          ```json
          {
            "properties": {
              "token": {
                "545799083": "<NEW_IMPORT_API_ACCESS_TOKEN>"
              }
            },
            "updated_at": "2019-02-06T14:22:53Z",
            "name": "import_api",
            "type": "import_api",
            "deleted_at": null,
            "system_paused_at": null,
            "stitch_client_id": 116078,
            "paused_at": null,
            "id": 126890,
            "display_name": "Import API",
            "created_at": "2019-02-05T16:44:55Z",
            "report_card": {
              "type": "import_api",
              "current_step": 2,
              "steps": [
                {
                  "type": "form",
                  "properties": [
                    {
                      "name": "token",
                      "is_required": true,
                      "provided": true,
                      "is_credential": false,
                      "system_provided": true,
                      "json_schema": {
                        "type": "string"
                      },
                      "tap_mutable": false
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
          ```

# -------------------------- #
#        NEXT STEPS          #
# -------------------------- #

next-steps: |
  TODO
---