---
title: Google BigQuery (v2) Data Loading Reference
permalink: /replication/reference/google-bigquery
redirect_from: /data-structure/bigquery-data-loading-behavior

layout: general
keywords: bigquery, google bigquery data warehouse, bigquery data warehouse, bigquery etl, etl to bigquery
summary: "Learn how Stitch will load data from your integrations into version 2 of Stitch's Google BigQuery destination."

key: "bigquery-loading-reference"

connection-type: "destination"
display_name: "BigQuery"
type: "bigquery"

this-version: "2"

intro: |
  {{ page_name }}
  {% capture version-notice %}
  **Note**: This guide is specific to **version 2** of the Google BigQuery destination. For info about data loading for version 1, refer to [version 1 of this guide]({{ link.destinations.loading.bigquery-v1 | prepend: site.baseurl }}).
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
    anchor: "replication-keys-scenarios"
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
    anchor: "table-scenarios"
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