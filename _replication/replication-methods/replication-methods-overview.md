---
title: Replication Methods
permalink: /replication/replication-methods/
keywords: replicate, replication, replication method, stitch replicates data
tags: [replication]
layout: general

content-type: "replication-methods"
toc: true
weight: 1

summary: "Replication Methods define the approach Stitch takes when extracting data from a source during a replication job. Additionally, Replication Methods can also impact how data is loaded into your destination and your overall row usage. This guide contains an overview of each method, how it compares to Stitch's other methods, and links to detailed documentation about the method."

# --------------------------- #
#       CONTENT SECTIONS      #
# --------------------------- #

sections:
  - content: |
      {{ page.title }} define the approach Stitch takes when extracting data from a source during a replication job. Additionally, {{ page.title }} can also impact how data is loaded into your destination and your overall row usage.

      {% include important.html type="single-line" content="**Replication Methods are one of the most important settings in Stitch.** Incorrectly defining a table's Replication Method can cause data discrepancies and latency. Before configuring the replication settings for an integration, Stitch recommends reading through the Replication Methods guides so you understand how Stitch will replicate your data." %}

  - title: "Replication Method types"
    anchor: "replication-method-types"
    content: |
      For any table you set to replicate, Stitch will use one of three methods to replicate your data:

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "Log-based Incremental Replication"
        anchor: "log-based-incremental-replication"
        content: |
          {{ site.data.tooltips.log-based-incremental-rep }}

          **Note**: This Replication Method is available only for Microsoft SQL Server, MySQL, Oracle, and PostgreSQL-backed databases that support binary log replication, and requires manual intervention when table structures change. [Learn more about Log-based Incremental Replication here]({{ link.replication.log-based-incremental | prepend: site.baseurl }}).

      - title: "Key-based Incremental Replication"
        anchor: "key-based-incremental-replication"
        content: |
          {{ site.data.tooltips.key-based-incremental-rep }}

          For example: Stitch will use a column like `updated_at` to identify records that have been updated since a specified time, and then only replicate those records.

          If Log-based Incremental Replication isn't feasible or availble for a data source, Key-based Incremental Replication is the next best option. [Learn more about Key-based Incremental Replication here]({{ link.replication.key-based-incremental | prepend: site.baseurl }}).

      - title: "Full Table Replication"
        anchor: "full-table-replication"
        content: |
          {{ site.data.tooltips.full-table-rep }}

          If a table doesn't have a column suitable for Key-based Incremental or if Log-based Incremental is unavailable, this method will be used to replicate data. [Learn more about Full Table Replication here]({{ link.replication.full-table | prepend: site.baseurl }}).

  - title: "Compare Replication Methods"
    anchor: "compare-replication-methods"
    content: |
      The table below contains a high-level look at each of Stitch's Replication Methods and how they compare to each other.

      **Note**: This is not intended as a substitute for the full documentation for each Replication Method. Stitch recommends reading the documentation linked below before selecting a Replication Method, as defining replication incorrectly can lead to data discrepancies, latency, and increased row usage.

      {% assign data-about = site.data.taps.extraction.replication-methods %}
      {% assign replication-methods = "full-table|key-based-incremental|log-based-incremental" | split: "|" %}
      {% assign attributes = "documentation|availability|soft-deletes|hard-deletes|view-support|structural-changes|configuration-requirements" | split:"|" %}

      <table class="attribute-list">
      <tr>
      <td>
      </td>
      {% for replication-method in replication-methods %}
      <td>
      <strong>
      {{ data-about[replication-method]display-name }}
      </strong>
      </td>
      {% endfor %}
      </tr>
      {% for attribute in attributes %}
      <tr>
      <td width="17%; fixed" align="right">
      <strong>{{ attribute | replace:"-","<br>" | capitalize }}</strong>
      </td>
      {% for replication-method in replication-methods %}
      <td width="28%; fixed">
      {% case attribute %}
      {% when 'documentation' %}
      <a href="{{ data-about[replication-method]documentation | flatify }}">Documentation</a>
      {% else %}
      {% if attribute contains "deletes" %}
      <a href="{{ link.replication.deleted-records | prepend: site.baseurl | append: "#" | append: replication-method }}">
      {{ data-about[replication-method][attribute]support | replace:"-"," " | capitalize }}
      </a>
      {% else %}
      {{ data-about[replication-method][attribute] | flatify | markdownify }}
      {% endif %}
      {% endcase %}
      </td>
      {% endfor %}
      </tr>
      {% endfor %}
      </table>

  - title: "Define a table's Replication Method"
    anchor: "define-replication-method-table"
    content: |
      How Replication Methods are defined depends on the type of integration being used:

      - **Database integrations**: Replication Methods are defined by you when tables are set to replicate. A table's Replication Method can be changed at any time in the {{ app.page-names.table-settings }} page.

      - **SaaS integrations**: With the exception of Salesforce, Stitch pre-defines the Replication Methods used for every table set to replicate.

         To learn more about the Replication Methods used by a particular SaaS integration, refer to the **Schema** section in the [integration's documentation]({{ site.baseurl }}/integrations/saas).

      - **Webhook integrations**: Because webhook data is sent to Stitch in real-time, only new records are ever replicated from a webhook source. This can be thought of as using Key-based Incremental Replication with a Replication Key of `created_at`.
---
{% include misc/data-files.html %}