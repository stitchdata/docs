---
title: Introduction
product-type: "import-api"
content-type: "api-doc"
order: 1

sections:
  - content: |
      {% include misc/data-files.html %}

      {{ site.data.import-api.api.description }}

      This API is a RESTful, method-oriented API that allows you to push data from a source (including those Stitch doesn't currently have an integration for) and send it to Stitch. Each endpoint uses standard HTTP verbs like GET and POST, and will return standard HTTP response codes to indicate request status or errors.

      The API is built to accept JSON or Transit requests and to return JSON in all responses, including errors.

  - title: "API functionality"
    anchor: "api-funcitonality"
    content: |
      Using the Import API, you can:

      - Push data from a source to Stitch
      - Check the status of the Import API
      - Validate requests and batches without persisting them to Stitch

  - title: "Accessing the API"
    anchor: "access-the-api"
    content: |
      Anyone with a Stitch account can use the Import API. If you don't currently have an account, [sign up for a free one here]({{ site.home }}){:target="new"}.

      After you have a Stitch account, refer to the [Stitch Import API access tokens documentation]({{ link.import-api.guides.access-tokens | prepend: site.baseurl }}) for instructions on generating an API access token. 

  - title: "API support"
    anchor: "getting-help"
    content: |
      While the Import API is a certified Stitch integration, using it does require some technical knowledge. This means that Stitch will address bugs and issues with the API that are within Stitch's infrastructure, but Stitch doesn't provide assistance for building or maintaining the scripts that send data to the API.

      The table below provides some examples of the types of requests Stitch will and will not provide assistance for.

      <table class="attribute-list">
      <tr>
      <td width="50%; fixed">
      <strong>Stitch Support can assist with:</strong>
      </td>
      <td width="50%; fixed">
      <strong>Stitch Support does not assist with:</strong>
      </td>
      </tr>
      <tr>
      <td width="50%; fixed">
      <ul>
      <li>Identifying and reporting Import API outages</li>
      <li>Identifying and resolving issues within Stitch</li>
      </ul>
      </td>
      <td width="50%; fixed">
      <ul>
      <li>Writing scripts</li>
      <li>Data typing in requests</li>
      <li>Troubleshooting scripts or API requests</li>
      <li>Troubleshooting open source scripts that use the Import API, e.g. <a href="{{ site.data.import-api.resources.google-sheets.url }}" target="new">Google Sheets</a></li>
      <li>Retrieving API access tokens</li>
      </ul>
      </td>
      </tr>
      </table>

      Refer to the [Import API guides and resources]({{ link.import-api.guides.category | prepend: site.baseurl }}) for assistance when developing and testing your script.

      Additionally, ask the [Stitch Community]({{ site.community }}){:target="new"} if you're still stuck.
---