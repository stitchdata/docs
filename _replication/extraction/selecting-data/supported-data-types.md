---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Understanding Data Typing in Stitch
permalink: /replication/extractions/understanding-data-typing
redirect_from: 
  - /replication/data-typing
  - /replication/supported-data-types
keywords: supported data types, data typing, data types, unsupported data types
summary: "Learn about the data types Stitch supports and how data is typed when loaded into your destination."

key: "data-typing"

layout: general
content-type: "select-data"
toc: true
weight: 4


# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  {% assign data-types = site.data.taps.extraction.data-types %}


# -------------------------- #
#          CONTENT           #
# -------------------------- #

sections:
  - title: "How data types are determined"
    anchor: "determining-data-types-during-extraction"
    content: |
      Stitch's data typing process consists of three steps which take place during replication:

      1. **Extraction**: Identify the data type in the source. The data type must be [supported by Stitch](#supported-source-data-types--reference) to replicate successfully.
      2. **Preparing**: Map the data type to a Stitch data type
      3. **Loading**: Convert the Stitch data type to a destination-compatible data type

      Stitch converts data types only where needed to ensure the data is accepted by your destination.

  - title: "Data type differences between source and destination"
    anchor: "data-type-differences-source-destination"
    content: |
      todo

    subsections:
      - title: "Columns with mixed data types"
        anchor: "columns-mixed-data-types"
        content: |
          Occasionally Stitch will encounter a column that contains more than one data type. As Stitch requires that there be only one data type per column to properly type and store your data, columns containing multiple data types may be "split" to ensure all values are correctly typed.

          For example: an `order_confirmed` column is synced and typed as `BOOLEAN`. In a subsequent sync, Stitch detects `VARCHAR` values in this column.

          As a result, Stitch will create an additional column to accommodate the `VARCHAR` values. The new column name will be the original name appended with the data type: `order_confirmed__string`

          How columns are named depends on the type of destination being used to warehouse data. Refer to the [Mixed Data Types guide for more info]({{ link.destinations.storage.column-splitting | prepend: site.baseurl }}).

  - title: "Unsupported columns and data types"
    anchor: ""
    content: |
      Columns containing data types that aren't supported may prevent an entire table from replicating. 

      If you determine a non-replicating column contains an unsupported data type, you'll need to de-select it to allow the table to successfully replicate.

      If a column you want to sync has a Status of `Not Supported`, the root cause may be an [unsupported data type or insufficient user permissions]({{ link.troubleshooting.unsupported-data-types | prepend: site.baseurl }}).

  - title: "Reference"
    anchor: "reference"
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Stitch data types"
        anchor: "stitch-data-types--reference"
        content: |
          During the **Preparing** phase of a replication job, Stitch will map the [source data type](#supported-source-data-types--reference) to one of the following data types:

          {% for stitch-type in data-types.stitch-types %}
          - `{{ stitch-type.name | upcase }}`
          {% endfor %}

      - title: "Supported source data types"
        anchor: "supported-source-data-types--reference"
        content: |
          {% include note.html type="single-line" content="**Note**: If a data type isn't listed in this section, replication isn't currently supported for that data type. Replicating columns with [unsupported data types may lead to issues with replication](#sync-unsupported-data-types)." %}

          This section contains the source data types Stitch supports and the data type Stitch will map the source type to during the **Preparing** phase:

          - [Data types supported for all integrations](#supported-source-data-types--reference-common)
          {% assign integrations-with-specific-types = site.documents | where:"has-specific-data-types",true | sort:"display_name" %}
          {% for integration in integrations-with-specific-types %}
          - [{{ integration.display_name }} integration-specific types](#supported-source-data-types--reference-{{ integration.db-type }})
          {% endfor %}

        sub-subsections:
          - title: "Common integration types"
            anchor: "supported-source-data-types--reference-common"
            content: |
              The following data types are supported for all integrations:

              {% assign common-types = data-types.source-types.all-supported | sort:"name" %}
              <table>
                <tr>
                  <td class="attribute-name">
                    <strong>Source data type</strong>
                  </td>
                  <td>
                    <strong>Stitch data type</strong>
                  </td>
                </tr>
                {% for type in common-types %} 
                  <tr>
                    <td class="attribute-name">
                      {{ type.name | upcase }}
                    </td>
                    <td>
                      {{ type.stitch-type | upcase }}
                    </td>
                  </tr>
                {% endfor %}
              </table>

              [Back to Stitch data types](##stitch-data-types--reference)<br>[Back to Supported source data types](#supported-source-data-types--reference)<br>[Forward to Destination data types](#destination-data-types--reference)

              {% for integration in integrations-with-specific-types %}
              #### {{ integration.display_name }} integration-specific types {#supported-source-data-types--reference-{{ integration.db-type }}}

              In addition to the [common data types](#supported-source-data-types--reference-common), {{ integration.display_name }} integrations also support the following data types:

              {% assign latest-version = site.data.taps.versions[integration.db-type]latest-version | prepend: "v" %}
              {% assign specific-types = data-types[integration.db-type]specific | sort:"name" %}

              <table>
                <tr>
                  <td class="attribute-name">
                    <strong>Source data type</strong>
                  </td>
                  <td>
                    <strong>Stitch data type</strong>
                  </td>
                </tr>
                {% for type in specific-types %}
                  {% unless data-types[integration.db-type][latest-version][type.name]stitch-type == "unsupported" %}
                  <tr>
                    <td class="attribute-name">
                      {{ type.name | upcase }}
                    </td>
                    <td>
                      {{ data-types[integration.db-type][latest-version][type.name]stitch-type | upcase }}
                    </td>
                  </tr>
                  {% endunless %}
                {% endfor %}
              </table>

              [Back to Stitch data types](##stitch-data-types--reference)<br>[Back to Supported source data types](#supported-source-data-types--reference)<br>[Forward to Destination data types](#destination-data-types--reference)
              {% endfor %}

      - title: "Destination data types"
        anchor: "destination-data-types--reference"
        content: |
          Stitch converts data types only where needed to ensure the data is accepted by your destination. Refer to the guides linked below to learn about the data types your destination supports and the Stitch type each destination type will map to.

          {% assign destinations = site.destinations | where:"destination",true | sort:"display_name" %}
          {% for destination in destinations %}
          
          {% assign latest-version = site.data.destinations[destination.type]versions.latest-version %}
          {% if destination.this-version == latest-version %}
          {% assign version = latest-version | prepend: "v" %}
          
          {% if site.data.destinations[destination.type][version]data-types %}

          {% assign page-key = destination.name | append: "-reference" %}
          {% assign destination-references = site.destinations | where:"key",page-key %}
          {% assign destination-reference = destination-references | where:"this-version",latest-version | first %}

          - [{{ destination.display_name }} ({{ version }})]({{ destination-reference.url | prepend: site.baseurl | append: "#transformations--data-typing" }})
          {% endif %}
          
          {% endif %}
          {% endfor %}

          [Back to Stitch data types](##stitch-data-types--reference)<br>[Back to Supported source data types](#supported-source-data-types--reference)
---
{% include misc/data-files.html %}