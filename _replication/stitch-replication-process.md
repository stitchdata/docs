---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Understanding Stitch's Replication Process
permalink: /replication/stitch-replication-process
keywords: 
summary: "Learn how Stitch extracts, prepares, and loads your data during the replication process."

key: "replication-overview"
category: "extraction, preparing, loading"
content-type: "basics"

layout: general
toc: false
weight: 


# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  {{ page.summary }}

  {% for section in page.sections %}
  - [{{ section.title }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#          CONTENT           #
# -------------------------- #

sections:
  - title: ""
    anchor: ""
    content: |
      The first phase of every Stitch replication job is called **Extraction**. During Extraction, Stitch completes the following: 

      1. Check for changes to the structure of your data, including the addition of new tables and columns.
      2. Query for data according to the integration's replication settings. This includes the [tables and fields you set to replicate]({{ link.replication.syncing | prepend: site.baseurl }}) and the [Replication Methods]({{ link.replication.rep-methods | prepend: site.baseurl }}) used by those tables.
      3. Extract the appropriate data, if any.

---
{% include misc/data-files.html %}