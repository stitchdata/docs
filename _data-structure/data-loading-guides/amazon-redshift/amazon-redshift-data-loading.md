---
title: Amazon Redshift Data Loading Reference
permalink: /replication/loading/reference/amazon-redshift/
redirect_from:
  - /data-structure/redshift-data-loading-behavior
  - /data-structure/panoply-data-loading-behavior

layout: general
keywords: redshift, redshift data warehouse, redshift data warehouse, redshift etl, etl to redshift
summary: "Learn how Stitch will load data from your integrations into Stitch's Amazon Redshift destination."

content-type: "loading-reference"
key: "redshift-loading-reference"

display_name: "Amazon Redshift"
type: "redshift"

this-version: "1.0"

intro: |
  {{ page.summary }}

  In this guide, we'll cover data loading scenarios involving: 

  {% for section in page.sections %}
  - [{{ section.summary | flatify | remove: "Scenarios involving " | remove: "." | | capitalize | strip }}](#{{ section.anchor }})
  {% endfor %}
  
  {% assign destination-reference = site.data.destinations.reference.redshift %}

## The data & copy for Amazon Redshift scenarios live here: _data/dataloading/redshift
## The error messages for Amazon Redshift live here: _data/errors/loading/redshift.yml
## The data & copy for 'default' scenarios live here: _data/dataloading/scenarios

sections:
  - title: "Applicable destination types"
    anchor: "applicable-destination-types"
    summary: "The destinations this guide is applicable to"
    content: |
      This guide is applicable to the all variations of the {{ page.display_name }} destination, including:

      - [Amazon Redshift]({{ link.destinations.overviews.redshift | prepend: site.baseurl }})
      - [Panoply]({{ link.destinations.overviews.panoply | prepend: site.baseurl }})

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