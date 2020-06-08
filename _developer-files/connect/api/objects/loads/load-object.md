---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-object"
endpoint: "load"
order: 11


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Load"
endpoint-url: "/{client_id}/loads"

description: |
  {{ site.data.connect.core-objects.loads.description | flatify }}
  
intro-short: "Retrieve status info about recent data loading attempts" # Used in the API functionality section of the docs


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
  - id: "list-last-loads-for-account"
    title: "{{ site.data.connect.core-objects.loads.list.title | flatify }}"
    method: "get"
    short: "{{ site.data.connect.core-objects.loads.list.short | flatify }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "source_name"
    type: "string"
    description: |
      The unique name of the source. This will correspond to the name of the destination schema or dataset where Stitch loads data for this source.
    example-value: "stitch_shopify"

  - name: "stream_name"
    type: "string"
    description: |
      The name of the stream (table) associated with the load.
    example-value: "orders"

  - name: "stitch_client_id"
    type: "integer"
    description: "The Stitch client ID associated with the load."
    example-value: "116078"

  - name: "error_state"
    type: "string"
    description: ""
    example-value: ""

  - name: "last_batch_loaded_at"
    type: "date-time"
    description: "The date and time the last batch was loaded for the `stream_name`."
    example-value: "2019-01-15T15:15:19Z"
---