---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "extractions"
key: "list-last-extractions"
version: "4"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "{{ site.data.connect.core-objects.extractions.list.title | flatify }}"
method: "get"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ site.data.connect.core-objects.extractions.list.short | flatify }}"
description: |
  {% include note.html type="single-line" content="**This endpoint is in beta.**" %}
  
  {{ site.data.connect.core-objects.extractions.list.description | flatify }}

  Responses from this endpoint are paginated. Every page, or result set, can contain up to 100 extraction records. Refer to the [Arguments section](#{{ endpoint.key }}--arguments) for more info.


# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

arguments:
  - name: "client_id"
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

      Each results set, or page, can contain up to 100 extraction records. This parameter is only required if you want to retrieve additional pages beyond the first 100 extraction records. By default, a request to `{{ endpoint.short-url | flatify }}` is equivalent to a request for page `1` using this parameter.

      If an account contains more than 100 extraction records, the response will include data about subsequent pages that can be used to retrieve them.

      Refer to the **Requests** tab for an example.
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
      An array of [Extraction objects]({{ site.data.connect.core-objects.extractions.object }}), one for each source that has had a completed extraction job in the past 60 days.

      **Note**: Extraction objects are returned in descending order by `source_id`.

  - name: "page"
    type: "integer"
    description: |
      The number of the current page of results. Each page of results can contain up to 100 extraction job records.
    example-value: |
      1

  - name: "total"
    type: "integer"
    description: |
      The total number of extraction job records in the result set.
    example-value: |
      5

  - name: "links"
    type: "object"
    description: |
      An object containing links to the next and previous pages of results.

      **Note**: This object will be empty if the result set contains less than 101 extraction job records, or `total < 101`.
    subattributes:
      - name: "next"
        type: "string"
        description: |
          A URL leading to the next paginated set of extraction job results. Use a subsequent `GET` request to this URL to retrieve the results for this page.

          Refer to the **Requests** tab for an example.
        example-value: |
          /v4/116078/extractions?page=3

      - name: "previous"
        type: "string"
        description: |
          A URL leading to the previous paginated set of extraction job results. Use a subsequent `GET` request to this URL to retrieve the results for this page.

          Refer to the **Requests** tab for an example.
        example-value: |
          /v4/116078/extractions?page=1


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
      - title: "Result set with less than 100 extraction records"
        code: |
          {
            "data": [
              {
                "target_exit_status": null,
                "job_name": "116078.123241.sync.43b3c535-b208-11ea-94a1-02cbbd504f7d",
                "start_time": "2020-06-19T08:38:35Z",
                "stitch_client_id": 116078,
                "tap_exit_status": null,
                "source_type": "tap-toggl",
                "target_description": "Terminated",
                "discovery_exit_status": null,
                "discovery_description": "Terminated",
                "tap_description": "Terminated",
                "completion_time": "2020-06-19T14:38:35Z",
                "source_id": 123241
              },
              {
                "target_exit_status": null,
                "job_name": "116078.123246.sync.9c6672c4-8a4c-11ea-840a-12021e29a739",
                "start_time": "2020-04-29T19:07:03Z",
                "stitch_client_id": 116078,
                "tap_exit_status": null,
                "source_type": "tap-toggl",
                "target_description": "Terminated",
                "discovery_exit_status": null,
                "discovery_description": "Terminated",
                "tap_description": "Terminated",
                "completion_time": "2020-04-30T01:07:03Z",
                "source_id": 123246
              }
            ],
            "page": 1,
            "total": 2,
            "links": {}
          }

      - title: "Result set with more than 100 extraction records"
        code: |
          {
            "data": [
              {
                "target_exit_status": null,
                "job_name": "116078.123241.sync.43b3c535-b208-11ea-94a1-02cbbd504f7d",
                "start_time": "2020-06-19T08:38:35Z",
                "stitch_client_id": 116078,
                "tap_exit_status": null,
                "source_type": "tap-toggl",
                "target_description": "Terminated",
                "discovery_exit_status": null,
                "discovery_description": "Terminated",
                "tap_description": "Terminated",
                "completion_time": "2020-06-19T14:38:35Z",
                "source_id": 123241
              },
              {
                "target_exit_status": null,
                "job_name": "116078.123246.sync.9c6672c4-8a4c-11ea-840a-12021e29a739",
                "start_time": "2020-04-29T19:07:03Z",
                "stitch_client_id": 116078,
                "tap_exit_status": null,
                "source_type": "tap-toggl",
                "target_description": "Terminated",
                "discovery_exit_status": null,
                "discovery_description": "Terminated",
                "tap_description": "Terminated",
                "completion_time": "2020-04-30T01:07:03Z",
                "source_id": 123246
              },
              {
                "target_exit_status": 0,
                "job_name": "116078.228068.sync.2ca63ab0-8a4e-11ea-840a-12021e29a739",
                "start_time": "2020-04-29T19:18:14Z",
                "stitch_client_id": 116078,
                "tap_exit_status": 1,
                "source_type": "tap-shopify",
                "target_description": null,
                "discovery_exit_status": 0,
                "discovery_description": null,
                "tap_description": "Response(code=401, body=\"b'{\"errors\":\"[API] Invalid API key or access token (unrecognized login or wrong password)\"}'\", headers={'X-Content-Type-Options': 'nosniff', 'CF-RAY': '58bb5e36f82eea86-IAD', 'X-ShopId': '4007166025', 'Content-Security-Policy': \"default-src 'self' data: blob: 'unsafe-inline' 'unsafe-eval' https://* shopify-pos://*; block-all-mixed-content; child-src 'self' https://* shopify-pos://*; connect-src 'self' wss://* https://*; frame-ancestors 'none'; img-src 'self' data: blob: https:; script-src https://cdn.shopify.com https://cdn.shopify.cn https://checkout.shopifycs.com https://js-agent.newrelic.com https://bam.nr-data.net https://api.stripe.com https://mpsnare.iesnare.com https://appcenter.intuit.com https://www.paypal.com https://js.braintreegateway.com https://c.paypal.com https://maps.googleapis.com https://www.google-analytics.com https://v.shopify.com https://widget.intercom.io https://js.intercomcdn.com 'self' 'unsafe-inline' 'unsafe-eval'; upgrade-insecure-requests; report-uri /csp",
                "completion_time": "2020-04-29T19:18:17Z",
                "source_id": 228068
              },
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
              },
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
              },
              [...]
            ],
            "page": 1,
            "total": 102,
            "links": {
              "next": "/v4/116078/extractions?page=2"
            }
          }

  - type: "Errors"
    # Included only if there are errors for the endpoint
    # The errors live in: _data/connect/response-codes.yml
---