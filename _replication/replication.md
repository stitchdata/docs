---
title: Extracting data
permalink: /replication/
keywords: 

content-type: "category-page"

level: "category"
icon: replication
display-title: "Replication"
display-summary: "Manage replication for your integrations."
weight: 5

summary: "Documentation and guides for configuring and managing data replication for your Stitch integrations."
feedback: false
toc: false

key: "replication"

# --------------------------- #
#          CATEGORIES         #
# --------------------------- #

## The sections (topics) this category contains.
## The `id` values are equal to the `content-type`
## values of the docs in this site's collection.

sections:
  - id: "select-data"
    name: "Select data"
    description: "Select the tables and columns you want Stitch to replicate from your integration."

  - id: "replication-scheduling"
    name: "Replication Scheduling"
    description: "Set the replication schedule for an integration, which defines when and how often Stitch should run replication jobs."

  - id: "replication-methods"
    name: "Replication Methods"
    description: "Replication Methods define the approach Stitch takes when extracting data from a source during a replication job."

  - id: "replication-keys"
    name: "Replication Keys"
    description: "Replication Keys are source table columns that Stitch uses to identify new and updated data when using an incremental Replication Method."

  - id: "replication-progress"
    name: "Replication progress"
    description: "Monitor the status of an integration's replication job, including extraction and loading progress."
---
{% include misc/data-files.html %}

{{ page.summary }}

{% for section in page.sections %}
- [**{{ section.name }}**](#{{ section.id | append: "-section" }}) - {{ section.description }}
{% endfor %}

---

{% for section in page.sections %}
{% assign all-section-docs = site.replication | where:"content-type",section.id | sort:"weight" %}

## {{ section.name }} {#{{ section.id | append: "-section" }}}

{{ section.description }}

{% for doc in all-section-docs %}
#### [{{ doc.title }}]({{ doc.url | prepend: site.baseurl }})

{{ doc.summary }}
{% endfor %}
{% unless forloop.last == true %}
---
{% endunless %}
{% endfor %}