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
  {{ site.data.connect.api.base-url }}{{ endpoint.short-url | flatify }}

short: "{{ site.data.connect.core-objects.sources.create-iapi-token.short }}"
description: |
  {{ site.data.connect.core-objects.sources.create-iapi-token.description }}

  When using this endpoint, note the following:

  - **Using this endpoint won't create an Import API source**. Use the [Create a source]({{ site.data.connect.core-objects.sources.create.anchor }}) endpoint to first create the source and retrieve its ID. Refer to the [Create and configure an Import API source guide]({{ link.connect.guides.create-import-api-source | prepend: site.baseurl }}) for more info.
  
  - **Each Import API source can have a maximum of active two access tokens**. To generate additional access tokens, revoke an active token first and then create a new token. Refer to the [Managing and Revoking Import API Access Tokens via the Connect API]({{ link.connect.guides.manage-import-api-access-tokens | prepend: site.baseurl | append: "#rotate-import-api-access-tokens" }}) guide for instructions.


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
  If successful, the API will return a status of `200 OK` and an [Import API access token object]({{ site.data.connect.data-structures.import-api-access-token.section }}).

  **Note**: The API will only return the Import API access token once, immediately after generation.


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    language: "json"
    code: |
      {% assign right-bracket = "}" %}curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | replace: "{source_id","126890" | remove: right-bracket | strip_newlines }} \
           -H "Authorization: Bearer <CONNECT_ACCESS_TOKEN>" \
           -H "Content-Type: application/json"

  - type: "Response"
    language: "json"
    code: |
      {
        "id": 828792559,
        "access_token": "<IMPORT_API_ACCESS_TOKEN>"
      }

  - type: "Errors"
---