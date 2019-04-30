---
title: Amazon Aurora (PostgreSQL) RDS
keywords: amazon, amazon aurora rds, amazon aurora postgres, rds, relational database services, database integration, etl rds, rds etl
permalink: /integrations/databases/amazon-aurora-postgresql
summary: "Connect and replicate data from your Amazon Aurora PostgreSQL RDS database using Stitch's PostgreSQL integration."
layout: general
input: false

show-in-menus: true
has-versions: true

db-type: "postgres"
name: "aurora-postgresql-rds"
display_name: "Aurora PostgreSQL RDS"

sections:
  - title: "Identify your version"
    anchor: "identify-your-version"
    content: |
      {% include integrations/templates/versioning/integration-version-tiles.html %}

  - title: "Version history"
    anchor: "version-history"
    content: |
      {% include integrations/templates/versioning/integration-history-and-changelog.html %}
  - title: "Version features"
    anchor: "version-features"
    content: |
      In this section:

      - [Supported features](#supported-features)
      - [Supported data types](#supported-data-types)
    subsections:
      - content: |
          {% include integrations/templates/versioning/integration-supported-features.html type="version-comparison" feature-type="databases" %}
      - content: |
          {% include replication/templates/data-types/integration-specific-data-types.html %}
---
{% include misc/data-files.html %}