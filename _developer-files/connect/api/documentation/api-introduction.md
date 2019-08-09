---
title: Introduction
product-type: "connect"
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

      {% assign api-objects = site.connect-files | where:"content-type","api-object" | sort:"order" %}

      {% for object in api-objects %}
      {% if object.intro-short %}
      - {{ object.intro-short | flatify }}
      {% endif %}
      {% endfor %}

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
      {% assign all-connect-docs = site.developer-files | where:"product-type","connect" %}
      {% assign api-terms = all-connect-docs | where:"content-type","api-terms" %}

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