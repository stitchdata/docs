---
title: Heroku PostgreSQL
keywords: heroku, heroku-postgres, database integration, etl heroku, heroku etl
tags: [database_integrations]
permalink: /integrations/databases/heroku
summary: "Connect and replicate data from your Heroku PostgreSQL database using Stitch's Heroku integration."
layout: general
input: false

microsites:
  - title: "{{ page.display_name }} to Postgres"
    url: "http://postgres.topostgres.com/"

show-in-menus: true
has-versions: true

db-type: "postgres"
name: "heroku"
display_name: "Heroku"

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

      {% for subsection in section.subsections %}
      - [{{ subsection.summary }}](#{{ subsection.summary | slugify }})
      {% endfor %}
    subsections:
      - summary: "Supported features"
        content: |
          {% include integrations/templates/versioning/integration-supported-features.html type="version-comparison" feature-type="databases" %}
      
      - title: "Data types"
        anchor: "data-types"
        summary: "Data types"
        content: |
          {% include replication/templates/data-types/integration-specific-data-types.html specific-types=true display-intro=true %}

---
{% include misc/data-files.html %}