---
title: Amazon PostgreSQL RDS
keywords: amazon, amazon rds, rds, relational database services, database integration, etl rds, rds etl
tags: [database_integrations]
permalink: /integrations/databases/amazon-rds-postgresql
summary: "Connect and replicate data from your Amazon RDS database using Stitch's RDS integration."
layout: general
input: false

show-in-menus: true
has-versions: true

db-type: "postgres"
name: "postgresql-rds"
display_name: "PostgreSQL RDS"

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
      {% include notifications/postgres-binlog-limitations.html %}

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