---
title: Replication Frequency
permalink: /replication/replication-frequency
keywords: replicate, replication, replication frequency, frequency, stitch replicates data, interval, change replication time
tags: [replication]

summary: "The Replication Frequency setting tells Stitch how often to replicate data from an integration. In this guide, we'll explain how replication jobs are scheduled and what you should consider when defining the Replication Frequency for your integrations."
type: "settings"
toc: true
weight: 1
---
{% include misc/data-files.html %}

The Replication Frequency setting, found in the {{ app.page-names.int-settings }} page, controls how often Stitch will attempt to replicate data from an integration.

The more frequently an integration is set to replicate, the higher the number of rows that will replicate through Stitch.

---

## Sync Scheduling & Replication Frequency

Stitch schedules syncs based on the **start time** of the previous sync.

If the previous sync is still in progress when it would be time to start the next sync, Stitch will wait until the next recurrence of the Replication Frequency to begin.

For example: A Facebook Ads integration has a Replication Frequency of 30 minutes. The Start and End Times for this integration's syncs might look like this:

| Sync # | Start Time | End Time | Duration (minutes) |
|--------+------------+----------+--------------------|
| Sync 1 | 12:00:00   | 12:42:00 | 42                 |
| Sync 2 | 13:00:00   | 13:29:00 | 29                 |
| Sync 3 | 13:30:00   | 14:03:00 | 33                 |
| Sync 4 | 14:30:00   | ...      | ...                |


Notice Sync 2's Start Time. This is because Sync 1 took 42 minutes to complete, or longer than the defined 30 minute Replication Frequency. In this case, Sync 2 began at the next recurrence of the Replication Frequency, or `13:00:00`.

---

## Row Count Impact & Replication Frequency

Replication Frequency affects not only how often your integrations are set to replicate, but how much data is replicated from the integration over time.

Even though we'll send out notifications when you're nearing your row limit, we recommend taking the following into consideration before setting the Replication Frequency for an integration:

- **Replication Frequency applies to the entire integration,** not individual tables. This means all tables set to sync will replicate according to the set frequency.
- **The number of syncing tables in the integration.** While you can sync individual tables in database integrations and the [SaaS integrations that support whitelisting]({{ link.replication.syncing | prepend: site.baseurl | append: "#integrations-that-support-whitelisting" }}), **most SaaS integrations have all tables set to sync by default.** 

   SaaS integrations with high table counts like QuickBooks can result in a high number of replicated rows if set to replicate frequently.
- **The Replication Methods syncing tables use.** Because it can reduce latency and your row count, we recommend using Incremental Replication for database integration tables whenever possible. A high Replication Frequency (such as 30 minutes) and a large number of tables that use Full Table Replication can quickly use up your row count and possibly lead to overages.

   - **If some tables have to use Full Table Replication**, check out the [Different Frequencies for Full & Incrementally Replicating Tables](#different-frequencies-for-full--incrementally-replicating-tables) section below for a solution that can significantly reduce row usage.

   - **For info on the Replication Methods used by SaaS integration tables**, refer to the [**Schema section**]({{ site.baseurl }}/integrations/saas) on any integration's page.
- **How the integration replicates as a whole.** This typically applies to SaaS integrations and the querying strategies Stitch employs to extract data.

  For example: Every time a sync runs for [Facebook Ads]({{ site.baseurl }}/integrations/saas/facebook-ads#replication), **the past 28 days' worth of data will be replicated**. This is to account for changes that can be made during the 28 day attribution window on campaigns. Even though all tables in this integration use Incremental Replication, the number of replicated rows can still be huge because of the strategy Stitch uses to query.

  For more info on how SaaS integration data is queried/replicated, refer to the [Replication section]({{ site.baseurl }}/integrations/saas) in the SaaS integration docs.
- **The importance of completely fresh data.** If you don't need data to be constantly replicated or if tasks can still be completed with _slightly_ older data, consider setting integrations to replicate less frequently.

---

## Define an Integration's Replication Frequency

When you initially create and set up an integration, you'll be asked to define its Replication Frequency.

You can either use the default (which is 30 minutes for most integrations) or define a custom setting. In some cases, you'll have to uncheck the **Use Integration Default** box:

![Defining the Replication Frequency for Mixpanel.]({{ site.baseurl }}/images/replication/replication-frequency.gif)

Then, Stitch will replicate data from all syncing tables in the integration based on their individual Replication Methods and the Frequency you select.

### Update an Integration's Replication Frequency

If at any time you want to change the Replication Frequency for an integration, here's what you need to do:

1. Click into the integration from the {{ app.page-names.dashboard }} page.
2. Click the {{ app.buttons.update-int-settings }} tab, next to **Tables to Replicate**.
3. Scroll down to the **Replication Frequency** section.
4. Change the Replication Frequency to your desired setting.
5. Click {{ app.buttons.save-int-settings }}.

---

## Define Different Frequencies for Full & Incremental Tables {#different-frequencies-for-full--incrementally-replicating-tables}

{% capture workaround %}**This workaround only applies to [integrations that support whitelisting at the table level]({{ link.replication.syncing | prepend: site.baseurl | append: "#integrations-that-support-whitelisting" }}).**

<br><br>Additionally, while this will work for some SaaS integrations, some SaaS integration providers may not allow more than one API session to be open at a time. [NetSuite]({{ site.baseurl }}/integrations/saas/netsuite#create-netsuite-admin-user) is just such an example. We are unsure of the exact impact this may have on any API quotas imposed by the integration provider.
{% endcapture %}
{% include note.html content=workaround %}

To help keep row counts low, you can create two integrations: one to sync tables using Full Table Replication, the other to sync Incremental tables. You can then set each integration's Replication Frequency appropriately.

### Example

Let's say you have two tables in a PostgreSQL database that you want to sync: `files` and `orders`.

The `files` table contains 50,000 rows and uses Full Table Replication, while `orders` contains 100,000 rows and updates incrementally.

On an average day, 500 rows are added or updated to the `orders` table. For `files`, perhaps 10 rows are added or updated each day. It isn't necessary to have `files` replicate as often as `orders`.

To help keep your row count down, you could:

1. Create a PostgreSQL integration and name it `Postgres - Full Table` or something similar.
2. Only select tables using **Full Table Replication** to sync. In this case, that would be the `files` table.
3. Set the integration's Replication Frequency to every **24 hours**.

Then, to ensure the `orders` table is updated regularly:

1. Create an additional PostgreSQL integration and name it `Postgres - Incremental` or something similar.
2. Only select tables using **Incremental Replication** to sync. In this case, that would be the `orders` table.
3. Set the integration's Replication Frequency to every **30 minutes, 1 hour**, etc.
