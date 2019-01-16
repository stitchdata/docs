---
title: Understanding & Reducing Your Row Usage
permalink: /account-security/understanding-stitch-billing-replicated-rows
keywords: billing, bill info, payment history, tier, plan, charge, overage, row usage, replicated row, replicated rows, usage, row count
tags: [account, getting_started]

summary: "Learn the basics of Stitch billing, how to view & understand your usage, mitigate overages, and keep your row count low."
type: "billing"
toc: true
weight: 2
---
{% include misc/data-files.html %}

Much like the data part of a cell phone plan, each Stitch plan is allotted a certain number of replicated rows per month. For detailed info on pricing and what's included in each plan, refer to the [pricing page]({{ site.pricing }}) on our website.

---

## Billing basics

{% include billing/replicated-row-definition.html %}

---

## Viewing rows replicated in Stitch

{% include billing/view-usage.html %}

The **reset date** - or the day your row count will reset to zero - can be found in the **Plan Details** section of your {{ app.page-names.billing }} page, accessed by clicking the {{ app.menu-paths.billing }}.

### Understanding your usage

When viewing the number of replicated rows in Stitch, you may be surprised by the totals. You may ask yourself: _"How did Stitch replicate this many rows? There aren't that many in my source or my data warehouse!"_

Keep in mind that the total reported by Stitch is the number of **replicated** rows. The number of rows Stitch replicates is directly impacted by:

{% include replication/replicated-rows-calculation.html %}

Because Stitch counts updated rows, copies of existing rows, and rows created from de-nesting towards your total usage, the total of replicated rows and the total number of rows in your data sources or data warehouse may not be equal.

---

## Overages

{% include billing/overages.html %}

### Mitigating overages

If you've incurred overages, it may be worthwhile to temporarily upgrade your plan. When you upgrade, the change will be made immediately and you will only be billed for the difference between your current plan and the new plan, thus cancelling out the overages.

For example: You're on the Basic plan which is $500 USD/month and includes 100 million rows. One month, your Mixpanel usage exceeds expectations and a total of 240 million rows are replicated. At $10 for each million rows above the limit, this would result in a total of **$1,900 USD** ($500 for the plan, $1,400 in overages) for the month.

Temporarily upgrading to the Premier plan - which is $1,000 USD/month and includes 250 million rows - would cancel the $1,400 USD in overages, thus saving $900.

We generally recommend switching plans mid-cycle only if the overages exceed the cost of the next-highest plan.

---

## Reducing your usage

Switching to a higher plan may help you avoid overages in the short-term, but to avoid awkward conversations with your Accounts Payable co-workers, you'll need a long-term strategy to reduce your usage. Below are some simple tips we recommend for keeping your row count low.

### Reduce the Replication Frequency

The default <a href="#" data-toggle="tooltip" data-original-title="{{ site.data.tooltips.replication-frequency }}">Replication Frequency</a> for the majority of integrations is **30 minutes**. If you can manage going without the freshest data, you can dial back the interval to something less frequent - for example, every hour or every 6 hours.

Keep in mind that the Replication Frequency setting applies to the **entire integration**, not individual tables. This is especially important if there are a lot of tables that use <a href="#" data-toggle="tooltip" data-original-title="{{ site.data.tooltips.full-table-rep }}">Full Table Replication</a> in the integration.

### Check table Replication Methods

**If a database integration is eating up a lot of your row limit**, check the Replication Methods of the tables you've set to sync. Whenever possible, we recommend using <a href="#" data-toggle="tooltip" data-original-title="{{ site.data.tooltips.incremental-rep }}">Incremental Replication</a>, as this can significantly reduce the amount of redundant data replicated by Stitch.

**Note**: With the exception of Salesforce, you cannot set Replication Methods for SaaS integrations at this time. To compensate for this, you can set the integration to replicate less often.

### Get to know your SaaS integrations

While we try to use Incremental Replication for SaaS integrations whenever possible, replicating high numbers of rows is sometimes unavoidable. This can be because:

- **The integration generates massive amounts of data.** Mixpanel, for example, typically contains large amounts of data.
- **Some tables require Full Table Replication or querying for a time range** (attribution window) to ensure accuracy. 
- **The integration contains nested data structures.** If you're using a data warehouse that doesn't natively support nested structures, Stitch will de-nest these structures and create sub-rows which will result in a higher number of replicated rows.

   For an in-depth walkthrough of how JSON arrays are deconstructed in Stitch, as well as what arrays are in the first place, check out the [Handling of Nested Data Structures & Row Count Impact]({{ link.destinations.storage.nested-structures | prepend: site.baseurl }}) guide.

To find out more about your SaaS integrations' data structure and replication methods, we recommend checking out our extensive [SaaS integration docs]({{ site.baseurl }}/integrations/saas). Every SaaS integration has detailed info about the tables Stitch will replicate and the methods used to do so. 

### De-select unnecessary tables

To keep your row count down and your data warehouse tidy, you can also de-select any tables you don't need.

**Note**: This is only applicable to database integrations and the SaaS [integrations that support whitelisting]({{ link.replication.syncing | prepend: site.baseurl | append: "#integrations-that-support-whitelisting" }}), or the replication of individual tables.

### Pause integrations

If all else fails, you can temporarily pause the integration to keep from going over your row limit.

**Note**: Pausing an integration will only prevent the extraction of additional records. Loading will continue for records that have been extracted prior to the pause.

For example: If there are records currently in **Preparing** when an integration is paused, Stitch will continue to load these records, complete the current replication job, and count them towards your usage.