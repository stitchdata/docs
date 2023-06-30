---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Destination and Source Connection Property API Reference
permalink: /developers/stitch-connect/guides/source-destination-reference
summary: "Resources for determining API availability and configuration details for each of Stitch's sources and destinations using the API."

product-type: "connect"
content-type: "guide"
content-id: &key "connect-connection-reference"

key: "connect-connection-reference"

layout: general
sidebar: on-page


# -------------------------- #
#      GUIDE PAGE INFO       #
# -------------------------- #

## This is used only on the /stitch-connect/guides page.
doc-type: "reference"
icon: source
order: 10

description: "Learn about API availability and configuration for Stitch's destinations and sources."


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "All destinations"
    link: "{{ site.baseurl }}/destinations"

  - title: "All integrations"
    link: "{{ site.baseurl }}/integrations"
    
  - title: "Connect API reference"
    link: "{{ link.connect.api | prepend: site.baseurl }}"

  - title: "All Connect guides"
    link: "{{ link.connect.guides.category | prepend: site.baseurl }}"


# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}
  {% include misc/icons.html %}

  Stitch connects to a large, diverse universe of applications and data warehouses, each of which is configured differently. Connection property objects contain the properties necessary to create a source or destination.

  This guide serves as a reference for connection property objects in the Connect API, including availability and the properties required (if supported) to configure each of Stitch's destinations and sources via the API.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#        GUIDE CONTENT       #
# -------------------------- #


sections:
  - title: "Connection property object basics"
    anchor: "basics"
    summary: "What connection property objects are and how to use them"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "What are connection property objects?"
        anchor: "what-are-connection-property-objects"
        endpoints:
          - connection: "destinations"
            action: "create"
          - connection: "destinations"
            action: "update"
          - connection: "sources"
            action: "create"
          - connection: "sources"
            action: "update"
        content: |
          A connection property object is a JSON object that contains the properties necessary to create a source or destination using the Connect API. Connection property objects include info like connection credentials, configuration details, and for sources, some replication settings.

          Connection property objects are used with the following endpoints to create and update connections:

          {% assign connect-core-objects = site.data.connect.core-objects %}

          <table>
            <tr>
              <td>
                <strong>Action</strong>
              </td>
              <td>
                <strong>Endpoint</strong>
              </td>
            </tr>
          {% for endpoint in subsection.endpoints %}
            {% assign connection-object = connect-core-objects[endpoint.connection] %}
            <tr>
              <td>
                <strong>{{ connection-object[endpoint.action]title }}</strong>
              </td>
              <td>
                <a href="{{ link.connect.api | prepend: site.baseurl | append: connection-object[endpoint.action]anchor }}">
                  {{ connection-object[endpoint.action]method | upcase }} {{ connection-object[endpoint.action]name | flatify }}
                </a>
              </td>
            </tr>
          {% endfor %}
          </table>

      - title: "Connection property types"
        anchor: "connection-property-types"
        content: |
          Connection property objects can contain two types of properties:

          - **Form properties** are required to create the source or destination and complete the connection's [`form` step]({{ site.data.connect.api.data-structures.connection-steps.section }}). The majority of sources and destinations will only have form properties.

          - **OAuth properties** are used to complete the source or destination's [`oauth` step]({{ site.data.connect.api.data-structures.connection-steps.section }}), if the connection supports OAuth. **OAuth properties are only required if you're performing OAuth for the connection yourself.** Otherwise, Stitch will perform the OAuth handshake using its own client credentials.

             Refer to the [Performing OAuth with Stitch Connect]({{ link.connect.guides.configure-connection-oauth | prepend: site.baseurl }}) guide for more info.

          All connection properties should be sent in the `properties` argument when creating or updating a source or destination. **Note**: OAuth properties may be provided alongside form properties in a single `POST` or `PUT` request. A separate request isn't necessary.
  
  - title: "Search for a connection type"
    anchor: "search-connection-properties"
    summary: "A resource for seeing what's supported for each connection"
    content: |
      Looking for info on a specific connection type? This section contains info about all of Stitch's sources and destinations and their availability in the API.

      In the table below:

      - **Connection name**: The name and version of the connection. 
      - **Connection type**: The type of connection. This will either be `destination` or `source`.
      - **Connection property**: Indicates if the connection is available via the API:

         - **If available**, this column will contain the name of the connection property used to create the connection type. Use the [Create a destination]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.core-objects.destinations.create.anchor }}) or the [Create a source]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.core-objects.sources.create.anchor }}) endpoint to create the connection, depending on the connection's type.
         - **If unavailable**, this column will contain {{ not-supported | replace:"TOOLTIP","Not available in Connect" }} **Unavailable**

      {% assign all-destinations = site.destinations | where:"content-type","destination-setup" | sort_natural:"display_name" %}
      {% assign destinations = all-destinations | where_exp:"destination","destination.key contains 'setup'" %}

      {% assign sources = site.documents | where:"input",true %}

      {% assign all-connections = destinations | concat: sources | sort_natural:"display_name" %}

      {% capture table %}
      <table class="attribute-list" id="filter-table">
      <tr>
      <th width="35%; fixed">
      <strong>Connection name</strong>
      </th>
      <th>
      <strong>Connection type</strong>
      </th>
      <th>
      <strong>Connection property</strong>
      </th>
      </tr>
      <tbody id="filter-body">
      {% for connection in all-connections %}

      {% case connection.collection %}

      {% when 'destinations' %}

        {% assign latest-version = site.data.destinations[connection.type]versions.latest-version %}
          {% assign version = "v" | append: latest-version %}

      {% else %}
        {% if connection.db-type %}

          {% assign latest-version = site.data.taps.versions[connection.db-type]latest-version %}

        {% else %}

          {% assign latest-version = site.data.taps.versions[connection.name]latest-version %}

      {% endif %}

      {% endcase %}

      {% if connection.collection == "webhook-integrations" or connection.this-version == latest-version or connection.override-api-type == true %}
      <tr>
      <td width="35%; fixed">
        <strong>
          {{ connection.display_name }} (v{{ connection.this-version }})
        </strong>
      </td>
      <td>
      {% if connection.collection == "destinations" %}
      Destination 
      {% else %}
      Source
      {% endif %}
      </td>
      <td>
      {% case connection.collection %}
      {% when 'destinations' %}
        {% if site.data.destinations[connection.type]stitch-details.api-type or site.data.destinations[connection.type][version]stitch-details.api-type %}

          {% if site.data.destinations[connection.type]stitch-details.api-type %}

            {% assign api-type = site.data.destinations[connection.type]stitch-details.api-type %}

          {% else %}

            {% assign api-type = site.data.destinations[connection.type][version]stitch-details.api-type %}

          {% endif %}

        {% endif %}

      {% else %}

        {% assign api-type = connection.api-type %}

      {% endcase %}

      {% assign form-properties = site.developer-files | where:"content-type","api-form" %}

      {% assign connection-property = form-properties | find:"api-type",api-type %}

      {% if api-type %}
        <a href="#{{ connection-property.key }}">
          {{ connection-property.api-type }}
        </a>

      {% else %}
        {{ not-supported | replace:"TOOLTIP","Not available in Connect" }} <strong>Unsupported</strong>
      {% endif %}
      </td>
      </tr>
      {% endif %}

      {% endfor %}
      <tr id="noConnectionYet" style="display: none">
      <td id="noConnectionYetName" colspan="3" align="center">
        <strong>Don't see the connection you want?</strong>
        <br>Contact support and submit some feedback for us!
      </td>
      </tr>
      </tbody>
      </table>
      {% endcapture %}

      {% include layout/on-page-search/table-search.html placeholder-copy="Find a destination or source connection" table=table %}

  - title: "All connection property objects"
    anchor: "all-form-properties"
    summary: "A reference of each connection property object's attributes"
    insert-subsections: |
      {% assign form-properties = site.developer-files | where:"content-type","api-form" | sort_natural:"display-name" %}
      
      {% for form-property in form-properties %}                         
        <li>
            <a href="#{{ form-property.key }}" class="api">
              <span class="method {{ form-property.form-type }} method-bullet">{{ form-property.form-type | upcase | strip_newlines }}</span>
                {{ form-property.display-name | flatify }}
              </a>
        </li>
      {% endfor %}
    content: |
      {% include developers/api-form-properties.html %}
---
