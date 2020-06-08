---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-object"
endpoint: "extraction"
order: 10


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Extraction"
endpoint-url: "/{client_id}/extractions"

description: |
  {{ site.data.connect.core-objects.extractions.description | flatify }}
  
intro-short: "Retrieve status info about recent extraction jobs" # Used in the API functionality section of the docs


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
  - id: "list-last-extractions"
    title: "{{ site.data.connect.core-objects.extractions.list.title | flatify }}"
    method: "get"
    short: "{{ site.data.connect.core-objects.extractions.list.short | flatify }}"

  - id: "get-logs-for-an-extraction-job"
    title: "{{ site.data.connect.core-objects.extractions.get-job-logs.title | flatify }}"
    method: "get"
    short: "{{ site.data.connect.core-objects.extractions.get-job-logs.short | flatify }}"



# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "job_name"
    type: "string"
    description: "The name of the extraction job."
    example-value: |
      3.1.sync.d7f18b02-a17c-44b7-bbd5-dc30e1dc6ce5

  - name: "client_id"
    type: "integer"
    description: "The Stitch client ID associated with the extraction job."
    example-value: |
      116078

  - name: "source_id"
    type: "integer"
    description: "The unique identifier of the source associated with the extraction job."
    example-value: |
      120645

  - name: "tap_name"
    type: "string"
    description: "TODO"
    example-value: |
      TODO

  - name: "start_time"
    type: "timestamp"
    description: |
      {{ site.data.connect.general.start-time | replace: "[JOB-TYPE]","extraction" }}
    example-value: |
      2019-01-15T15:15:19Z

  - name: "completion_time"
    type: "timestamp"
    description: |
      {{ site.data.connect.general.completion-time | replace: "[JOB-TYPE]","extraction" }}
    example-value: |
      2019-01-15T15:15:22Z

  - name: "discovery_exit_status"
    type: "integer"
    description: |
      {{ site.data.connect.general.discovery-exit-status | replace: "[JOB-TYPE]","extraction" }}
    example-value: |
      0

  - name: "discovery_description"
    type: "string"
    description: |
      {{ site.data.connect.general.discovery-error-message | replace: "[JOB-TYPE]","extraction" }}
    example-value: |
      null

  - name: "tap_exit_status"
    type: "integer" 
    description: |
      {{ site.data.connect.general.tap-exit-status }}
    example-value: |
      0

  - name: "tap_description"
    type: "string"
    description: |
      {{ site.data.connect.general.tap-error-message }}
    example-value: |
      null

  - name: "target_exit_status"
    type: "integer"
    description: |
      {{ site.data.connect.general.target-exit-status | replace: "[JOB-TYPE]","extraction" }}
    example-value: |
      0

  - name: "target_description"
    type: "string"
    description: |
      todo: Exception message raised when the target fails. If successful, this will be `null`.
    example-value: |
      <todo>
---