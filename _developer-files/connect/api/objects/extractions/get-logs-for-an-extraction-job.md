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
  {% include note.html type="single-line" content="**This endpoint is in beta.**" %}
  
  {{ site.data.connect.core-objects.extractions.get-job-logs.description | flatify }}

  {{ endpoint.returns | flatify }}


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

  - name: "job_name"
    required: true
    type: "path parameter"
    description: |
      A path parameter corresponding to the unique ID of the extraction job to be retrieved.

      Make a request to [GET {{ site.data.connect.core-objects.extractions.list.name | flatify }}]({{ site.data.connect.core-objects.extractions.list.anchor | flatify }}) to retrieve the most recent extraction jobs for the specified Stitch account.
    example-value: |
      116078.233312.sync.e4d8eae5-b23e-11ea-94a1-02cbbd504f7d


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of `302 Found`. The **Location** header field in the response will contain a URL where you can download the logs for the specified extraction job.


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    request-url: |
      {% assign right-bracket = "}" %}{{ endpoint.short-url | flatify | replace: "{client_id","116078" | replace: "{job_name","116078.233312.sync.e4d8eae5-b23e-11ea-94a1-02cbbd504f7d" | remove: right-bracket | strip_newlines }}
    header: "{{ site.data.connect.request-headers.get.without-body | flatify }}"

  - type: "Response"
    language: "shell"
    code: |
      HTTP/1.1 302 Found
      Access-Control-Allow-Credentials: true
      Access-Control-Allow-Headers: Authorization, X-Requested-With, Content-Type, Accept, X-Stitch-Csrf-Token
      Access-Control-Allow-Methods: GET, POST, PUT, DELETE
      Access-Control-Max-Age: 604800
      Date: Tue, 23 Jun 2020 00:58:50 GMT
      Location: https://com-stitchdata-prod-platform-pod-logs.s3.amazonaws.com/116078.233312.sync.e4d8eae5-b23e-11ea-94a1-02cbbd504f7d?x-amz-security-token=<TOKEN>
      Server: nginx/1.10.2
      Content-Length: 0
      Connection: Close

  - type: "Errors"
    # Included only if there are errors for the endpoint
    # The errors live in: _data/connect/response-codes.yml
---