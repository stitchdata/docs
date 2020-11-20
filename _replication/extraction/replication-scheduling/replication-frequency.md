---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Replication Frequency
permalink: /replication/extractions/replication-scheduling/replication-frequency
redirect_from: 
  - /replication/replication-frequency
  - /replication/replication-scheduling/replication-frequency
keywords: replicate, replication, replication frequency, frequency, scheduling, schedule, interval, change replication time
summary: "Replication Frequency is a type of replication scheduling that runs replication jobs based on a time interval you specify."

key: "rep-frequency"
category: "extraction"
content-type: "replication-scheduling"
method: true ## Used in the scheduling overview page

layout: general
toc: true
weight: 2


# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  {{ page.summary }}

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}

example-formatting: |
  {% assign schedule-examples = site.data.taps.extraction.replication-scheduling.replication-frequency.examples | where:"name",subsection.type %}

  {% for schedule-example in schedule-examples %}
  {{ schedule-example.description | flatify }}

  Based on these settings, Stitch will kick off a replication job **{{ schedule-example.schedule-summary }}**. The schedule for this integration might look like this:

  <table class="attribute-list">
  <tr>
  <td align="right"><strong>Job #</strong></td>
  <td><strong>Start Time (EST)</strong></td>
  <td><strong>Start Time (UTC)</strong></td>
  {% if schedule-example.name == "long-running-skipped-job" %}
  <td><strong>End Time (EST)</strong></td>
  <td><strong>Duration</strong></td>
  {% endif %}
  </tr>
  {% for job in schedule-example.jobs %}
  <tr>
  <td align="right">{{ job.number }}</td>
  <td> {{ job.start-est }}</td>
  <td>{{ job.start-utc }}</td>
  {% if schedule-example.name == "long-running-skipped-job" %}
  <td>{{ job.end-est }}</td>
  <td>{{ job.duration }}</td>
  {% endif %}
  </tr>
  {% endfor %}
  </table>
  {% endfor %}


# -------------------------- #
#          CONTENT           #
# -------------------------- #

sections:
  - title: "Replication Frequency availability"
    anchor: "replication-frequency-availability"
    summary: "Replication Frequency availability"
    content: |
      Replication Frequency is available for all database and SaaS integrations.

  - title: "How Replication Frequency works"
    anchor: "how-replication-frequency-works"
    summary: "How Replication Frequency works"
    content: |
      The Replication Frequency setting, found in the {{ app.page-names.int-settings }} page, defines how often Stitch will attempt to extract data from an integration. For example: If set to **30 minutes**, Stitch will attempt to connect to and extract data from the integration every 30 minutes.

    subsections:
      - title: "Initial (historical) replication jobs"
        anchor: "initial-replication-jobs"
        content: |
          After you define and save the integration, Stitch will update the integration's **Sync Status** to **Pending**. This status indicates that Stitch is in the process of scheduling a replication job for the integration.

          **Note**: For newly created integrations, scheduling a replication job can take up to 30 minutes. You can also [manually start a job]({{ link.replication.start-stop-extraction | prepend: site.baseurl }}), but note that this will determine how [ongoing replication jobs](#ongoing-replication-jobs) are scheduled.

      - title: "Ongoing replication jobs"
        anchor: "ongoing-replication-jobs"
        content: |
          Ongoing replication jobs are scheduled based on the start time of the previous job.

          If a job runs over into the next recurrence of the selected Replication Frequency, it will be skipped. Jobs will resume at the next Replication Frequency interval. Refer to the next section [for an example](#long-running-skipped-job).

  - title: "Example schedules using Replication Frequency"
    anchor: "examples"
    summary: "Some example schedules using Replication Frequency "
    content: |
      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "Example 1: Schedule using a 6 hour Replication Frequency"
        anchor: "6-hour-replication-frequency"
        type: "six-hour"
        content: |
          {{ page.example-formatting | flatify }}

      - title: "Example 2: Long-running and skipped jobs"
        anchor: "long-running-skipped-job"
        type: "long-running-skipped-job"
        content: |
          {{ page.example-formatting | flatify }}

          In this example, Job 3 (scheduled for `04:30:00`) was skipped because Job 2 took longer than the Replication Frequency (1 hour/60 minutes) to complete. Replication then resumed on the next recurrence of the Replication Frequency, which was at `05:30:00`.

          **Note**: Stitch doesn't currently send or display notifications when a job is skipped.

  - title: "Create an interval schedule for an integration"
    anchor: "create-schedule"
    summary: "How to create an interval schedule for an integration"
    content: |
      You can create an interval schedule using Replication Frequency in an integration's **Settings** page. 

      1. To access this page, click the integration from the {{ app.page-names.dashboard }} and then click the {{ app.buttons.update-int-settings }} tab.
      2. In the **Replication Frequency** section, uncheck the **Use integration default** checkbox.
      3. Using the slider, select the Replication Frequency interval you want the schedule to use.
      4. When finished, click the {{ app.buttons.save-int-settings }} button.
---