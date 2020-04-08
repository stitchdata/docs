---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "destinations"
key: "create-a-destination"
version: "3"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Create a destination"
method: "post"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.destinations.create.short }}"
description: "{{ api.core-objects.destinations.create.description | flatify }}"


# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

arguments:
  - name: "type"
    required: true
    type: "string"
    description: "{{ connect.common.attributes.destination-type | flatify }}"

  - name: "connection"
    required: true
    type: "object"
    description: "A [Destination Form Properties object]({{ api.form-properties.destination-forms.section }}) corresponding to the value of `type`."


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of `200 OK` and a [Destination object]({{ api.core-objects.destinations.object }}).


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    language: "json"
    code: |
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip_newlines }} \
           -H "Authorization: Bearer <ACCESS_TOKEN>" \
           -H "Content-Type: application/json" \
           -d "{
                "type":"s3",
                "connection": {
                  "s3_bucket":"com-stitch-test-bucket",
                  "output_file_format":"csv",
                  "s3_key_format_string":"[integration_name]/[table_name]/[table_version]_[timestamp_loaded].csv",
                  "csv_delimiter":",",
                  "csv_force_quote":true
                  }
               }"

  - type: "Response"
    language: "json"
    code: |
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

  - type: "Errors"
---