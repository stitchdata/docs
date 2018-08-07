---
title: PostgreSQL
keywords: postgresql, postgres, database integration, etl postgres, postgres etl, postgresql etl, etl
tags: [database_integrations]
permalink: /integrations/databases/postgresql
summary: ""
layout: general
input: false

microsites:
  - title: "{{ page.display_name }} to Postgres"
    url: "http://postgres.topostgres.com/"

show-in-menus: true
has-versions: true

db-type: "postgres"
name: "postgres"
display_name: "PostgreSQL"

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
      {% include notifications/postgres-binlog-limitations.html %}

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