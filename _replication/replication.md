---
title: Extracting data
permalink: /replication/
keywords: 
summary: "Documentation and guides for configuring and managing data replication for your Stitch integrations."

feedback: false
toc: false

content-type: "category-page"
key: "replication"

level: "category"

# -------------------------- #
#       HOME PAGE DATA       #
# -------------------------- #

## Used to display info on the home page as a category tile

icon: "replication"
display-title: "Extracting data"
display-summary: "Get the data flowing with Stitch's simple, straightforward replication settings."
weight: 5


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
    description: |
      Replication Methods define the approach Stitch takes when [extracting data](https://www.stitchdata.com/resources/what-is-data-extraction/){:target="new"} from a source during a replication job.

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

{{ section.description | flatify }}

{% for doc in all-section-docs %}
#### [{{ doc.title }}]({{ doc.url | prepend: site.baseurl }})

{{ doc.summary }}
{% endfor %}
{% unless forloop.last == true %}
---
{% endunless %}
{% endfor %}
