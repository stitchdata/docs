---
title: Replication Scheduling
permalink: /replication/replication-scheduling
redirect_from: /replication/replication-frequency
keywords: replicate, replication, replication frequency, frequency, anchor time, scheduling, schedule, interval, change replication time
tags: [replication]

content-type: "replication-scheduling"
toc: true
weight: 1

summary: "Create a replication schedule for your integration's using Stitch's Replication Frequency and Anchor Time features."
---
{% include misc/data-files.html %}

An integration's replication schedule affects the time that the replication process begins. Replication schedules can be created using two settings: **Replication Frequency** and **Anchor Time**.

Stitch offers two methods of creating a replication schedule:

- [**Replication Frequency**](#replication-frequency): This method requires selecting the interval you want replication to run for the integration. Start times of replication jobs are based on the start time and duration of the previous job.
- [**Anchor scheduling**](#anchor-scheduling): Based on the Replication Frequency, or interval, you select, this method "anchors" the start times of replication jobs to a time you select to create a predictable schedule. Anchor Scheduling is a combination of the Anchor Time and Replication Frequency settings, which must both be defined to use this method. 

**Note**: An integration's replication schedule affects the time Extraction begins, not the time to data loaded.

---

## Replication Frequency

The Replication Frequency setting, found in the {{ app.page-names.int-settings }} page, defines how often Stitch will attempt to extract data from an integration. For example: If set to **30 minutes**, Stitch will attempt to connect to and extract data from the integration every 30 minutes.

### Replication frequency intervals and scheduling {#frequency-intervals-scheduling}

When you define an integration's Replication Frequency, Stitch will schedule replication jobs based on the **start time** of the previous job.

If the previous job is still in progress when it would be time to start the next job, Stitch will wait until the next recurrence of the Replication Frequency to begin.

For example: A Facebook Ads integration has a Replication Frequency of 30 minutes. The Start and End Times for this integration's replication jobs might look like this:

| Job # | Start Time | End Time | Duration (minutes) |
|-------+------------+----------+--------------------|
| Job 1 | 12:00:00   | 12:42:00 | 42                 |
| Job 2 | 13:00:00   | 13:29:00 | 29                 |
| Job 3 | 13:30:00   | 14:03:00 | 33                 |
| Job 4 | 14:30:00   | ...      | ...                |


Notice Job 2's Start Time. Because Job 1 took 42 minutes to complete, or longer than the 30 minute Replication Frequency, Job 2 began at the next recurrence of the frequency. In this case, that was `13:00:00` instead of `12:30:00`.

---

## Anchor scheduling

Anchor scheduling uses an Anchor Time in conjunction with a Replication Frequency to create a replication schedule. Anchor scheduling allows you to establish more predictable replication and ensure that your downstream processes run as scheduled with the most up-to-date data.

To use anchor scheduling, you'll need to:

- **Select a Replication Frequency** greater than an hour. One hour is the minimum frequency required to use anchor scheduling, as using an anchor time with a frequency less than an hour won't affect an integration's replication schedule.
- **Define an Anchor Time**. An Anchor Time is the time that the Replication Frequency is "anchored" to, which Stitch will use to create a replication schedule. Anchor times are available in half hour increments. **Selecting an Anchor Time is only required when using anchor scheduling.**

### Job scheduling and anchor times

{% capture loading-tip %}
As scheduling affects the time a replication job starts - **not the time to loaded data** - you should factor in time for loading the data when setting an Anchor Time. To get an idea of your integration's average loading times, use the [Loading Reports]({{ link.replication.loading-reports | prepend: site.baseurl }}).
{% endcapture %}

{% include tip.html content=loading-tip %}

When you select an Anchor Time, Stitch will use it and your selected Replication Frequency to schedule the initial replication job. Based on the Anchor Time, an initial replication job will kick off at the next recurrence of your Replication Frequency. **This means that an initial job may not begin immediately.**

See the examples below for more detail.

#### Example 1: Anchor scheduling with a six hour frequency {#anchor-scheduling--example-one}

In this example:

- **Current date and time**: May 1 @ 8:00 AM (EST), or UTC 12:00
- **Replication Frequency**: 6 hours
- **Anchor Time**: 9:00 AM (EST), or UTC 13:00

Based on these settings, Stitch will kick off a replication job **every 6 hours starting on May 1 at 9:00 AM (EST)**. The schedule for this integration would look like this:

| Job # | Start Time (EST) | Start Time (UTC) |
|-------+------------------+------------------|
| Job 1 | May 1 09:00:00   | May 1 13:00:00   |
| Job 2 | May 1 15:00:00   | May 1 19:00:00   |
| Job 3 | May 1 21:00:00   | May 2 01:00:00   |
| Job 4 | May 2 03:00:00   | May 2 07:00:00   |
| Job 5 | May 2 09:00:00   | May 2 13:00:00   |

#### Example 2: Anchor scheduling with a 24 hour frequency {#anchor-scheduling--example-two}

In this example:

- **Current date and time**: May 1 @ 12:00 (EST), or UTC 16:00
- **Replication Frequency**: 24 hours
- **Anchor Time**: 9:00 AM (EST), or UTC 13:00

Based on these settings, Stitch will kick off a replication job **every 24 hours starting the following day (May 2) at 9:00 AM (EST)**. The schedule for this integration would look like this:

| Job # | Start Time (EST) | Start Time (UTC) |
|-------+------------------+------------------|
| Job 1 | May 2 09:00:00   | May 2 13:00:00   |
| Job 2 | May 3 09:00:00   | May 3 13:00:00   |
| Job 3 | May 4 09:00:00   | May 4 13:00:00   |
| Job 4 | May 5 09:00:00   | May 5 13:00:00   |
| Job 5 | May 6 09:00:00   | May 6 13:00:00   |

---

## Row count impact and Replication Frequency

Replication Frequency affects not only how often your integrations are set to replicate, but how much data is replicated from the integration over time.

Even though Stitch will notify you when you're nearing your row limit, we recommend taking the following into consideration before setting the Replication Frequency for an integration:

- **Replication Frequency applies to the entire integration,** not individual tables. This means all selected tables will replicate according to the set frequency.
- **The number of selected tables in the integration.** While you can select individual tables in database integrations and the [SaaS integrations that support whitelisting]({{ link.replication.syncing | prepend: site.baseurl | append: "#integrations-that-support-whitelisting" }}), **most SaaS integrations have all tables set to replicate by default.** 

   SaaS integrations with high table counts, such as QuickBooks, can result in a high number of replicated rows if set to replicate frequently.
- **The Replication Methods selected tables use.** Use Incremental Replication for database integrations whenever possible, as it will reduce latency and your overall usage.

   - **If some tables must use Full Table Replication**, check out the [Different frequencies for select tables](#different-frequencies-for-full--incrementally-replicating-tables) section below for a solution that can significantly reduce row usage.

   - **For info on the Replication Methods used by SaaS integration tables**, refer to the [**Schema section**]({{ site.baseurl }}/integrations/saas) on any integration's page.

- **Integration attribution windows**. For some SaaS integrations, Stitch will use an <a href="#" data-toggle="tooltip" data-original-title="{{ site.data.tooltips.attribution-window }}">attribution or conversion window</a> to extract data. These windows are employed to account for changes made to ads and campaigns during a conversion period, ensuring that the replicated data isn't stale.

   For example: Every time a replication job runs for [Google AdWords]({{ site.baseurl }}/integrations/saas/google-adwords#replication), the past 15 days' worth of data will be replicated for every table using Incremental Replication. This is to account for any updates made during the attribution/conversion window.

   For more info on how SaaS integration data is replicated, refer to the [Replication section]({{ site.baseurl }}/integrations/saas) on any integration's page.
- **The importance of completely fresh data.** If you don't need data to be constantly replicated or if tasks can still be completed with slightly older data, consider setting integrations to replicate less frequently.

---


## Define different frequencies for select tables {#different-frequencies-for-full--incrementally-replicating-tables}

{% capture workaround %}
This workaround only applies to [integrations that support whitelisting at the table level]({{ link.replication.syncing | prepend: site.baseurl | append: "#integrations-that-support-whitelisting" }}).**

Additionally, while this will work for some SaaS integrations, some SaaS integration providers may not allow more than one API session to be open at a time. [NetSuite]({{ site.baseurl }}/integrations/saas/netsuite) is just such an example. We are unsure of the exact impact this may have on any API quotas imposed by the integration provider.
{% endcapture %}

{% include note.html first-line="**Only applicable to integrations with table selection**" content=workaround %}

To help keep row counts low, you can create two integrations: one to replicate tables using Full Table Replication, the other to replicate Incremental tables. You can then set each integration's Replication Frequency appropriately.

### Example

Let's say you have two tables in a PostgreSQL database that you want to replicate: `files` and `orders`.

The `files` table contains 50,000 rows and uses Full Table Replication, while `orders` contains 100,000 rows and updates incrementally.

On an average day, 500 rows are added or updated to the `orders` table. For `files`, perhaps 10 rows are added or updated each day. It isn't necessary to have `files` replicate as often as `orders`.

To help keep your row count down, you could:

1. Create a PostgreSQL integration and name it `Postgres - Full Table` or something similar.
2. Only set tables using **Full Table Replication** to replicate. In this case, that would be the `files` table.
3. Set the integration's Replication Frequency to every **24 hours**.

Then, to ensure the `orders` table in your destination is updated regularly:

1. Create an additional PostgreSQL integration and name it `Postgres - Incremental` or something similar.
2. Only set tables using **Incremental Replication** to replicate. In this case, that would be the `orders` table.
3. Set the integration's Replication Frequency to every **30 minutes, 1 hour**, etc.