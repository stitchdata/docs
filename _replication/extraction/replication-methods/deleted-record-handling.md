---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Deleted Record Handling
permalink: /replication/extractions/deleted-record-handling
redirect_from: /replication/deleted-record-handling
keywords: deletes, delete, hard delete, soft delete, deletion
summary: "Stitch's detection of deleted records depends on how records are deleted in the source and the Replication Method being used. In this guide, we explain the different deletion methods and how each one works with each of Stitch's supported Replication Methods."

key: "deleted-record-handling"
category: "extraction"
content-type: "replication-methods"

layout: general
toc: true
weight: 7


# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  Depending on the [Replication Method]({{ link.replication.rep-methods | prepend: site.baseurl }}) being used and how records are deleted in the source, deletes may not be captured during the replication process.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary | flatify }}](#{{ section.anchor }})
  {% endfor %}


# --------------------------- #
#       CONTENT SECTIONS      #
# --------------------------- #

sections:
  - title: "Deletion methods"
    anchor: "deletion-methods"
    summary: "The types of deletion methods"
    content: |
      There are two methods that can be used to delete a source record:

      - **Soft deletes**, which will leave a record in the source and use a flag to indicate deletion, such as `is_deleted` or `deleted_on`. If the delete event updates the record's Replication Key value, Stitch will detect and replicate the changes.
      - **Hard deletes**, which completely remove records from the source. It's as if the record never existed. If using Key-based Incremental Replication, this will remove the record's Replication Key value, which Stitch uses to identify new and updated records. Without a Replication Key value to check, Stitch can't identify the change and update the record in the destination.

    subsections:
      - title: "Delete support overview"
        anchor: "delete-support-overview"
        content: |
          {% assign data-about = site.data.taps.extraction.replication-methods %}
          {% assign replication-methods = "full-table|key-based-incremental|log-based-incremental" | split: "|" %}
          {% assign attributes = "display-name|soft-deletes|hard-deletes" | split:"|" %}
          {% include misc/icons.html %}

          In the table below are each of Stitch's Replication Methods and the level at which each deletion method is supported.

          Click the Replication Method name to check out examples of how each deletion method works with that specific Replication Method.

          <table class="attribute-list">
          <tr>
          {% for attribute in attributes %}
          {% if forloop.first == true %}
          <td class="attribute-name">
          <strong>Replication Method</strong>
          {% else %}
          <td>
          <strong>{{ attribute | replace:"-"," " | capitalize }}</strong>
          {% endif %}
          </td>
          {% endfor %}
          </tr>
          {% for replication-method in replication-methods %}
          <tr>
          <td class="attribute-name">
          <a href="#{{ data-about[replication-method]name }}">
          {{ data-about[replication-method]display-name }}
          </a>
          </td>
          {% for attribute in attributes %}
          {% if attribute != "display-name" %}
          <td width="35%; fixed">
          {{ data-about[replication-method][attribute]icon | flatify }}
          <strong>{{ data-about[replication-method][attribute]support | replace:"-"," " | capitalize }}</strong><br><br>

          {{ data-about[replication-method][attribute]destination | flatify | markdownify }}
          </td>
          {% endif %}
          {% endfor %}
          </tr>
          {% endfor %}
          </table>

  - title: "Full Table Replication"
    anchor: "full-table"
    summary: &examples "Examples of deleted records with {{ section.title }}"
    content: |
      {% include replication/deleted-record-examples.html replication-method="full-table" display-name="Full Table" %}

  - title: "Key-based Incremental Replication"
    anchor: "key-based-incremental"
    summary: *examples
    content: |
      {% include replication/deleted-record-examples.html replication-method="key-based-incremental" display-name="Key-based Incremental" %}

  - title: "Log-based Incremental Replication"
    anchor: "log-based-incremental"
    summary: *examples
    content: |
      {% include replication/deleted-record-examples.html replication-method="log-based-incremental" display-name="Log-based Incremental" %}
---
{% include misc/data-files.html %}