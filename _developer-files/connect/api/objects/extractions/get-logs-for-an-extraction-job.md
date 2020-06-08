---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "extraction"
key: "get-logs-for-an-extraction-job"
version: "4"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "{{ site.data.connect.core-objects.extractions.get-job-logs.title | flatify }}"
method: "get"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}/{job_name}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ site.data.connect.core-objects.extractions.get-job-logs.short | flatify }}"
description: |
  {{ site.data.connect.core-objects.extractions.get-job-logs.description | flatify }}

  TODO: Explain how getting the logs works


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

  - name: "job_name"
    required: true
    type: "path parameter"
    description: "A path parameter corresponding to the unique ID of the extraction job to be retrieved."
    example-value: |
      3.1.sync.d7f18b02-a17c-44b7-bbd5-dc30e1dc6ce5


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and TODO.


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    request-url: |
      {% assign right-bracket = "}" %}{{ endpoint.short-url | flatify | replace: "{client_id","116078" | replace: "{job_name","3.1.sync.d7f18b02-a17c-44b7-bbd5-dc30e1dc6ce5" | remove: right-bracket | strip_newlines }}
    header: "{{ site.data.connect.request-headers.get.without-body | flatify }}"

  - type: "Response"
    language: "json"
    code: |
      TODO

  - type: "Errors"
    # Included only if there are errors for the endpoint
    # The errors live in: _data/connect/response-codes.yml
---