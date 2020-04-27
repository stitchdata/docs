---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "replication-jobs"
key: "stop-a-job"
version: "4"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Stop a replication job"
method: "delete"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ site.data.connect.core-objects.replication-jobs.delete.description }}"
description: "{{ site.data.connect.core-objects.replication-jobs.delete.description }}"


# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

arguments:
  - name: "source_id"
    required: true
    type: "path parameter"
    description: |
      A path parameter corresponding to the [unique ID of the source]({{ api.core-objects.sources.object }}).
    example-value: |
      120643


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and an object with a `status` property with a value of `200`.


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    request-url: |
      {% assign right-bracket = "}" %}{{ endpoint.short-url | flatify | replace: "{source_id","120643" | remove: right-bracket | strip_newlines }}
    header: "{{ site.data.connect.request-headers.delete | flatify }}"
    code: ""

  - type: "Response"
    language: "json"
    code: |
      {
        "status": 200
      }
---