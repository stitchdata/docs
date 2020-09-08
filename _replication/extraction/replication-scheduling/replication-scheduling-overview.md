---
title: Replication Scheduling
permalink: /replication/replication-scheduling
keywords: replicate, replication, replication frequency, frequency, anchor time, scheduling, schedule, interval, change replication time
summary: "Create a replication schedule for your integrations."

key: "rep-scheduling"
content-type: "replication-scheduling"

layout: general
toc: true
weight: 1

comparison-tooltips:
  level-of-control: "The level of control the scheduling method offers."
  plan-availability: "The Stitch plans that can access the scheduling method."
  integration-availability: "The integrations that support the scheduling method."
  select-days: "Indicates if the scheduling method supports selecting specific days for starting extraction jobs."
  select-hours: "Indicates if the scheduling method supports selecting specific hours for starting extraction jobs."


# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  An integration's replication schedule affects the time that replication jobs begin and how often they occur. Specifically, replication scheduling controls the frequency and start time of the Extraction phase of the replication process, which is when Stitch extracts data from the data source.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#          CONTENT           #
# -------------------------- #

sections:
  - title: "How replication scheduling works"
    anchor: "how-replication-scheduling-works"
    summary: "How replication scheduling works"
    content: |
      When you create a replication schedule for a SaaS or database integration, you're telling Stitch when and how frequently data extraction should occur. When creating a replication schedule, keep the following in mind:

      1. **Replication scheduling can only control the time a replication job begins, not the time it ends or the time data is loaded**. The completion of the job, including the time to load extracted data into your destination, is not controllable using any of Stitch's replication scheduling features. Remember to factor in time for Stitch's data preparation and loading phases of replication.

      2. **Replication scheduling only applies to database and SaaS integrations.** Due to the as-it-happens nature of webhooks, [webhook integration data]({{ site.baseurl }}/integrations/webhooks) is replicated continuously and doesn't require a schedule.

      3. **Only one replication job can run at a time.** If a replication job is in progress when the next job is scheduled to begin, the second job will be skipped. The next job will be scheduled according to the next iteration in the replication schedule.

      4. **An integration's replication schedule applies to all selected tables**. Defining replication schedules for individual tables isn't currently supported. You can, however, [use this workaround]({{ link.replication.table-scheduling | prepend: site.baseurl }}), but note that there are some limitations.

      5. **Critical errors that occur during Extraction will end the current job.** Errors during the Extraction phase can occur for a myriad of reasons, such as connection/credential issues, Stitch or third-party outages, etc. When Stitch encounters an error during this phase of the replication process, the current job will end. The next job will be scheduled according to the next iteration in the replication schedule.

  - title: "Replication scheduling methods"
    anchor: "replication-scheduling-methods"
    summary: "The scheduling methods offered by Stitch"
    content: |
      Stitch offers three methods of creating a replication schedule:

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}

    subsections:
      - title: "Replication Frequency"
        anchor: "replication-frequency"
        content: |
          [Replication Frequency]({{ link.replication.rep-frequency | prepend: site.baseurl }}) allows you to select how frequently you want Stitch to run replication jobs for an integration, based on intervals of 30 minutes, one hour, three hours, six hours, 12 hours, and 24 hours.

          For this method, the start times of replication jobs are based on the start time and duration of the previous job. Refer to the [Replication Frequency documentation]({{ link.replication.rep-frequency | prepend: site.baseurl }}) for more info and examples.

      - title: "Anchor Scheduling"
        anchor: "anchor-scheduling"
        content: |
          [Anchor Scheduling]({{ link.replication.anchor-scheduling | prepend: site.baseurl }}) is a combination of two settings: Replication Frequency and Anchor Time.

          The Anchor Time "anchors" the start times of replication jobs to a time you select, and in conjunction with the Replication Frequency, creates a predictable replication schedule. For example: Run a replication job every 3 hours, starting at 1:00 PM. Refer to the [Anchor Scheduling documentation]({{ link.replication.anchor-scheduling | prepend: site.baseurl }}) for more info and examples.

          **Note**: This feature is only available for Singer-backed integrations.

      - title: "Advanced Scheduling using cron expressions"
        anchor: "advanced-scheduling"
        content: |
          The [Advanced Scheduler feature]({{ link.replication.advanced-scheduling | prepend: site.baseurl }}) allows you to specify granular start times for data extraction. Using cron expressions, you can specify the exact times, days of the week, or even days of the month data extraction should begin. Refer to the [Advanced Scheduling documentation]({{ link.replication.advanced-scheduling | prepend: site.baseurl }}) for more info and examples.

          **Note**: This feature is only available on Enterprise plans.

  - title: "Compare Replication Scheduling types"
    anchor: "compare-replication-scheduling-types"
    summary: "A comparison of each Replication Scheduling type"
    content: |
      {% include misc/icons.html %}

      The table below contains a high-level look at each of Stitch’s Replication Scheduling types and how they compare to each other.

      **Note**: This is not intended as a substitute for the full documentation for each Replication Scheduling type.

      {% assign data-about = site.data.taps.extraction.replication-scheduling %}

      {% assign scheduling-methods = "replication-frequency|anchor-scheduling|advanced-scheduling" | split:"|" %}

      {% assign attributes = "level-of-control|plan-availability|integration-availability|select-days|select-hours|documentation" | split:"|" %}

      <table class="attribute-list">
      <tr>
      <td>
      </td>
      {% for method in scheduling-methods %}
      <td>
      <strong>{{ data-about[method]display-name }}</strong>
      </td>
      {% endfor %}
      </tr>
      {% for attribute in attributes %}
      <tr>
      <td align="right">
      <strong>{{ attribute | replace:"-"," " | capitalize }}</strong> {{ info-icon | replace:"TOOLTIP",page.comparison-tooltips[attribute] }}
      </td>
      {% for method in scheduling-methods %}
      <td width="24%; fixed">
      {% case data-about[method][attribute] %}
      {% when true %}
      {{ supported | replace:"TOOLTIP","" }}
      {% when false %}
      {{ not-supported | replace:"TOOLTIP","" }}
      {% else %}
      {% if attribute == "documentation" %}
      <a href="{{ data-about[method][attribute] | flatify }}">Documentation</a>
      {% else %}
      {{ data-about[method][attribute] }}
      {% endif %}
      {% endcase %}
      </td>
      {% endfor %}
      </tr>
      {% endfor %}
      </table>

  - title: "Define an integration's replication schedule"
    anchor: "define-replication-schedule"
    summary: "How to define an integration's replication schedule"
    content: |
      How an integration's replication schedule is defined depends on the type of scheduling type you're using. Click the links below to view instructions for defining each scheduling type:

      {% assign scheduling-methods = site.replication | where:"content-type","replication-scheduling" | sort:"weight" %}

      {% for scheduling-method in scheduling-methods %}
      {% if scheduling-method.method == true %}
      - [{{ scheduling-method.title }}]({{ scheduling-method.url | prepend: site.baseurl }}#create-schedule)
      {% endif %}
      {% endfor %}
---
{% include misc/data-files.html %}