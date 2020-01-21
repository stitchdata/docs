---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Managing and Revoking Import API Access Tokens via the Connect API
permalink: /developers/stitch-connect/guides/manage-import-api-access-tokens
summary: ""

product-type: "connect"
content-type: "guide"
content-id: "manage-import-api-access-tokens"
content-topics: "import api, authentication"

key: "manage-import-api-access-tokens"

layout: tutorial


# -------------------------- #
#      GUIDE PAGE INFO       #
# -------------------------- #

## This is used only on the /stitch-connect/guides page.
doc-type: "tutorial"
icon: source
order: 6

description: "Manage and revoke access tokens for Import API sources using the Stitch Connect API."


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Stitch Import API access tokens"
    link: "{{ link.import-api.guides.access-tokens | prepend: site.baseurl }}"

  - title: "Import API reference"
    link: "{{ link.import-api.api | prepend: site.baseurl }}"

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
  - title: "Get the Import API's report card"
    anchor: "get-iapi-report-card"
    content: |
      todo


  - title: "Rotate Import API access tokens"
    anchor: "rotate-import-api-access-tokens"
    content: |
      {% capture rotate-tokens-notice %}
      **Note**: This step isn't required to create an Import API source. This is only required if you wish to generate and replace an access token. For example: If your token is lost or compromised.
      {% endcapture %}

      {% include note.html type="single-line" content=rotate-tokens-notice %}

      Each Import API source is allowed a maximum of two active access tokens at a time.

      If you need to revoke a token, we recommend first creating a replacement and updating your application with it to prevent interruptions. **Note**: Any requests you attempt to send to Stitch during the time an invalid token is in use must be re-sent once a valid token is in place.

      In the following steps, you'll use the Connect API and your Connect API token to generate and revoke the Import API source's access tokens.

# substeps:
#   - title: "Generate a replacement access token"
#     anchor: "generate-replacement-access-token"
#     content: |
#       {% assign source-id = "126890" %}
#       {% assign original-token-id = "544973525" %}

#       To generate a new Import API access token, make a request to `POST {{ site.data.connect.core-objects.sources.create-iapi-token.name | flatify }}`, replacing `{source_id}` with the Import API source's `source_id`. In the [report card in Step 2](#create-import-api-source), you'll see the source ID is `{{ source-id }}`.

#       ```json
#       curl -X POST {{ site.data.connect.api.base-url | strip_newlines }}{{ site.data.connect.core-objects.sources.create-iapi-token.name | flatify | replace: "{source_id",source-id | remove: right-bracket | strip_newlines }}
#            -H 'Content-Type: application/json' \
#            -H 'Authorization: Bearer <CONNECT_API_TOKEN>'
#       ```

#       The response will be a source object with access token, connection, and report card properties:

#       - `access_token` - The value of this property is the newly generated Import API access token.
#       - `connection` - The `properties.token` object contains key-value pairs indicating the access tokens currently in use for the Import API source. The key is the `token_id`, and the value is the access token.
#          - `545799083` is the `token_id` for the newly generated Import API access token
#          - `{{ original-token-id }}` is the `token_id` for the original Import API access token. Keep this handy, as you'll need it in the next step to revoke the token.
#       - `report_card` - The source's current configuration status.

#       ```json
#       {
#         "access_token": "<NEW_IMPORT_API_ACCESS_TOKEN>",
#         "connection": {
#           "properties": {
#             "token": {
#               "{{ original-token-id }}": "<ORIGINAL_IMPORT_API_ACCESS_TOKEN>",
#               "545799083": "<NEW_IMPORT_API_ACCESS_TOKEN>"
#             }
#           },
#           "updated_at": "2019-02-06T14:22:53Z",
#           "name": "import_api",
#           "type": "import_api",
#           "deleted_at": null,
#           "system_paused_at": null,
#           "stitch_client_id": 116078,
#           "paused_at": null,
#           "id": 126890,
#           "display_name": "Import API",
#           "created_at": "2019-02-05T16:44:55Z",
#           "report_card": {
#             "type": "import_api",
#             "current_step": 2,
#             "steps": [
#               {
#                 "type": "form",
#                 "properties": [
#                   {
#                     "name": "token",
#                     "is_required": true,
#                     "provided": true,
#                     "is_credential": false,
#                     "system_provided": true,
#                     "json_schema": {
#                       "type": "string"
#                     },
#                     "tap_mutable": false
#                   }
#                 ]
#               },
#               {
#                 "type": "fully_configured",
#                 "properties": []
#               }
#             ]
#           }
#         }
#       }
#       ```

#   - title: "Revoke the original access token"
#     anchor: "revoke-original-access-token"
#     content: |
#       After you've replaced the access token in your application, you should revoke the original access token.

#       To revoke the token, make a request to `DELETE {{ site.data.connect.core-objects.sources.revoke-iapi-token.name | flatify }}`, replacing `{source_id}` with the source ID and `{token_id}` with the token ID. In this example, that would be:

#       - **Source ID** - {{ source-id }}
#       - **Token ID** - {{ original-token-id }}

#       ```json
#       curl -X DELETE {{ site.data.connect.api.base-url | strip_newlines }}{{ site.data.connect.core-objects.sources.revoke-iapi-token.name | flatify | replace: "{source_id",source-id | replace:"{token_id",original-token-id | remove: right-bracket | strip_newlines }}
#            -H 'Content-Type: application/json' \
#            -H 'Authorization: Bearer <CONNECT_API_TOKEN>'
#       ```

#       The response will be a source object with report card and properties objects. In the example respose below, note that the `properties.token` object no longer contains the original Import API access token:

---