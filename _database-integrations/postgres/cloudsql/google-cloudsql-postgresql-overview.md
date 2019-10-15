---
title: Google CloudSQL PostgreSQL
keywords: postgresql, postgres, google cloudsql postgres, google cloudsql postgresql, database integration, etl postgres, etl cloudsql, cloudsql etl, postgres etl, postgresql etl
tags: [database_integrations]
permalink: /integrations/databases/google-cloudsql-postgresql
summary: "Connect and replicate data from your Google CloudSQL PostgreSQL database using Stitch's Google CloudSQL PostgreSQL integration."
layout: general
input: false

show-in-menus: true
has-versions: true

db-type: "postgres"
name: "cloudsql-postgres"
display_name: "Google CloudSQL PostgreSQL"

sections:
  - title: "Identify your version"
    anchor: "identify-your-version"
    content: |
      {% include integrations/templates/versioning/integration-version-tiles.html %}

  - title: "Version history"
    anchor: "version-history"
    content: |
      {% include shared/versioning/history-and-changelog.html %}

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
      
      - title: "Data types"
        anchor: "data-types"
        summary: "Data types"
        content: |
          {% include replication/templates/data-types/integration-specific-data-types.html specific-types=true display-intro=true %}
---
{% include misc/data-files.html %}