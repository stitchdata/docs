---
title: Pagination
product-type: "connect"
content-type: "api-doc"
order: 6

anchor: "pagination--overview"

sections:
  - content: |
      Some endpoints in the API return lists of objects such as extraction jobs, loading records, and so on. As lists can be quite large depending on the number of sources in a client account, several API endpoints will return paginated results.

  - title: "Per page record limits"
    anchor: "pagination--per-page-record-limits"
    content: |
      Pages are currently limited to 100 records per page.

  - title: "Result sorting and ordering"
    anchor: "pagination--result-sorting-ordering"
    content: |
      Paginated results are sorted and ordered. The data used to sort and order records varies by endpoint.

      Refer to the [Endpoints with pagination](#pagination--endpoints) for a list of endpoints with pagination and how results are returned.

  - title: "Pagination data"
    anchor: "pagination--data"
    content: |
      Endpoints with paginated results have `page`, `total`, and `links` properties in their responses:

      {% capture code %}{
        "page": 1,
        "total": 37,
        "links": {}
      }
      {% endcapture %}
      {% include layout/code-snippet.html code=code %}

      If the result set doesn't exceed the per page maximum, the `links` property will be empty, like in the previous example.

      If the result set exceeds the per page maximum, the `links` property will have `next` and `previous` properties. These values are URLs to the next and previous pages of results, respectively:

      {% capture code %}{
        "page": 2,
        "total": 237,
        "links": {
          "next": "/v4/116078/extractions?page=3",
          "previous": "/v4/116078/extractions?page=1"
        }
      }
      {% endcapture %}
      {% include layout/code-snippet.html code=code %}

      The `next` and `previous` values can be used as path parameters to make subsequent requests and retrieve additional pages of results. If there aren't any pages before or after the current page, the `links` object won't have a `previous` or `next` property, respectively.

      For example: If `page: 2` and `next: /v4/116078/extractions?page=3`, make a request to the endpoint using this URL to retrieve page 3 of the results:

      {% assign right-bracket = "}" %}
      {% assign request-url = site.data.connect.core-objects.extractions.base | replace: "{client_id","116078" | append: "?page=3" | remove: right-bracket | strip_newlines %}
      {% assign header = site.data.connect.request-headers.get.without-body %}
      {% assign description = "GET " | append: site.data.connect.core-objects.extractions.base %}

      {% include developers/api-request-examples.html code-description=description header=header request-url=request-url %}

      To retrieve all pages, continue paging until the response no longer contains a `next` property:

      {% capture code %}{
        "page": 3,
        "total": 237,
        "links": {
          "previous": "/v4/116078/extractions?page=2"
        }
      }
      {% endcapture %}
      {% include layout/code-snippet.html code=code %}

  - title: "Limitations"
    anchor: "pagination--limitations"
    content: |
      A request made for a specific page returns only the results for that page, not the entire result set.

      To determine which records display on each page, Stitch divides the total record count by the [per page maximum](#pagination--per-page-record-limits). Keep in mind that if the total number of records changes, records may shift between pages. This means that some records may appear multiple times or be skipped all together while iterating over the entire list.

      As a result, multiple requests will be required to retrieve all the data from a paginated endpoint. When making subsequent requests, keep in mind that some endpoints are subject to [rate limiting]({{ site.data.connect.api.rate-limits }}).

      Consider the following example:

      {% include layout/image.html enlarge=true file="/connect/pagination-example.png" max-width="500" alt="Example of pagination and shifting records to different pages" %}

  - title: "Endpoints with pagination"
    anchor: "pagination--endpoints"
    content: |
      {% assign all-endpoints = site.developer-files | where:"product-type","connect" %}
      {% assign connect-endpoints = all-endpoints | where:"content-type","api-endpoint" %}

      **Note**: Only endpoints with pagination are listed in this section. If an endpoint isn't listed, pagination is not currently applicable for that endpoint.

      <table class="attribute-list table-hover">
      <tr>
      <td width="35%; fixed" align="right">
      <strong>Endpoint</strong>
      </td>
      <td>
      <strong>Ordered by</strong>
      </td>
      <td>
      <strong>Sorting</strong>
      </td>
      </tr>
      {% for endpoint in connect-endpoints %}
      {% if endpoint.pagination %}
      <tr>
      <td align="right">
      <a href="#{{ endpoint.key }}">{{ endpoint.method | upcase }} {{ endpoint.short-url | flatify }}</a>
      </td>
      <td>
      {{ endpoint.order-by }}
      </td>
      <td>
      {{ endpoint.sort-type }}
      </td>
      </tr>
      {% endif %}
      {% endfor %}
      </table>
---