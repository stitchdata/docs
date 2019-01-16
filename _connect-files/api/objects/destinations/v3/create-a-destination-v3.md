---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

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
    subexamples:
      - title: "Create an Amazon S3 destination"
        code: |
          {% capture request-header %}
          curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip_newlines }}
               -H "Authorization: Bearer <ACCESS_TOKEN>" 
               -H "Content-Type: application/json"
               -d "{
          {% endcapture %}

          {{ request-header | flatify | lstrip | rstrip }}
                    "type":"s3",
                    "connection": {
                      "s3_bucket":"com-stitch-test-bucket",
                      "output_file_format":"csv",
                      "s3_key_format_string":"[integration_name]/[table_name]/[table_version]_[timestamp_loaded].csv",
                      "csv_delimiter":",",
                      "csv_force_quote":true
                      }
                   }"

      - title: "Create an Amazon Redshift destination"
        code: |
          {{ request-header | flatify | lstrip | rstrip }}
                    "type":"redshift",
                    "connection": {
                      "host":"<HOST>",
                      "port":5439,
                      "username":"<USERNAME>",
                      "database":"<DATABASE>",
                      "password":"<PASSWORD>",
                      "ssl":false
                      }
                   }"

      - title: "Create a PostgreSQL destination"
        code: |
          {{ request-header | flatify | lstrip | rstrip }}
                    "type":"postgres",
                    "connection": {
                      "host":"<HOST>",
                      "port":5432,
                      "username":"<USERNAME>",
                      "database":"<DATABASE>",
                      "password":"<PASSWORD>",
                      "ssl":false
                      }
                   }"

      - title: "Create a Snowflake destination"
        code: |
          {{ request-header | flatify | lstrip | rstrip }}
                    "type":"snowflake",
                    "connection": {
                      "host":"<HOST>",
                      "port":443,
                      "user":"<USERNAME>",
                      "warehouse":"<WAREHOUSE>",
                      "database":"<DATABASE>",
                      "password":"<PASSWORD>",
                      "role":"<OPTIONAL_ROLE>",
                      "ssl":false
                      }
                   }"

  - type: "Response"
    language: "json"
    subexamples:
      - title: "Amazon S3 destination response"
        description: |
          **Note**: There are additional steps to creating an Amazon S3 destination beyond submitting a successful request to this endpoint. Refer to the [Amazon S3 Destination Form Property documentation]({{ api.form-properties.destination-forms.section | append: "-amazon-s3-object" }}) for more info.
        code: |
          {% capture response-header %}
          HTTP/1.1 200 OK
          Content-Type: application/json;charset=ISO-8859-1

          {
            "id":"<DESTINATION_ID>",
            "type":"[DESTINATION-TYPE]",
            "created_at":"2018-02-06T15:36:36Z",
            "updated_at":"2018-02-06T15:36:36Z",
            "connection": {
          {% endcapture %}

          {% capture last-check-object %}
            "last_check":{
                "error":false,
                "started_at":"2018-02-06T16:15:19Z",
                "completed_at":"2018-02-06T16:16:21Z"
            }
          }
          {% endcapture %}

          {{ response-header | flatify | replace: "[DESTINATION-TYPE]","s3" | lstrip | rstrip }}
                "s3_bucket":"com-stitch-test-bucket",
                "output_file_format":"csv",
                "s3_key_format_string":"[integration_name]/[table_name]/[table_version]_[timestamp_loaded].csv",
                "csv_delimiter":",",
                "csv_force_quote":true,
                "sentinel_key":"stitch-challenge-file-af295ad1-7a4b-4881-89dc-c9be27de13a5"
            },
          {{ last-check-object | rstrip }}

      - title: "Amazon Redshift destination response"    
        code: |
          {{ response-header | flatify | replace: "[DESTINATION-TYPE]","redshift" | lstrip | rstrip }}
                "host":"<HOST>",
                "port":5439,
                "username":"<USERNAME>",
                "database":"<DATABASE>",
                "password":"<PASSWORD>",
                "ssl":false
            },
          {{ last-check-object | rstrip }}

      - title: "PostgreSQL destination response"    
        code: |
          {{ response-header | flatify | replace: "[DESTINATION-TYPE]","postgres" | lstrip | rstrip }}
                "host":"<HOST>",
                "port":5432,
                "username":"<USERNAME>",
                "database":"<DATABASE>",
                "password":"<PASSWORD>",
                "ssl":false
            },
          {{ last-check-object | rstrip }}

      - title: "Snowflake destination response"    
        code: |
          {{ response-header | flatify | replace: "[DESTINATION-TYPE]","snowflake" | lstrip | rstrip }}
                "host":"<HOST>",
                "port":443,
                "user":"<USERNAME>",
                "warehouse":"<WAREHOUSE>",
                "database":"<DATABASE>",
                "password":"<PASSWORD>",
                "role":"<OPTIONAL_ROLE>",
                "ssl":false
            },
          {{ last-check-object | rstrip }}

  - type: "Errors"
---