---
title: Replication Frequency
permalink: /replication/replication-scheduling/replication-frequency
redirect_from: /replication/replication-frequency
keywords: replicate, replication, replication frequency, frequency, scheduling, schedule, interval, change replication time
tags: [replication]

summary: "The simplest of Stitch's scheduling methods, Replication Frequency uses an interval you define to create a replication schedule."
type: "scheduling"
toc: true
weight: 2
---
{% include misc/data-files.html %}

The simplest of Stitch's [three replication scheduling methods]({{ link.replication.rep-scheduling | prepend: site.baseurl }}), Replication Frequency uses an interval you define and the start time of replication jobs to create a replication schedule. This will determine how often Stitch attempts to extract data from an integration.

In this guide, we'll cover:

- [How Replication Frequency works](#how-it-works)
- [How jobs are scheduled](#job-scheduling)
- [How Replication Frequency impacts your row usage](#row-usage)

---

## How Replication Frequency works {#how-it-works}

In addition to the [general behavior applicable to all replication scheduling methods]({{ link.replication.rep-scheduling | prepend: site.baseurl | append: "#how-it-works" }}), Replication Frequency will:

1. **Immediately schedule a replication job for newly created integrations.** This means that a replication job will be scheduled shortly after an integration is created, regardless of the selected frequency.

   **Note**: An integration's status will show as **Pending** for up to 30 minutes after it's created. This means that Stitch is in the process of scheduling the initial replication job.

2. **Use the interval you define and the start time of previous jobs to schedule subsequent jobs.** [See the Job scheduling section below for examples](#job-scheduling).

---

## Job scheduling {#job-scheduling}

When you define an integration's Replication Frequency, Stitch will use the frequency and the start time of the initial job to create a replication schedule.

See the examples below for more detail.

### Example 1: Initial replication jobs {#example-1--initial-jobs}

When an integration is initially created, Stitch will start scheduling a job immediately following its creation. **Note**: Scheduling initial replication jobs can take up to 30 minutes.

In this example:

- **Initial job start time**: 17:25:00
- **Replication Frequency**: 3 hours

| Job | Scheduled start time | End time | Duration (minutes) |
|-----+----------------------+----------+--------------------|
| 1   | 17:25:00             | 18:11:00 | 46                 |
| 2   | 20:25:00             | 20:56:00 | 31                 |
| 3   | 23:25:00             | 23:02:00 | 37                 |
| 4   | 02:25:00             | ...      | ...                |

### Example 2: Overlapping jobs {#example-2--overlapping-jobs}

If the previous job is still in progress when it would be time to start the next job, Stitch will wait until the next recurrence of the Replication Frequency to begin.

In this example:

- **Start time**: 12:00:00
- **Replication Frequency**: 30 minutes

| Job | Scheduled start time | End time | Duration (minutes) |
|-----+----------------------+----------+--------------------|
| 1   | 12:00:00             | 12:42:00 | 42                 |
| --- | 12:30:00             | **Skipped**  | **Skipped**            |
| 2   | 13:00:00             | 13:29:00 | 29                 |
| 3   | 13:30:00             | 14:03:00 | 33                 |
| 4   | 14:30:00             | ...      | ...                |

In this example, **Job 1** took longer to complete than the Replication Frequency of 30 minutes, which meant it was in progress when it was time for **Job 2** to begin.

Instead of **Job 2** beginning at 12:30:00, this job was skipped and re-scheduled to the next recurrence of the Replication Frequency. In this case, that was 13:00:00.

### Example 3: Changing Replication Frequencies {#example-3--change-replication-frequencies}

Changing an integration's Replication Frequency can affect the start time of future jobs. In this example, the Replication Frequency is changed from 30 minutes to 1 hour in between replication jobs.

**Note**: Changing the Replication Frequency won't immediately kick off a replication job. Future replication jobs will be scheduled based on the previous job's start time.

In this example:

- **Start time**: 09:00:00
- **Initial Replication Frequency**: 30 minutes
- **Updated Replication Frequency**: 1 hour

| Job | Replication Frequency used | Scheduled start time | End time | Duration (minutes) |
|-----+----------------------------+----------------------+----------+--------------------|
| 1   | 30 minutes                 | 09:00:00             | 09:15:00 | 15                 |
| 2   | 30 minutes                 | 09:30:00             | 09:56:00 | 26                 |
| 3   | 1 hour                     | 10:30:00             | 10:51:00 | 21                 |
| 4   | 30 minutes                 | 11:00:00             | 11:23:00 | 23                 |

---

## Impact on row usage {#row-usage}

Replication Frequency affects not only how often integrations replicate, but how much data is replicated from the integration over time.

For more info, refer to the [Replication scheduling and row usage]({{ link.replication.rep-scheduling | prepend: site.baseurl | append: "#row-usage" }}) section of the Replication Scheduling guide.