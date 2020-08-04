---
title: SaaS Integration Start Dates
permalink: /replication/extractions/replication-keys/understanding-saas-start-dates

redirect_to: /replication/extractions/replication-keys#applicable-integrations

keywords: replicate, replication, replication key, keys, stitch replicates data, rp, saas, historical data, reset bookmark, reset replication key

key: "define-saas-start-date"
content-type: "replication-keys"
toc: true
weight: 6

summary: "By default, a historical replication job for most SaaS integrations will go back one year. While the Start Date setting allows you to define historical data loads, it can also reset an integration's Replication Keys when you need to re-replicate data."
---
{% include misc/data-files.html %}

{% capture feature-availability %}
The Historical Sync/Start Date feature may not be available for some integrations. Because this approach uses date-based replication, some integrations may be incompatible.
{% endcapture %}

{% include note.html first-line="**Feature availibility**" content=feature-availability %}

When you connect a SaaS integration, Stitch will begin the process of replicating not only that integration’s recent data, but the historical data as well. During the setup of the integration, you can choose the start date by using Stitch's default starting date or defining your own custom date.



---
How they work

An integration's start date can be defined when you initially connect the integration to Stitch or after the fact. If the date is changed after the initial setup, **the integration's Replication Keys will be reset AND a full re-replication of all the integration's data will be queued.**

The default starting date (or a custom date, if you define one) essentially sets the [Replication Keys]({{ link.replication.rep-keys | prepend: site.baseurl }}) for the [Incremental tables]({{ link.replication.rep-methods | prepend: site.baseurl | append: "#incremental-replication" }}) in the integration. This tells Stitch how far back in time to query for historical data.

      **Note:** Any tables using [Full Table Replication]({{ link.replication.rep-methods | prepend: site.baseurl | append: "#full-table-replication" }}) will still replicate in full during every replication job, even during the initial job.

      Unless you define a different starting date for an integration, Stitch will use the integration's default starting date:

      ![Selecting a custom start date in the Integration Settings page of the Stitch app]({{ site.baseurl }}/images/replication/saas-historical-start-date-default.gif)

      The majority of integrations have a default starting date of **-1 year** from the date the integration is created. For example: If you use the integration's default date of -1 year and the date you create the integration is January 22, 2019, Stitch queue a historical replication job for data created/updated between January 22, 2018 - January 22, 2019.

---

## Historical data loads and Replication Keys



### Default starting dates {#starting-date-rollup}

In the table below (click the link to open it), you'll find a rollup of **all the default start dates for SaaS integrations.**

**To see a list of that integration's tables and the Replication Methods they use**, click the integration name.


--- 

## Uses and considerations



### Considerations



---


