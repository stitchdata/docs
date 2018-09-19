---
title: Replicating Database Views
permalink: /replication/replicating-database-views
keywords: replicate, replication, replicate views, view, database view, replicate database view
tags: [replication]

summary: "Replicating a database view is almost the same as replicating a database table. In this guide, we'll cover the database integrations that support views and the additional steps required to replicate a database view."
type: "syncing"
toc: true
weight: 3
---
{% include misc/data-files.html %}

{% capture db-views%}
Database views can be replicated from the following database integrations only:

{% assign all-databases = site.database-integrations | where:"input",true %}
{% assign databases-with-view-support = all-databases | where:"view-replication",true | sort:"display_name" %}

{% for integration in databases-with-view-support %}
- [{{ integration.display_name }}]({{ integration.url | prepend: site.baseurl }})
{% endfor %}
{% endcapture %}
{% include note.html first-line="**Supported databases**" content=db-views %}

While the steps for replicating a database view are [almost the same as those for replicating a table]({{ link.replication.syncing | prepend: site.baseurl }}), there are some slight differences.

---

## Verify the database user's permissions

To replicate the view, the Stitch database user must have the appropriate level of permissions to access it.

**If you don't see the view you want in the Stitch app**, it may be because the Stitch user has insufficient permissions. Verify that the Stitch user's permissions and, if necessary, grant any that are missing.

For a refresher on the permissions Stitch needs, refer to the articles linked below:

{% for integration in databases-with-view-support %}
- [{{ integration.display_name }}]({{ integration.url | prepend: site.baseurl | append: "#create-stitch-db-user" }})
{% endfor %}

--- 

## Set the view to replicate

Note that any [parent objects]({{ link.replication.syncing | prepend: site.baseurl | append: "#parent-objects--syncing" }}) - like the database containing the view - must also be set to replicate. If they aren't, set them to replicate before continuing.

1. Click into the database integration from the {{ app.page-names.dashboard }} page.
2. Navigate to the view you want to replicate.
3. Click the icon next to the **Sync Status** column to set the view to replicate.
3. Once a view has been set to replicate, the **View Settings** page will display.

---

## Define the view's Primary Key setting

Next, you'll define the Primary Key setting for the view. There are two options:

- **No Primary Key:** If selected, the view will be replicated using [Append-Only Incremental Replication]({{ link.replication.rep-methods | prepend: site.baseurl | append: "#append-only-incremental-replication" }}). This means that existing rows will not be updated, and any new rows will be appended to the end of the table.
- **Custom Primary Key:** If selected, the field or fields you define will be used as the view's Primary Keys. To add additional fields, click the **Add** button.

Note that you can change the Primary Key setting - including adding or removing fields to the Custom Primary Key - at any time, but **doing so will require a full re-replication of the view**. This is to ensure that there aren't any gaps in the data.

---

## Define the view's Replication Method

The last step is to define the Replication Method for the view:

- [**Incremental Replication**]({{ link.replication.rep-methods | prepend: site.baseurl | append: "#incremental-replication" }}): If selected, Stitch will only replicate new and/or updated data (based on the [Replication Key]({{ link.replication.rep-keys | prepend: site.baseurl }}) you define) during every replication attempt. When using Incremental Replication, keep in mind that:
   - **Replication Keys are required to use Incremental Replication**. When Stitch replicates your data, it will store the last recorded maximum value in the Replication Key column and compare it against the data source - **not what's in your data warehouse** - to identify new/updated data. Any row with a Replication Key value greater than or equal to the stored value is where Stitch will begin the next replication attempt.
   - If no Primary Key is selected for the view, data will be replicated using [Append-Only Incremental Replication]({{ link.replication.rep-methods | prepend: site.baseurl | append: "#append-only-incremental-replication" }})
- [**Full Table Replication**]({{ link.replication.rep-methods | prepend: site.baseurl | append: "#full-table-replication" }}): If selected, Stitch will replicate the entire contents of the view on every replication attempt. As this can increase latency and quickly use up your row limit, it's the most inefficient way to use Stitch. 

After you've finished defining the view's settings, click **Save Settings**.