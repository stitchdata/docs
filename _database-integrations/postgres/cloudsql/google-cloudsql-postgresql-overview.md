---
title: Google CloudSQL PostgreSQL
keywords: postgresql, postgres, google cloudsql postgres, google cloudsql postgresql, database integration, etl postgres, etl cloudsql, cloudsql etl, postgres etl, postgresql etl
permalink: /integrations/databases/google-cloudsql-postgresql
summary: "Connect and replicate data from your Google CloudSQL PostgreSQL database using Stitch's Google CloudSQL PostgreSQL integration."
layout: general
input: false

key: "cloudsql-postgres-integration"
content-type: "database-category"

show-in-menus: true
has-versions: true
show-in-version-menu: true

db-type: "postgres"
name: "cloudsql-postgres"
display_name: "Google CloudSQL PostgreSQL"

sections:
  - title: "Identify your version"
    anchor: "identify-your-version"
    content: |
      {% include shared/versioning/integration-version-tiles.html %}

  - title: "{{ integration.display_name }} updates"
    anchor: "integration-updates"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title | flatify }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "{{ integration.display_name }} version history"
        anchor: "version-history"
        content: |
          {% include shared/versioning/version-history.html %}

      - title: "{{ integration.display_name }} changelog"
        anchor: "integration-changelog"
        content: |
          {% include changelog/entry-list.html type="connection-overview" %}

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
          {% include shared/versioning/integration-supported-features.html type="version-comparison" feature-type="databases" %}
      
      - title: "Data types"
        anchor: "data-types"
        summary: "Data types"
        content: |
          {% include replication/templates/data-types/integration-specific-data-types.html specific-types=true display-intro=true %}
---
{% include misc/data-files.html %}