---
title: Response codes
product-type: "connect"
content-type: "api-doc"
order: 4

sections:
  - content: |
      The API will attempt to return [HTTP status codes](http://en.wikipedia.org/wiki/List_of_HTTP_status_codes) for every request.

      {% include developers/api-response-code-table.html %}

  - title: "Error message format"
    anchor: "error-message-formats"
    content: |
      {% assign response-codes = site.data.connect.response-codes %}

      The API will return error messages in JSON format. Some error messages may be returned as strings:

      ```
      {{ site.data.connect.response-codes.general-codes.example-responses.string | remove: "`" }}
      ```

      While others may be JSON objects:

      {{ site.data.connect.response-codes.general-codes.example-responses.object | markdownify }}

  - title: "Error message text"
    anchor: "error-message-text"
    content: |
      The text in error messages will vary by root cause and endpoint.

      Each endpoint section contains a rollup of the errors specific to that endpoint. Refer to the documentation for the endpoint for specifics on errors, their possible causes, and the messages the API will return.

---