---
title: Versioning
product-type: "connect"
content-type: "api-doc"
order: 5

sections:
  - content: |
      The API is currently versioned by object. The table below lists the core objects, all available versions, and the endpoints available for each version.

      {% assign all-connect-docs = site.developer-files | where:"product-type","connect" %}
      {% assign objects = all-connect-docs | where:"content-type","api-object" | sort:"order"%}

      <table class="attribute-list">
      {% for object in objects %}
      <tr>
      <td colspan="2" class="table-subheading">
      <strong>
      <a href="#{{ object.endpoint | append: "--section" }}">{{ object.title | upcase }}
        </a>
        </strong>
      </td>
      </tr>
      
      <tr>
      <td width="15%; fixed" align="right">
      <strong>Version</strong>
      </td>
      <td class="attribute-description">
      <strong>Endpoints</strong>
      </td>
      </tr>

      {% for version in object.versions %}
      <tr>
      <td width="15%; fixed" align="right">
      <strong>{{ version.number | prepend: "v" }} {% if version.number == object.latest-version %} (latest){% endif %}</strong>
      </td>
      <td class="attribute-description">
      {% assign all-endpoints = site.developer-files | where:"content-type","api-endpoint" %}
        {% assign object-endpoints = all-endpoints | where:"endpoint",object.endpoint %}
          {% assign version-endpoints = object-endpoints | where:"version",version.number | sort: "order" %}

          <ul>
          {% for endpoint in version-endpoints %}
          {% unless endpoint.not-available-until-version %}
          <li style="margin: 0">
          <a href="#{{ endpoint.key }}">{{ endpoint.method | upcase }} {{ endpoint.short-url | flatify }}</a>
          </li>
          {% endunless %}
          {% endfor %}
          </ul>
      </td>
      </tr>
      {% endfor %}

      {% endfor %}
      </table>
---