---
title: Google BigQuery (v1) Data Loading Reference
permalink: /replication/reference/google-bigquery/v1/

keywords: bigquery, google bigquery data warehouse, bigquery data warehouse, bigquery etl, etl to bigquery
summary: "Learn how Stitch will load data from your integrations into version 2 of Stitch's Google BigQuery destination."

layout: general
content-type: "loading-reference"
key: "bigquery-loading-reference"

display_name: "Google BigQuery"
type: "bigquery"

this-version: "1"

intro: |
  {% capture version-notice %}
  **Note**: This guide is specific to **version 1** of the Google BigQuery destination. For info about data loading for version 2, refer to [version 2 of this guide]({{ link.destinations.loading.bigquery-v2 | prepend: site.baseurl }}).
  {% endcapture %}

  {% include note.html type="single-line" content=version-notice %}

  {{ page.summary }}

  In this guide, we'll cover data loading scenarios involving: 

  {% for section in page.sections %}
  - [{{ section.summary | flatify | remove: "Scenarios involving " | remove: "." | | capitalize | strip }}](#{{ section.anchor }})
  {% endfor %}
  
  {% assign destination-reference = site.data.destinations.bigquery %}

## The data & copy for BigQuery scenarios live here: _data/dataloading/bigquery
## The error messages for BigQuery live here: _data/errors/loading/bigquery.yml
## The data & copy for 'default' scenarios live here: _data/dataloading/scenarios

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