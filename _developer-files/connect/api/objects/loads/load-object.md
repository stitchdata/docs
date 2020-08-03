---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-object"
endpoint: "loads"
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
  - name: "stitch_client_id"
    type: "integer"
    description: "The Stitch client ID associated with the load."
    example-value: "116078"

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

  - name: "last_batch_loaded_at"
    type: "date-time"
    description: |
      The date and time the last batch was loaded for the stream (`stream_name`).

      **Note**: If the load for the stream is currently in an error state, this will be `null`.
    example-value: "2019-01-15T15:15:19Z"

  - name: "error_state"
    type: "object"
    description: |
      If the error was unsuccessful, this object will contain data about the reason for the failure.

      **Note**: This object and its attributes are subject to change. We don't recommend relying on its data, as the structure may be altered in the future.
    # subattributes:
    #   - name: "notification_data"
    #     type: "object"
    #     description: "Details about the notification triggered as a result of the failure."
    #     subattributes:
    #       - name: "message"
    #         type: "string"
    #         description: &error-message "A general summary of the reason for the failure."
    #         example-value: "There was an internal error. We are investigating."

    #       - name: "exception_message"
    #         type: "string"
    #         description: *error-message
    #         example-value: &raw-error-example "Billing has not been enabled for this project. Enable billing at https://console.cloud.google.com/billing. DML queries are not allowed in the free tier. Set up a billing account to remove this restriction."

    #       - name: "warehouse_error_code"
    #         type: "integer"
    #         description: "TODO"
    #         example-value: "null"

    #       - name: "error"
    #         type: "string"
    #         description: "This will be `LOADER_INTERNAL_ERROR`."
    #         example-value: "LOADER_INTERNAL_ERROR"

    #       - name: "new_column"
    #         type: "TODO"
    #         description: ""
    #         example-value: "null"

    #       - name: "status"
    #         type: "string"
    #         description: "This will be `ERROR`."
    #         example-value: "ERROR"

    #       - name: "warehouse_sql_state"
    #         type: "string"
    #         description: "TODO"
    #         example-value: "null"

    #       - name: "action"
    #         type: "string"
    #         description: |
    #           The action that resulted in failure. For example: If this value is `get-connection`, Stitch encountered issues connecting successfully to the destination.
    #         example-value: "null"

    #       - name: "warehouse_message"
    #         type: "string"
    #         description: &warehouse-message |
    #           The raw error message returned by the destination. Error messages vary by cause and destination.

    #           For help troubleshooting loading errors, refer to the [Destination Loading Error Reference]({{ link.troubleshooting.dw-loading-errors | prepend: site.baseurl }}).
    #         example-value: *raw-error-example

    #       - name: "column"
    #         type: "TODO"
    #         description: ""
    #         example-value: "null"

    #   - name: "exception_chain"
    #     type: "array"
    #     description: "An array of exception objects. Exception objects contain data about the code classes that returned the exception, resulting in loading failure."
    #     subattributes:
    #       - name: "class"
    #         type: "string"
    #         description: "The class of the exception."
    #         example-value: "com.google.cloud.bigquery.BigQueryException"

    #       - name: "message"
    #         type: "string"
    #         description: *warehouse-message
    #         example-value: *raw-error-example

    #       - name: "chain_sequence_num"
    #         type: "integer"
    #         description: "The index of the exception object in the array."
    #         example-value: "0"

    #       - name: "action"
    #         type: "string"
    #         description: ""
    #         example-value: "null"


# -------------------------- #
#           EXAMPLES         #
# -------------------------- #

examples:
  - type: "Successful load"
    code: |
      {
        "stitch_client_id": 116078,
        "source_name": "heroku",
        "stream_name": "customers",
        "last_batch_loaded_at": "2020-06-23T01:35:47Z",
        "error_state": null
      }

  - type: "Unsuccessful load"
    code: |
      {
        "stitch_client_id": 116078,
        "source_name": "recurly",
        "stream_name": "accounts",
        "last_batch_loaded_at": null,
        "error_state": {
          "notification_data": {
            "message": "establish a connection to your data warehouse",
            "exception_message": "establish a connection to your data warehouse",
            "warehouse_error_code": 500151,
            "error": "LOADER_WAREHOUSE_ERROR",
            "new_column": null,
            "status": "ERROR",
            "warehouse_sql_state": "HY000",
            "action": "get-connection",
            "warehouse_message": "[Simba][SparkJDBCDriver](500151) Error setting/closing session: Open Session Error.",
            "column": null
          },
          "exception_chain": [
            {
              "class": "clojure.lang.ExceptionInfo",
              "message": "establish a connection to your data warehouse",
              "chain_sequence_num": 0,
              "action": "get-connection"
            }
          ]
        }
      }
---