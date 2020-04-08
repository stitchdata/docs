---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "connection-check"
key: "retrieve-sources-last-connection-check"
version: "4"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Retrieve a source's last connection check"
method: "get"
short-url: |
  /v{{ endpoint.version }}/sources/{source_id}/last-connection-check
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.connection-checks.get-source.short }}"
description: |
  {{ api.core-objects.connection-checks.get-source.description | flatify }}


# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

arguments:
  - name: "source_id"
    required: true
    type: "path parameter"
    description: "A path parameter corresponding to the unique ID of the source."
    example-value: |
      86741


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of `200 OK` and a single [Connection Check object]({{ api.core-objects.connection-checks.object }}).


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    language: "json"
    code: |
      {% assign right-bracket = "}" %}
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | replace: "{source_id","86741" | remove: right-bracket | strip_newlines }} \
           -H "Authorization: Bearer <ACCESS_TOKEN>" \
           -H "Content-Type: application/json"


## Code samples live in: _data/connect/code-examples/connection-checks.yml
  - type: "Response"
    language: "json"
    subexamples:
      - type: "In progress connection check"
        code: |
          {{ site.data.connect.code-examples.connection-checks.in-progress }}

      - type: "Successful connection check"
        code: |
          {{ site.data.connect.code-examples.connection-checks.successful }}

      - type: "Failed connection check"
        code: |
          {{ site.data.connect.code-examples.connection-checks.in-progress }}
---