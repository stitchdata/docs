---
title: Introduction
content-type: "api-doc"
order: 1

sections:
  - content: |
      The Stitch Connect API enables you to seamlessly integration Stitch’s data pipeline functionality into your own platform. This API is a RESTful, resource-oriented API that allows you to programmatically provision Stitch accounts, create and modify data sources, and configure destination connections.

      Each endpoint uses standard HTTP verbs like GET and POST, and will return [standard HTTP response codes]({{ api.response-codes }}) to indicate request status or errors.

      We built the API to accept and return [JSON](http://json.org) in all responses, including [errors]({{ api.error-message-formats }}).

  - title: "Accessing the API"
    anchor: "access-the-api"
    content: |
      To use the API, you'll need partner credentials. These are necessary for authenticating successfully.

      To request access, please complete and submit [this form]{{ connect.interest-form | strip }}.

  - title: "Terminology"
    anchor: "terminology"
    content: |
      {% assign api-terms = site.connect-files | where:"content-type","api-terms" %}

      <table width="100%; fixed">
      {% for item in api-terms %}
      {% for term in item.all-terms %}
      <tr>
      <td width="20%; fixed" align="right">
      <strong>{{ term.name }}</strong>
      </td>

      <td>
      {{ term.definition | flatify | markdownify }}
      </td>

      </tr>
      {% endfor %}
      {% endfor %}
      </table>


---

