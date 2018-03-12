---
title: Introduction
content-type: "embed-doc"
order: 1

sections:
  - content: |
      The {{ page.api-name }} can be used to:

        - Create Stitch client accounts,
        - Access existing Stitch client accounts, and
        - Configure source and destination connections within those clients' accounts

      The {{ page.api-name }} is organized around REST and uses resource-oriented URLs to promote usability. Each endpoint uses standard HTTP verbs like `GET` and `POST`, and we will return [standard HTTP response codes](#response-codes) to indicate request status or errors.

      We built the {{ page.api-name }} to accept and return [JSON](http://json.org) in all responses, including errors.


  - title: "Obtain Partner Credentials"
    anchor: "obtain-partner-credentials"
    content: "To use the API, you need to register your application and obtain partner credentials. Reach out to [{{ page.contact-email }}](mailto:{{ page.contact-email }}) to get started."


  - title: "Terminology"
    anchor: "terminology"
    content: |
      {% assign api-terms = site.api-files | where:"content-type","embed-terms" %}

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