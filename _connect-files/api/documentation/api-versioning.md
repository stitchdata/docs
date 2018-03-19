---
title: Versioning
content-type: "api-doc"
order: 5

sections:
  - content: |
      The API is currently versioned **by object**.

      {% assign objects = site.connect-files | where:"content-type","api-object" | sort:"order"%}

        <table width="100%; fixed" style="font-size: 15px;">
        <tr>
        <td align="right" width="25%; fixed">
        <strong>
        Object
        </strong>
        </td>
        <td width="15%; fixed">
        <strong>
        Version
        </strong>
        </td>
        <td>
        <strong>
        Endpoints
        </strong>
        </td>
        </tr>
        {% for object in objects %}
        <tr>
        <td align="right">
        <strong>
        <a href="#{{ object.title | downcase | replace: " ", "-" | append: "--object" }}">{{ object.title }}
        </a></strong>
        </td>
        <td>
        v{{ object.version }}
        </td>
        <td>
        {% assign all-endpoints = site.connect-files | where:"content-type","api-endpoint" %}
        {% assign object-endpoints = all-endpoints | where:"endpoint",object.endpoint %}
        {% assign same-version = object-endpoints | where:"version",object.version %}
        {% assign endpoints = same-version | sort:"order" %}
        <ul>
        {% for endpoint in endpoints %}
        <li style="margin: 0">
        <a href="#{{ endpoint.key }}">{{ endpoint.method | upcase }} {{ endpoint.short-url | flatify }}</a>
        </li>
        {% endfor %}
        </ul>
        </td>
        </tr>
        {% endfor %}
        </table>

---