---
title: Stitch Replication
permalink: /replication/
keywords: 
tags: [replication]

summary: "Documentation and guides for configuring and managing data replication for your Stitch integrations."
feedback: false
toc: false

# --------------------------- #
#          CATEGORIES         #
# --------------------------- #

## The sections (topics) this category contains.
## The `id` values are equal to the `content-type`
## values of the docs in this site's collection.

sections:
  - id: "select-data"
    name: "Select data"

  - id: "replication-scheduling"
    name: "Replication Scheduling"

  - id: "replication-methods"
    name: "Replication Methods"

  - id: "replication-keys"
    name: "Replication Keys"

  - id: "replication-progress"
    name: "Replication progress"
---
{% include misc/data-files.html %}

{{ page.summary }}

{% for section in page.sections %}
{% assign all-section-docs = site.replication | where:"content-type",section.id %}

{% for doc in all-section-docs %}
{% if doc.weight == 1 %}
- [**{{ section.name }}**](#{{ section.id }}) - {{ doc.category-summary }}
{% endif %}
{% endfor %}

{% endfor %}

---

{% for section in page.sections %}
{% assign all-section-docs = site.replication | where:"content-type",section.id | sort:"weight" %}

## {{ section.name }} {#{{ section.id }}}

{% for doc in all-section-docs %}
### [{{ doc.title }}]({{ doc.url | prepend: site.baseurl }})

{{ doc.summary }}
{% endfor %}
---
{% endfor %}