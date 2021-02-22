---
title: Advanced Replication Scheduling Using Cron Expressions
permalink: /replication/replication-scheduling/advanced-scheduling
keywords: replicate, replication, replication frequency, frequency, anchor time, scheduling, schedule, interval, change replication time
layout: general

summary: "The Advanced Scheduler feature allows you to specify granular start times for data extraction. Using cron expressions, you can specify the exact times, days of the week, or even days of the month data extraction should begin."

key: "advanced-scheduling"
method: true
content-type: "replication-scheduling"
toc: true
weight: 4

enterprise: true
enterprise-cta:
  title: "Advanced Scheduling is an Enterprise feature"
  url: "?utm_medium=docs&utm_campaign=cron-scheduling"
  copy: |
    **Advanced replication scheduling is only available on an Enterprise plan**. Cron scheduling allows you to fine-tune an integration's replication schedule, ensuring you have the data you need when you need it. [Contact Stitch Sales for more info]({{ site.sales | append: page.enterprise-cta.url }}){:target="new"}.

intro: |
  {{ page.summary }}

  **Note**: All replication scheduling methods (Replication Frequency, Anchor Scheduling, and Advanced Scheduling) define when data extractions begin. They do not control how long a replication job runs or when data is loaded into a destination.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}

sections:
  - title: "Uses for Advanced Scheduling"
    anchor: "uses"
    summary: "The uses for Advanced Scheduling"
    content: |
      Using Advanced Scheduling, you can:

      1. **Run reports on specified days**. Using Advanced Scheduling, you can create a replication schedule that ensures reports for a weekly 9:00AM meeting are up-to-date.

      2. **Whitelist hours for starting data extractions.** For example: Scheduling replication during off-peak hours will reduce load on your production database.

         **Note**: An extraction may run over into "blackout" hours as the Advanced Scheduler only controls the times jobs **start**. [See the Limitations section for more info](#limitations).

      3. **Reduce your row usage**. Only scheduling data extractions when you need them can not only reduce load on data sources and your destination, it can reduce your overall row usage in Stitch.

      4. **Reduce the re-replication of data.** Because replication scheduling applies to all selected tables in an integration, tables using [Full Table Replication]({{ link.replication.full-table | prepend: site.baseurl }}) will replicate in full each time a replication job runs. Reducing the number of replication jobs overall will decrease the number of times the same record is replicated.

  - title: "Access to Advanced Scheduling"
    anchor: "access-advanced-scheduling"
    summary: "How to access Advanced Scheduling"
    content: |
      Advanced Scheduling is available during the Free Trial or on an Enterprise plan. Contact [Stitch Sales]({{ page.enterprise-cta.url | prepend: site.home }}){:target="new"} for more info about Enterprise plans.

    subsections:
      - title: "Plan downgrades"
        anchor: "plan-downgrades"
        content: |
          When the Free Trial ends or if you downgrade from an Enterprise plan, you'll lose access to the Advanced Scheduling feature.

          In the event that you downgrade, Stitch will automatically pause any integrations using Advanced Scheduling and reset their [Replication Frequencies]({{ link.replication.rep-frequency | prepend: site.baseurl }}) to their defaults. You will need to manually un-pause the integrations to continue replication.

  - title: "Advanced Scheduling basics"
    anchor: "basics"
    summary: "The basics of cron scheduling"
    content: |
      Stitch's Advanced Scheduler feature uses cron scheduling to create replication schedules. In this section, we'll:

      {% for subsection in section.subsections %}
      - [{{ subsection.summary }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Introduction to cron"
        anchor: "intro-to-cron"
        summary: "Introduce you to cron and cron expressions"
        content: |
          So, what's cron? **Cron** is a time-based scheduler used in Unix-like operating systems such as Mac OS, Linux, etc. Tasks, or jobs, created through cron are called **cron jobs**. Stitch uses the [Quartz standard]({{ cron.resource-urls.quartz }}){:target="new"} for cron scheduling.

          To create a cron job - in this case, an integration's replication schedule - a **cron expression** is used. A cron expression describes the details of the schedule, and when combined, translates to the schedule Stitch will use to extract data from the integration.

          Using a cron expression, you can create replication schedules such as _"At 12:00AM every day"_ or _"At 7:00PM every Monday, Wednesday, and Friday"_. Stitch will then start replication jobs at these times.

      - title: "Cron expression syntax"
        anchor: "cron-expression-syntax"
        summary: "Describe cron expression syntax"
        content: |
          {% include misc/icons.html %}

          A cron expression in Stitch is made up of six fields that describe the elements of the schedule, separated by spaces.

          Fields in the expression must be in the following order, and an expression must have all six fields to be considered valid:

          ```conf
          [seconds] [minute] [hour] [day of month] [month] [day of week]
          ```

          Fields can contain any of the allowed values, along with various combinations of the allowed special characters for that field. **Note**: Entering anything other than a field's allowed values or special characters will result in an error when you try to save the integration's settings. Refer to the [Troubleshooting section](#troubleshooting-cron-errors) for help resolving these errors.

          {% assign cron = site.data.ui.cron-scheduling %}

          {% assign cron-attributes = "name|allowed-values|allowed-special-characters" | split:"|" %}

          <table class="attribute-list">
          <tr>
          {% for attribute in cron-attributes %}
          <td>
          <strong>{{ attribute | replace:"-"," " | capitalize }}</strong>
          </td>
          {% endfor %}
          </tr>
          {% for field in cron.required-fields %}
          <tr>
          {% for attribute in cron-attributes %}
          <td>
          {% case attribute %}
          {% when 'allowed-values' %}
          {%- capture tooltip -%}
          {{ field.info | markdownify }}
          {%- endcapture -%}
          {{ field[attribute] }}{% if field.info %}{{ notice-icon | replace: "TOOLTIP",tooltip }}{% endif %}
          {% else %}
          {{ field[attribute] }}
          {% endcase %}
          </td>
          {% endfor %}
          </tr>
          {% endfor %}
          </table>

      - title: "Allowed special characters"
        anchor: "special-characters"
        summary: "Explain how to use special characters"
        content: |
          Each field in a cron expression has its own list of allowed special characters. These characters allow you to select all values, a list or range of values, specify increments, and more. Fields may also contain both a range and a list. Refer to the [Example replication schedules section](#examples) for examples.

          {% assign special-character-columns = "Special character|Allowed in|Description and examples" | split:"|" %}

          <table class="attribute-list">
          <tr>
          {% for column in special-character-columns %}
          <td{% if forloop.first == true %} align="right"{% endif %}>
          <strong>{{ column }}</strong>
          </td>
          {% endfor %}
          </tr>
          {% for special-character in cron.special-characters %}
          <tr>
          <td width="20%; fixed" align="right">
          <strong><code>{{ special-character.character }}</code></strong><br>

          {{ special-character.name | upcase }}
          </td>
          <td width="20%; fixed">
          {{ special-character.allowed-in }}
          </td>
          <td>
          {{ special-character.description | markdownify }}

          <strong>Examples:</strong>

          {{ special-character.example | markdownify }}
          </td>
          </tr>
          {% endfor %}
          </table>  

  - title: "Example replication schedules"
    anchor: "examples"
    summary: "Examples of replication schedules using cron expressions"
    content: |
      {% capture resource-callout %}
      **Want to test an expression?** Try the [{{ cron.resource-names.freeformatter }}]({{ cron.resource-urls.freeformatter }}){:target="new"}.
      {% endcapture %}

      {% include tip.html content=resource-callout %}

      Based on scheduling feedback we've collected, we've put together a list of some of the most commonly requested replication schedules. You can use these examples to define an integration's replication schedule in Stitch, or create your own. Keep in mind that there are some [limitations](#limitations).

      {% for example in cron.examples %}
      - [{{ example.translation }}](#{{ example.anchor }})
      {% endfor %}

      {% assign expression-fields = "seconds|minutes|hours|day-of-month|month|day-of-week" | split:"|" %}

      {% for example in cron.examples %}
      ### {{ example.translation }} {#{{ example.anchor }}}

      <table class="attribute-list">
        <tr>
          {% for field in expression-fields %}
          <td>
            <strong>{{ field | capitalize }}</strong>
          </td>
          {% endfor %}
        </tr>
        {% for expression in example.expressions %}
          <tr>
            {% for field in expression-fields %}
              <td>
                {{ expression[field] }}
              </td>
            {% endfor %}
          </tr>
        {% endfor %}
      </table>
      {% endfor %}

  - title: "Limitations of cron scheduling"
    anchor: "limitations"
    summary: "Limitations of cron scheduling in Stitch"
    content: |
      While using cron expressions will give you the most control over your integrations' replication schedules, there are some limitations to keep in mind:

      1. **You can specify a Day of week OR Day of month value, but not both**. Quartz, the cron implementation used by Stitch, [doesn't currently support specifying values for both fields in an expression](http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html#notes){:target="new"}. One of these fields must contain the `?` character for the expression to be considered valid.

      3. **Advanced Scheduling can only be used to whitelist extraction start times**. This means that a job could start during a whitelisted time period but continue running beyond that window, depending on the duration of the extraction.

         For example: An integration has a schedule that tells it to run every 20 minutes between the hours of noon and 2:00PM, starting at noon.

         On average, extractions for this integration take between 2-5 minutes. However, the extraction that starts at 1:40PM takes longer than average, causing the job to continue running even after the 2:00PM mark. As a result, the job scheduled for 2:00PM will be skipped and resume at the next scheduled interval.

  - title: "Create an Advanced Schedule for an integration"
    anchor: "create-schedule"
    summary: "How to create an Advanced Schedule for an integration"
    content: |
      You can create an Advanced Schedule in an integration's **Settings** page. 

      1. To access this page, click the integration from the {{ app.page-names.dashboard }} and then click the {{ app.buttons.update-int-settings }} tab.
      2. In the **Replication Frequency** section, check the **Advanced** box located under the **Anchor time** menu. This will open the **Advanced Scheduler**.

         **Note**: This feature is only available [during the Free Trial or on an Enterprise plan](#access-advanced-scheduling).
      3. Enter the values you want into each of the fields. Stitch will validate the schedule after each change. If the schedule is valid, a sample schedule will display under the fields.

      4. When finished, click the {{ app.buttons.save-int-settings }} button.

# Refer to the [Troubleshooting section](#troubleshooting-cron-errors) for help resolving these errors.

  # - title: "Troubleshooting"
  #   anchor: "troubleshooting-cron-errors"
  #   summary: "Troubleshooting validation errors"
  #   content: |
  #     {% assign cron-errors = site.data.errors.cron-scheduling.errors %}

  #     If there's an illegal value or the expression syntax is incorrect, Stitch will display an error beneath the Advanced Scheduler fields.

  #     Before you can move on, you'll need to resolve what's causing the error.

  #     <table class="attribute-list">
  #         <tr>
  #             <td width="50%; fixed">
  #                 <strong>
  #                     Error
  #                 </strong>
  #             </td>

  #             <td>
  #                 <strong>
  #                     Solution
  #                 </strong>
  #             </td>
  #         </tr>
  #         {% for error in cron-errors %}
  #             <tr>
  #                 <td>
  #     <pre>
  #     {{ error.message | strip }}
  #     </pre>
  #                 </td>
  #                 <td>
  #                     <strong>Meaning</strong>
  #                     {{ error.meaning | flatify | markdownify }}
  #                     <hr>
  #                     <strong>Solution</strong>
  #                     {{ error.fix-it | flatify | markdownify }}
  #                 </td>
  #             </tr>
  #         {% endfor %}
  #     </table>

  - title: "Additional cron resources"
    anchor: "resources"
    summary: "Additional cron resources"
    content: |
      {% for resource in cron.resource-list %}
      - [**{{ resource.name }}**]({{ resource.url }}) - {{ resource.description | flatify }}
      {% endfor %}
---