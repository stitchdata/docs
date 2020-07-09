---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Snowflake Data Loading Reference
permalink: /replication/loading/reference/snowflake/
redirect_from: 
  - /replication/reference/snowflake/
  - /data-structure/snowflake-data-loading-behavior
keywords: snowflake, snowflake data warehouse, snowflake data warehouse, snowflake etl, etl to snowflake
summary: "Learn how Stitch will load data from your integrations into Stitch's Snowflake destination."

key: "snowflake-loading-reference"

layout: general
content-type: "loading-reference"

display_name: "Snowflake"
type: "snowflake"
this-version: "1"


# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  {{ page.summary }}

  In this guide, we'll cover data loading scenarios involving: 

  {% for section in page.sections %}
  - [{{ section.summary | flatify | remove: "Scenarios involving " | remove: "." | | capitalize | strip }}](#{{ section.anchor }})
  {% endfor %}
  
  {% assign destination-reference = site.data.destinations.snowflake %}

## The data & copy for Snowflake scenarios live here: _data/dataloading/snowflake
## The error messages for Snowflake live here: _data/errors/loading/snowflake.yml
## The data & copy for 'default' scenarios live here: _data/dataloading/scenarios


# -------------------------- #
#          CONTENT           #
# -------------------------- #

sections:
  - title: "Primary Key scenarios"
    anchor: "primary-key-scenarios"
    summary: |
      {{ site.data.dataloading.scenarios.primary-keys.description }}
    content: |
      {% include data-structure/data-loading-tabs.html category="primary-keys"%}

  - title: "Replication Key scenarios"
    anchor: "replication-key-scenarios"
    summary: |
      {{ site.data.dataloading.scenarios.replication-keys.description }}
    content: |
      {% include data-structure/data-loading-tabs.html category="replication-keys" %}

  - title: "Object naming scenarios"
    anchor: "object-name-scenarios"
    summary: |
      {{ site.data.dataloading.scenarios.object-names.description }}
    content: |
      {% include data-structure/data-loading-tabs.html category="object-names" %}

  - title: "Table scenarios"
    anchor: "table-name-scenarios"
    summary: |
      {{ site.data.dataloading.scenarios.tables.description }}
    content: |
      {% include data-structure/data-loading-tabs.html category="tables" %}

  - title: "Data typing scenarios"
    anchor: "data-typing-scenarios"
    summary: |
      {{ site.data.dataloading.scenarios.data-types.description }}
    content: |
      {% include data-structure/data-loading-tabs.html category="data-types" %}

  - title: "Schema change scenarios"
    anchor: "schema-change-scenarios"
    summary: |
      {{ site.data.dataloading.scenarios.schema-changes.description }}
    content: |
      {% include data-structure/data-loading-tabs.html category="schema-changes" %}

  - title: "Destination changes"
    anchor: "destination-change-scenarios"
    summary: |
      {{ site.data.dataloading.scenarios.warehouse-changes.description }}
    content: |
      {% include data-structure/data-loading-tabs.html category="warehouse-changes" %}
---
{% include misc/data-files.html %}
{% assign destination = page %}