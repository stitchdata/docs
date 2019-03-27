---
title: Getting Started with Stitch
permalink: /getting-started/
keywords: getting started, get started, get set up, set up stitch, setup, guide
tags: [getting_started]
layout: page
toc: true
summary: "In just minutes, you can get your Stitch data pipeline up and running. Here's everything you need to know to get started."
---

{% capture ex-table %}batches{% endcapture %}
{% include misc/data-files.html %}

Welcome to Stitch!

This guide will help you get your Stitch data pipeline up and running. In this guide, you'll learn how to:

- Connect a data warehouse (we call them **destinations**)
- Connect an integration
- Configure & monitor replication
- Find additional resources and support

In this guide, we'll walk you through setting up Stitch by demonstrating how to connect a **MySQL** database integration and replicate data from it to a **Panoply** destination.

{% capture more-help %}If you have any questions not covered in this guide, check out the [rest of our documentation]({{ site.baseurl }}/ ) or reach out to our support team.{% endcapture %}

{{ more-help }}

Let's get started.

---

## Basics

A simple, powerful ETL service, Stitch connects to all your data sources -- from databases like MySQL and MongoDB, to SaaS tools like Salesforce and Zendesk -- and replicates that data to a data warehouse of your choosing. 

With Stitch, developers can provision data to analysts and team members in minutes, not weeks. Stitch takes care of source management so your developers and analysts can get back to what they do best.

To use Stitch, you need:

- A [Stitch account]({{ site.home }}),
- A [destination]({{ link.destinations.overviews.choose-destinations | prepend: site.baseurl }}), and
- An [integration]({{ site.baseurl }}/integrations)

Stitch works best when viewed on a desktop or laptop computer. To ensure the app works properly, we also recommend temporarily **pausing any ad blocking software** and **enabling pop-ups**. 

---

## Destinations

A [**destination**]({{ site.baseurl }}/destinations/) - or data warehouse - is a central repository of integrated data from disparate sources. When Stitch replicates your data, we'll load it into the destination of your choosing.

There are a few important things you should know about destinations:

- A destination is required to use Stitch
- Stitch allows **one** destination per account
- Your free trial won't officially start until data is replicated to your destination. Additionally, Stitch won't replicate data until a destination is connected.
- Stitch itself isn't a destination, and won't provide one for you

If you're new to data warehousing or you want to see how Stitch's destination offerings compare to each other, check out our [Choosing a Destination guide]({{ link.destinations.overviews.choose-destination | prepend: site.baseurl }}). This guide will help you choose the best Stitch destination for your data warehousing needs, from ensuring your data sources are compatible to staying within your budget.

[You can find setup instructions for each of our destinations here.]({{ site.baseurl }}/destinations/)

### Connect a destination

For the purpose of this guide, we'll walk you through the simplest destination to setup: [Panoply.io]({{ link.destinations.overviews.panoply | prepend: site.baseurl }}). Panoply is a cloud-hosted, fully managed data warehouse solution based on Amazon Redshift.

Some of Stitch's other destinations require a bit more time and technical expertise to configure and connect, but with just a few clicks, you can spin up a free`*` Panoply destination of your own.

- To create a new Panoply destination, [follow these instructions]({{ link.destinations.setup.panoply-new | prepend: site.baseurl }}).
- To connect an existing Panoply destination, [follow these instructions]({{ link.destinations.setup.panoply-ex | prepend: site.baseurl }}).

After you've set up a destination, you can start connecting your integrations.

---

## Integrations

An **integration** is the Stitch word for **data source**. Using Stitch's native integrations, you can replicate data from [**databases**]({{ site.baseurl }}/integrations/databases/) and [**SaaS applications**]({{ site.baseurl }}/integrations/saas/) like PostgreSQL, MongoDB, Salesforce, Zendesk, Segment, Autopilot, and more into your destination.

During your Free Trial, you'll have access to all of the integrations we offer. After your trial ends, some integrations - for example, MongoDB or Salesforce - will only be available if you select a **paid** plan.

### Don't see an integration you want?

Don't worry - there are options:

- Use the [**Import API**]({{ link.integrations.import-api | prepend: site.baseurl }}) integration to push arbitrary data into your data warehouse. You can use the IAPI to replicate data from CSV files, Google Sheets, and more.
- Use the [**Stitch Incoming Webhooks**]({{ link.integrations.stitch-incoming-webhooks | prepend: site.baseurl }}) integration to pull event data from a webhook-based service. This generic integration can be used with dozens of services.
- Check out (and contribute to) [**Singer**]({{ site.singer }}), our open-source, community-driven ETL platform. 
- Use the **Suggest Integration** button on the Integrations page in the Stitch app. We're always looking to add new integrations to our offerings.

You can find setup instructions in our [database]({{ site.baseurl }}/integrations/databases/) and [SaaS]({{ site.baseurl }}/integrations/saas/) integration docs.

### Connect a Database Integration

To provide you with a comprehensive look at how Stitch works, the rest of this guide will walk you through what the setup process would look like if a [MySQL database integration]({{ site.baseurl }}/integrations/databases/mysql) were connected to Stitch.

Connecting a database to Stitch may be a little intimidating if you're not a developer or tech-savvy. Not to worry - SaaS integrations are typically much easier to set up and you can always [invite someone from your team]({{ link.account.team-members | prepend: site.baseurl }}) to help you.

---

## Replication

The next step is to define **how** you want Stitch to replicate data from your integration. Before we walk you through how to define replication, you should know a bit about Stitch's replication process.

### Stitch's replication process

The Stitch replication process consists of three steps: extracting, preparing, and loading.

During the **Extract** part of the replication process, Stitch will use the replication settings to determine how often to replicate data, what tables and columns to replicate, and whether to replicate data incrementally or fully from the data source. We'll go into more detail about these settings in the next section.

Once the data has been extracted, it moves into the **Preparing** phase of the replication process. During this phase, Stitch will perform light transformations such as [de-nesting JSON]({{ link.destinations.storage.nested-structures | prepend: site.baseurl }}) (if applicable to your destination), [column splitting for fields with multiple data types]({{ link.destinations.storage.structure-changes | prepend: site.baseurl }}), and data typing for some integrations to ready the data for the data warehouse.

The last step is **Loading**. Stitch completes the replication process by writing the replicated data to your data warehouse in batches.

### Defining replication

Let's define the replication settings for our MySQL database integration. The following settings dictate how and how often Stitch will replicate data from your integration. It's important to be thoughtful when defining these settings, as they can impact what data is replicated from your integration and how many rows you replicate.

To extract data from your data source, you need to:

1. Define the [Replication Frequency](#replication-frequency)
2. Sync [tables and columns](#syncing-data)
3. Define [Replication Methods](#replication-methods)
4. Define [Replication Keys](#replication-keys)

#### Replication Frequency

The [**Replication Frequency**]({{ link.replication.rep-frequency | prepend: site.baseurl }}) tells Stitch how often to attempt to replicate data from an integration. For example: if set to 30 minutes, Stitch will queue a replication job roughly every half hour.

1. Click into the integration from the {{ app.page-names.dashboard }} page.
2. Click the {{ app.buttons.update-int-settings }} tab.
3. Scroll down to the **Replication Frequency** section.
4. Use the slider to select how often you want Stitch to attempt replication. We opted for every **hour**:

   ![Defining Replication Frequency.]({{ site.baseurl }}/images/getting-started/replication-frequency.png)

5. Click {{ app.buttons.save-int-settings }}.

Keep in mind that the more often an integration is set to replicate, the higher your overall row usage.

#### Replicating data

[Selecting tables and columns]({{ link.replication.syncing | prepend: site.baseurl }}) tells Stitch what data you want to replicate. If selecting tables and columns is required to finish setting up an integration, Stitch will direct you to do so after the connection has been saved.

- [**Whitelisting**]({{ link.replication.syncing | prepend: site.baseurl | append: "#integrations-that-support-whitelisting" }}) is the Stitch term for the ability to replicate specific tables and columns.
- All **database integrations** support some level of whitelisting...
- ... However, most **SaaS integrations** currently don't. For SaaS integrations that don't support whitelisting, **all available tables** will be selected for replication. Check out the **Schema** section in any of the [SaaS integration docs]({{ site.baseurl }}/integrations/saas/) to learn more about the tables Stitch pulls in.

##### Set tables and columns to replicate

1. In the {{ app.page-names.int-details }} page, click the {{ app.buttons.tables }}.
2. {{ app.menu-paths.sync }}
3. If there are [child objects]({{ link.replication.syncing | prepend: site.baseurl | append:"#parent-objects--syncing" }}), they'll automatically display and you'll be prompted to select some. 

   For example: when the `stats_service` database shown below is set to sync, the tables it contains immediately displayed and along with a prompt to sync some:

   ![Selecting a parent database.]({{ site.baseurl }}/images/getting-started/syncing-parent-object.gif)
4. Repeat this process for every table you want to replicate. **Note**: When you select a table, by default **all** columns will also be set to select.

After you set a **table** to replicate, a new window will display. This is the {{ app.page-names.table-settings }} page and contains the remaining replication settings you need to define: the Replication Method and Replication Key. **Note**: Replication Methods and Keys can only be set for tables in **database integrations.**

#### Replication Methods

{% capture rep-methods-warning %}
Before you set Replication Methods and Keys for your own database integration tables, we strongly recommend checking out the [Replication Methods]({{ link.replication.rep-methods | prepend: site.baseurl }}) and [Replication Keys]({{ link.replication.rep-keys | prepend: site.baseurl }}) articles. This guide will only give you a high-level view of both topics.

Replication Methods and Keys are the most important settings when it comes to ensuring Stitch replicates your data accurately. Incorrectly defining them can lead to data discrepancies, increased row usage, and increase the potential for latency.
{% endcapture %}

{% include important.html first-line="**Avoid discrepancies: Learn about Replication Methods and Keys**" content=rep-methods-warning %}

[**Replication Methods**]({{ link.replication.rep-methods | prepend: site.baseurl }}) tell Stitch how to replicate the data in selected tables: Fully or Incrementally.

{% include layout/inline_image.html file="getting-started/replication-methods.png" alt="Table Settings page > Replication Methods" type="right" max-width="65%" %}
##### Incremental Replication

{{ site.data.tooltips.incremental-rep | replace: "Incremental Replication","**Incremental Replication**" }} To reduce latency and keep your row count down, we recommend using Incremental Replication whenever possible.

To use Incremental Replication, the table must contain a `datetime`, `timestamp`, or `integer` column that is changed whenever data is updated. This column is called a **Replication Key** and is used to identify new and updated data for replication. We'll go into more detail about Replication Keys in the next section.

##### Full Table Replication
{{ site.data.tooltips.full-table-rep | replace: "Full Table Replication","**Full Table Replication**" }}


**Replication Methods can only be set for tables in database integrations**. Replication Methods for SaaS integration tables are set by Stitch and can't be changed. To learn more about how tables in SaaS integrations replicate, refer to the **Schema** section in the [SaaS integration docs]({{ site.baseurl }}/integrations/saas/).

In our example MySQL integration, we want to replicate the `{{ ex-table }}` table. New records are regularly created in this table, and existing records are **never** updated. To keep our row counts down while ensuring that we capture all new data in our  `{{ ex-table }}` table, we'll want to replicate using Incremental Replication. 

Next, we'll show you how to choose the appropriate Replication Key for a table.

#### Replication Keys

If you want to use Incremental Replication, you'll also need to select a [**Replication Key**]({{ link.replication.rep-keys | prepend: site.baseurl }}). {{ site.data.tooltips.replication-key }}

When Stitch replicates your data, it will store the last recorded maximum value of the Replication Key column and compare it against the data source - **not what’s in your data warehouse** - to identify new/updated data. Any row with a Replication Key value greater than or equal to the stored value is where Stitch will begin the next replication attempt.

##### Define Replication Methods and Keys

The `created_at` value in this table is populated with the present time each time a new record is created in this table. Since records are never updated, Stitch only needs to know when new data is created. Because of this, we can use `created_at` as the Replication Key for the `{{ ex-table }}` table.

1. {{ app.menu-paths.sync }}
2. When the {{ app.page-names.table-settings }} page displays, select the **Incremental Replication** option.
3. In the drop-down menu, select the column to be used as the table's **Replication Key**.
4. Click {{ app.buttons.save-table-settings }}.

Here's how we set the `{{ ex-table }}` table to use Incremental Replication based on the Replication Key of `created_at`:

![Syncing & Defining Incremental Replication.]({{ site.baseurl }}/images/getting-started/syncing-replication-method.gif)

---

## Monitor the replication process

After you initially connect an integration, you might see a **Pending** status in the **Last Sync Status** field on the {{ app.page-names.dashboard }} page or on the {{ app.page-names.int-details }} page:

![Newly connected integration with Pending Sync status.]({{ site.baseurl }}/images/getting-started/new-pending-integration.png)

A **Pending** status indicates that Stitch is in the process of scheduling a replication job for the integration. For newly created integrations, this can take up to 30 minutes.

### Initial/Historical data loads

During the initial replication job, Stitch will replicate the integration's historical data. Historical syncs tend to be larger in volume compared to subsequent replication jobs, and as a result may take longer to process and load into your data warehouse. It's normal to see a large spike in replicated rows during this time.

After the Free Trial ends, any new integrations you create will replicate data free for seven days. [Refer to the Billing FAQ]({{ link.billing.billing-faq | prepend: site.baseurl | append: "#integrations" }}) for more info.

### Ongoing replication jobs

After the integration's historical replication completes, you can expect the number of replicated rows for the integration to decrease and eventually level out. The time it takes for Stitch to extract, prep, and load data should also decrease.

{% include replication/replication-stats-copy.html %}

---

## What's Next?

Congratulations! You set up a destination, connected an integration, and configured the replication settings. Stitch will soon begin replicating your data.

While you wait for the initial sync to complete, we recommend:

### Learning About Stitch billing

Our pricing is built on the number of replicated rows Stitch loads into your data warehouse. But what does "replicated row" mean? How can you keep your row count low? [Check out the Understanding Your Usage guide]({{ link.billing.billing-guide | prepend: site.baseurl }}) to learn more about Stitch billing and how to reduce your usage.

### Getting to know your destination

Every destination handles data differently, which will impact how Stitch loads and stores the data it replicates from your integrations. [**Check out the Destination Data Loading guide**]({{ link.destinations.storage.loading-data | prepend: site.baseurl }}) for the specifics on your destination.

### Getting to know your SaaS integrations

Just like destinations, every SaaS integration structures its data differently. How Stitch replicates and loads SaaS data depends in part on how that data is created and structured. [**Our extensive SaaS integration docs**]({{ site.baseurl }}/integrations/saas/) cover what Stitch will replicate and how.

### Selecting an Analysis Integration

If your end-goal is to analyze or interact with the data Stitch replicates, you'll need an additional tool. [**Check out our list of Analysis Integration Partners**]({{ site.baseurl }}/analysis-integrations/) to find the visualization, analysis, or data science tool that's right for you.

---

## Documentation & Support

{{ more-help }}
