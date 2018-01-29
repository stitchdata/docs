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

The last phase of every Stitch replication job is called **Loading**. During Loading, Stitch completes the following:


The **Loading Reports** tab - accessed by clicking into the integration from the {{ app.page-names.dashboard }} - provides detail about the loading portion of the replication process for a given integration.

---

## Report Retention

Loading reports are grouped by day. The number of days' worth of logs available to you depends on your Stitch plan:

{% for plan in stitch.subscription-plans.all-plans %}
- **{{ plan.name }}**: {{ plan.reports }}
{% endfor %}

### Report and Plan Changes

Changing your plan can impact reports currently available to you.

### Plan Downgrades

If you downgrade to a plan that offers fewer days' reports, you'll **lose** access to the difference between your current plan and your new plan.

For example: If you downgrade to Free from the Starter plan, you'll lose access to six days' worth of reports.

### Plan Upgrades

Likewise, if you upgrade to a plan that offers more days' reports, you'll immediately **gain** access to the difference.

For example: If you upgrade to Basic from the Free plan, you'll gain access to an additional six days' worth of reports.

---

## Report Composition

### Loading Report Columns

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
            <strong>{{ field.name }}</strong>
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