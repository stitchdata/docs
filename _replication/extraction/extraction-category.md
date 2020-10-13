---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Extracting Data
permalink: /replication/extractions
keywords: extraction, extracting data, replication settings, replication job
summary: "Resources for learning about how Stitch extracts data from your integrations."

key: "extracting-data-category"
category: "extraction"
content-type: "category-page"
display-title: "All Extraction guides"

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
  - title: "Understanding Extraction"
    anchor: "understanding-extraction-category"
    content: |
      Learn the basics of data extraction and how to monitor progress in these starter guides.

      {% assign guides = this-collection | where_exp:"guide","guide.content-type contains 'basics'" | sort:"weight" %}

      {% include layout/category-section-tiles.html %}

  - title: "Selecting data"
    anchor: "selecting-data-category"
    content: |
      Learn to select integration tables and columns and how your selections can impact replication overall.

      {% assign guides = this-collection | where_exp:"guide","guide.content-type contains 'select-data'" | sort:"weight" %}

      {% include layout/category-section-tiles.html %}

  - title: "Understanding Replication Methods"
    anchor: "understanding-replication-methods"
    content: |
      Learn about the methods Stitch uses to extract the data you select for replication.

      {% assign guides = this-collection | where_exp:"guide","guide.content-type contains 'replication-methods'" | sort:"weight" %}

      {% include layout/category-section-tiles.html %}

  - title: "Understanding incremental replication"
    anchor: "understanding-incremental-replication"
    content: |
      Dive deeper into Stitch's incremental Replication Methods - [Key-based Incremental]({{ link.replication.key-based-incremental | prepend: site.baseurl }}) and [Log-based Incremental]({{ link.replication.log-based-incremental | prepend: site.baseurl }}) - with these detailed guides.

      {% assign guides = this-collection | where_exp:"guide","guide.content-type contains 'incremental-replication'" | sort:"weight" %}

      {% include layout/category-section-tiles.html %}

  - title: "Scheduling replication jobs"
    anchor: "scheduling-replication-jobs"
    content: |
      Learn how to set the replication schedule for an integration, which defines when and how often Stitch should run replication jobs.

      {% assign guides = this-collection | where_exp:"guide","guide.content-type contains 'replication-scheduling'" | sort:"weight" %}

      {% include layout/category-section-tiles.html %}
---
{% include misc/data-files.html %}