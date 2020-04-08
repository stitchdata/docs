---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "sources"
key: "revoke-iapi-access-token"
version: "4"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Revoke Import API access token"
method: "delete"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}/{source_id}/tokens/{token_id}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}

short: "{{ site.data.connect.core-objects.sources.revoke-iapi-token.short }}"
description: "{{ site.data.connect.core-objects.sources.revoke-iapi-token.description | flatify }}"


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

  - name: "token_id"
    required: true
    type: "string"
    description: |
      A path parameter corresponding to the unique ID of the Import API access token to be revoked.
    example-value: |
      544973525


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of `200 OK` and a [Source object]({{ api.core-objects.sources.object }}) a `report_card` property.


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    language: "json"
    code: |
      {% assign token-id = "544973525" %}{% assign right-bracket = "}" %}curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | replace: "{source_id","126890" | replace:"{token_id",token-id | remove: right-bracket | strip_newlines }} \
           -H "Authorization: Bearer <CONNECT_ACCESS_TOKEN>" \
           -H "Content-Type: application/json"

  - type: "Response"
    language: "json"
    code: |
      {{ site.data.connect.code-examples.sources.import-api.full-object }}

  - type: "Errors"
---