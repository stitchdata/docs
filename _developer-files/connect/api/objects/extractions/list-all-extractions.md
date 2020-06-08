---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "extraction"
key: "list-last-extractions"
version: "4"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "{{ site.data.connect.core-objects.extractions.list.title | flatify }}"
method: "get"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ site.data.connect.core-objects.extractions.list.short | flatify }}"
description: "{{ site.data.connect.core-objects.extractions.list.description | flatify }}"


# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

## This depends on the method being used, and the type of endpoint.

arguments:
  - name: "client_id"
    required: true
    type: "path parameter"
    description: "A path parameter corresponding to the unique ID of a Stitch account."
    example-value: |
      116078


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and an array of [Extraction objects]({{ site.data.connect.core-objects.extractions.object }}), one for each source that has had a completed extraction job in the past 60 days.


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