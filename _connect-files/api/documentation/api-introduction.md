---
title: Introduction
content-type: "api-doc"
order: 1

sections:
  - content: |
      {% include misc/data-files.html %}

      The Stitch Connect API enables users to programmatically access and manage their Stitch accounts, or Stitch partners to seamlessly integrate Stitch's data pipleine functionality into their own platforms.

      This API is a RESTful, resource-oriented API that allows you to programmatically provision Stitch accounts, create and modify data sources, and configure destination connections.

      Each endpoint uses standard HTTP verbs like GET and POST, and will return [standard HTTP response codes]({{ api.response-codes }}) to indicate request status or errors.

      We built the API to accept and return [JSON](http://json.org) in all responses, including [errors]({{ api.error-message-formats }}).

  - title: "API functionality"
    anchor: "api-funcitonality"
    content: |
      Using the API, you can:

      - Create Stitch client accounts (Partners only)
      - Access Stitch client accounts
      - Create, update, and delete destinations
      - Retrieve configuration info for destinations
      - Create, update, pause, unpause, and delete data sources
      - Retrieve configuration info for data sources
      - Select streams and fields from data sources for replication
      - Start and stop replication jobs

      Check out the [tutorials and resources]({{ link.connect.guides.category | prepend: site.baseurl }}) to learn more about using Stitch Connect.

# {% capture source-config %}
# **OAuth sources**: To fully configure an OAuth data source, you will also need to use the [{{ js.name }}]({{ js.section | prepend: site.baseurl | flatify }}). This will send the user to Stitch, where they will be prompted to authorize access to the data source.
# {% endcapture %}
# {% include note.html type="single-line" content=source-config %}

  - title: "Accessing the API"
    anchor: "access-the-api"
    content: |
      To use the API, you'll need to obtain an API access token. This is necessary for authenticating successfully. Refer to the [Authentication section]({{ site.data.connect.api.authentication }}) for more info.

  - title: "Terminology"
    anchor: "terminology"
    content: |
      {% assign api-terms = site.connect-files | where:"content-type","api-terms" %}

      <table class="attribute-list">
      {% for item in api-terms %}
      {% for term in item.all-terms %}
      <tr>
      <td class="attribute-name">
      <strong>{{ term.name }}</strong>
      </td>

      <td class="description">
      {{ term.definition | flatify | markdownify }}
      </td>

      </tr>
      {% endfor %}
      {% endfor %}
      </table>
---