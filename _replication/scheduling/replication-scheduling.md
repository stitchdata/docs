---
title: Replication Scheduling
permalink: /replication/replication-scheduling
keywords: replicate, replication, replication frequency, frequency, anchor time, scheduling, schedule, interval, change replication time
tags: [replication]

summary: "[TODO]"
type: "settings"
toc: true
weight: 1
---
{% include misc/data-files.html %}

An integration's replication schedule affects the time that replication jobs begin and how often they occur. Specifically, replication scheduling controls the frequency and start time of the Extraction phase of the replication process, which is when Stitch extracts data from the data source.

In this guide, we'll cover:

- [How replication scheduling works](#how-it-works)
- [The methods for creating replication schedules](#methods)
- [How replication schedules can impact your row usage](#row-usage)

---

## How replication scheduling works {#how-it-works}

1. **Replication scheduling can only control the time a replication job begins**, not the time it ends or the time data is loaded. The completion of the job, including the time to load extracted data into your destination, is not controllable using any of Stitch's replication scheduling features. Remember to factor in time for Stitch's data preparation and loading phases of replication.

2. **Replication scheduling only applies to database and SaaS integrations.** Due to the as-it-happens nature of webhooks, [webhook integration data]({{ site.baseurl }}/integrations/webhooks) is replicated continuously and doesn't require a schedule.

3. **Jobs that are currently in progress must complete before the next scheduled job can start.** If a replication job is in progress when the next job is scheduled to begin, the second job will be skipped. The next job will be scheduled according to the next iteration in the replication schedule.

4. **An integration's replication schedule applies to all selected tables**. Defining replication schedules for individual tables isn't currently supported.

---

## Methods for creating replication schedules {#methods}

Stitch offers three methods of creating a replication schedule, listed below.

### Replication Frequency

[Replication Frequency]({{ link.replication.rep-frequency | prepend: site.baseurl }}) allows you to select how frequently you want Stitch to run replication jobs for an integration, based on intervals of 30 minutes, one hour, three hours, six hours, 12 hours, and 24 hours.

For this method, the start times of replication jobs are based on the start time and duration of the previous job. [Refer to [TODO] for examples]().

### Anchor Scheduling

[Anchor Scheduling]({{ link.replication.anchor-scheduling | prepend: site.baseurl }}) is a combination of two settings: Replication Frequency and Anchor Time.

The Anchor Time "anchors" the start times of replication jobs to a time you select, and in conjunction with the Replication Frequency, creates a predictable replication schedule. For example: Run a replication job every 3 hours, starting at 1:00 PM. [Refer to [TODO] for more examples]().

**Note**: This feature may not be available for all integrations.

### Advanced Scheduling using cron expressions

The [Advanced Scheduler feature]({{ link.replication.cron-scheduling | prepend: site.baseurl }}) allows you to specify granular start times for data extraction. Using cron expressions, you can specify the exact times, days of the week, or even days of the month data extraction should begin.

**Note**: This feature is only available on Enterprise plans.

---

## Replication scheduling and row usage {#row-usage}

{% capture usage-guide %}
**Need some help understanding row usage and Stitch billing?** Check out the [Understanding and reducing your row usage guide]({{ link.billing.billing-guide | prepend: site.baseurl }}).
{% endcapture %}

{% include tip.html content=usage-guide %}

Replication scheduling affects not only how often your integrations are set to replicate, but how much data is replicated from the integration over time.

Even though Stitch will notify you when you're nearing your row limit, consider the following before defining an integration's replication schedule:

- **The number of tables set to replicate.** An integration's replication schedule applies to all tables set to replicate. The more tables that are selected, the higher the row count is likely to be.

   **Note**: [MongoDB]({{ site.baseurl }}/integrations/databases/mongodb) and some [SaaS integrations]({{ site.baseurl }}/integrations/saas) don't support selecting individual tables and columns for replication. In this case, all tables are set to replicate by default. This can result in a high number of replicated rows if the integration is scheduled to run frequently.

- **The Replication Methods selected tables use.** Tables using Full Table Replication replicate fully during each replication job, resulting in a higher number of rows.

   - **For database integrations**, use [Log-based Replication]({{ link.replication.rep-methods | prepend: site.baseurl }}) or [Incremental Replication]({{ link.replication.rep-methods | prepend: site.baseurl }}) whenever possible. Also consider using [this workaround to set different replication schedules for Full and Incremental tables]([TODO]).

   - **For SaaS integrations**, check out the [**Schema section**]({{ site.baseurl }}/integrations/saas) in any integration's documentation for info about the Replication Methods tables use. Consider setting the integration to replicate less frequently if a high number of tables use Full Table Replication.

- **Integration attribution windows**. For some SaaS integrations, Stitch will use an <a href="#" data-toggle="tooltip" data-original-title="{{ site.data.tooltips.attribution-window }}">attribution or conversion window</a> to extract data. These windows are employed to account for changes made to ads and campaigns during a conversion period, ensuring that the replicated data isn't stale.

   For example: Every time a replication job runs for [Google AdWords]({{ site.baseurl }}/integrations/saas/google-adwords#replication), the past 15 days' worth of data will be replicated for every table using Incremental Replication. This is to account for any updates made during the attribution/conversion window.

   For more info on how SaaS integration data is replicated, refer to the [Replication section]({{ site.baseurl }}/integrations/saas) on any integration's page.

- **The importance of completely fresh data.** If you don't need data to be constantly replicated or if tasks can still be completed with slightly older data, consider setting integrations to replicate less frequently, such as once or twice a day.