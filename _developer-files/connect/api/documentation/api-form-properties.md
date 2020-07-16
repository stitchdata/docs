---
title: Connection property objects
product-type: "connect"
content-type: "api-doc"
anchor: "form-properties"
order: 7

# This parameter is used in _includes/connect/api-endpoint-rollup.html
# To display the correct description for a given form property
property-description: |
  {% assign connection-name = VARIABLE.display-name %}

  {% case VARIABLE.form-type %}

  {% when "source" %}
  {% if VARIABLE.property-description %}
  {{ connection-name }} connections read data from {{ VARIABLE.property-description | flatify }} and correspond to source `type: {{ VARIABLE.api-type }}`.

  {% else %}

  {% case VARIABLE.source-type %}
  {% when 'database' %}

  {{ connection-name }} connections read data from {{ connection-name }} databases and correspond to source `type: {{ VARIABLE.api-type }}`.

  {% when 'saas' %}
  {{ connection-name }} connections read data from the {{ connection-name }} API and correspond to source `type: {{ VARIABLE.api-type }}`.

  {% when 'import-api' %}
  {{ connection-name }} connections receive data you push to the Import API and correspond to source `type: {{ VARIABLE.api-type }}`.
  
  {% endcase %}
  {% endif %}

  {% when "destination" %}
  {% if VARIABLE.property-description %}
  {{ connection-name }} connections write data to {{ VARIABLE.property-description | flatify }} and correspond to destination `type: {{ VARIABLE.api-type }}`.

  {% else %}

  {{ connection-name }} connections write data to a {{ connection-name }} database and correspond to destination `type: {{ VARIABLE.api-type }}`.

  {% endif %}
  {% endcase %}

sections:
  - content: |
      Stitch connects to a large, diverse universe of applications and data warehouses, each of which is configured differently.

      Connection property objects contain the properties necessary to create a source or destination object. Connection object property objects can contain two types of properties:

      - **Form properties** are required to create the source or destination and complete the connection's [`form` step]({{ site.data.connect.api.data-structures.connection-steps.section }}). The majority of sources and destinations will only have form properties.

      - **OAuth properties** are used to complete the source or destination's [`oauth` step]({{ site.data.connect.api.data-structures.connection-steps.section }}), if the connection supports OAuth. **OAuth properties are only required if you're performing OAuth for the connection yourself.** Otherwise, Stitch will perform the OAuth handshake using its own client credentials.

         Refer to the [Performing OAuth with Stitch Connect]({{ link.connect.guides.configure-connection-oauth | prepend: site.baseurl }}) guide for more info.

      All connection properties should be sent in the `properties` argument when creating or updating a source or destination. **Note**: OAuth properties may be provided alongside form properties in a single `POST` or `PUT` request. A separate request isn't necessary.

  - title: "Search for a connection property object"
    anchor: "search-connection-properties"
    content: |
      Search all supported destination and source connection properties below. **Note**: If a connection isn't listed here, it isn't currently available in the API. Refer to the [Destination and Source API availability reference]({{ link.connect.guides.connection-reference | prepend: site.baseurl }}) for a full list of Stitch's connections.

      {% assign form-properties = all-docs | where:"content-type","api-form" | sort_natural: "title" %}

      {% capture table %}
      <table class="attribute-list" id="filter-table">
      <tr>
      <th width="35%; fixed">
      <strong>Connection property name</strong>
      </th>
      <th>
      <strong>Connection type</strong>
      </th>
      <th>
      <strong>Connection property type</strong>
      </th>
      </tr>
      <tbody id="filter-body">
      {% for form-property in form-properties %}
      <tr>
      <td width="35%; fixed">
      <a href="#{{ form-property.key }}">{{ form-property.title | remove: " Destination Form Property" | remove: " Source Form Property" }}</a>
      </td>
      <td>
      {{ form-property.form-type | capitalize }}
      </td>
      <td>
      {{ form-property.api-type }}
      </td>
      </tr>
      {% endfor %}
      <tr id="noConnectionYet" style="display: none">
      <td id="noConnectionYetName" colspan="3" align="center">
        <strong>Don't see the connection you want?</strong>
        <br>Refer to the <a href="{{ link.connect.guides.connection-reference | prepend: site.baseurl }}">Destination and Source API availability reference</a> to check the connection's availability in Stitch.
      </td>
      </tr>
      </tbody>
      </table>
      {% endcapture %}

      {% include layout/on-page-search/table-search.html placeholder-copy="Find a destination or source connection property" table=table %}

  - title: "All connection property objects"
    anchor: "all-form-properties"
    include: |
      {% include developers/api-form-properties.html %}
---