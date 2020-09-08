---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Replication Scheduling for Tables
permalink: /replication/replication-scheduling/scheduling-for-tables
keywords: replicate, replication, replication frequency, frequency, anchor time, scheduling, schedule, interval, change replication time, schedule tables
summary: "A workaround for replicating sets of tables on different schedules."

key: "table-scheduling"
content-type: "replication-scheduling"
method: false

layout: tutorial
use-tutorial-sidebar: false
toc: true
weight: 5


# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  Replication scheduling is currently supported only at the integration level. This means that when Stitch runs a replication job, all selected tables will be replicated.

  If you want to replicate data for tables on different schedules, you can create two integrations and configure the schedules to match your needs. This can be useful for reducing your row usage or simply replicating data only when you need it.

  The method outlined in this tutorial can be used with all [Replication Scheduling types]({{ link.replication.rep-scheduling | prepend: site.baseurl }}).

  ---

  ## Example use cases

  - Reducing your overall row usage
  - Reducing re-replication of tables using [Full Table Replication]({{ link.replication.full-table | prepend: site.baseurl }})
  - Replicating different data sets at different intervals


# -------------------------- #
#       REQUIREMENTS         #
# -------------------------- #

requirements:
  - item: |
      **An integration that supports table selection.** This tutorial is applicable only to [database]({{ site.baseurl }}/integrations/databases) and [SaaS]({{ site.baseurl }}/integrations/saas) integrations that support table selection.

      {% capture important-callout %}
      The method outlined in this tutorial can cause data discrepancies for PostgreSQL tables using Log-based Incremental Replication due to how replication slots function. Refer to the [Log-based Incremental Replication documentation]({{ link.replication.log-based-incremental | prepend: site.baseurl | append: "#limitation-8--replication-slot-data-loss-postgresql" }}) for more info before proceeding.
      {% endcapture %}

      {% include important.html first-line="**PostgreSQL and Log-based Incremental Replication**" content=important-callout %}
  - item: |
      **An integration that supports multiple connections.** Some integrations may only allow one connection at a time. For example: [NetSuite]({{ site.baseurl }}/integrations/saas/netsuite-suitetalk) only allows a user to have a single API session open at any given time.


# -------------------------- #
#          CONTENT           #
# -------------------------- #

steps:
  - title: "Create the first integration"
    anchor: "create-the-first-integration"
    content: |
      In this step, you'll create the first integration in [your Stitch account]({{ site.sign-in }}){:target="new"}. Refer to the [database]({{ site.baseurl }}/integrations/databases) or  [SaaS]({{ site.baseurl }}/integrations/saas) documentation for instructions.

  - title: "Define the first integration's schedule"
    anchor: "define-first-integration-schedule"
    content: |
      Next, define the integration's replication schedule. You can use any of Stitch's supported replication scheduling methods: [Replication Frequency]({{ link.replication.rep-frequency | prepend: site.baseurl }}), [Anchor Scheduling]({{ link.replication.anchor-scheduling | prepend: site.baseurl }}), or [Advanced Scheduling]({{ link.replication.advanced-scheduling | prepend: site.baseurl }}).

      When finished, save the integration.

  - title: "Set tables to replicate"
    anchor: "set-tables-to-replicate"
    content: |
      After you've saved the first integration, you'll be prompted to [set tables (and columns, if supported) to replicate]({{ link.replication.syncing | prepend: site.baseurl }}).

      Select the tables and columns you want to replicate according to the [schedule you defined in Step 2](#define-first-integration-schedule).

  - title: "Repeat steps 1-3"
    anchor: "repeat-steps-1-3"
    content: |
      Lastly, repeat steps 1-3 to create a second integration, define its replication schedule, and set tables to replicate. This will allow you to select a different table or set of tables and replicate them on a schedule separate from the first integration.
---