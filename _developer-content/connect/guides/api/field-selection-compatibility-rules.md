---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Field Selection and Compatibility Rules
doc-type: "concept"

type: "connect"
content-type: "connect-guide"
content-id: "field-selection-compatibility-rules"
layout: general
sidebar: on-page

permalink: /stitch-connect/guides/field-selection-compatibility-rules
icon: file
order: 4

toc: false
summary: false
feedback: false

summary: "To ensure compatibility and that the fields Stitch requires for replication are included in selected streams, Stitch enforces field selection and compatibility rules. Learn about the metadata types that control field inclusion in the Connect API."
## This is used only on the /stitch-connect/guides page.
description: "Learn about the rules and metadata types that control field inclusion."


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Connect API reference"
    link: "{{ link.connect.api | prepend: site.baseurl }}"

  - title: "Select streams and fields with the Connect API"
    link: "{{ link.connect.guides.select-streams-and-fields | prepend: site.baseurl }}"

  - title: "Connect guides"
    link: "{{ link.connect.guides.category | prepend: site.baseurl }}"

  - title: "Key-based Incremental Replication"
    link: "{{ link.replication.key-based-incremental | prepend: site.baseurl }}"

  - title: "Replication Keys"
    linK: "{{ link.replication.rep-keys | prepend: site.baseurl }}"


# -------------------------- #
#         GUIDE INTRO        #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}
  {% include misc/icons.html %}

  {{ page.summary }}


# -------------------------- #
#      CONTENT SECTIONS      #
# -------------------------- #

sections:
  - title: "Field types"
    anchor: "field-types"
    content: |
      Stitch requires two types of fields for stream replication: [Primary Keys](#primary-key-fields) and, when applicable, [Replication Keys](#replication-key-fields).
    subsections:
      - title: "Primary Key fields"
        anchor: "primary-key-fields"
        content: |
          To accurately replicate data for a stream, Stitch requires the Primary Key information for each stream. A Primary Key is a column or set of columns that uniquely define a record.

          Depending on the source and stream type, this is handled one of several ways.

        sub-subsections:
          - title: "Database sources"
            anchor: "primary-key-fields--database-sources"
            content: |
              For database sources, Stitch will typically query the database's information schema to determine the Primary Key fields and then store the list of Primary Key field names as a list in the [stream's metadata]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.data-structures.metadata.stream-level.section }}) `table-key-properties` property:

              ```json
              {{ site.data.connect.code-examples.streams.database-stream | rstrip }}
              ```

          - title: "Database views"
            anchor: "primary-key-fields--database-views"
            content: |
              For database views, the [stream's metadata]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.data-structures.metadata.stream-level.section }})  will contain an `is-view` property with a value of `true`:

              ```json
              {{ site.data.connect.code-examples.streams.database-view | rstrip }}
              ```

              Primary Key information must be provided in the `view-key-properties` metadata property when the stream is selected for replication. 

          - title: "SaaS sources"
            anchor: "primary-key-fields--saas-sources"
            content: |
              For SaaS sources, Primary Keys are typically hard-coded in the Singer tap backing the source. The list of Primary Key field names will be stored as a list in the [stream's metadata]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.data-structures.metadata.stream-level.section }}) `table-key-properties` property:

              ```json
              {{ site.data.connect.code-examples.streams.saas-stream | rstrip }}
              ```


      - title: "Replication Key fields"
        anchor: "replication-key-fields"
        content: |
          If a stream's `replication-method` is `INCREMENTAL`, an appropriate field must be set as the stream's [Replication Key]({{ link.replication.rep-keys | prepend: site.baseurl }}). {{ site.data.tooltips.replication-key | replace:"columns.","columns" }} and are required to use [Key-based Incremental Replication]({{ link.replication.key-based-incremental | prepend: site.baseurl }}).

          Like Primary Keys, this is handled in one of several ways depending on the source type.

        sub-subsections:
          - title: "Database sources"
            anchor: "replication-key-fields--database-sources"
            content: |
              For database sources, a valid Replication Key must be provided using the `replication-key` metadata property when the stream is selected.

              ```json
              {{ site.data.connect.code-examples.streams.database-stream | rstrip }}
              ```

              **Note**: This is also applicable to database views if the stream's `replication-method` is set to `INCREMENTAL`.
              
          - title: "SaaS sources"
            anchor: "replication-key-fields--saas-sources"
            content: |
              For SaaS sources, Replication Keys are hard-coded in the Singer tap backing the source. The list of Replication Key field names will be stored as a list in the [stream's metadata]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.data-structures.metadata.stream-level.section }}) `valid-replication-keys` property:

              ```json
              {{ site.data.connect.code-examples.streams.saas-stream | rstrip }}
              ```

  - title: "Field selection rules"
    anchor: "understand-field-selection-rules"
    content: |
      Stitch requires Primary Key and Replication Key fields in streams to be selected in order to successfully and accurately replicate data.

      To ensure the required fields are included in a stream's field inclusion list, Stitch enforces field selection rules.
    subsections:
      - title: "Metadata in field selection"
        anchor: "metadata-field-selection"
        content: |
          Field selection rules are shaped by three `metadata` fields in a [Field-level Metadata object]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.data-structures.metadata.field-level.section }}):

            <table class="attribute-list">
            {% for field in site.data.connect.field-selection-rules.metadata-fields %}
            <tr>
            <td width="30%; fixed" align="right">
            <strong>{{ field.name }}</strong><br>
            {{ field.type | upcase }}<br>
            {% if field.modifiable == false %}<font color="#cc3399">READ-ONLY</font>{% endif %}
            </td>
            <td class="attribute-description">
            {{ field.description | flatify | markdownify }}
            </td>
            </tr>
            {% endfor %}
            </table>

      - title: "Field selection metadata combinations"
        anchor: "field-selection-metadata-combinations"
        content: |
          Below are the possible combinations of `metadata` field values and whether a field will be selected with the listed settings.

          **Note**: A `*` in the table indicates any possible value (`null`, `true`, or `false`) for the `metadata` field.

          {% assign attributes = "inclusion|selected|selected-by-default|replicated?" | split: "|" %}

          <table class="attribute-list">
          <tr>
          {% for attribute in attributes %}
          {% if forloop.first == true %}
          <td width="30%; fixed" align="right">
          {% else %}
          <td width="20%; fixed">
          {% endif %}
          <strong>{{ attribute }}</strong>
          </td>
          {% endfor %}
          </tr>
          {% for combination in site.data.connect.field-selection-rules.combinations %}
          <tr>
          {% for attribute in attributes %}
          {% assign name = attribute | remove:"?" %}

          {% if forloop.first == true %}
          <td width="30%; fixed" align="right">
          {% else %}
          <td width="20%; fixed">
          {% endif %}

          {% if combination[name] == true %}
          {{ supported | replace:"TOOLTIP","The field will be replicated" }}
          
          {% elsif combination[name] == false %}
          {{ not-supported | replace:"TOOLTIP","The field will not be replicated"}}

          {% else %}
          {{ combination[name] }}

          {% endif %}

          </td>
          {% endfor %}
          </tr>
          {% endfor %}
          </table>

  - title: "Field compatibility rules"
    anchor: "field-compatibility-rules"
    content: |
      While all fields are subject to field selection rules, some fields are also subject to field compatibility rules. This means that certain combinations of fields are not able to be selected together in a single stream.

      These restrictions primarily affect SaaS sources like [Bing Ads]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.data-structures.source-form-properties.section | append: "-bing-ads-object" }}) or [Google AdWords]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.data-structures.source-form-properties.section | append: "-google-adwords-object" }}), and are set by the source.

    subsections:
      - title: "Field exclusion metadata"
        anchor: "field-exclusion-metadata"
        content: |
          If a field is subject to compatibility rules, its [Field-level Metadata object]({{ link.connect.api | prepend: site.baseurl | append: site.data.connect.data-structures.metadata.field-level.section }}) will contain a `fieldExclusion` property. This property contains a list of arrays that correspond to the `breadcrumb` of an incompatible field.

          For example: Below is the field-level metadata for the `DeviceOS` field in the Bing Ads `ad_group_performance_report` stream:

          ```json
          {{ site.data.connect.code-examples.field-metadata.field-exclusion }}
          ```

          This indicates that when the `DeviceOS` field is selected, the fields listed in the `fieldExclusions` property cannot also be selected.

      - title: "Field exclusion violations"
        anchor: "field-exclusion-violations"
        content: |
          The Connect API may allow you to select fields that violate `fieldExclusion` rules, but doing so will likely result in extraction job failures.

          To avoid this scenario, Stitch recommends considering `fieldExclusions` when building your own application.
---