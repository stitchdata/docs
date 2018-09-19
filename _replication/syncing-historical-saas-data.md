---
title: Syncing Historical SaaS Data & Resetting SaaS Replication Keys
permalink: /replication/syncing-historical-saas-data-resetting-replication-keys
keywords: replicate, replication, replication key, keys, stitch replicates data, rp, saas, historical data, reset bookmark, reset replication key
tags: [replication]

summary: "By default, a historical replication job for most SaaS integrations will go back one year. While the Start Date setting allows you to define historical data loads, it can also reset an integration's Replication Keys when you need to re-replicate data."
type: "syncing"
toc: true
weight: 2
---
{% include misc/data-files.html %}

{% capture feature-availability %}
The Historical Sync/Start Date feature may not be available for some integrations. Because this approach uses date-based replication, some integrations may be incompatible.
{% endcapture %}

{% include note.html first-line="**Feature availibility**" content=feature-availability %}

When you connect a SaaS integration, Stitch will begin the process of replicating not only that integration’s recent data, but the historical data as well. During the setup of the integration, you can choose the start date by using Stitch's default starting date or defining your own custom date. 

---

## Historical data loads and Replication Keys

The default starting date (or a custom date, if you define one) essentially sets the [Replication Keys]({{ link.replication.rep-keys | prepend: site.baseurl }}) for the [Incremental tables]({{ link.replication.rep-methods | prepend: site.baseurl | append: "#incremental-replication" }}) in the integration. This tells Stitch how far back in time to query for historical data.

**Note that any tables using [Full Table Replication]({{ link.replication.rep-methods | prepend: site.baseurl | append: "#full-table-replication" }}) will still replicate in full during every replication job, even during the initial job.**

The majority of integrations have a default starting date of **-1 year** from the Stitch connection date. For example: If an integration has a default starting date of -1 year and was connected to Stitch on October 1, 2016, a historical replication job will **start** on October 1, 2015 and replicate all data created/updated between then and October 1, 2016.

### Default Starting Dates {#starting-date-rollup}

In the table below (click the link to open it), you'll find a rollup of **all the default start dates for SaaS integrations.**

**To see a list of that integration's tables and the Replication Methods they use**, click the integration name.

<div class="panel-group" id="accordion">
<div class="panel panel-default">
<div class="panel-heading">
<h4 class="panel-title" id="starting-date-rollup">
<a class="noCrossRef accordion-toggle" data-toggle="collapse" data-parent="#accordion" href="#collapseOne">SaaS Integration Default Starting Dates</a>
</h4>
</div>
<div id="collapseOne" class="panel-collapse collapse noCrossRef">
<div class="panel-body">
<table>
<thead>
<th valign="top" markdown="span">Integration</th>
<th valign="top" markdown="span">Default Starting Date</th>
</thead>
<tbody>
{% assign saas-integrations = site.saas-integrations | where:"input","true" %}
{% for integration in saas-integrations %}
<tr>
<td valign="top">
<a href="{{ integration.url | prepend: site.baseurl | append: "#schema" }}"><img src="{{ integration.icon | prepend: site.baseurl }}"></a>
</td>
<td valign="center">
{% if integration.historical == "Webhook" %}
<a href="#" data-toggle="tooltip" data-original-title="Webhooks typically don't retain historical data due to their real-time nature. See this integration's doc for more info.">None</a>
{% else %}
{{ integration.historical }}
{% endif %}
</td>
</tr>
{% endfor %}
</tbody>
</table>
</div>
</div>
</div>
</div>

--- 

## Uses & Considerations

An integration's start date can be defined when you initially connect the integration to Stitch or after the fact. If the date is changed after the initial setup, **the integration's Replication Keys will be reset AND a full re-replication of all the integration's data will be queued.**

### Uses 

Aside from ensuring Stitch replicates all the historical data you need, changing an integration's start date can serve several other purposes:

1. **Account for hard-deletes.** While we strongly recommend you use soft-deletes whenever possible, the full re-replication triggered by changing an integration's start date will overwrite the data in your data warehouse. This will remove any hard-deleted records that may exist in your data warehouse but not in the source.
2. **Reset Replication Keys.** 
2. **Resolve data discrepancies.** If you believe you’re missing data, try to narrow it down to a specific timeframe. If that timeframe falls outside the default starting date, this may be the root cause of the discrepancy. Changing the start date for the integration will bring in the data outside the original range.

   If this doesn't apply, check out the [Data Discrepancy Troubleshooting Guide]({{ link.troubleshooting.discrepancy-guide | prepend: site.baseurl }}) for more data discrepancy troubleshooting tips.

### Considerations

Note that these points shouldn't cause worry or discourage you from setting up historical replication job or queueing re-replications - they're only intended to give you a comprehensive look at the process so you can make an informed decision.

If you have any questions or concerns, reach out to support **before** changing the start date.

1. **This process cannot be undone**. Once a historical replication job is queued, there's no way to stop it.
2. **Depending on the integration, there may be limitations**. Webhook-based integrations like SendGrid, for example, don't retain historical data. Check out the [rollup in the Default Starting Dates section](#starting-date-rollup) for specifics.
3. **Row usage will spike.** It should be noted that some integrations - like Mixpanel - can contain large (sometimes astronomical) amounts of data. The full re-replication triggered by changing the start date will count against your row count.
4. **Recent data may be re-replicated.** For example: you set up an integration and the original replication job contained data only for 2016. You are now setting up a historical job for this integration with a start date of 1/1/2015. This will replicate data for all of 2015 and 2016.
5. **You may experience stale data/reports.** When a historical replication job runs, no recent data will be retrieved until the replication and loading of the historical data is complete. The volume of data to be replicated and the design of the provider's API can both affect how long a historical data load will take.

   For example: NetSuite's API tends to be on the slower side, so it may take some time to complete a full re-replication due to the API design and the sheer amount of data that's available.
6. **The time a historical replication job takes may be affected by an integration's API quota**. Some integrations - like Salesforce and Marketo - use API quotas, which limit your API usage. While our integrations are designed not to consume all of your available quota, if you're using the integration's API somewhere else, this process may use up your quota.

   As Stitch will be unable to continue replicating data once the quota has been consumed, this can extend the length of time the historical replication job will take, thus affecting the freshness of your reports.

---

## Changing an Integration's Start Date

### During the Initial Setup
To use a custom start date during the initial setup:

1. After defining the rest of the integration's settings, locate the **Sync Historical Data** section.
2. Uncheck the **Use Integration Default** box.
3. Define the new starting date using the drop-down.
4. When finished, click the **Save Integration** button.

**Note**: It may take some time for Stitch to perform a structure sync for the integration and begin replicating data. After the structure sync is complete, Stitch will begin replicating data according to the integration's [Replication Schedule]({{ link.replication.rep-scheduling | prepend: site.baseurl }}).

### After the Initial Setup
1. From the {{ app.page-names.dashboard }} page, click into the integration.
2. In the {{ app.page-names.int-details }} page, click the {{ app.buttons.update-int-settings }} tab, next to **Tables to Replicate**.
3. Scroll down to the **Sync Historical Data** section.
4. In the **Start Date** section, click the **Change Date** link.
5. Define the new starting date using the drop-down.
6. Click the **Reset Date** button.
7. When prompted, click **OK** to confirm and proceed with changing the starting date.

If successful, a confirmation message will display indicating the replication job has been queued. After a structure sync is performed, Stitch will begin replicating data according to the integration's [Replication Schedule]({{ link.replication.rep-scheduling | prepend: site.baseurl }}).