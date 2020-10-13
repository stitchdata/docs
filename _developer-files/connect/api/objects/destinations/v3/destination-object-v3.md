---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-version-object"
endpoint: "destinations"

# -------------------------- #
#        VERSION INFO        #
# -------------------------- #

version: "3"

# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "connection"
    type: "object"
    sub-type: "destination form properties"
    url: "{{ api.form-properties.destination-forms.section }}"
    description: |
      Parameters for connecting to the destination, excluding any sensitive credentials.

      The parameters must adhere to the type of destination.

      **Note**: This has been renamed to `properties` in v4 of the Destinations endpoint.

  - name: "last_check"
    type: "timestamp"
    # sub-type: "connection check"
    # url: "{{ api.data-structures.connection-checks.section }}"
    description: |
      The time the last connection check to the destination completed.

      **Note**: This field has been deprecated in v4 of the Destinations endpoint.

# -------------------------- #
#           EXAMPLES         #
# -------------------------- #

examples:
  - code: |
      {
        "id":"<DESTINATION_ID>",
        "type":"s3",
        "created_at":"2018-02-06T15:36:36Z",
        "updated_at":"2018-02-06T15:36:36Z",
        "connection": {
            "s3_bucket":"com-stitch-test-bucket",
            "output_file_format":"csv",
            "s3_key_format_string":"[integration_name]/[table_name]/[table_version]_[timestamp_loaded].csv",
            "csv_delimiter":",",
            "csv_force_quote":true,
            "sentinel_key":"stitch-challenge-file-af295ad1-7a4b-4881-89dc-c9be27de13a5"
        },
        "last_check":{
            "error":false,
            "started_at":"2018-02-06T16:15:19Z",
            "completed_at":"2018-02-06T16:16:21Z"
        }
      }
---