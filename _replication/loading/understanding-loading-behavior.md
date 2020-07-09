---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Understanding Loading Behavior
permalink: /replication/loading/understanding-loading-behavior
keywords: loading behavior, loading, append, append-only, upsert, insert. truncate
summary: "Learn about the methods Stitch uses to load data into your destination and what the impact will be on your destination tables."

key: "understanding-loading-behavior"
type: "loading-basics"

layout: general
toc: true
order: 1
content-type: "guide"


# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  {{ page.summary }}

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#          CONTENT           #
# -------------------------- #

sections:
  - title: "Loading behavior types"
    anchor: "loading-behavior-types"
    summary: "The loading behavior types Stitch supports"
    content: |
      When data is loaded into your destination, Stitch will use one of the following loading behavior types:

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
# This data is kept in _data/tooltips.yml
      - title: "Upsert"
        anchor: "loading-behavior-types--upsert"
        content: |
          {{ site.data.tooltips.upsert }}

      - title: "Append-Only"
        anchor: "loading-behavior-types--append-only"
        content: |
          {{ site.data.tooltips.append-only }}

  - title: "Determining loading behavior"
    anchor: "loading-behavior-determined"
    summary: "How loading behavior is determined"
    content: |
      At a high level, loading behavior is determined by the following:

      - The destination's support for Upsert loading
      - The presence of Primary Keys in the source data and destination
      - The integration or table has pre-configured loading behavior

    subsections:
      - title: "Upsert loading"
        anchor: "upsert-loading-conditions"
        content: |
          Upsert loading is used when **all** of the following conditions are met:

          1. The destination supports or is configured to use Upsert loading, **and**
          2. The data has defined Primary Keys in the source **and** destination, **and**
          3. The integration or table is not pre-configured to use Append-Only loading

          **Note**: This is applicable to all [Replication Methods]({{ link.replication.rep-methods | prepend: site.baseurl }}).

      - title: "Append-Only loading"
        anchor: "append-only-conditions"
        content: |
          Append-Only loading is used when **any** of the following conditions are met:

          - The destination only supports or is configured to use Append-Only loading, **or**
          - The data doesn't have defined Primary Keys in the source **or** destination, **or**
          - The integration or table is pre-configured to use Append-Only loading

  - title: "Examples"
    anchor: "examples"
    summary: "Examples of each loading behavior type"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Upsert loading example"
        anchor: "example--upsert-loading"
        summary: "Upsert loading"
        content: |
          In this example:

          1. The destination supports **or** is configured to use Upsert loading, and
          2. The data has defined Primary Keys in the source and destination, and
          3. The integration or table being loaded is not pre-configured to use Append-Only loading

          {% include layout/image.html enlarge=true file="/replication/upsert-loading-example.png" alt="Click to enlarge: Upsert loading example" %}

      - title: "Append-Only example"
        anchor: "example--append-only-loading"
        summary: "Append-Only examples"
        content: |
          This example is applicable **any** of the following are true:

          - The destination only supports **or** is configured to use Append-Only loading, **or**
          - The integration or table being loaded is pre-configured to use Append-Only loading, **or**
          - The source data has defined Primary Keys, but the table in the destination doesn't. For example: Primary Key table comments are removed from a table in Amazon Redshift.

          {% include layout/image.html enlarge=true file="/replication/append-only-loading.png" alt="Click to enlarge: Append-Only loading example" %}

      - title: "Append-Only loading, no defined source Primary keys"
        anchor: "example--append-only--no-primary-keys"
        content: |
          This example is applicable when the source data doesn't have a defined Primary Key.

          When source data that doesn't have a Primary Key is replicated, Stitch appends an `{{ system-column.primary-key }}` to the data to function as a Primary Key. Data will be loaded using Append-Only loading, regardless of what loading behavior the destination supports or is configured to use.

          {% include layout/image.html enlarge=true file="/replication/append-only-no-primary-key.png" alt="Click to enlarge: Append-Only loading as a result of no defined Primary Keys" %}

  - title: "Reference"
    anchor: "reference"
    summary: "References lists for destinations, integrations, and loading behavior"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Destinations and default loading behavior"
        anchor: "reference--destinations-loading-behavior"
        content: |
          {% include misc/icons.html %}

          **Note**: If a destination supports and is configured to use Upsert loading, Stitch will attempt to use Upsert loading before Append-Only. All [other conditions for Upsert loading](#upsert-loading-conditions) must also be met.

          {% assign attributes = "Destination|Version|Default loading behavior|Loading behavior is configurable?" | split:"|" %}

          {% assign destinations = site.destinations | where:"destination",true | sort:"display_name" %}

          <table class="attribute-list">
          <tr>
          {% for attribute in attributes %}
          {% if forloop.first == true %}
          <td align="right">
          {% else %}
          <td>
          {% endif %}
          <strong>{{ attribute }}</strong>
          </td>
          {% endfor %}
          </tr>
          {% for destination in destinations %}
          {% assign version = destination.this-version | prepend: "v" %}
          <tr>
          <td align="right">
          {{ destination.display_name }}
          </td>
          <td width="15%; fixed">
          {{ version }}
          </td>
          <td width="20%; fixed">
          {{ site.data.destinations[destination.type][version]replication.default-loading-behavior }}
          </td>
          <td width="25%; fixed">
          {% case site.data.destinations[destination.type][version]replication.configurable-loading-behavior %}
          {% when true %}
          {{ supported | replace:"TOOLTIP","Loading behavior is configurable for this destination and version." }}
          {% when false %}
          {{ not-supported | replace:"TOOLTIP","Loading behavior is not configurable for this destination and version." }}
          {% endcase %}
          </td>
          </tr>
          {% endfor %}
          </table>

      - title: "Append-Only integrations and tables"
        anchor: "reference--append-only-integrations"
        content: |
          {% assign all-integrations = site.documents | where:"input",true %}
          {% assign append-only-integrations = all-integrations | where:"append-only-integration",true %}
          {% assign append-only-tables = all-integrations | where:"append-only-tables",true %}

          {% assign all-append-only = append-only-integrations | concat: append-only-tables | sort:"display_name" %}

          {% assign attributes = "Integration|Version|Notes" | split:"|" %}

          The integrations listed below are pre-configured to use Append-Only loading for all or some tables.

          <table class="attribute-list">
          <tr>
          {% for attribute in attributes %}
          {% if forloop.first == true %}
          <td align="right" width="40%; fixed">
          {% else %}
          <td>
          {% endif %}
          <strong>{{ attribute }}</strong>
          </td>
          {% endfor %}
          </tr>
          {% for integration in all-append-only %}
          <tr>
          <td align="right">
          {{ integration.display_name }}
          </td>
          <td width="15%; fixed">
          {{ integration.this-version | prepend: "v" }}
          </td>
          <td>
          {% if integration.append-only-integration == true %}
          All tables use Append-Only loading
          {% endif %}
          {% if integration.append-only-tables == true %}
          {{ integration.append-only-tables-description }}
          {% endif %}
          </td>
          </tr>
          {% endfor %}
          </table>
---