---
title: Microsoft SQL Server
keywords: microsoft sql server, sql server, mssql, database integration, etl mssql, mssql etl, sql server etl
permalink: /integrations/databases/microsoft-sql-server
summary: "Connect and replicate data from your Microsoft SQL Server database using Stitch's MSSQL integration."
layout: general
input: false

show-in-menus: true
has-versions: true

hosting-type: "generic"

db-type: "mssql"
name: "mssql"
display_name: "Microsoft SQL Server"

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

      - [Supported features](#supported-features)
    subsections:
      - content: |
          {% include integrations/templates/versioning/integration-supported-features.html type="version-comparison" feature-type="databases" %}
      # - content: |
      #     {% include replication/templates/data-types/integration-specific-data-types.html %}
---
{% include misc/data-files.html %}