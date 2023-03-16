---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "loads"
key: "list-last-loads-for-account"
version: "4"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "{{ site.data.connect.core-objects.loads.list.title | flatify }}"
method: "get"
short-url: |
  /v4/{stitch_client_id}/loads
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}

short: "{{ site.data.connect.core-objects.loads.list.short | flatify }}"
description: |
  {{ site.data.connect.core-objects.loads.list.description | flatify }}


# ---------------------------- #
#  RATE LIMITING & PAGINATION  #
# ---------------------------- #

# The resource type, applicable to rate limits.
# Info about this resource/rate limit type lives in: _data/connect/rate-limits
rate-limit-type: "jobs"

# The number of records returned for each page of results
pagination: "100"

# How results are ordered in the response
order-by: "stream_name"
sort-type: "Ascending (A-Z)"


# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

## This depends on the method being used, and the type of endpoint.

arguments:
  - name: "stitch_client_id"
    required: true
    type: "path parameter"
    description: |
      A path parameter corresponding to the unique ID of a Stitch account.

      **Note**: The client ID must be associated with the provided access token.
    example-value: |
      116078

  - name: "page"
    required: false
    type: "path parameter"
    description: |
      A path parameter corresponding to the page of results to retrieve, adhering to the format `?page={page_number}`, where `{page_number}` is the number of the page to retrieve.

      Each results set, or page, can contain up to 100 load attempt records. This parameter is only required if you want to retrieve additional pages beyond the first 100 load attempt records. By default, a request to `{{ endpoint.short-url | flatify }}` is equivalent to a request for page `1` using this parameter.

      If an account contains more than 100 load attempt records, the response will include data about subsequent pages that can be used to retrieve them. Refer to the **Requests** tab for an example.

      Refer to the [Pagination section]({{ site.data.connect.api.pagination }}) for more info on paginating through lists.
    example-value: |
      2


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and the following properties:

response-attributes:
  - name: "data"
    type: "array"
    description: |
      An array of [Load objects]({{ site.data.connect.core-objects.loads.object }}), one for each stream that has had an attempted load in the past 60 days.

      **Note**: Load objects are returned in ascending order by `stream_id`.

  - name: "page"
    type: "integer"
    description: |
      The number of the current page of results. Each page of results can contain up to 100 load attempt records.
    example-value: |
      1

  - name: "total"
    type: "integer"
    description: |
      The total number of load attempt records in the result set.
    example-value: |
      5

  - name: "links"
    type: "object"
    description: |
      An object containing links to the next and previous pages of results.

      **Note**: This object will be empty if the result set contains less than 101 load attempt records, or `total < 101`.
    subattributes:
      - name: "next"
        type: "string"
        description: |
          A URL leading to the next paginated set of load attempt results. Use a subsequent `GET` request to this URL to retrieve the results for this page.

          Refer to the **Requests** tab for an example.
        example-value: |
          /v4/116078/loads?page=3

      - name: "previous"
        type: "string"
        description: |
          A URL leading to the previous paginated set of load attempt results. Use a subsequent `GET` request to this URL to retrieve the results for this page.

          Refer to the **Requests** tab for an example.
        example-value: |
          /v4/116078/loads?page=1


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    subexamples:
    - title: "Retrieving the first page of results"
      request-url: "{{ endpoint.short-url | flatify | strip_newlines }}"
      header: "{{ site.data.connect.request-headers.get.without-body | flatify }}"

    - title: "Retrieving the second page of results"
      request-url: "{{ endpoint.short-url | flatify | strip_newlines }}?page=2"
      header: "{{ site.data.connect.request-headers.get.without-body | flatify }}"

  - type: "Response"
    language: "json"
    subexamples:
      - title: "Result set with less than 100 load attempt records"
        code: |
          {
             "data":[
                {
                   "stitch_client_id":116078,
                   "source_name":"recurly",
                   "stream_name":"accounts",
                   "last_batch_loaded_at":null,
                   "error_state":{
                      "notification_data":{
                         "message":"establish a connection to your data warehouse",
                         "exception_message":"establish a connection to your data warehouse",
                         "warehouse_error_code":500151,
                         "error":"LOADER_WAREHOUSE_ERROR",
                         "new_column":null,
                         "status":"ERROR",
                         "warehouse_sql_state":"HY000",
                         "action":"get-connection",
                         "warehouse_message":"[Simba][SparkJDBCDriver](500151) Error setting/closing session: Open Session Error.",
                         "column":null
                      },
                      "exception_chain":[
                         {
                            "class":"clojure.lang.ExceptionInfo",
                            "message":"establish a connection to your data warehouse",
                            "chain_sequence_num":0,
                            "action":"get-connection"
                         }
                      ]
                   }
                },
                {
                   "stitch_client_id":116078,
                   "source_name":"heroku_1",
                   "stream_name":"customers",
                   "last_batch_loaded_at":"2020-06-23T15:14:59Z",
                   "error_state":null
                }
             ],
             "page":1,
             "total"2,
             "links":{}
          }

      - title: "Result set with more than 100 load attempt records"
        code: |
          {
             "data":[
                {
                   "stitch_client_id":116078,
                   "source_name":"recurly",
                   "stream_name":"accounts",
                   "last_batch_loaded_at":null,
                   "error_state":{
                      "notification_data":{
                         "message":"establish a connection to your data warehouse",
                         "exception_message":"establish a connection to your data warehouse",
                         "warehouse_error_code":500151,
                         "error":"LOADER_WAREHOUSE_ERROR",
                         "new_column":null,
                         "status":"ERROR",
                         "warehouse_sql_state":"HY000",
                         "action":"get-connection",
                         "warehouse_message":"[Simba][SparkJDBCDriver](500151) Error setting/closing session: Open Session Error.",
                         "column":null
                      },
                      "exception_chain":[
                         {
                            "class":"clojure.lang.ExceptionInfo",
                            "message":"establish a connection to your data warehouse",
                            "chain_sequence_num":0,
                            "action":"get-connection"
                         }
                      ]
                   }
                },
                {
                   "stitch_client_id":116078,
                   "source_name":"heroku_1",
                   "stream_name":"customers",
                   "last_batch_loaded_at":"2020-06-23T15:14:59Z",
                   "error_state":null
                },
                [...]
             ],
              "page": 1,
              "total": 102,
              "links": {
                "next": "/v4/116078/loads?page=2"
              }
            }

  - type: "Errors"
    # Included only if there are errors for the endpoint
    # The errors live in: _data/connect/response-codes/loads.yml
---