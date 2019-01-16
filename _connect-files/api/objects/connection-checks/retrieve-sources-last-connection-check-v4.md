---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

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
description: "{{ api.core-objects.connection-checks.get-source.description | flatify }}"


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
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | replace: "{source_id","86741" | remove: right-bracket | strip_newlines }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json"

  - type: "Response"
    language: "json"
    subexamples:
      - title: "In progress connection check"
        code: |
          {
            "target_exit_status": null,
            "tap_error_message": null,
            "check_exit_status": null,
            "name":"116078.120645.check.7bc049a4-18cf-11e9-a502-0e61abdd375a",
            "start_time":"2018-10-08T18:12:34Z",
            "mode":"check",
            "tap_exit_status": null,
            "target_error_message":null,
            "discovery_exit_status": null,
            “status”: “running”,
            "completion_time": null,
            "error":false,
            "discovery_error_message":null
          }

      - title: "Successful connection check"
        code: |
          {
            "target_exit_status": null,
            "tap_error_message": null,
            "check_exit_status": 0,
            "name": "116078.120645.check.5ee35614-18d8-11e9-b44f-06828117ecd6",
            "start_time": "2019-01-15T15:15:19Z",
            "mode": "check",
            "tap_exit_status": null,
            "target_error_message": null,
            "discovery_exit_status": 0,
            "status": "succeeded",
            "completion_time": "2019-01-15T15:15:22Z",
            "error": false,
            "discovery_error_message": null
          }

      - title: "Failed connection check"
        code: |
          {
            "target_exit_status": null,
            "tap_error_message": null,
            "check_exit_status": null,
            "name": "116078.120643.check.fefa6543-19a7-11e9-9068-12a37e8cec78",
            "start_time": "2019-01-16T16:01:34Z",
            "mode": "check",
            "tap_exit_status": null,
            "target_error_message": null,
            "discovery_exit_status": 1,
            "status": "failed",
            "completion_time": "2019-01-16T16:01:36Z",
            "error": true,
            "discovery_error_message": "FATAL:  password authentication failed for user \"<USERNAME>\""
          }
---