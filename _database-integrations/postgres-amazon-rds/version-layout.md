---
title: Amazon RDS PostgreSQL
keywords: amazon, amazon rds, rds, relational database services, database integration, etl rds, rds etl
tags: [database_integrations]
permalink: /integrations/databases/testing-version-layout
summary: "Connect and replicate data from your Amazon RDS database using Stitch's RDS integration."
layout: general
input: false

db-type: "postgres"
name: "postgresql-rds"
display_name: "PostgreSQL RDS"

sections:
  - title: "Identify your version"
    anchor: "identify-your-version"
    content: |
      [ TO DO! ]

      {% include integrations/templates/versioning/integration-version-tiles.html %}

  - title: "Version history"
    anchor: "version-history"
    content: |
      {% include integrations/templates/versioning/integration-version-history.html %}
    subsections:
      - content: |
          {% include integrations/templates/versioning/integration-supported-features.html %}
      - content: |
          {% include replication/templates/data-types/integration-specific-data-types.html %}

---
{% include misc/data-files.html %}