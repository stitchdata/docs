---
permalink: /test
layout: general

sections:
  # - content: |
  #     

  #     {% for table in all-tables %}
  #     **{{ table.name }}**
  #     {% include functions/f_navtree.html table=table.attributes %}
  #     {% endfor %}

  - title: "testing"
    content: |
      {% assign all-tables = site.integration-schemas | where:"tap","bigcommerce" %}
      {% for table in all-tables %}
      {% include integrations/templates/schemas/TEST-table-schemas.html table=table.attributes %}
      {% endfor %}
---