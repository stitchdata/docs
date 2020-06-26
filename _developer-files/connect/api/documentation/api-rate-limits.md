---
title: Rate limits
product-type: "connect"
content-type: "api-doc"
order: 5

anchor: "rate-limit-overview"

sections:
  - content: |
      A [rate limit](https://en.wikipedia.org/wiki/Rate_limiting){:target="new"} defines the maximum number of requests, over a period of time, that can be made to the Connect API.

      Rate limits are enforced for endpoints that can return large amounts of data or may require polling to identify updates. To ensure all API consumers receive the same high quality experience, Stitch employs rate limits to ensure API stability and availability.

  - title: "Rate limit application"
    anchor: "rate-limits--application"
    content: |
      Stitch imposes a limit on the number of requests that can be made for a given client ID over a period of time. The number of requests and the time period over which requests can be made varies by resource type.

      Endpoints are grouped based on resource type. Usage counting towards the rate limit for a resource type is aggregated across requests made to all endpoints in the resource type group.

      For example: The **Extractions** and **Loads** endpoints are part of the **Jobs** resource. Requests made to any extraction- or load-based endpoint counts towards the rate limit usage for the **Jobs** resource type.

  - title: "Rate limit types"
    anchor: "rate-limits--types"
    content: |
      The resource type for an endpoint determines how many API requests can be made for a given time period. Refer to the table below for details about resource types and the endpoints that are subject to rate limits.

      **Note**: Only endpoints subject to rate limiting are listed in the table. If an endpoint isn't listed, rate limiting is not currently applicable for that endpoint.
      
      <table class="attribute-list">
      <tr>
      <td width="20%; fixed" align="right">
      <strong>Resource type</strong>
      </td>
      <td>
      <strong>API requests</strong>
      </td>
      <td>
      <strong>Time period</strong>
      </td>
      <td>
      <strong>Affected endpoints</strong>
      </td>
      </tr>
      {% assign rate-limits = site.data.connect.rate-limits %}
      {% for resource-type in rate-limits.resource-types %}
      {% assign this-resource = rate-limits[resource-type.id] %}
      <tr>
      <td align="right">
      <p id ="{{ resource-type.id | append: "--resource-type" }}">{{ this-resource.type | capitalize }}</p>
      </td>
      <td>
      {{ this-resource.request-limit }}
      </td>
      <td>
      {{ this-resource.total-time }} {{ this-resource.time-interval | append: "s" }}
      </td>
      <td>
      <ul style="margin-top: 0px;">
      {% assign endpoints = site.developer-files | where:"rate-limit-type",resource-type.id | group_by:"endpoint" %}
      {% for endpoint in endpoints %}
      <li>
      <a href="#{{ endpoint.key }}">{{ endpoint.method | upcase }} {{ endpoint.short-url | flatify }}</a>
      </li>
      {% endfor %}
      </ul>
      </td>
      </tr>
      {% endfor %}
      </table>

  - title: "Avoid rate limiting violations"
    anchor: "rate-limits--avoid-violations"
    content: |
      Currently, Stitch takes a **DTRT (Do The Right Thing)** approach to enforcing rate limits. There isn't functionality built into the API to programmatically enforce rate limits, but this may change in the future. We're trusting everyone to be good API consumers.

      If a client repeatedly exceeds rate limits, Stitch may block that client from accessing rate limited endpoints.

      To avoid rate limit violations, we recommend making requests only for the data you need, only when you need it. Additionally, distribute requests to ensure you stay within the maximum number of requests during the allowed time period for the endpoint.
---