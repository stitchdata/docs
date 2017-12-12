---
title: Data Discrepancy Troubleshooting Guide
keywords: troubleshooting, integration, trouble, issue, help, data discrepancy, discrepancies, discrepancy guide, discrepancy
permalink: /troubleshooting/data-discrepancy-troubleshooting-guide
tags: [data_discrepancy]

summary: "If you've noticed missing or incorrect data in your data warehouse, this guide is the place to start. In it we'll walk you through the most common causes of data discrepancies, how to verify the root cause, and how to fix it. We also outline the next steps should you need to contact support."
type: "discrepancy"
weight: 1
---
{% include misc/data-files.html %}

If you're missing data, this is the place to start. 

In this article, we'll walk you through the common causes for data discrepancies and how to diagnose them. 

{% include important.html content="Note that working through this guide is required before support can begin investigating a data discrepancy. We understand how frustrating and urgent missing or incorrect data can be, but to effectively troubleshoot a discrepancy, we need your help narrowing down the possible causes." %}

---

## Data Incompatibilities

From time to time, Stitch may run into problems when attempting to load data into your destination. When data is deemed incompatible by the destination, the record will be “rejected” and logged in a table called `_sdc_rejected`. What looks like missing data may actually be a compatibility issue.

If you're missing data, the first place you should look is in the `_sdc_rejected` table in the integration's schema. [Click here]({{ link.destinations.storage.rejected-records | prepend: site.baseurl }}) for more info on this table and how to use it to troubleshoot.

---

## Data Loading

While Stitch is designed to quickly and efficiently process large amounts of data, it can take some time to replicate and load your data into your data warehouse. What looks like missing data may actually be incomplete processing, meaning Stitch hasn’t finished loading all the data.

Processing time can be affected by a variety of factors:

- The volume of data being replicated,
- The integration's [Replication Frequency]({{ link.replication.rep-frequency | prepend: site.baseurl }}), and
- API quotas (for SaaS integrations).

Most data discrepancies can be solved by simply waiting and giving Stitch time to process and load the data.

You can keep an eye on an integration's progress by using the [Replication Stats]({{ link.replication.rep-progress | prepend: site.baseurl }}) dashboard.

---

## Downtime

If a SaaS integration provider (ex: Salesforce) is undergoing maintenance or experiencing downtime, Stitch may be unable to replicate data. We recommend [checking the provider's status page]({{ link.troubleshooting.third-party-downtime | prepend: site.baseurl }}) for reported outages.

Stitch may also occasionally encounter performance issues. You can stay up-to-date with the latest by [subscribing to our status page]({{ site.status }}).

---

## Queries

Before reporting a data discrepancy to Stitch support, we recommend that you double-check how you're querying the data.

<div class="panel-group" id="accordion">
    <div class="panel panel-default">
        <div class="panel-heading">
            <h4 class="panel-title">
                <a class="noCrossRef accordion-toggle" data-toggle="collapse" data-parent="#accordion" href="#collapseSQLClient">Are you using a SQL client to directly query your data warehouse?</a>
            </h4>
        </div>
        <div id="collapseSQLClient" class="panel-collapse collapse noCrossRef">
            <div class="panel-body">
                <p>Make sure you're using a SQL client to <strong>directly query</strong> your data warehouse. This will eliminate the possibility of:</p>

                <ol>
                    <li>Report refresh lags, which can occur in visualization tools like Tableau or Mode,</li>
                    <li><a href="{{ link.troubleshooting.third-party-downtime | prepend: site.baseurl }}">Third party defects or downtime</a>, and</li>
                    <li>Any other type of data delay.</li>
                </ol>
            </div>
        </div>
    </div>
    <!-- /.panel -->
    <div class="panel panel-default">
        <div class="panel-heading">
            <h4 class="panel-title">
                <a class="noCrossRef accordion-toggle" data-toggle="collapse" data-parent="#accordion" href="#collapseStartDates">Are you querying for the same timeframe in the data source and data warehouse?</a>
            </h4>
        </div>
        <div id="collapseStartDates" class="panel-collapse collapse noCrossRef">
            <div class="panel-body">
                <p>Unless you specify a start date, the majority of SaaS integrations will sync historical data going back <strong>one year</strong> from the Stitch connection date.</p>

                <p>To verify an integration's start date, click into the integration from the {{ app.page-names.dashboard }}. Click the <strong>Settings</strong> tab, then scroll down to the <strong>Sync Historical Data</strong> section.</p>

                <img src="{{ site.baseurl }}/images/replication/sync-historical-data.png" alt="Sync Historical Data section.">

                <p>When querying in your data warehouse, check that the timeframe you're querying for matches up with the integration's start date. If you find that the integration's start date was set incorrectly, <a href="{{ link.replication.saas-historical | prepend: site.baseurl }}">you can reset it to queue a full re-sync</a>.</p>
            </div>
        </div>
    </div>
    <!-- /.panel -->
    <div class="panel panel-default">
        <div class="panel-heading">
            <h4 class="panel-title">
                <a class="noCrossRef accordion-toggle" data-toggle="collapse" data-parent="#accordion" href="#collapseTimezoneVariation">Have you accounted for any timezone variation?</a>
            </h4>
        </div>
        <div id="collapseTimezoneVariation" class="panel-collapse collapse noCrossRef">
            <div class="panel-body">
                <p>Keep in mind that your data warehouse may handle timestamp data in a specific way, even if your data source is configured to report in a specific timezone.</p>

                <p>Consider this timestamp as an example: <code>2017-08-14 11:24:02 GMT-0400 (EDT)</code></p>

                <p>Below is an explanation and example of how each data warehouse will store this same data point.</p>

                <table>
                    <tr>
                        <th width="18%; fixed">
                            Data Warehouse
                        </th>
                        <th>
                            Explanation
                        </th>
                        <th width="35%; fixed">
                            Example Timestamp
                        </th>
                    </tr>
                    <tr>
                        <td>
                            PostgreSQL
                        </td>
                        <td>
                            Timestamp data is stored as <code>TIMESTAMP WITH TIME ZONE</code> and converted to UTC using the appropriate offset for the timezone.
                        </td>
                        <td>
                            <code>2017-08-14 15:24:02</code>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            Redshift
                        </td>
                        <td>
                            Timestamp data is stored as <code>TIMESTAMP WITHOUT TIME ZONE</code> and expressed as UTC without the timezone information.
                        </td>
                        <td>
                            <code>2017-08-14 11:24:02</code>
                        </td>
                    </tr>
                </table>
            </div>
        </div>
    </div>
    <!-- /.panel -->
</div>

---

## Discrepancy Consistencies

When investigating a data discrepancy, look for consistencies such as records missing over a specific timeframe or issues that only affect certain records or data types.

For example: [formula fields in Salesforce]({{ link.troubleshooting.salesforce-formula-fields | prepend: site.baseurl }}) can occasionally cause data discrepancies due to how they're updated.

We recommend checking the [Additional & Integration Specific Resources]({{ site.baseurl }}/troubleshooting/data-discrepancies/#additional--integration-specific-resources) section for causes of common data discrepancies and how to resolve them.

---

## Replication Frequency

If the missing records were created very recently, you may need to wait for an update of your data to complete before they appear in your data warehouse.

We recommend checking the integration's [Replication Frequency]({{ link.replication.rep-frequency | prepend: site.baseurl }}), located in the {{ app.buttons.update-int-settings }} tab of the {{ app.page-names.int-details }} page. If it's set to a lower frequency like 12 hours, you may want to increase it temporarily to ensure Stitch kicks off a replication job sooner rather than later.

---

## Replication Keys

{% include note.html content="This section is only applicable to database integrations." %}

When a table in a database integration is initially set to use [Incremental Replication]({{ link.replication.rep-methods | prepend: site.baseurl | append:"#incremental-replication" }}), a Replication Key must be defined. For Stitch to accurately replicate data, Replication Keys must align with how data in the table is updated.

If the table in question is set to use Incremental Replication, keep in mind that:

1. Stitch won't capture hard deletes.
2. Replication Key columns with `NULL` values are only replicated during an integration's initial replication job.
3. Records that are updated over time should use a modification timestamp to ensure updates are captured.
4. [Mongo Replication Keys]({{ link.replication.mongo-rep-keys | prepend: site.baseurl }}) have additional considerations. For example: multiple data types in the Replication Key column can lead to missing data.
5. BigQuery destinations only support [**Append-Only Incremental Replication**]({{ link.replication.rep-methods | prepend: site.baseurl | append:"#append-only-incremental-replication" }}). What looks like duplicate data may actually be updated records being appended to a table.

---

## Contacting Support

If the discrepancy can’t be explained by any of the points above, please reach out to support. Depending on the type of discrepancy, we'll ask you to provide us some information that will help us investigate.

**Row count discrepancies** describe discrepancies that affect the number of records in your data warehouse. Complete records may be missing, duplicated, etc.

**Field value discrepancies** describe discrepancies that affect values in individual columns.

<div class="panel-group" id="accordion">
    <div class="panel panel-default">
        <div class="panel-heading">
            <h4 class="panel-title">
                <a class="noCrossRef accordion-toggle" data-toggle="collapse" data-parent="#accordion" href="#collapseRowCountDiscrepancies">Row Count Discrepancies</a>
            </h4>
            <p>For row count discrepancies, please provide us with the info in this section.</p>
        </div>
        <div id="collapseRowCountDiscrepancies" class="panel-collapse collapse noCrossRef">
            <div class="panel-body">
                <ol>
                    <li><strong>3-5 examples of records that exist in the source but not in your data warehouse</strong>. You can send us the entire record, but at the very least we need:</li>
                        <ul>
                            <li>The Primary Key</li>
                            <li>The Replication Key</li>
                            <li>The field with the discrepancy</li>
                        </ul>
                    <li>The results for the queries listed below, <strong>run in the data source</strong> for <code>[source_integration_schema].[table_name]</code>:</li>
                    {% capture queries %}
                    <ul>
                        <li><code>MIN(PRIMARY_KEY)</code></li>
                        <li><code>MAX(PRIMARY_KEY)</code></li>
                        <li><code>MIN(REPLICATION_KEY)</code></li>
                        <li><code>MAX(REPLICATION_KEY)</code></li>
                        <li><code>COUNT(*)</code></li>
                    </ul>
                    {% endcapture %}

                    {{ queries }}
                    <li>The results for the queries listed below, <strong>run in the data warehouse</strong> for <code>[data_warehouse_schema].[table_name]</code>:</li>

                    {{ queries }}

                    <li>For SaaS integrations, whenever possible, please provide us with:</li>
                    <ul>
                        <li>Raw exports showing row-level data that illustrates the discrepancy</li>
                        <li>Screenshots from the source integration’s UI that illustrate discrepancy</li>
                        <li>Exact API calls and full responses that illustrate the discrepancy (<strong>make sure you exclude your API key</strong>)</li>
                    </ul>
                </ol>
            </div>
        </div>
    </div>
    <div class="panel panel-default">
        <div class="panel-heading">
            <h4 class="panel-title">
                <a class="noCrossRef accordion-toggle" data-toggle="collapse" data-parent="#accordion" href="#collapseFieldValueDiscrepancies">Field Value Discrepancies</a>
            </h4>
            <p>For field value discrepancies, please provide us with the info in this section.</p>
        </div>
        <div id="collapseFieldValueDiscrepancies" class="panel-collapse collapse noCrossRef">
            <div class="panel-body">
                <ol>
                    <li><strong>3-5 examples of discrepancies between the source integration and your data warehouse</strong>. Please include:</li>
                        <ul>
                            <li>The record's <code>id</code></li>
                            <li>The field with the discrepancy</li>
                            <li>The <code>updated_at</code> value, if applicable</li>
                        </ul>
                    <li><strong>For database integrations:</strong></li>
                        <ul>
                            <li>Confirmation that the Replication Method is appropriately capturing changed values</li>
                            <li>Confirmation that the Replication Key is being appropriately populated and does not contain <code>NULL</code> values</li>
                        </ul>
                    <li><strong>For SaaS integrations</strong>, whenever possible, please provide us with:</li>
                        <ul>
                            <li>Raw exports showing row-level data that illustrates the discrepancy</li>
                            <li>Screenshots from the UI that illustrate discrepancy</li>
                            <li>Exact API calls and full responses that illustrate discrepancy (make sure you exclude your API key)</li>
                        </ul>
                </ol>
            </div>
        </div>
    </div>
