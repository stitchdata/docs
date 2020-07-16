---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-object"
endpoint: "extractions"
order: 10


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Extraction"
endpoint-url: "/{client_id}/extractions"

description: |
  {{ site.data.connect.core-objects.extractions.description | flatify }}

  An extraction job contains three phases, which occur in this order:

  1. **Discovery**: This is also referred to as a structure sync. During this phase, Stitch detects the tables and columns available in the source, along with any changes to the structure of those tables and columns.
  2. **Tap**: During this phase, Stitch replicates data from the source.
  3. **Target**: During this phase, Stitch sends the replicated data to the Stitch target, or Import API.

  Each phase must be successful to proceed to the next phase. If a phase is unsuccessful, the entire extraction job will fail. For example: If discovery is unsuccessful, the entire extraction job will fail.
  
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
    description: |
      The name of the extraction job.
    example-value: |
      116078.233312.sync.2ca63ab0-8a4e-11ea-840a-12021e29a739

  - name: "stitch_client_id"
    type: "integer"
    description: "The Stitch client account ID associated with the extraction job."
    example-value: |
      116078

  - name: "source_id"
    type: "integer"
    description: "The unique identifier of the source associated with the extraction job."
    example-value: |
      228068

  - name: "tap_name"
    type: "string"
    description: |
      The name of the tap powering the source. This will typically be in the format of `tap-<type>`, where `type` is the name of the tap, or source. For example: A Facebook Ads source will have a `tap_name` value of `tap-facebook`.
    example-value: |
      tap-facebook

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
      Exception message raised when the target fails. If successful, this will be `null`.
    example-value: |
      null


# -------------------------- #
#           EXAMPLES         #
# -------------------------- #

examples:
  - type: "Successful extraction"
    code: |
      {
        "target_exit_status": 0,
        "job_name": "116078.233312.sync.e4d8eae5-b23e-11ea-94a1-02cbbd504f7d",
        "start_time": "2020-06-19T15:09:38Z",
        "stitch_client_id": 116078,
        "tap_exit_status": 0,
        "source_type": "tap-recurly",
        "target_description": null,
        "discovery_exit_status": 0,
        "discovery_description": null,
        "tap_description": null,
        "completion_time": "2020-06-19T15:09:43Z",
        "source_id": 233312
      }

  - type: "Unsuccessful extraction"
    code: |
      {
        "target_exit_status": 0,
        "job_name": "116078.244788.sync.2deb271f-b23b-11ea-894c-0ee2efcbf789",
        "start_time": "2020-06-19T14:43:03Z",
        "stitch_client_id": 116078,
        "tap_exit_status": 1,
        "source_type": "tap-recurly",
        "target_description": null,
        "discovery_exit_status": 0,
        "discovery_description": null,
        "tap_description": "Response returned http error code 401\n401 Client Error: Unauthorized for url: https://partner-api.recurly.com/sites/subdomain-stitchdata/accounts?limit=200&sort=updated_at&begin_time=2019-04-29T00%3A00%3A00Z&order=asc",
        "completion_time": "2020-06-19T14:43:08Z",
        "source_id": 244788
      }
---