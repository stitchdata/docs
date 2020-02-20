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

  - name: "created_at"
    type: "timestamp"
    description: "The time at which the source object was created."

  - name: "deleted_at"
    type: "timestamp"
    description: "The time at which the source object was deleted."

  - name: "display_name"
    type: "string"
    description: "The display name of the source connection."

  - name: "name"
    type: "string"
    description: "{{ connect.common.attributes.name }}"

  - name: "paused_at"
    type: "timestamp"
    description: "If the connection was paused by the user, the time the pause began. Otherwise, or if the connection is active, this will be `null."

  - name: "properties"
    type: "object"
    sub-type: " source form properties"
    url: "{{ api.form-properties.source-forms.section }}"
    description: |
      Parameters for connecting to the source, excluding any sensitive credentials. The parameters must adhere to the `type` of source.

      **Note**: When included in responses, this object will contain the current values for the source's form properties. If an optional property (`is_required: false`) has not been provided, it will not be present in this object.

  - name: "report_card"
    type: "object"
    sub-type: "source report card"
    url: "{{ api.data-structures.report-cards.source.section }}"
    description: "A description of the source's configuration state."

  - name: "stitch_client_id"
    type: "integer"
    description: "The ID of the Stitch client account."

  - name: "system_paused_at"
    type: "timestamp"
    description: "If the connection was paused by the system, the time the pause began. Otherwise, or if the connection is active, this will be null."

  - name: "type"
    type: "string"
    description: "The source type."

  - name: "updated_at"
    type: "timestamp"
    description: "The time at which the object was last updated."
---