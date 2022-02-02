---
title: MariaDB
keywords: mariadb, database integration, etl mariadb, mariadb etl
permalink: /integrations/databases/mariadb
summary: "Connect and replicate data from your MariaDB database using Stitch's MariaDB integration."
layout: general
input: false

key: "mariadb-integration"
content-type: "database-category"

show-in-menus: true
has-versions: true
show-in-version-menu: true

has-specific-data-types: true

db-type: "mysql"
name: "mariadb"
display_name: "MariaDB"

connection-type: "integration"

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
      {% include replication/templates/data-types/integration-specific-data-types.html version="2" specific-types=true display-intro=true %}        
---
{% include misc/data-files.html %}