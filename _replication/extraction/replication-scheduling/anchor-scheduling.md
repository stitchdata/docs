---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Anchor Scheduling
permalink: /replication/replication-scheduling/anchor-scheduling
keywords: replicate, replication, replication frequency, frequency, scheduling, schedule, interval, change replication time, anchor scheduling, anchor
summary: "Anchor Scheduling is a type of replication scheduling that 'anchors' the start time of extraction jobs to a time you select. This allows you to establish predictable replication and ensure that your downstream processes run as scheduled with the most up-to-date data."

key: "anchor-scheduling"
content-type: "replication-scheduling"
method: true

layout: general
toc: true
weight: 3

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
  {% assign schedule-examples = site.data.taps.extraction.replication-scheduling.anchor-scheduling.examples | where:"name",subsection.type %}

  {% for schedule-example in schedule-examples %}
  {{ schedule-example.description }}

  - **Current date and time**: {{ schedule-example.current-date-time }}
  - **Replication Frequency**: {{ schedule-example.replication-frequency }}
  - **Anchor Time**: {{ schedule-example.anchor-time }}

  Based on these settings, Stitch will kick off a replication job **{{ schedule-example.schedule-summary }}**. The schedule for this integration would look like this:

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
  - title: "Anchor Scheduling availability"
    anchor: "anchor-scheduling-availability"
    summary: "Anchor Scheduling availability"
    content: |
      Anchor Scheduling is currently supported only for Singer-backed database and SaaS integrations.

      As integrations are converted to Singer taps, this feature will be made available.
  - title: "How Anchor Scheduling works"
    anchor: "how-anchor-scheduling-works"
    summary: "How Anchor Scheduling works"
    content: |
      Anchor scheduling uses an Anchor Time in conjunction with a [Replication Frequency]({{ link.replication.rep-frequency | prepend: site.baseurl }}) to create a replication schedule.

      As scheduling affects the time a replication job starts - not the time to loaded data - you should factor in time for loading the data when setting an Anchor Time. To get an idea of your integration's average loading times, use the [Loading Reports]({{ link.replication.loading-reports | prepend: site.baseurl }}).

      To use anchor scheduling, you'll need to:

      - **Select a Replication Frequency** greater than an hour. One hour is the minimum frequency required to use anchor scheduling, as using an anchor time with a frequency less than an hour won't affect an integration's replication schedule.
      - **Define an Anchor Time**. An Anchor Time is the time that the Replication Frequency is "anchored" to, which Stitch will use to create a replication schedule. Anchor times are available in half hour increments. Selecting an Anchor Time is only required when using anchor scheduling.

      When you select an Anchor Time, Stitch will use it and your selected Replication Frequency to create a replication schedule for the integration.

    subsections:
      - title: "Initial (historical) replication jobs"
        anchor: "initial-replication-jobs"
        content: |
          After you define and save the integration, based on the selected Anchor Time, an initial replication job will kick off at the next recurrence of the Replication Frequency.

          Refer to the [examples in the next section](#examples) for more detail.

          **Note**: If the Anchor Time you select has already passed for the day, an initial job may not immediately begin. In this case, you can [manually start a job]({{ link.replication.start-stop-extraction | prepend: site.baseurl }}).

      - title: "Ongoing replication jobs"
        anchor: "ongoing-replication-jobs"
        content: |
          Ongoing replication jobs will be scheduled based on the selected Anchor Time and Replication Frequency.

          If a job runs over into the next recurrence of the selected Replication Frequency, it will be skipped. Jobs will resume at the next Replication Frequency interval.

          Refer to [this example](#long-running-skipped-job) for more detail.

  - title: "Example schedules using Anchor Scheduling"
    anchor: "examples"
    summary: "Some example schedules using Anchor Scheduling"
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

      - title: "Example 2: Schedule with delayed initial job"
        anchor: "24-hour-replication-frequency"
        type: "twenty-four-hour"
        content: |
          {{ page.example-formatting | flatify }}

          Because the Anchor Time in thi example had already passed for the current day, the initial replication job for the integration didn't start immediately. To start a replication job sooner, you can [manually kick off a job]({{ link.replication.start-stop-extraction | prepend: site.baseurl }}).

      - title: "Example 3: Long-running and skipped jobs"
        anchor: "long-running-skipped-job"
        type: "long-running-skipped-job"
        content: |
          {{ page.example-formatting | flatify }}

          In this example, the job that would have been scheduled for `May 1 04:30:00` was skipped because Job 2 took longer than the Replication Frequency (1 hour/60 minutes) to complete. Replication then resumed on the next recurrence of the Replication Frequency, which was at `May 1 05:30:00`.

          **Note**: Stitch doesn't currently send or display notifications when a job is skipped.

  - title: "Create an anchored schedule for an integration"
    anchor: "create-schedule"
    summary: "How to create an anchored schedule for an integration"
    content: |
      You can create an Anchored Schedule in an integration's **Settings** page. 

      1. To access this page, click the integration from the {{ app.page-names.dashboard }} and then click the {{ app.buttons.update-int-settings }} tab.
      2. In the **Replication Frequency** section, uncheck the **Use integration default** checkbox.
      3. Using the slider, select the Replication Frequency interval you want the schedule to use. **Note**: The Replication Frequency must be **1 hour or greater** to use Anchor Scheduling.
      4. In the **Anchor time** dropdown, select the anchor time you want the schedule to use. Stitch will display a sample schedule at the bottom of the section, which will update as you change the Replication Frequency or anchor time:

         ![]({{ site.baseurl }}/images/replication/scheduling-create-anchored-schedule.gif)
      5. When finished, click the {{ app.buttons.save-int-settings }} button.
---