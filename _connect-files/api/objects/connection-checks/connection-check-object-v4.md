---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-object"
endpoint: "connection-check"
order: 7


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Connection Check"  
endpoint-url: "/v4/{connection_type}/{connection_id}/last-connection-check"

description: "{{ api.core-objects.connection-checks.description | flatify }}"
intro-short: "Retrieve connection check results for a data source" # Used in the API functionality section of the docs

# -------------------------- #
#        VERSION INFO        #
# -------------------------- #

latest-version: "4"
versions:
  - number: "4"
    deprecated: false


# -------------------------- #
#      AVAILABLE METHODS     #
# -------------------------- #

available-methods:
  - id: "retrieve-sources-last-connection-check"
    title: "Retrieve a source's last connection check"
    method: "get"
    short: "{{ api.core-objects.connection-checks.get-source.short | flatify }}"

  # - id: "retrieve-destinations-last-connection-check"
  #   title: "Retrieve a destination's last connection check"
  #   method: "get"
  #   short: "{{ api.core-objects.last-connection-check.get-destination.short | flatify }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "name"
    type: "string"
    description: "The name of the connection check job."
    example-value: |
      116078.120645.check.5ee35614-18d8-11e9-b44f-06828117ecd6

  - name: "mode"
    type: "string"
    description: "This value will always be `check`."
    example-value: |
      check

  - name: "status"
    type: "string"
    description: |
      The status of the connection check job. Possible values are:

      - `running`
      - `succeeded`
      - `failed`
    example-value: |
      succeeded

  - name: "start_time"
    type: "timestamp"
    description: "The date and time the connection check job started."
    example-value: |
      2019-01-15T15:15:19Z

  - name: "completion_time"
    type: "timestamp"
    description: "The date and time the connection check job was completed."
    example-value: |
      2019-01-15T15:15:22Z

  - name: "error"
    type: "boolean"
    description: |
      Indicates if the connection check job resulted in an error. This will be `true` if any of the `exit_status` properties are non-zero.
    example-value: |
      false

  - name: "check_exit_status"
    type: "integer"
    description: |
      The exit status of the connection check job. Possible values are:

      - `null` - The connection check job is still running
      - `0` - The connection check job was successful
      - `1` - The connection check job was unsuccessful
    example-value: |
      0

  - name: "discovery_exit_status"
    type: "integer"
    description: |
      The exit status of the discovery portion of the connection check job. Possible values are:

      - `null` - Job is still running
      - `0` - Job was successful
      - Any non-zero value - Discovery failed
    example-value: |
      0

  - name: "discovery_error_message"
    type: "string"
    description: |
      Exception message raised when discovery failed during the connection check job. If successful, this will be `null`.
    example-value: |
      null

  - name: "tap_exit_status"
    type: "integer"
    description: |
      The exit status of the tap. Possible values are:

      - `null` - Tap is still running
      - `0` - Tap was successful
      - Any non-zero value - Tap failed

    example-value: |
      0

  - name: "tap_error_message"
    type: "string"
    description: |
      Exception message raised when extraction failed during the job. If successful, this will be `null`.
    example-value: |
      null

  - name: "target_exit_status"
    type: "integer"
    description: |
      The exit status of the target portion of the connection check job. Possible values are:

      - `null` - Target is still running
      - `0` - Target was successful
      - Any non-zero value - Target failed
    example-value: |
      0

  - name: "target_error_message"
    type: "string"
    description: "This value will always be `null`."
    example-value: |
      null
---