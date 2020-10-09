---
title: Amazon PostgreSQL RDS
keywords: amazon, amazon rds, rds, relational database services, database integration, etl rds, rds etl
tags: [database_integrations]
permalink: /integrations/databases/amazon-rds-postgresql
summary: "Connect and replicate data from your Amazon PostgreSQL RDS database using Stitch's PostgreSQL integration."
layout: general
input: false

key: "postgresql-rds-integration"
content-type: "database-category"

show-in-menus: true
has-versions: true
show-in-version-menu: true

db-type: "postgres"
name: "postgresql-rds"
display_name: "Amazon PostgreSQL RDS"

sections:
  - title: "Identify your version"
    anchor: "identify-your-version"
    content: |
      {% include shared/versioning/integration-version-tiles.html %}

  - title: "Version history"
    anchor: "version-history"
    content: |
      {% include shared/versioning/version-history.html %}

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