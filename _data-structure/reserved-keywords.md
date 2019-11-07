---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Stitch and Destination Reserved Keywords
permalink: /data-structure/reserved-keywords
keywords: keywords, reserved words, reserved keywords
summary: "A reference of Stitch and destination-reserved keywords."

layout: general
toc: true

level: "guide"
key: "reserved-keywords"

weight: 7


# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}
  
  A reserved keyword is a word that has a special meaning, and is therefore "reserved from use." Reserved keywords are also known as **reserved identifiers**.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#      CONTENT SECTIONS      #
# -------------------------- #

sections:
  - title: "Reserved keyword basics"
    anchor: "reserved-keyword-basics"
    summary: "Some reserved keyword basics"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "What's a reserved keyword?"
        anchor: "what-is-a-reserved-keyword"
        content: |
          A reserved keyword is a word that has a special meaning, and is therefore "reserved from use." Reserved keywords are also known as **reserved identifiers**.

          In Stitch, there are two types of reserved keywords:

          - **Stitch reserved keywords**, or words that are reserved to Stitch. For example: The `{{ system-column.prefix }}` prefix used in Stitch system tables and columns.
          - **Destination reserved keywords**, or words that are reserved by a destination.

      - title: "Why can't I use reserved keywords?"
        anchor: "why-cant-i-use-reserved-keywords"
        content: |
          Stitch reserves its own keywords to ensure your data is loaded accurately. Additionally, each destination has its own list of reserved keywords and its own reasons for reserving those words.

          Refer to the [Keyword reference section](reserved-keyword-reference) for info about the keywords reserved for each destination.

      - title: "What happens to data that contains reserved keywords?"
        anchor: "data-containing-reserved-keywords"
        content: |
          If a table or column contains a reserved keyword, the destination will reject the data and create a record in the [rejected records log]({{ link.destinations.storage.rejected-records | prepend: site.baseurl }}).

          An error will also surface in the **Notifications** tab in Stitch.

  - title: "Reserved keyword reference"
    anchor: "reserved-keyword-reference"
    summary: "The keywords reserved by Stitch and its destinations"
    content: |
      In this section are the reserved keywords for each destination supported by Stitch.

      **Note**: Keywords are **case-insensitive**. This means that `ABC`, `aBc`, `abc`, etc. are all considered the same.

      {% assign destinations = site.destinations | where:"destination",true | sort:"title" %}

      {% for destination in destinations %}
      {% if stitch.reserved-keywords[destination.type] %}
      - [{{ destination.display_name }}](#{{ destination.type }}-reserved-keywords)
      {% endif %}
      {% endfor %}
      
      {% assign table-attributes = "name|type|description" | split:"|" %}
      {% for destination in destinations %}

      {% if stitch.reserved-keywords[destination.type] %}
      {% assign reserved-keywords = stitch.reserved-keywords[destination.type] | sort:"name" %}

      ### {{ destination.display_name }} reserved keywords {#{{ destination.type }}-reserved-keywords}

      {% if site.data.destinations.resource-links[destination.type]reserved-words %}
      Refer to [{{ destination.title | remove: " Destination" }}'s documentation]({{ site.data.destinations.resource-links[destination.type]reserved-words }}){:target="new"} for the full list of keywords reserved by {{ destination.display_name }}.
      {% endif %}

      <table class="attribute-list">
      <tr>
      {% for attribute in table-attributes %}
      {% if forloop.first == true %}
      <td align="right" width="20%; fixed">
      <strong>
      Keyword

      {% else %}
      <td>
      <strong>
      {{ attribute | capitalize }}
      {% endif %}
      </strong>
      </td>
      {% endfor %}
      </tr>
      {% for keyword in reserved-keywords %}
      <tr>
      <td align="right">
      <strong>{{ keyword.name | flatify | upcase }}</strong>
      </td>
      <td width="15%; fixed">
      {{ keyword.type | capitalize }}
      </td>
      <td>
      {{ keyword.description | flatify | markdownify }}
      </td>
      </tr>
      {% endfor %}
      </table>
      {% endif %}

      {% endfor %}
---
{% include misc/data-files.html %}