---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Replication
permalink: /replication/
keywords: replication, extraction, extract, loading, load, preparing, replicate, replication job, job
summary: "Resources for configuring and managing data replication for your Stitch integrations."

key: "replication"
content-type: "category-page"

layout: general
feedback: false
toc: false


# -------------------------- #
#       HOME PAGE DATA       #
# -------------------------- #

## Used to display info on the home page as a category tile

level: "category"

icon: "replication"
display-title: "Replication"
display-summary: "Configure replication and learn how data is loaded into your destination."
weight: 5


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
  - title: "Replication basics"
    anchor: "stitch-replication-basics-category"
    content: |
      Stitch's replication process has three steps: Extraction, Preparing, and Loading. Get an overview of Stitch's system and the replication process with these starter guides.

      {% assign system-overview = site.getting-started | where:"key","basic-concepts" %}
      {% assign replication-overview = site.replication | where:"key","replication-overview" %}

      {% assign guides = system-overview | concat: replication-overview %}

      {% include layout/category-section-tiles.html %}

  - title: "Extraction"
    anchor: "extraction-category"
    content: |
      During Extraction, Stitch pulls data from your [integrations]({{ site.baseurl }}/integrations) using the replication settings you define. Learn how Extraction works and what settings are available in these guides.

      {% assign parent-category = this-collection | where:"key","extracting-data-category" | first %}
      {% assign guides = parent-category.sections %}

      {% include layout/category-section-tiles.html subsection=true %}

  - title: "Preparing"
    anchor: "preparing-category"
    content: |
      After data is extracted from an integration, Stitch readies the data for loading in its durable, highly available internal data pipeline. Understand the light transformations Stitch performs to ensure data is compatible with your destination in these guides.

      {% assign parent-category = this-collection | where:"key","preparing-data-category" | first %}
      {% assign guides = parent-category.sections %}

      {% include layout/category-section-tiles.html subsection=true %}

  - title: "Loading"
    anchor: "loading-category"
    content: |
      During Loading, Stitch loads the prepared data into your destination. Learn how data will be structured and how to intereact with it using these resources.

      {% assign parent-category = this-collection | where:"key","loading-data-category" | first %}
      {% assign guides = parent-category.sections %}

      {% include layout/category-section-tiles.html subsection=true %}

  - title: "Monitoring progress"
    anchor: "monitoring-progress-category"
    content: |
      Learn more about monitoring the progress of your replication jobs with Stitch's built-in reporting tools.

      {% assign guides = this-collection | where_exp:"guide","guide.content-type contains 'monitoring'" | sort:"weight" %}

      {% include layout/category-section-tiles.html %}
---
{% include misc/data-files.html %}