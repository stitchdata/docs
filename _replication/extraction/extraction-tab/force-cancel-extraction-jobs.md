---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Starting and Stopping Extraction Jobs
permalink: /replication/extractions/start-stop-extraction-jobs
keywords: start job, force job, stop job, stop replication, start extraction, extraction job
summary: "All integrations run on a schedule, but you can also start and stop extractions on demand. This is useful for testing configuration changes or recovering from an error."

key: "start-stop-extraction"
content-type: "replication-scheduling, basics"

layout: general
toc: true
weight: 5


# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  {% include note.html type="single-line" content="**Feature availability**: This feature is available only for integrations powered by Singer taps. As integrations are converted to the Singer system, this feature will be made available." %}

  All Stitch integrations run on a schedule, but Stitch can also start and stop an extraction on demand. This is useful for testing configuration changes or recovering from an error.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#          CONTENT           #
# -------------------------- #

sections:
  - title: "How Extraction jobs work"
    anchor: "about-replication-jobs"
    summary: "How Extraction jobs work"
    content: |
      When starting or stopping Extraction jobs, keep the following in mind:

      1. **Manually starting and stopping jobs is only available for Singer-powered integrations.** As integrations are converted to the Singer system, these features will be made available. 
      2. **Only one job may run at a time for an integration**. If a job is in progress, you will not be able to start a new job without first stopping the one that is in progress.
      3. **Canceling a job won't stop data that has already been extracted from loading**. Canceling an in progress job only cancels the remaining portion of the Extraction phase. Any data extracted prior to the cancellation will be loaded to your destination.

  - title: "Start a manual job"
    anchor: "start-a-job"
    summary: "How to start a manual job"
    content: |
      {% include note.html type="single-line" content="**Note**: Integrations run according to the schedule set in the **Integration Settings** page. Unless you want to kick off a job outside of the integration's schedule, you don't need to perform this process." %}

      You can manually start a job for any Singer-powered integration, regardless of whether the integration is active or paused. Starting a job for a paused integration won't change its paused status, so you can kick off jobs as needed.

      To manually start a job, click into an integration's {{ app.tabs.extractions }} tab and then click the {{ app.buttons.start-extraction }} button:

      ![Manually starting a job.]({{ site.baseurl }}/images/replication/start-replication.gif)

      If successful, an **Extraction starting now** banner will display and the job will kick off shortly.

  - title: "Stop an in-progress job"
    anchor: "stop-a-job"
    summary: "How to stop an in progress job"
    content: |
      You can stop any in-progress job, whether it was manually started by you or automatically started by Stitch.

      To stop a job that is currently in progress:

      1. Scroll to the **Extraction Logs** section of the {{ app.tabs.extractions }} tab. The first item in this section will have an **In Progress** status and a {{ app.buttons.stop-extraction }} button:

         ![An In Progress job and Stop Extraction button, highlighted]({{ site.baseurl }}/images/replication/stop-in-progress-job.png)

         **Note**: The {{ app.buttons.stop-extraction }} button will only display when a job is currently running.

      2. Click {{ app.buttons.stop-extraction }}. You'll be asked to confirm the job cancellation.
      3. To continue, click the **Stop Extraction** button.

      Stitch will cancel the remainder of the Extraction phase of the replication job. **Note**: This will not cancel the loading of data that has already been extracted. Any data extracted prior to the cancellation will be loaded to your destination.
---
{% include misc/data-files.html %}