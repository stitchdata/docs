---
title: MongoDB
keywords: mongodb, mongodb, database integration, etl mongodb, mongodb etl, mongodb etl, etl
permalink: /integrations/databases/mongodb
summary: "Connect and replicate data from your MongoDB database using Stitch's MongoDB integration."
layout: general
input: false

show-in-menus: true
has-versions: true
has-specific-data-types: false

db-type: "mongo"
name: "mongodb"
display_name: "MongoDB"

sections:
  - title: "Identify your version"
    anchor: "identify-your-version"
    content: |
      {% include integrations/templates/versioning/integration-version-tiles.html %}

  - title: "{{ integration.display_name }} version history"
    anchor: "version-history"
    content: |
      {% include integrations/templates/versioning/integration-history-and-changelog.html %}

  - title: "{{ integration.display_name }} version features"
    anchor: "version-features"
    content: |
      In this section:

      {% for subsection in section.subsections %}
      - [{{ subsection.summary }}](#{{ subsection.summary | slugify }})
      {% endfor %}
    subsections:
      - summary: "Supported features"
        content: |
          {% include integrations/templates/versioning/integration-supported-features.html type="version-comparison" feature-type="databases" %}
      
      # - title: "Data types"
      #   anchor: "data-types"
      #   summary: "Data types"
      #   content: |
      #     {% include replication/templates/data-types/integration-specific-data-types.html specific-types=true display-intro=true %}
---
{% include misc/data-files.html %}