---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: System tables and columns
permalink: /data-structure/system-tables-and-columns
keywords: sdc, _sdc, system columns, system tables
summary: "When data is loaded into your destination, Stitch will create some additional columns and tables. Learn about these system columns and tables and how Stitch uses them."

layout: general
toc: true

level: "guide"
key: "system-tables-and-columns"

weight: 1

# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}

  When data is loaded into your destination, Stitch will create some additional columns and tables. These columns and tables are used not only in the replication process, but to provide additional insight and transparency about your data as it moves through Stitch.
  
  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#      CONTENT SECTIONS      #
# -------------------------- #

sections:
  - title: "System columns"
    anchor: "system-columns"
    summary: "The system columns Stitch creates in destination tables"
    content: |
      When Stitch loads data into a destination table, two types of columns will be created: The columns you set to replicate, and Stitch system columns. Stitch system columns are prepended with `{{ system-column.prefix }}`.

      These columns contain metadata about records as they move through Stitch's replication process, such as when they were extracted from the source or batched for loading.

      The system columns Stitch adds to a table depend on table and integration type. System columns can fall into one of the following categories:

      {% assign sdc-categories = site.data.stitch.sdc-columns.categories %}

      {% for category in sdc-categories %}
      - [{{ category.display-name }}](#{{ category.name | append:"-system-columns" }})
      {% endfor %}

      **Note**: Removing or blocking access to system columns will cause replication issues. Stitch relies on these columns to correctly replicate and load your data.

      {% for category in sdc-categories %}
      ### {{ category.display-name }} {#{{ category.name | append:"-system-columns" }}}

      {{ category.description | flatify }}

      {% assign attribute-list=site.data.stitch.sdc-columns[category.name] %}

      {% include stitch/stitch-system-table.html attribute-list=attribute-list %}
      {% endfor %}

  - title: "System tables"
    anchor: "system-tables"
    summary: "The system tables Stitch creates in integration schemas"
    content: |
      In addition to the `{{ system-column.prefix }}` columns, Stitch will create the following system tables in your destination:

      <table class="attribute-list">
      <tr>
      <td class="attribute-name">
      <strong>Table name</strong>
      </td>
      <td>
      <strong>Description</strong>
      </td>
      </tr>
      {% for table in stitch.system-tables.all-tables %}
      <tr>
      <td class="attribute-name">
      <strong>{{ stitch.system-tables[table.name]name }}</strong>
      </td>
      <td>
      {{ stitch.system-tables[table.name]description | flatify | markdownify }}

      Refer to the <a href="{{ stitch.system-tables[table.name]documentation | flatify }}"><code>{{ stitch.system-tables[table.name]name }}</code></a> documentation for more info and column descriptions.
      </td>
      </tr>
      {% endfor %}
      </table>
---