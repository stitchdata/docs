---
title: Amazon Microsoft SQL Server RDS
keywords: microsoft sql server rds, sql server, mssql, database integration, etl mssql, mssql etl, sql server etl, amazon rds
permalink: /integrations/databases/amazon-rds-microsoft-sql-server
summary: "Connect and replicate data from your Amazon Microsoft SQL Server RDS database using Stitch's Microsoft SQL Server integration."
layout: general
input: false

key: "amazon-mssql-rds-integration"

show-in-menus: true
has-versions: true
show-in-version-menu: true

hosting-type: "amazon"

db-type: "mssql"
name: "sql-server-rds"
display_name: "Amazon Microsoft SQL Server RDS"

sections:
  - title: "Identify your version"
    anchor: "identify-your-version"
    content: |
      {% include shared/versioning/integration-version-tiles.html %}

  - title: "{{ integration.display_name }} version history"
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
          {% include shared/versioning/integration-supported-features.html type="version-comparison" feature-type="databases" %}
      
      - title: "Data types"
        anchor: "data-types"
        summary: "Data types"
        content: |
          {% include replication/templates/data-types/integration-specific-data-types.html version="1.0" specific-types=true display-intro=true %}
---
{% include misc/data-files.html %}