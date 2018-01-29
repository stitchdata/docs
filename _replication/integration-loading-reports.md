---
title: Loading Reports
permalink: /replication/integration-loading-reports
keywords: replication, load, loading, report
tags: [replication]
summary: "Loading reports provide detail about the loading protion of the replication process for a given integration."

type: "monitoring"
toc: true
weight: 3
---
{% include misc/data-files.html %}

{% include note.html content="Loading reports are available only for integrations powered by Singer taps. As integrations are converted to the Singer system, loading reports will be made available." %}

The last phase of every Stitch replication job is called **Loading**. During Loading, Stitch loads [extracted data]({{ link.replication.extraction-logs | prepend: site.baseurl }}) into your destination according to the table's defined [Replication Method]({{ link.replication.rep-methods | prepend: site.baseurl }}):

- **Incremental Replication**: Data is de-duped based on the table's Primary Key and upserted into the table. Updates to existing records are also upserted.
- **Full Table Replication**: New data overwrites the table in its entirety.
- **Append-Only Replication**: Data is appended to the end of the table.

The **Loading Reports** tab - accessed by clicking into the integration from the {{ app.page-names.dashboard }} - provides detail about the loading portion of the replication process for a given integration.

---

## Report Retention

Loading reports are grouped by day. The number of days' worth of logs available to you depends on your Stitch plan:

{% for plan in stitch.subscription-plans.all-plans %}
- **{{ plan.name }}**: {{ plan.reports }}
{% endfor %}

### Report and Plan Changes

Changing your plan can impact reports currently available to you.

#### Plan Downgrades

If you downgrade to a plan that offers fewer days' reports, you'll **lose** access to the difference between your current plan and your new plan.

For example: If you downgrade to Free from the Starter plan, you'll lose access to six days' worth of reports.

#### Plan Upgrades

Likewise, if you upgrade to a plan that offers more days' reports, you'll immediately **gain** access to the difference.

For example: If you upgrade to Basic from the Free plan, you'll gain access to an additional six days' worth of reports.

---

## Report Composition

Every row in the Loading Reports tab corresponds to a single table that is set to replicate. The data in this row is updated upon every successful load to your destination.

[Image here when UI is ready]

### Loading Report Columns

Loading reports are made up of four columns, which are explained in the table below.

{% assign loading-reports = site.data.ui.loading-reports %}

<table>
    <tr>
        <td width="20%; fixed" align="right">
            <strong>Column Name</strong>
        </td>
        <td>
            <strong>Example</strong>
        </td>
        <td width="55%; fixed">
            <strong>Description</strong>
        </td>
    </tr>
    {% for field in loading-reports.fields %}
    <tr>
        <td align="right">
            <strong>{{ field.name | markdownify }}</strong>
        </td>
        <td>
            {{ field.example | markdownify }}
        </td>
        <td>
            {{ field.description | flatify | markdownify }}
        </td>
    </tr>
    {% endfor %}
</table>

### Loading Data for Subtables

To view the number of rows loaded for subtables, click the <i class="fa fa-plus-square" aria-hidden="true"></i><span class="sr-only">Plus icon</span> icon next to the total rows loaded:

[GIF will go here when UI is ready]

Subtables are created by Stitch based on the structure of the data in the source and your destination. Read more about subtables in the [Nested Data and Row Counts guide]({{ link.destinations.storage.nested-structures | prepend: site.baseurl }}).

### View Non-Replicating Tables

{% include layout/inline_image.html type="right" file="replication/loading-reports-time-range.png" alt="Rows Loaded time range selection" %}Loading data for tables that may be available if the time of the last load is within the selected **Rows Loaded** range.

For example: If the last load occurred less than 24 hours ago, the table's loading data will display when **24 hours** is selected.

Otherwise, the table's loading data will be available based on your plan's [report retention period](#report-retention). For example: If you're on the Starter plan and a load occurred less than 7 days ago, you can select the **Billing Period** option to view the last load for the table.

---

## Loading Errors

If an error occurs during the loading process, an [ICON] will display to the left of the affect table(s). To view the error for the table, click the icon.

[IMAGE when UI is ready]

If an error arises, check out our [troubleshooting guides]({{ link.troubleshooting.main | prepend: site.baseurl }}) for help.