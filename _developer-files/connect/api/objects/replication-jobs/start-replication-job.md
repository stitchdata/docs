---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "replication-jobs"
key: "start-a-job"
version: "4"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Start a replication job"
method: "post"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.replication-jobs.post.description }}"
description: |
  {{ api.core-objects.replication-jobs.post.description }}

  **Note**: Stitch allows only one replication job to run at a time. Attempting to start a job when another is in progress will return a status of `200 OK` and a single error object. See the **Responses** tab below for an example.


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
  If successful, the API will return a status of <code class="api success">200 OK</code> and single [Replication Job object]({{ api.core-objects.replication-jobs.object }}).

  **Note**: Stitch allows only one replication job to run at a time. Attempting to start a job when another is in progress will return a status of `200 OK` and a single error object.

# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    language: "json"
    code: |
      {% assign right-bracket = "}" %}curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | replace: "{source_id","120643" | remove: right-bracket | strip_newlines }} \
           -H "Authorization: Bearer <ACCESS_TOKEN>" \
           -H "Content-Type: application/json"

  - type: "Response"
    subexamples:
      - title: "Replication job successfully started"
        code: |
          {
          "job_name": "116078.120643.sync.c12fb0a7-7e4a-11e9-abdc-0edc2c318fba"
          }

      - title: "Replication not started; another job is in progress"
        code: |
          {
            "error": {
              "type": "already_running",
              "message": "Did not create job for client-id: <CLIENT_ID>; connection-id: <SOURCE_ID> because one already exists"
            }
          }

  - type: "Errors"
  # The errors live in: _data/connect/response-codes/replication-jobs.yml
---