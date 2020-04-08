---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "sources"
key: "get-iapi-access-token-ids"
version: "4"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Get Import API access token IDs"
method: "get"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}/{source_id}/tokens
full-url: |
  {{ site.data.connect.api.base-url }}{{ endpoint.short-url | flatify }}

short: "{{ site.data.connect.core-objects.sources.get-iapi-access-token-ids.short }}"
description: "{{ site.data.connect.core-objects.sources.get-iapi-access-token-ids.description }}"


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
  If successful, the API will return a status of `200 OK` and an array containing the IDs of the access tokens associated with the specified Import API source ID.


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    language: "json"
    code: |
      {% assign right-bracket = "}" %}curl {{ endpoint.full-url | flatify | replace: "{source_id","126890" | remove: right-bracket | strip_newlines }} \
           -H "Authorization: Bearer <CONNECT_ACCESS_TOKEN>" \
           -H "Content-Type: application/json"

  - type: "Response"
    language: "json"
    code: |
      [
        815713587
      ]

  # - type: "Errors"
---