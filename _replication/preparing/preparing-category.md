---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Preparing Data
display-title: "All Preparing guides"

permalink: /replication/preparing
keywords: preparing, preparing data, replication job
summary: "Resources for understanding how Stitch prepares extracted data for loading."

key: "preparing-data-category"
content-type: "category-page"
category: "preparing"

layout: general
feedback: false
toc: false


# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  {% assign this-collection = site.replication | where_exp:"guide","guide.category contains page.category" %}

  {{ page.summary }}

  {% for section in page.sections %}
  - [{{ section.title }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#          CONTENT           #
# -------------------------- #

sections:
  - title: "Understanding Preparing"
    anchor: "understanding-preparing-category"
    content: |
      Learn the basics of data preparation and how to monitor progress in these starter guides.

      {% assign guides = this-collection | where_exp:"guide","guide.content-type contains 'basics'" | sort:"weight" %}

      {% include layout/category-section-tiles.html %}

  - title: "Data typing"
    anchor: "data-typing-category"
    content: |
      To ensure compatibility and successful loading with your destination, Stitch converts data types only when necessary. Use these resources to learn how Stitch determines data types for extracted fields.

      {% assign guides = this-collection | where_exp:"guide","guide.content-type contains 'data-typing'" | sort:"weight" %}

      {% include layout/category-section-tiles.html %}

  - title: "Data structuring"
    anchor: "data-structuring-category"
    content: |
      Each of Stitch's destinations structures data differently. Learn how Stitch prepares extracted data to ensure compatibility for loading in these guides.

      {% assign guides = this-collection | where_exp:"guide","guide.content-type contains 'data-structuring'" | sort:"weight" %}

      {% include layout/category-section-tiles.html %}
---
{% include misc/data-files.html %}