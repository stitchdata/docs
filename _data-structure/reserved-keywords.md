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
key: "reserved-words"

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
          Stitch [reserves its own keywords](#stitch-reserved-keywords) to ensure your data is loaded accurately.

          Additionally, each destination has [its own list of reserved keywords](#destination-reserved-keywords) and its own reasons for reserving those words.

      - title: "What happens to data that contains reserved keywords?"
        anchor: "data-containing-reserved-keywords"
        content: |
          If a table or column contains a reserved keyword, the destination will reject the data and create a record in the [rejected records log]({{ link.destinations.storage.rejected-records | prepend: site.baseurl }}).

  - title: "Reserved keyword reference"
    anchor: "reserved-keyword-reference"
    summary: "The keywords reserved by Stitch and its destinations"
    content: |
      In Stitch, there are two types of keywords:

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }}): {{ subsection.summary }}
      {% endfor %}

    subsections:
      - title: "Stitch reserved keywords"
        anchor: "stitch-reserved-keywords"
        summary: "Keywords reserved by Stitch"
        content: |
          {% assign destinations = site.destinations | where:"destination",true | sort:"title" %}

          The following table provides the list of reserved keywords in Stitch, the reason, and the destination(s) the keyword applies to.

          **Note**: Keywords are **case-insensitive**. This means that `ABC`, `aBc`, `abc`, etc. are all considered the same.

          <table class="attribute-list">
          <tr>
          <td align="right" width="15%; fixed">
          <strong>
          Keyword
          </strong>
          </td>
          <td>
          <strong>
          Comment
          </strong>
          </td>
          <td width="35%; fixed">
          <strong>
          Applies to
          </strong>
          </td>
          </tr>
          {% assign reserved-keywords = stitch.reserved-keywords %}
          {% for keyword in reserved-keywords %}
          <tr>
          <td align="right">
          <strong>{{ keyword.name | flatify | upcase }}</strong>
          </td>
          <td>
          {{ keyword.description | flatify | markdownify }}
          </td>

          <td>
          {% if keyword.applies-to %}
          <ul>
          {% for destination in destinations %}
          {% if keyword.applies-to contains destination.type %}
          <li style="margin: 0px;">{{ destination.title | remove: " Destination" }}</li>
          {% endif %}
          {% endfor %}
          </ul>

          {% else %}
          All destinations
          {% endif %}

          </td>
          </tr>
          {% endfor %}
          </table>

      - title: "Destination reserved keywords"
        anchor: "destination-reserved-keywords"
        summary: "Keywords reserved by the destination"
        content: |
          In addition to the keywords Stitch reserves, each destination also has its own list of reserved or limited keywords. For more info, including a list of reserved keywords, refer to your destination's official documentation: 

          {% for destination in destinations %}
          {% if site.data.destinations.resource-links[destination.type]reserved-words %}
          - [{{ destination.title | remove: " Destination" }}]({{ site.data.destinations.resource-links[destination.type]reserved-words }}){:target="new"}
          {% endif %}
          {% endfor %}
---
{% include misc/data-files.html %}