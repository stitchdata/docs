---
title: Google CloudSQL PostgreSQL
keywords: postgresql, postgres, google cloudsql postgres, google cloudsql postgresql, database integration, etl postgres, etl cloudsql, cloudsql etl, postgres etl, postgresql etl
tags: [database_integrations]
permalink: /integrations/databases/google-cloudsql-postgresql
summary: ""
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
      [ TO DO! ]

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
          {% include integrations/templates/versioning/integration-supported-features.html feature-type="databases" %}
      - content: |
          {% include replication/templates/data-types/integration-specific-data-types.html %}

---
{% include misc/data-files.html %}