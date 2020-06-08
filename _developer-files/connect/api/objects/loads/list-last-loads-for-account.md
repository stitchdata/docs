---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "load"
key: "list-last-loads-for-account"
version: "4"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "{{ site.data.connect.core-objects.loads.list.title | flatify }}"
method: "get"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ site.data.connect.core-objects.loads.list.short | flatify }}"
description: |
  {% include note.html type="single-line" content="**This endpoint is in beta.**" %}

  {{ site.data.connect.core-objects.loads.list.description | flatify }}


# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

## This depends on the method being used, and the type of endpoint.

arguments:
  - name: "client_id"
    required: true
    type: "path parameter"
    description: |
      A path parameter corresponding to the unique ID of a Stitch account.

      **Note**: The client ID must be associated with the provided access token.
    example-value: |
      116078


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and an array of [Load objects]({{ site.data.connect.core-objects.load.object }}), one for each stream associated with the provided client ID.


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    request-url: "{{ endpoint.short-url | flatify | strip_newlines }}"
    header: "{{ site.data.connect.request-headers.get.without-body | flatify }}"

  - type: "Response"
    language: "json"
    code: |
      TODO

  - type: "Errors"
    # Included only if there are errors for the endpoint
    # The errors live in: _data/connect/response-codes.yml
---