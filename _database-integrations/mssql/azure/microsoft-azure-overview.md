---
title: Microsoft Azure SQL Database
keywords: microsoft azure sql database, sql server, mssql, database integration, etl mssql, mssql etl, sql server etl
permalink: /integrations/databases/microsoft-azure
summary: "Connect and replicate data from your Microsoft Azure SQL Database using Stitch's Microsoft Azure integration."
layout: general
input: false

show-in-menus: true
has-versions: true

hosting-type: "generic"

db-type: "mssql"
name: "microsoft-azure"
display_name: "Microsoft Azure SQL Database"

sections:
  - title: "Identify your version"
    anchor: "identify-your-version"
    content: |
      {% include integrations/templates/versioning/integration-version-tiles.html %}

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