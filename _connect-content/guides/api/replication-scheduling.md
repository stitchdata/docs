---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Replication Scheduling for Sources Using the API
doc-type: "concept"
content-type: "connect-guide"
content-id: "replication-scheduling-for-sources"
layout: general
sidebar: on-page

permalink: /stitch-connect/guides/replication-scheduling-for-sources
icon: clock
order: 4

toc: false
summary: false
feedback: false

summary: "Stitch supports three replication scheduling methods: Replication Frequency, Anchor Scheduling, and Advanced Scheduling. Learn about each scheduling type and how to use them in the Connect API."
## This is used only on the /stitch-connect/guides page.
description: "Learn how to use each of Stitch's replication scheduling methods via the API."


# -------------------------- #
#   RELATED SIDEBAR LINKS    #
# -------------------------- #

related:
  - title: "Replication Frequency"
    link: "{{ link.replication.rep-frequency | prepend: site.baseurl }}"

  - title: "Anchor Scheduling"
    link: "{{ link.replication.anchor-scheduling | prepend: site.baseurl }}"

  - title: "Advanced Scheduling using Cron"
    link: "{{ link.replication.advanced-scheduling | prepend: site.baseurl }}"

  - title: "Connect API reference"
    link: "{{ link.connect.api | prepend: site.baseurl }}"

  - title: "Connect guides"
    link: "{{ link.connect.guides.category | prepend: site.baseurl }}"


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

method-comparison-table:
  - scheduling-used: "Replication Frequency"
    frequency-selected: true
    anchor-selected: false
    cron-selected: false

  - scheduling-used: "Anchor Scheduling"
    frequency-selected: true
    anchor-selected: true
    cron-selected: false

  - scheduling-used: "Advanced Scheduling"
    frequency-selected: true
    anchor-selected: false
    cron-selected: true

  - scheduling-used: "Advanced Scheduling"
    frequency-selected: true
    anchor-selected: true
    cron-selected: true



sections:
  - title: "What is replication scheduling?"
    anchor: "what-is-replication-scheduling"
    content: |
      Replication scheduling tells Stitch when and how often data extraction should occur.

      **Note**: All replication scheduling methods (Replication Frequency, Anchor Scheduling, and Advanced Scheduling) define when data extractions begin. They do not control how long a replication job runs or when data is loaded into a destination.

      For a more in-depth look at replication scheduling, refer to the [Replication Scheduling overview]({{ link.replication.rep-scheduling | prepend: site.baseurl }}).

  - title: "Replication scheduling API properties"
    anchor: "replication-scheduling-api-properties"
    content: |
      With a few exceptions, every [source form property]({{ link.connect.api | append: site.data.connect.data-structures.source-form-properties.section | prepend: site.baseurl }}) available in the API contains the following properties:

      {% assign common = site.data.connect.common.all-sources %}
      {% assign properties = common.fields | sort:"order" %}

      <table class="attribute-list">
      <tr>
      <td align="right" width="30%; fixed"><strong>Property name</strong></td>
      <td><strong>Description</strong></td>
      </tr>
      {% for property in properties %}
      {% if property.category contains "scheduling" %}
      <tr>
      <td align="right">
      <strong>{{ property.name }}</strong><br>
      {{ property.type | upcase }}
      </td>
      <td>
      {{ property.short | flatify | markdownify }}
      </td>
      </tr>
      {% endif %}
      {% endfor %}
      </table>

      These properties are used to create a source's replication schedule. Depending on the replication scheduling type you want to use, you will need to define values for one or several of these properties.

  - title: "Scheduling property hierarchy"
    anchor: "api-property-hierarchy"
    content: |
      {% include misc/icons.html %}

      When determining which replication scheduling type to use, Stitch will consider the `{{ common.names.advanced }}` property above the `{{ common.names.frequency }}` and `{{ common.names.anchor-time }}` properties.

      The table below demonstrates which replication scheduling type will be used for the various combinations of scheduling properties:

      - {{ supported | replace: "TOOLTIP","This property has been defined with a valid value." }} indicates that the property has been defined with a valid value
      - {{ not-supported | replace: "TOOLTIP", "This property has not been defined." }} indicates that the property has not been defined

      {% assign field-list = "frequency-selected|anchor-selected|cron-selected" | split:"|" %}

      <table class="attribute-list">
      <tr>
      {% for property in properties %}
      {% if property.category contains "scheduling" %}
      <td><strong>{{ property.name }}</strong></td>
      {% endif %}
      {% endfor %}
      <td><strong>Scheduling used</strong></td>
      </tr>
      {% for method in page.method-comparison-table %}
      <tr>
      {% for field in field-list %}
      <td width="25%; fixed">
      {% case method[field] %}
      {% when true %}
      {{ supported | replace: "TOOLTIP","This property has been defined with a valid value." }}

      {% when false %}
      {{ not-supported | replace: "TOOLTIP", "This property has not been defined." }}
      {% endcase %}
      </td>
      {% endfor %}
      <td>
      <a href="#{{ method.scheduling-used | slugify }}">{{ method.scheduling-used }}</a>
      </td>
      </tr>
      {% endfor %}
      </table>

      **Note**: If you choose not to manually set the `{{ common.names.frequency }}` value, Stitch will use the source's default value. This means `{{ common.names.frequency }}` will never be `null`. The default value varies by source.

  - title: "Define a replication schedule for a source"
    anchor: "define-replication-schedule-for-source"
    content: |
      In this section, we'll cover which scheduling properties need to be set to use each replication scheduling type:

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Replication Frequency"
        anchor: "replication-frequency"
        content: |
          To create an interval schedule for a source, the `{{ common.names.frequency }}` property must be set. The `{{ common.names.frequency }}` property defines how often, in minutes, Stitch should attempt to replicate data from the source.

          For example: The request below updates the `{{ common.names.frequency }}` property to `1440`, or 24 hours:

          {% assign right-bracket = "}" %}

          ```json
          curl -X {{ site.data.connect.core-objects.sources.update.method | upcase }} {{ site.data.connect.core-objects.sources.update.name | flatify | replace: "{source_id","86741" | remove: right-bracket | prepend: site.data.connect.api.base-url | strip_newlines  }}
               -H "Authorization: Bearer <ACCESS_TOKEN>" 
               -H "Content-Type: application/json"
               -d "{
                     "display_name":"Shopify",
                     "properties":{
                        "start_date":"2017-01-01T00:00:00Z",
                        "frequency_in_minutes":"1440"
                     }
                    }"
          ```

          This means that Stitch will attempt to replicate data from this source every `1440` minutes, or every 24 hours.

          For more info, refer to the [Replication Frequency documentation]({{ link.replication.rep-frequency | prepend: site.baseurl }}).

      - title: "Anchor Scheduling"
        anchor: "anchor-scheduling"
        content: |
          To create an anchored schedule for a source, the following properties must be set:

          {% assign anchor-properties = common.fields | where_exp:"property","property.category contains 'anchor-scheduling'" %}

          {% for property in anchor-properties %}
          - `{{ property.name }}`
          {% endfor %}

          When both properties are defined, the `{{ common.names.anchor-time }}` value will define the time that the `{{ common.names.frequency }}` value is "anchored" to. For example:

          ```json
          curl -X {{ site.data.connect.core-objects.sources.update.method | upcase }} {{ site.data.connect.core-objects.sources.update.name | flatify | replace: "{source_id","77234" | remove: right-bracket | prepend: site.data.connect.api.base-url | strip_newlines  }}
               -H "Authorization: Bearer <ACCESS_TOKEN>" 
               -H "Content-Type: application/json"
               -d "{
                     "display_name":"Marketo",
                     "properties":{
                        "anchor_time":"2018-04-30T03:30:00Z",
                        "frequency_in_minutes":"360"
                     }
                    }"
          ```

          In this case, Stitch will run a replication job for the source every `360` minutes, starting at `03:30:00`. This means a job would run at `09:30:00`, `15:30:00`, `21:30:00`, etc.

          For more info, refer to the [Anchor Scheduling documentation]({{ link.replication.anchor-scheduling | prepend: site.baseurl }}).

      - title: "Advanced Scheduling using cron"
        anchor: "advanced-scheduling"
        content: |
          {% include note.html type="single-line" content="**Note**: Advanced Scheduling using cron is only availble to Stitch client accounts with an Enterprise plan." %}

          To create an advanced (cron) schedule for a source, the `{{ common.names.advanced }}` property must be set. The `{{ common.names.advanced }}` value must be a valid Quartz cron expression representing the replication schedule for the source. For example:

          ```json
          curl -X {{ site.data.connect.core-objects.sources.update.method | upcase }} {{ site.data.connect.core-objects.sources.update.name | flatify | replace: "{source_id","12345" | remove: right-bracket | prepend: site.data.connect.api.base-url | strip_newlines  }}
               -H "Authorization: Bearer <ACCESS_TOKEN>" 
               -H "Content-Type: application/json"
               -d "{
                     "display_name":"MySQL",
                     "properties":{
                        "cron_expression":"0 0 12 ? * MON-FRI *"
                     }
                    }"
          ```

          In this case, Stitch will run a replication job for the source at 12:00PM every day between Monday and Friday.

          For more info, refer to the [Advanced Scheduling documentation]({{ link.replication.advanced-scheduling | prepend: site.baseurl }}).
---