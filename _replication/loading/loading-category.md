---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Loading Data
permalink: /replication/loading
redirect_from: /data-structure/
keywords: data structure, schema, data load, loading data
summary: "Resources for learning about how Stitch loads and organizes data into your destination."

key: "loading-data-category"
content-type: "category-page"
display-title: "All Loading guides"

layout: general
toc: false
feedback: false


# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  {% assign this-collection = site.replication %}

  {{ page.summary }}

  {% for section in page.sections %}
  - [{{ section.title }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#          CONTENT           #
# -------------------------- #

sections:
  - title: "Understanding loading behavior"
    anchor: "understand-loading-behavior-category"
    additional-guides:
      - title: "Monitoring Loading Progress"
        url: "{{ link.replication.loading-reports }}"
        weight: 1
    content: |
      Understand the basics of how Stitch loads data in these starter guides.

      {% assign guides = this-collection | where_exp:"guide","guide.type contains 'loading-basics'" | concat: section.additional-guides | sort:"weight" %}

      {% include layout/category-section-tiles.html %}

  - title: "Interacting with your data"
    anchor: "interacting-with-your-data-category"
    additional-guides:
      - title: "Exploring Analysis Tools"
        url: "{{ link.analysis-tools.main }}"
        weight: 1

      - title: "Identifying and Resolving Record Rejections"
        url: "{{ link.destinations.storage.rejected-records }}"
        weight: 2

      - title: "Understanding the Primary Keys Table"
        url: "{{ link.destinations.storage.rejected-records }}"
        weight: 3

      - title: "Querying Append-Only Tables"
        url: "{{ link.replication.append-only-querying }}"
        weight: 4
    content: |
      Resources and tutorials for interacting with data loaded by Stitch into your destination.

      {% assign guides = section.additional-guides | sort:"weight" %}
      {% include layout/category-section-tiles.html %}

  - title: "Stitch system columns and tables"
    anchor: "stitch-system-columns-tables-category"
    content: |
      Learn about the system columns, tables, and reserved keywords Stitch uses to load data.

      {% assign guides = this-collection | where_exp:"guide","guide.type contains 'system'" | sort:"weight" %}

      {% include layout/category-section-tiles.html %}

  - title: "Destination loading references"
    anchor: "destination-loading-references-category"
    content: |
      Every destination handles data differently. Learn about what your destination supports, what it doesn't, and how Stitch will load your data as a result in these detailed references.

      {% assign guides = this-collection | where:"content-type","loading-reference" | sort: "display_name" %}

      {% include layout/category-section-tiles.html %}
---
{% include misc/data-files.html %}