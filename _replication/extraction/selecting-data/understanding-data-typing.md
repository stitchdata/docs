---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Understanding Data Typing in Stitch
permalink: /replication/understanding-data-typing
redirect_from: 
  - /replication/data-typing
  - /replication/supported-data-types
keywords: supported data types, data typing, data types, unsupported data types
summary: "Learn about the data typing process Stitch performs during replication, including the types Stitch supports and how data will be loaded into your destination."

key: "data-typing"

layout: general
content-type: "select-data, preparing"
toc: true
weight: 4


# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  {% assign data-types = site.data.taps.extraction.data-types %}

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#          CONTENT           #
# -------------------------- #

sections:
  - title: "How data types are determined"
    summary: "How data types are determined"
    anchor: "determining-data-types-during-extraction"
    example-table:
      - name: "id"
        source-type: "uuid"
        stitch-type: "string"
        destination-type: "nvarchar"

      - name: "name"
        source-type: "varchar"
        stitch-type: "string"
        destination-type: "nvarchar"

      - name: "is_active"
        source-type: "boolean"
        stitch-type: "boolean"
        destination-type: "boolean"

      - name: "age"
        source-type: "decimal"
        stitch-type: "number"
        destination-type: "numeric"

      - name: "updated_at"
        source-type: "timestamp"
        stitch-type: "date"
        destination-type: "timestamp"
    content: |
      Stitch's data typing process consists of three steps which take place during replication:

      1. **Extraction**: Identify the data type in the source. The data type must be [supported by Stitch](#supported-source-data-types--reference) to replicate successfully.
      2. **Preparing**: Map the data type to a [Stitch data type](#stitch-data-types--reference)
      3. **Loading**: Convert the Stitch data type to a [destination-compatible data type](#destination-data-types--reference). **Note**: Stitch converts data types only where needed to ensure the data is accepted by your destination.

      Let's take a look at an example of a table from a PostgreSQL database being replicated and loaded into a Microsoft Azure Synapse Analytics destination.

    subsections:
      - title: "Extraction: Identify the source data type"
        anchor: "determining-data-types-during-extraction--extraction"
        content: |
          {% include note.html type="single-line" content="**Note**: Some source data types used in this example are only supported for PostgreSQL integrations." %}

          The first step of the Extraction phase is called **Discovery**, which is sometimes called a structure sync. During Discovery, Stitch examines the structure of your data, including the data types of available columns.

          During this phase, Stitch detects a table with the following structure in a PostgreSQL database integration:

          <table style="font-size: 14px;">
          <tr>
          <td align="right" width="15%; fixed">
          <strong>Column name</strong>
          </td>
          <td>
          <strong>Extraction: Source data type</strong>
          </td>
          </tr>
          {% for column in section.example-table %}
          <tr>
          <td align="right">
          {{ column.name }}
          </td>
          <td>
          {{ column.source-type | upcase }}
          </td>
          </tr>
          {% endfor %}
          </table>

      - title: "Preparing: Map the data types to Stitch data types"
        anchor: "determining-data-types-during-extraction--preparing"
        content: |
          During the **Preparing** phase of replication, Stitch performs some [light transformations]({{ link.getting-started.basic-concepts | prepend: site.baseurl | append: "#transformations" }}) - including data typing - to ensure the data is compatible with your destination.

          During this phase, Stitch maps the source data types to the following Stitch data types:

          <table style="font-size: 14px;">
          <tr>
          <td align="right" width="15%; fixed">
          <strong>Column name</strong>
          </td>
          <td width="26%; fixed">
          <strong>Extraction: Source data type</strong>
          </td>
          <td>
          <strong>Preparing: Stitch data type</strong>
          </td>
          </tr>
          {% for column in section.example-table %}
          <tr>
          <td align="right">
          {{ column.name }}
          </td>
          <td>
          {{ column.source-type | upcase }}
          </td>
          <td>
          {{ column.stitch-type | upcase }}
          </td>
          </tr>
          {% endfor %}
          </table>

          Refer to the [Supported source data types and Stitch data type mappings reference](#supported-source-data-types--reference) for more info about supported source data types and the Stitch types they will map to.

      - title: "Loading: Convert to destination-compatible data types"
        anchor: "determining-data-types-during-extraction--loading"
        content: |
          {% assign microsoft-azure-data-type = site.data.destinations.microsoft-azure.v1.data-types %}

          During the **Loading** phase of replication, Stitch will convert the Stitch data types to a data type compatible with your destination, if necessary.

          This example will use **Microsoft Azure Synapse Analytics** as the destination. During this phase, Stitch converts the Stitch data types to Microsoft Azure Synapse Analytics-compatible data types:

          <table style="font-size: 14px;">
          <tr>
          <td align="right" width="15%; fixed">
          <strong>Column name</strong>
          </td>
          <td width="26%; fixed">
          <strong>Extraction: Source data type</strong>
          </td>
          <td width="25%; fixed">
          <strong>Preparing: Stitch data type</strong>
          </td>
          <td>
          <strong>Loading: Destination data type</strong>
          </td>
          </tr>
          {% for column in section.example-table %}
          <tr>
          <td align="right">
          {{ column.name }}
          </td>
          <td>
          {{ column.source-type | upcase }}
          </td>
          <td>
          {{ column.stitch-type | upcase }}
          </td>
          <td>
          {{ microsoft-azure-data-type[column.stitch-type]destination-type | upcase }}
          </td>
          </tr>
          {% endfor %}
          </table>

          Refer to the [Destination data types reference](#destination-data-types--reference) for more info about data typing for each destination type.

  - title: "Altering destination table structures"
    summary: "When destination tables might be altered to accommodate data types"
    anchor: "data-type-differences-source-destination"
    content: |
      As previously mentioned, Stitch will only convert data types where needed to ensure data is accepted by your destination.

      Occasionally, Stitch may need to alter the structure of the destination table to accommodate these conversions. For example: Accommodating `VARCHAR` columns of varying widths or a column containing multiple data types.

      Refer to the [Understanding table structural changes guide]({{ link.destinations.storage.structure-changes | prepend: site.baseurl }})  for more info and examples.

  - title: "Handling unsupported data types"
    summary: "How Stitch handles unsupported data types"
    anchor: "unsupported-columns-data-types"
    content: |
      If a column you want to replicate has a Status of `Not Supported`, the root cause may be an [unsupported data type or insufficient user permissions]({{ link.troubleshooting.unsupported-data-types | prepend: site.baseurl }}).

      Additionally, columns set to replicate that contain unsupported data types may prevent an entire table from replicating. 

      If you determine a non-replicating column contains an unsupported data type, you'll need to de-select it to allow the table to successfully replicate.

  - title: "Reference"
    summary: "References for supported, Stitch, and destination data types"
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

      - title: "Supported source data types and Stitch data type mappings"
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
          - title: "Common integration data types"
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