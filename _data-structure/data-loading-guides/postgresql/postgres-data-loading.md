---
title: PostgreSQL Data Loading Behavior
permalink: /replication/loading/postgresql/
redirect_from: /data-structure/postgresql-data-loading-behavior

layout: general
keywords: postgres, postgres data warehouse, postgres data warehouse, postgres etl, etl to postgres
summary: "Learn how Stitch will load data from your integrations into Stitch's PostgreSQL destination."

display_name: "PostgreSQL"
type: "postgres"

this-version: "1.0"

intro: |
  {{ page.summary }}

  In this guide, we'll cover data loading scenarios involving: 

  {% for section in page.sections %}
  - [{{ section.summary | flatify | remove: "Scenarios involving " | remove: "." | | capitalize | strip }}](#{{ section.anchor }})
  {% endfor %}
  
  {% assign destination-reference = site.data.destinations.reference.postgres %}

## The data & copy for PostgreSQL scenarios live here: _data/dataloading/postgres
## The error messages for PostgreSQL live here: _data/errors/loading/postgres.yml
## The data & copy for 'default' scenarios live here: _data/dataloading/scenarios

sections:
  - title: "Applicable destination types"
    anchor: "applicable-destination-types"
    summary: "The destinations this guide is applicable to"
    content: |
      This guide is applicable to the all variations of the {{ page.display_name }} destination, including:

      {% assign setup-destinations = site.destinations | where:"content-type","destination-setup" %}
      {% assign postgres-destinations = setup-destinations | where:"type","postgres" | sort:"title" %}

      {% for destination in postgres-destinations %}
      - [{{ destination.title | remove: "Connecting an " | remove: "Connecting a " | remove: " Destination to Stitch" }}]({{ destination.url | prepend: site.baseurl }})
      {% endfor %}

  - title: "Primary Key scenarios"
    anchor: "primary-keys"
    summary: |
      {{ site.data.dataloading.scenarios.primary-keys.description }}
    content: |
      {% include data-structure/data-loading-tabs.html category="primary-keys"%}

  - title: "Replication Key scenarios"
    anchor: "replication-keys"
    summary: |
      {{ site.data.dataloading.scenarios.replication-keys.description }}
    content: |
      {% include data-structure/data-loading-tabs.html category="replication-keys" %}

  - title: "Object naming scenarios"
    anchor: "object-names"
    summary: |
      {{ site.data.dataloading.scenarios.object-names.description }}
    content: |
      {% include data-structure/data-loading-tabs.html category="object-names" %}

  - title: "Table scenarios"
    anchor: "tables"
    summary: |
      {{ site.data.dataloading.scenarios.tables.description }}
    content: |
      {% include data-structure/data-loading-tabs.html category="tables" %}

  - title: "Data typing scenarios"
    anchor: "data-typing"
    summary: |
      {{ site.data.dataloading.scenarios.data-types.description }}
    content: |
      {% include data-structure/data-loading-tabs.html category="data-types" %}

  - title: "Schema change scenarios"
    anchor: "schema-changes"
    summary: |
      {{ site.data.dataloading.scenarios.schema-changes.description }}
    content: |
      {% include data-structure/data-loading-tabs.html category="schema-changes" %}

  - title: "Destination changes"
    anchor: "destination-changes"
    summary: |
      {{ site.data.dataloading.scenarios.warehouse-changes.description }}
    content: |
      {% include data-structure/data-loading-tabs.html category="warehouse-changes" %}
---
{% include misc/data-files.html %}
{% assign destination = page %}