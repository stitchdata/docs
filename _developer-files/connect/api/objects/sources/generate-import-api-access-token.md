---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "sources"
key: "generate-iapi-access-token"
version: "4"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Generate Import API access token"
method: "post"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}/{source_id}/tokens
full-url: |
  {{ site.data.connectapi.base-url }}{{ endpoint.short-url | flatify }}

short: "{{ site.data.connect.core-objects.sources.create-iapi-token.short }}"
description: "{{ site.data.connect.core-objects.sources.create-iapi-token.description }}"


# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

arguments:
  - name: "source_id"
    required: true
    type: "string"
    description: |
      A path parameter corresponding to the unique ID of the Import API source.
    example-value: |
      126890


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of `200 OK` and a [Source object]({{ site.data.connect.core-objects.sources.object }}) with `access_token`, `connection`, and `report_card` properties.

  The `access_token` property contains the newly generated Import API access token.

  The `connection` property contains a `properties.token` object. This object contains key-value pairs of the token IDs and access tokens currently in use for the Import API source.

# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    language: "json"
    code: |
      {% assign right-bracket = "}" %}
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | replace: "{source_id","126890" | remove: right-bracket | strip_newlines }}
           -H "Authorization: Bearer <CONNECT_ACCESS_TOKEN>" 
           -H "Content-Type: application/json"

  - type: "Response"
    language: "json"
    code: |
      {
        "access_token": "<NEW_IMPORT_API_ACCESS_TOKEN>",
        "connection": {
          "properties": {
            "token": {
              "544973525": "<ORIGINAL_IMPORT_API_ACCESS_TOKEN>",
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

  - type: "Errors"
---