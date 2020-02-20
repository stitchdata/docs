---
title: "Libraries and resources"
product-type: "import-api"
content-type: "overview"
list-type: "resources"
order: 3

sections:
  - content: |
      Below are some of the community-supported libraries and resources for the Stitch Import API.

      If you need help using these resources, we recommend creating an issue on the GitHub repository (linked below) or asking the [Stitch Community]({{ site.community }}){:target="new"}. **Note**: Stitch Support doesn't provide assistance for these resources.

      **Created your own library or have an example you want to share?** [Let us know](mailto:{{ site.support }}) and we'll add it to the list.

      {% assign languages = site.data.import-api.resources.all | sort:"language" %}

      {% for language in languages %}
      ### {{ language.display-name }}

      {% assign resources = language.resources | sort:"title" %}

      {% for resource in resources %}
      - [{{ resource.title }}]({{ resource.url | flatify }}){:target="new"} by {{ resource.author | flatify }}
      {% endfor %}

      {% endfor %}
---