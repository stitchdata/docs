---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-object"
endpoint: "sources"
order: 6


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Source"
endpoint-url: "/sources"

description: "{{ api.core-objects.sources.description }}"
intro-short: "Create, update, pause, unpause, and delete data sources" # Used in the API functionality section of the docs

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
  - id: "create-a-source"
    title: "Create a source"
    method: "post"
    short: "{{ site.data.connect.core-objects.sources.create.short | flatify }}"

  - id: "update-a-source"
    title: "Update a source"
    method: "put"
    short: "{{ site.data.connect.core-objects.sources.update.description | flatify }}"

  - id: "pause-a-source"
    title: "Pause a source"
    method: "put"
    short: "{{ api.core-objects.sources.pause.description | flatify }}"

  - id: "unpause-a-source"
    title: "Unpause a source"
    method: "put"
    short: "{{ api.core-objects.sources.unpause.description | flatify }}"

  - id: "retrieve-a-source"
    title: "Retrieve a source"
    method: "get"
    short: "{{ site.data.connect.core-objects.sources.retrieve.description | flatify }}"

  - id: "list-sources"
    title: "List all sources"
    method: "get"
    short: "{{ site.data.connect.core-objects.sources.list.description | flatify }}"

  - id: "delete-a-source"
    title: "Delete a source"
    method: "delete"
    short: "{{ site.data.connect.core-objects.sources.delete.description | flatify }}"

  - id: "generate-iapi-access-token"
    title: "Generate an Import API source access token"
    method: "post"
    short: "{{ site.data.connect.core-objects.sources.create-iapi-token.short | flatify }}"

  - id: "get-iapi-access-token-ids"
    title: "Get Import API access token IDs"
    method: "get"
    short: "{{ site.data.connect.core-objects.sources.create-iapi-token.short | flatify }}"

  - id: "revoke-iapi-access-token"
    title: "Revoke an Import API source access token"
    method: "delete"
    short: "{{ site.data.connect.core-objects.sources.get-iapi-access-token-ids.short | flatify }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "id"
    type: "integer"
    description: "The unique identifier for this source."

  - name: "properties"
    type: "object"
    sub-type: " source form properties"
    url: "{{ api.form-properties.source-forms.section }}"
    description: |
      Parameters for connecting to the source, excluding any sensitive credentials. The parameters must adhere to the `type` of source.

      **Note**: When included in responses, this object will contain the current values for the source's form properties. If an optional property (`is_required: false`) has not been provided, it will not be present in this object.

  - name: "updated_at"
    type: "timestamp"
    description: "The time at which the object was last updated."

  - name: "schedule"
    type: "object"
    sub-type: "schedule"
    url: "{{ site.data.connect.data-structures.schedule.section }}"
    description: |
      An object describing the replication schedule for the source.

      **Note**: This will be `null` if the source is paused or has been deleted.

  - name: "check_job_name"
    type: "string"
    description: "The name of the last connection check job that ran for the source."

  - name: "name"
    type: "string"
    description: "{{ connect.common.attributes.name }}"

  - name: "type"
    type: "string"
    description: "The source type."

  - name: "deleted_at"
    type: "timestamp"
    description: "The time at which the source object was deleted."

  - name: "system_paused_at"
    type: "timestamp"
    description: "If the connection was paused by the system, the time the pause began. Otherwise, or if the connection is active, this will be `null`."

  - name: "stitch_client_id"
    type: "integer"
    description: "The ID of the Stitch client account associated with the source."

  - name: "paused_at"
    type: "timestamp"
    description: "If the connection was paused by the user, the time the pause began. Otherwise, or if the connection is active, this will be `null."

  - name: "display_name"
    type: "string"
    description: "The display name of the source connection."

  - name: "created_at"
    type: "timestamp"
    description: "The time at which the source object was created."

  - name: "report_card"
    type: "object"
    sub-type: "source report card"
    url: "{{ api.data-structures.report-cards.source.section }}"
    description: "A description of the source's configuration state."


# -------------------------- #
#           EXAMPLES         #
# -------------------------- #

examples:
  - code: |
      {
        "properties": {
          "anchor_time": "2018-11-06T22:00:00.000Z",
          "cron_expression": null,
          "frequency_in_minutes": "60",
          "image_version": "1.latest",
          "product": "pipeline",
          "repository": "docs",
          "start_date": "2017-11-06T21:20:32Z"
        },
        "updated_at": "2020-06-22T18:07:32Z",
        "schedule": {
          "type": "interval",
          "unit": "minute",
          "interval": 60.0,
          "next_fire_time": "2020-06-22T19:00:00Z"
        },
        "check_job_name": "116078.108726.check.3e20af99-b4b3-11ea-a947-0e6d53ce325f",
        "name": "github",
        "type": "platform.github",
        "deleted_at": null,
        "system_paused_at": null,
        "stitch_client_id": 116078,
        "paused_at": null,
        "id": 108726,
        "display_name": "GitHub",
        "created_at": "2018-11-06T21:22:45Z",
        "report_card": {
          "type": "platform.github",
          "current_step": 4,
          "current_step_type": "fully_configured",
          "steps": [
            {
              "type": "form",
              "properties": [
                {
                  "name": "access_token",
                  "is_required": true,
                  "is_credential": true,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": true,
                  "tap_mutable": false
                },
                {
                  "name": "anchor_time",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "format": "date-time"
                  },
                  "provided": true,
                  "tap_mutable": false
                },
                {
                  "name": "cron_expression",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": null,
                  "provided": false,
                  "tap_mutable": false
                },
                {
                  "name": "frequency_in_minutes",
                  "is_required": false,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^1$|^30$|^60$|^360$|^720$|^1440$"
                  },
                  "provided": true,
                  "tap_mutable": false
                },
                {
                  "name": "image_version",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": true,
                  "property_type": "read_only",
                  "json_schema": null,
                  "provided": true,
                  "tap_mutable": false
                },
                {
                  "name": "repository",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string"
                  },
                  "provided": true,
                  "tap_mutable": false
                },
                {
                  "name": "start_date",
                  "is_required": true,
                  "is_credential": false,
                  "system_provided": false,
                  "property_type": "user_provided",
                  "json_schema": {
                    "type": "string",
                    "pattern": "^\\d{4}-\\d{2}-\\d{2}T00:00:00Z$"
                  },
                  "provided": true,
                  "tap_mutable": false
                }
              ]
            },
            {
              "type": "discover_schema",
              "properties": []
            },
            {
              "type": "field_selection",
              "properties": []
            },
            {
              "type": "fully_configured",
              "properties": []
            }
          ]
        }
      }
---