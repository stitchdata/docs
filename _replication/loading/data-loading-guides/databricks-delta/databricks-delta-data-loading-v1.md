---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Databricks Delta Lake on AWS (v1) Data Loading Reference
permalink: /replication/loading/destination-guides/databricks-delta
redirect_from: /replication/reference/databricks-delta
keywords: databricks delta, databricks delta data warehouse, databricks data warehouse, databricks etl, etl to databricks
summary: "Learn how Stitch will load data from your integrations into Stitch's Databricks Delta Lake on AWS destination."

key: "databricks-delta-loading-reference"

layout: general
content-type: "loading-reference"

display_name: "Databricks Delta"
type: "databricks-delta"
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
  
  {% assign destination-reference = site.data.destinations.databricks-delta %}

## The data & copy for Databricks Delta scenarios live here: _data/dataloading/databricks-delta
## The error messages for Databricks Delta live here: _data/destinations/databricks-delta/loading-errors.yml
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