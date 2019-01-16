---
title: Syncing New & Additional Columns on Already-Syncing Tables
permalink: /replication/syncing-new-additional-columns
keywords: syncing, sync, replicate, replication, select data, sync data, sync table, sync column, add new columns, sync new column, add additional columns
tags: [replication]
layout: general

content-type: "select-data"
toc: true
weight: 3

summary: "What happens when you add a brand-new column in a data source or you want to replicate additional columns on an already-replicating table? How will your row count be impacted? In this guide, we cover how Stitch handles new columns, what you can expect for existing rows, and how to backfill data."

sections:
  - content: |
      When you add a new column to a table in your data source, what happens in Stitch? What about replicating additional columns on already-replicating tables? Depending on the type of integration and the [Replication Method]({{ link.replication.rep-methods | prepend: site.baseurl }}) the table uses, there are a few possible outcomes.

      In this guide, we'll cover the scenarios listed below and how these factors impact replication.

  - title: "Scenario {{ forloop.index | minus: 1 }}: New columns in the data source"
    anchor: "scenario--new-columns-data-source"
    content: |
      When a new column is added in a data source, it may take some time before it is available in selection in Stitch. A replication job must first run, during which Stitch will perform a structure sync to detect the new column. The column will be available for selection after the job completes.  

      For some integrations, Stitch will automatically set new columns to replicate. Refer to the tabs below for more info.

      {% assign salesforce = singer-saas | where:"name","salesforce" %}

      {% assign non-singer-saas-integrations = site.saas-integrations | where:"singer",false | sort:"title" %}

      {% assign singer-saas = site.saas-integrations | where:"singer",true %}
        {% assign singer-saas-without-column-selection = singer-saas | where:"column-selection",false | sort:"title" %}

      {% assign categories = "non-singer-saas-integrations|singer-saas-without-column-selection" | split:"|" %}

      <ul id="profileTabs" class="nav nav-tabs">
          <li class="active">
          <a href="#integrations-with-automatic-selection" data-toggle="tab">Integrations with automatic selection</a>
          </li>
          <li>
          <a href="#integrations-without-automatic-selection" data-toggle="tab">Integrations without automatic selection</a>
          </li>
      </ul>
      <div class="tab-content">
      <div role="tabpanel" class="tab-pane active" id="integrations-with-automatic-selection">
      <table class="attribute-list">

      <tr>
      <td colspan="4">
      <a href="{{ link.integrations.databases | prepend: site.baseurl }}"><strong>All database integrations</strong></a>
      </td>
      </tr>

      <tr>
      <td colspan="4">
      <a href="{{ link.integrations.webhooks | prepend: site.baseurl }}"><strong>All webhook integrations</strong></a>
      </td>
      </tr>

      {% for integration in salesforce %}
      <tr>
      <td colspan="4">
      <a href="{{ integration.url | prepend: site.baseurl }}">{{ integration.display_name }}</a>
      </td>
      </tr>
      {% endfor %}

      {% for category in categories %}
      <tr>
      <td colspan="4">
      <strong>{{ category | replace:"-"," " | capitalize | replace:"saas","SaaS" | replace:"Non singer","Non-Singer" }}</strong>
      </td>
      </tr>

      {% for integration in [category] %}
      {% assign integration-number = forloop.index | modulo: 4 %}
      {% if integration-number == 1 %}
      <tr>
      {% endif %}
      <td>
      <a href="{{ integration.url | prepend: site.baseurl }}">{{ integration.title }}</a>
      </td>

      

      {% if integration-number == 0 %}
      </tr>
      {% endif %}

      {% endfor %}
      {% endfor %}

      </table>
      </div>
      </div>


# <div role="tabpanel" class="tab-pane" id="integrations-without-automatic-selection">
# #     TAB TWO
# # </div>

# Not automatically selected:
# - Singer SaaS with column selection (column-selection == true)
#   {% assign signer-saas-with-columns = site.saas-integrations | where_exp:"integration","integration.singer == true and integration.column-selection == true" %}

# - Salesforce (depends on setting)
#   {% assign non-automatic-integrations = signer-saas-with-columns | concat: salesforce | sort:"title" %}


  - title: "Scenario {{ forloop.index | minus: 1 }}: Additional columns in already-replicating tables" 
    anchor: "scenario--selecting-additional-columns"
    content: |
      In this scenario, you set a previously existing, never-before-replicated column to replicate in an already-replicating table. This column contains historical data for existing records.

      The [Replication Method]({{ link.replication.rep-methods | prepend: site.baseurl }}) the table uses determines how data for the additional column is replicated.

    subsections:
      - title: "Full Table Replication"
        anchor: "additional-columns--full-table"
        content: |
          For tables using [Full Table Replication]({{ link.replication.full-table | prepend: site.baseurl }}), data for the newly-selected column will be available for all records the next time a replication job for the table completes. This includes new and existing records.

      - title: "Key-based Incremental Replication"
        anchor: "additional-columns--key-based-incremental"
        content: |
          For tables using [Key-based Incremental Replication]({{ link.replication.key-based-incremental | prepend: site.baseurl }}), data for the newly-selected column will be available for records that are added or modified after last saved maximum Replication Key value for the table. If the integration supports [Loading Reports]({{ link.replication.loading-reports | prepend: site.baseurl }}), you can view this value in the integration's Loading Reports tab.

          Records added or modified before this will have `null` values in the newly selected column. To replicate historical data for the new column, you'll need to backfill the column by [resetting the table]({{ link.replication.reset-rep-keys | prepend: site.baseurl }}).

      - title: "Log-based Incremental Replication"
        anchor: "additional-columns--log-based-incremental"
        content: |
          To replicate additional columns in tables using [Log-based Incremental Replication]({{ link.replication.log-based-incremental | prepend: site.baseurl }}), you'll need to [reset the table]({{ link.replication.reset-rep-keys | prepend: site.baseurl }}).

          Any change that alters the destination table's schema requires a reset [to accommodate how Log-based Replication works]({{ link.replication.log-based-incremental | prepend: site.baseurl | append: "#limitation-3--structural-changes" }}).

          After the table is reset, the next replication job will fully re-replicate the table. Historical values for the column will be available for all records, and going forward, values for new and modified records will be replicated.
---
{% include misc/data-files.html %}