---
title: Anchor Scheduling
permalink: /replication/replication-scheduling/anchor-scheduling
keywords: replicate, replication, replication frequency, frequency, anchor time, scheduling, schedule, interval, change replication time
tags: [replication]

summary: "Create a replication schedule for your integration's using Stitch's Replication Frequency and Anchor Time features."
type: "settings"
toc: true
weight: 1
---
{% include misc/data-files.html %}

Anchor scheduling uses an Anchor Time in conjunction with a [Replication Frequency]({{ link.replication.rep-frequency | flatify | prepend: site.baseurl }}) to create a replication schedule. Anchor scheduling allows you to establish more predictable replication and ensure that your downstream processes run as scheduled with the most up-to-date data.

In this guide, we'll cover:

- [How Anchor Scheduling works](#how-it-works)
- [How jobs are scheduled](#job-scheduling)
- [How Anchor Scheduling impacts your row usage](#row-usage)

---

## How Anchor Scheduling works {#how-it-works}

Anchor Scheduling is a combination of the Replication Frequency and Anchor Time settings in Stitch. The Anchor Time "anchors" the start times of replication jobs to a time you select, and in conjunction with the Replication Frequency, creates a predictable replication schedule.

In addition to the [general behavior applicable to all replication scheduling methods]({{ link.replication.rep-scheduling | prepend: site.baseurl | append: "#how-it-works" }}), Anchor Scheduling:

1. **Requires a Replication Frequency greater than an hour.** One hour is the minimum frequency required to use Anchor Scheduling, as using an anchor time with a frequency less than an hour won't affect an integration's replication schedule.

2. **May not immediately schedule an initial replication job for new integrations.** [See the Job scheduling section below for examples](#job-scheduling).

3. **May not be available for some database integrations.** If you're unable to select an Anchor Time in Stitch for a database integration, reach out to support to request one.

---

## Job scheduling

{% capture loading-tip %}
As scheduling affects the time a replication job starts - **not the time to loaded data** - you should factor in time for loading the data when setting an Anchor Time. To get an idea of your integration's average loading times, use the [Loading Reports]({{ link.replication.loading-reports | prepend: site.baseurl }}).
{% endcapture %}

{% include tip.html content=loading-tip %}

### Example 1: Initial replication job with a six hour frequency {#example-1--initial-job}

When you select an Anchor Time, Stitch will use it and the Replication Frequency to schedule the initial replication job. Based on the Anchor Time, an initial replication job will kick off at the next recurrence of your Replication Frequency. **This means that an initial job may not begin immediately.**

In this example:

- **Current date and time**: May 1 @ 8:00 AM (EST), or UTC 12:00
- **Replication Frequency**: 6 hours
- **Anchor Time**: 9:00 AM (EST), or UTC 13:00

Based on these settings, Stitch will kick off a replication job **every 6 hours starting on May 1 at 9:00 AM (EST)**. The schedule for this integration would look like this:

| Job | Start time (EST) | Start time (UTC) |
|-----+------------------+------------------|
| 1   | May 1 09:00:00   | May 1 13:00:00   |
| 2   | May 1 15:00:00   | May 1 19:00:00   |
| 3   | May 1 21:00:00   | May 2 01:00:00   |
| 4   | May 2 03:00:00   | May 2 07:00:00   |
| 5   | May 2 09:00:00   | May 2 13:00:00   |

### Example 2: Initial replication job with a 24 hour frequency {#example-2--initial-job}

Next, we'll look at an integration where an initial replication job will **not** kick off right away, or even on the same day.

In this example:

- **Current date and time**: May 1 @ 12:00 PM (EST), or UTC 16:00
- **Replication Frequency**: 24 hours
- **Anchor Time**: 9:00 AM (EST), or UTC 13:00

Based on these settings, Stitch will kick off a replication job **every 24 hours starting the following day (May 2) at 9:00 AM (EST)**. The schedule for this integration would look like this:

| Job | Start time (EST) | Start time (UTC) |
|-----+------------------+------------------|
| 1   | May 2 09:00:00   | May 2 13:00:00   |
| 2   | May 3 09:00:00   | May 3 13:00:00   |
| 3   | May 4 09:00:00   | May 4 13:00:00   |
| 4   | May 5 09:00:00   | May 5 13:00:00   |
| 5   | May 6 09:00:00   | May 6 13:00:00   |

### Example 3: Overlapping jobs {#example-3--overlapping-jobs}

If the previous job is still in progress when it would be time to start the next job, Stitch will wait until the next recurrence of the Replication Frequency to start the job. In this example, we'll look at how an integration's schedule would be impacted by a long-running extraction job.

In this example:

- **Current date and time**: May 1 @ 8:00 AM (EST), or UTC 12:00
- **Replication Frequency**: 1 hour
- **Anchor Time**: 9:00 AM (EST)

Based on these settings, Stitch will kick off a replication job **every hour starting on May 1 at 9:00 AM (EST)**. The schedule for this integration would look like this:

| Job | Scheduled start time (EST) | End time (EST) | Duration (minutes) |
|-----+----------------------------+----------------+--------------------|
| 1   | May 1 09:00:00             | May 1 09:21:00 | 21                 |
| 2   | May 1 10:00:00             | May 1 10:35:00 | 35                 |
| 3   | May 1 11:00:00             | May 1 12:05:00 | 65                 |
| --- | May 1 12:00:00             | **Skipped**    | **Skipped**        |
| 4   | May 1 13:00:00             | May 1 13:29:00 | 29                 |
| 5   | May 1 14:00:00             | May 1 14:33:00 | 33                 | 

In this example, **Job 3** took longer to complete than the Replication Frequency of 30 minutes, which meant it was in progress when it was time for **Job 4** to begin.

Instead of **Job 4** beginning at 12:00:00, this job was skipped and re-scheduled to the next recurrence of the Replication Frequency. In this case, that was 13:00:00.

---

## Impact on row usage {#row-usage}

Anchor Scheduling affects not only how often integrations replicate, but how much data is replicated from the integration over time.

For more info, refer to the [Replication scheduling and row usage]({{ link.replication.rep-scheduling | prepend: site.baseurl | append: "#row-usage" }}) section of the Replication Scheduling guide.
