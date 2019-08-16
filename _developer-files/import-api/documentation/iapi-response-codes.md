---
title: Response Codes
product-type: "import-api"
content-type: "api-doc"

anchor: "all-response-codes"
order: 4

sections:
  - content: |
      The API will attempt to return [HTTP status codes](http://en.wikipedia.org/wiki/List_of_HTTP_status_codes){:target="new"} to indicate the success or failure of a request sent to the API.

      In general:

      - Codes in the `2xx` range indicate success
      - Codes in the `4xx` range indicate an error with the request, such as an invalid API access token, missing client ID, malformed request body, etc.
      - Codes in the `5xx` range indicate an issue with Stitch. Persistent `5xx` codes may indicate an outage, which you can monitor on [Stitch's status page]({{ site.status }}){:target="new"}.

      Your application should handle each of the following statuses gracefully:

      {% include developers/api-response-code-table.html %}

  - title: "Response and error message formats"
    anchor: "response-error-message-formats"
    content: |
      The API will return responses - successful or errors - in JSON format. Below are descriptions and examples of each type of response.

    subsections:
      - title: "Response message formats"
        anchor: "response-message-formats"
        content: |
          For successful responses (codes in the `2xx` range) the API will return messages as a JSON object:

          ```json
          {
            "status": "OK",
            "message": "Batch Accepted!"
          }
          ```

          In the Import API documentation, this is referred to as a [Batch Status object]({{ site.data.import-api.data-structures.batch-status.section }}).


      - title: "Error message formats"
        anchor: "error-message-formats"
        content: |
          For error responses (codes in the `4xx` range), the API will return error messages in JSON format. In the Import API documentation, this is referred to as an [Error object]({{ site.data.import-api.data-structures.error.section }}).

          Some error messages may be returned as strings:

          ```json
          Content-Type must be application/json
          ```

          While others may be JSON objects:

          ```json
          {
            "status": "ERROR",
            "error": "Forbidden",
            "errors": {
              "error": "Access token is not associated with this client."
            }
          }
          ```

      - title: "Error message text"
        anchor: "error-message-text"
        content: |
          The text in error messages will vary by root cause and endpoint.

          Each endpoint section contains a list of the errors specific to that endpoint. Refer to the documentation for the endpoint for specifics on errors, their possible causes, and the messages the API will return.
---