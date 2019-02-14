---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "import-api"
content-type: "api-endpoint"
endpoint: "status"
key: "get-status"
version: "2"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Get Import API status"
method: "get"
short-url: |
  /v{{ object.version }}{{ object.endpoint-url | flatify }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ site.data.import-api.api.core-objects.api-status.short | flatify }}"
description: |
  {{ site.data.import-api.api.core-objects.api-status.description | flatify | markdownify }}

authorization-required: false
request-header-required: false

# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a `200 OK` status and an [API status]({{ site.data.import-api.api.core-objects.api-status.object-anchor }}) object.

# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    language: "curl"
    code: |
      curl {{ endpoint.full-url | flatify | strip_newlines }}

  - type: "Response"
    language: "json"
    code: |
      {
        "name": "pipeline.gate",
        "version": "0.3.3-SNAPSHOT",
        "revision": "a154360ad8c43182965049dbf6239aa7c1f3c84d",
        "status": "OK",
        "reason": null
      }
---