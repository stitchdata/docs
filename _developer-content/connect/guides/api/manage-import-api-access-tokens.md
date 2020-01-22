---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Managing and Revoking Import API Access Tokens via the Connect API
permalink: /developers/stitch-connect/guides/manage-import-api-access-tokens
summary: "Learn to create and manage access tokens for Import API sources using the Connect API."

product-type: "connect"
content-type: "guide"
content-id: "manage-import-api-access-tokens"
content-topics: "import api, authentication"

key: "manage-import-api-access-tokens"

layout: general
sidebar: on-page


# -------------------------- #
#      GUIDE PAGE INFO       #
# -------------------------- #

## This is used only on the /stitch-connect/guides page.
doc-type: "tutorial"
icon: lock
order: 6

description: "Manage and revoke access tokens for Import API sources using the Stitch Connect API."


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Manage Import API access tokens in Stitch"
    link: "{{ link.import-api.guides.access-tokens | prepend: site.baseurl }}"

  - title: "Connect API reference"
    link: "{{ link.connect.api | prepend: site.baseurl }}"

  - title: "Import API reference"
    link: "{{ link.import-api.api | prepend: site.baseurl }}"

  - title: "All Connect guides"
    link: "{{ link.connect.guides.category | prepend: site.baseurl }}"

  - title: "All Import API guides"
    link: "{{ link.import-api.guides.category | prepend: site.baseurl }}"


# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}
  {% capture stitch-notice %}
  **Note**: This guide is specific to the Connect API. Refer to the [Managing and Revoking Import API Access Tokens in Stitch guide]({{ link.import-api.guides.manage-access-tokens-stitch | prepend: site.baseurl }}) for info about managing Import API access tokens in Stitch.
  {% endcapture %}

  {% include note.html type="single-line" content=stitch-notice %}

  {{ page.summary }}


# -------------------------- #
#     GUIDE REQUIREMENTS     #
# -------------------------- #

requirements:
  - item: |
      **Access to Stitch Connect and valid Connect API credentials.** Connect access is a Stitch Enterprise feature. Refer to the [Connect API reference]({{ link.connect.api | flatify | prepend: site.baseurl }}#authentication) for more info on obtaining API credentials.
  - item: |
      **An existing Import API source.** This guide assumes you've already created an Import API source, either in Stitch or using the Connect API. If you haven't, create one before continuing by using one of the following guides:

      - [Create and configure an Import API source with the Connect API]({{ link.connect.guides.create-import-api-source | prepend: site.baseurl }})
      - [Create an Import API integration in Stitch]({{ link.import-api.guides.quick-start | prepend: site.baseurl | append: "#obtain-api-credentials" }})


# -------------------------- #
#       TUTORIAL STEPS       #
# -------------------------- #

client-id: "116078"
source-id: "216359"
token-id: "828704779"


sections:
  - title: "Import API access tokens and destination schemas"
    anchor: "import-api-access-tokens-integrations"
    content: |
      {% include developers/import-api/obtaining-credentials.html type="general" %}

  - title: "Generate an Import API access token"
    anchor: "generate-import-api-access-token"
    content: |
      In this section:

      {% include developers/api-tutorial-step-table.html item=subsection item-list=section.subsections %}

    subsections:
      - title: "Step 1: Retrieve the Import API source's ID"
        anchor: "generate--retrieve-iapi-source-id"
        endpoint: "GET {{ site.data.connect.core-objects.sources.list.name | flatify }}"
        content: |
          If you know the ID of the Import API source you want to use, [skip to the next step](#generate--create-access-tokens).

          {% capture get-id-content %}
          If you're logged into Stitch, you can locate the ID of your Import API source by clicking into the integration and looking at its URL. The number between `connections/` and `/summary` in the URL is the source ID:

          ![The Stitch app in a web browser, with the source ID highlighted in the URL.]({{ site.baseurl }}/images/integrations/import-api-source-id-url.png)

          In this example, the source ID is `{{ page.source-id }}`.

          Otherwise, you can use the [List all sources]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.core-objects.sources.list.anchor }}) endpoint (`{{ site.data.connect.core-objects.sources.list.method | upcase }} {{ site.data.connect.core-objects.sources.list.name | flatify }}`) to get a list of the current Stitch account's sources:

          ```shell
           # GET {{ site.data.connect.core-objects.sources.list.name | flatify }}
          curl "{{ site.data.connect.api.base-url }}{{ site.data.connect.core-objects.sources.list.name | flatify }}" \
               -H "Authorization: Bearer <CONNECT_ACCESS_TOKEN>" \
               -H "Content-Type: application/json"
          ```

          The response will be an array of [Source objects]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.core-objects.sources.object }}). Locate the Import API source you want to use, and take note of its `id` value:

          ```json
          [
            {
              ...
            },
            {
              "properties": {},
              "updated_at": "2020-01-21T22:38:21Z",
              "schedule": null,
              "name": "import_api_tokens_example",
              "type": "import_api",
              "deleted_at": null,
              "system_paused_at": null,
              "stitch_client_id": {{ page.client-id }},
              "paused_at": null,
              "id": {{ page.source-id }},                                 /* Source ID */
              "display_name": "Import API tokens example",
              "created_at": "2020-01-21T22:38:21Z",
              "report_card": {
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
                ]
              }
            },
            {
              ...
            }
          ]
          ```
          {% endcapture %}

          {{ get-id-content | flatify }}

      - title: "Step 2: Create the access token"
        anchor: "generate--create-access-tokens"
        endpoint: "POST {{ site.data.connect.core-objects.sources.create-iapi-token.name | flatify }}"
        content: |
          {% capture generate-access-token-content %}
          {% assign right-bracket = "}" %}

          Using the Import API source's ID, make a request to the [Generate an Import API access token endpoint]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.core-objects.sources.create-iapi-token.anchor }}) (`{{ site.data.connect.core-objects.sources.create-iapi-token.method | upcase }} {{ site.data.connect.core-objects.sources.create-iapi-token.name | flatify }}`), replacing `{source_id}` with the ID of the Import API source. In this example, the ID is `{{ page.source-id }}`:

          ```shell
          # POST {{ site.data.connect.core-objects.sources.create-iapi-token.name | flatify }}
          curl -X "POST" {{ site.data.connect.api.base-url }}{{ site.data.connect.core-objects.sources.create-iapi-token.name | flatify | replace: "{source_id",page.source-id | remove: right-bracket | strip_newlines }} \
               -H "Authorization: Bearer <CONNECT_ACCESS_TOKEN>" \
               -H "Content-Type: application/json"
          ```

          The response will be an [Import API access token object]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.data-structures.import-api-access-token.section }}) with an `access_token` property. The value of this property is the access token you'll need to include in requests made to the Import API:

          ```json
          {
            "access_token": "<IMPORT_API_ACCESS_TOKEN>"
          }
          ```
          {% endcapture %}

          {{ generate-access-token-content | flatify }}

      - title: "Step 3: Retrieve the Import API access token's ID"
        anchor: "generate--get-iapi-access-token-id"
        endpoint: "GET {{ site.data.connect.core-objects.sources.get-iapi-access-token-ids.name | flatify }}"
        content: |
          {% capture retrieve-token-id-content %}
          Using the Import API source's ID, make a request to the [Get Import API access token IDs endpoint]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.core-objects.sources.get-iapi-access-token-ids.anchor }}) (`{{ site.data.connect.core-objects.sources.get-iapi-access-token-ids.method | upcase }} {{ site.data.connect.core-objects.sources.get-iapi-access-token-ids.name | flatify }}`), replacing `{source_id}` with the ID of the Import API source. In this example, the ID is `{{ page.source-id }}`:

          ```shell
          # GET {{ site.data.connect.core-objects.sources.get-iapi-access-token-ids.name | flatify }}
          curl {{ site.data.connect.api.base-url }}{{ site.data.connect.core-objects.sources.get-iapi-access-token-ids.name | flatify | replace: "{source_id",page.source-id | remove: right-bracket | strip_newlines }} \
               -H "Authorization: Bearer <CONNECT_ACCESS_TOKEN>" \
               -H "Content-Type: application/json"
          ```
          {% endcapture %}

          {{ retrieve-token-id-content | flatify }}

          The response will be an array containing the IDs of the access tokens associated with the specified Import API source ID:

          ```json
          [
            {{ page.token-id }}
          ]
          ```

          Store the access token ID somewhere secure, in case you need to revoke it at a later point.

  - title: "Rotate Import API access tokens"
    anchor: "rotate-import-api-access-tokens"
    content: |
      In this section:

      {% include developers/api-tutorial-step-table.html item=subsection item-list=section.subsections %}

    subsections:
      - title: "Step 1: Retrieve the Import API source's ID"
        anchor: "rotate--retrieve-iapi-source-id"
        endpoint: "GET {{ site.data.connect.core-objects.sources.list.name | flatify }}"
        content: |
          If you know the ID of the Import API source you want to use, [skip to the next step](#rotate--create-new-access-token).

          {{ get-id-content | flatify }}

      - title: "Step 2: Create a new Import API access token"
        anchor: "rotate--create-new-access-token"
        endpoint: "POST {{ site.data.connect.core-objects.sources.create-iapi-token.name | flatify }}"
        content: |
          Before you revoke the original access token, we recommend generating a new one to take its place. This will minimize disruptions to replication while you update your Import API credentials.

          {{ generate-access-token-content | flatify }}

      - title: "Step 3: Retrieve the Import API access token IDs"
        anchor: "rotate--get-iapi-access-token-id"
        endpoint: "GET {{ site.data.connect.core-objects.sources.get-iapi-access-token-ids.name | flatify }}"
        content: |
          {{ retrieve-token-id-content | flatify }}

          The response will be an array containing the IDs of the access tokens associated with the specified Import API source ID:

          ```json
          [
            828705046,            /* New token ID */
            {{ page.token-id | strip }}             /* Original token ID */
          ]
          ```

          Import API Access token IDs are auto-incrementing, meaning their values will only increase. The ID with the greater value is the ID for the newer access token. In this example, the ID for the new access token would be `828705046`.

          Store the ID for the new access token somewhere secure, in case you need to revoke it at a later point.

          Keep the ID of the original access token (`{{ page.token-id | strip }}`) handy - you'll need it to complete the last step in this guide.

      - title: "Step 4: Update your Import API credentials"
        anchor: "rotate--update-your-import-api-credentials"
        content: |
          Before continuing, update your application with the new Import API access token you generated in [Step 2](#rotate--create-new-access-token).

      - title: "Step 5: Revoke the original Import API access token"
        anchor: "rotate--revoke-original-access-token"
        endpoint: "DELETE {{ site.data.connect.core-objects.sources.revoke-iapi-token.name | flatify }}"
        content: |
          Make a request to the [Revoke Import API access token endpoint]({{ link.connect.api | prepend: site.baseurl | append:site.data.connect.core-objects.sources.revoke-iapi-token.anchor }}) endpoint (`DELETE {{ site.data.connect.core-objects.sources.revoke-iapi-token.name | flatify }}`), replacing `{source_id}` with the source ID and `{token_id}` with the ID of the access token to be revoked.

          In this example, that would be `{{ page.source-id }}` and `{{ page.token-id }}`, respectively:

          ```shell
          # DELETE {{ site.data.connect.core-objects.sources.revoke-iapi-token.name | flatify }}
          curl -X DELETE {{ site.data.connect.api.base-url | strip_newlines }}{{ site.data.connect.core-objects.sources.revoke-iapi-token.name | flatify | replace: "{source_id",page.source-id | replace:"{token_id",page.token-id | remove: right-bracket | strip_newlines }} \
               -H "Authorization: Bearer <CONNECT_ACCESS_TOKEN>" \
               -H "Content-Type: application/json"
          ```

          If successful, the response will be a [Source object]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.core-objects.sources.object }}) with an updated `updated_at` value:

          ```json
          {
            "properties": {},
            "updated_at": "2020-01-22T09:40:32Z",
            "schedule": null,
            "name": "import_api_tokens_example",
            "type": "import_api",
            "deleted_at": null,
            "system_paused_at": null,
            "stitch_client_id": {{ page.client-id }},
            "paused_at": null,
            "id": {{ page.source-id }},
            "display_name": "Import API tokens example",
            "created_at": "2020-01-21T22:38:21Z",
            "report_card": {
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
              ]
            }
          }
          ```

      - title: "Step 6: Verify the access token revocation"
        anchor: "rotate--verify-token-revocation"
        endpoint: "GET {{ site.data.connect.core-objects.sources.get-iapi-access-token-ids.name | flatify }}"
        content: |
          Additionally, you can verify that the access token has been successfully revoked by checking the access token IDs associated with the Import API source.

          {{ retrieve-token-id-content | flatify }}

          The response should only contain the ID for the new access token:

          ```json
          [
            828705046
          ]
          ```
---
{% include misc/data-files.html %}