---
title: Choosing a Destination
permalink: /destinations/choosing-a-stitch-destination

redirect_from: /destinations/choosing-a-destination
keywords: destination, destinations, data warehouse, data warehouses, warehouse, stitch etl, etl, compare destinations, choose destination, select destination
summary: "If you're new to data warehousing or want to see how Stitch's destination offerings compare to each other, look no further. This guide will help you choose the best Stitch destination for your data warehousing needs."

content-type: "destination-general"
key: "choose-a-destination"

toc: true
layout: general
type: "all"
destination: false

intro: |
  {% capture data-strategy%}
  If you're feeling overwhelmed or you're unsure of what to look for, don't worry. For a primer on data warehouses and setting the data strategy for your organization, check out our [Data Strategy Guide]({{ site.data-strategy }}).
  {% endcapture %}

  {% include note.html first-line="**Not sure where to start?**" content=data-strategy %}

  When Stitch replicates your data, we'll load it into the destination of your choosing.

  **As Stitch currently only allows you to connect one destination to your account**, we recommend asking yourself the questions below before making your selection. By fully assessing each choice first, you'll decrease the likelihood of needing to switch destinations or re-replicate all of your data at a later date.

  In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}

sections:
  - title: "Side-by-side comparison"
    anchor: "compare-destinations"
    summary: "A high-level look at each of Stitch's destinations"
    content: |
      The following tabs contain a high-level look at each of Stitch's destinations and how they compare to each other.

      The remaining sections of this guide expand on the information in these tabs.

      {% include destinations/overviews/choosing-a-destination-rollup.html %}

  - title: "Destination and data source compatibility"
    anchor: "integration--destination-compatibility"
    summary: "Compatibility for each of Stitch's integrations and destinations"
    content: |
      Some integrations may be partially or fully incompatible with some of the destinations offered by Stitch. For example: Some destinations don't support storing multiple data types in the same column. If a SaaS integration sends over a column with mixed data types, some destinations may "reject" the data.

      For integrations that allow you to control how data is structured, you may be able to fix the problem at the source and successfully replicate the data. If this is not possible, however, Stitch may never be able to successfully replicate the incompatible data.

      Refer to the [Integration and destination compatibility reference]({{ link.destinations.overviews.compatibility | prepend: site.baseurl }}) for more info.

  - title: "Destination and analysis tool compatibility"
    anchor: "destination--tool-compatibility"
    summary: "Support for analysis tools with each of Stitch's destinations"
    content: |
      You may want to investigate whether your prefered analysis tool supports a native connection to your Stitch destination. We've investigated some popular options for you. See the [Analysis tools reference]({{ site.baseurl }}/analysis-tools/#analytics) for more about using popular analysis tools with Stitch.

      {% include analysis-tools/destination-compatibility.html %}

  - title: "Replication, transformations, and data structure"
    anchor: "replication-transformations"
    summary: "How data is replicated and structured for each destination"
    content: |
      While the majority of your data will look the same across our destinations, there are some key differences you should be aware of:

      {% for subsection in section.subsections %}
      - [{{ subsection.summary }}](#{{ subsection.anchor }})
      {% endfor %}
    subsections:
      - title: "Loading behavior and updates to existing records"
        anchor: "incremental-and-append-only-replication"
        summary: "How updates to existing records are handled"
        content: |
          Loading behavior determines how data is loaded into your destination. Specifically, how updates are made to existing rows in the destination.

          Stitch supports two loading behavior types:

          - **Upsert**: {{ site.data.tooltips.upsert }}
          - **Append-Only**: {{ site.data.tooltips.append-only }}

          The table below lists the default loading behavior for each destination and whether it can be configured.

          {% include misc/icons.html %}

          **Note**: If a destination supports and is configured to use Upsert loading, Stitch will attempt to use Upsert loading before Append-Only. All [other conditions for Upsert loading]({{ link.destinations.storage.loading-behavior | prepend: site.baseurl }}#upsert-loading-conditions) must also be met.

          Refer to the [Understanding loading behavior guide]({{ link.destinations.storage.loading-behavior | prepend: site.baseurl }}) for more info and examples of each loading bheavior type.

          {% assign attributes = "Destination|Version|Default loading behavior|Loading behavior is configurable?" | split:"|" %}

          {% assign destinations = site.destinations | where:"destination",true | sort_natural:"display_name" %}

          <table class="attribute-list">
          <tr>
          {% for attribute in attributes %}
          {% if forloop.first == true %}
          <td align="right">
          {% else %}
          <td>
          {% endif %}
          <strong>{{ attribute }}</strong>
          </td>
          {% endfor %}
          </tr>
          {% for destination in destinations %}
          {% assign version = destination.this-version | prepend: "v" %}
          <tr>
          <td align="right">
          <strong>{{ destination.display_name }}</strong>
          </td>
          <td width="15%; fixed">
          {{ version }}
          </td>
          <td width="20%; fixed">
          {{ site.data.destinations[destination.type][version]replication.default-loading-behavior }}
          </td>
          <td width="25%; fixed">
          {% case site.data.destinations[destination.type][version]replication.configurable-loading-behavior %}
          {% when true %}
          {{ supported | replace:"TOOLTIP","Loading behavior is configurable for this destination and version." }}
          {% when false %}
          {{ not-supported | replace:"TOOLTIP","Loading behavior is not configurable for this destination and version." }}
          {% endcase %}
          </td>
          </tr>
          {% endfor %}
          </table>

      - title: "Nested data structures"
        anchor: "nested-data-structures"
        summary: "How destinations handle nested data structures"
        content: |
          Some destinations don't natively support nested structures, meaning that before Stitch can load replicated data, these structures must be "de-nested". During this process, Stitch will flatten nested structures into relational tables and subtables. As a result of creating subtables, a higher number of rows will be used.

          If a destination does natively support nested structures, no de-nesting will occur and Stitch will store the records intact.

          Check out the [Handling of Nested Data & Row Count Impact guide]({{ link.destinations.storage.nested-structures | prepend: site.baseurl }}) for an in-depth look at what we mean by nested records, how Stitch handles nested data, and what those records will look like in your data warehouse.

          {% assign attributes = "Destination|Version|Support|Notes" | split:"|" %}

          <table class="attribute-list">
          <tr>
          {% for attribute in attributes %}
          {% if forloop.first == true %}
          <td width="30%; fixed" align="right">
          {% else %}
          <td>
          {% endif %}
          <strong>{{ attribute }}</strong>
          </td>
          {% endfor %}
          </tr>
          {% for destination in destinations %}
          {% assign version = destination.this-version | prepend: "v" %}
          {% assign destination-replication = site.data.destinations[destination.type][version]replication %}
          <tr>
          <td align="right">
          <strong>{{ destination.display_name }}</strong>
          </td>
          <td width="12%; fixed">
          {{ version }}
          </td>
          <td>
          {% case destination-replication.nested-structure-support %}
          {% when true %}
          {{ supported | replace:"TOOLTIP","Nested data structures are natively supported." }}
          {% when false %}
          {{ not-supported | replace:"TOOLTIP","Nested data structures aren't natively supported." }}
          {% else %}
          {{ not-applicable | replace:"TOOLTIP","See Notes column for more info." }}
          {% endcase %}
          </td>
          <td>
          {{ destination-replication.nested-structure-support-description | flatify | markdownify }}
          </td>
          </tr>
          {% endfor %}
          </table>

  - title: "Maintenance and support"
    anchor: "setup--maintenance"
    summary: "A high-level look at each destination provider's maintenance and support offerings"
    content: |
      With the exception of a self-hosted PostgreSQL instance, all the destinations offered by Stitch are cloud-hosted databases, meaning you won't have to factor in server maintenance when making a decision.

      In the table below are:

      - **Fully-managed destinations** that include routine maintenance and upgrades in their plans
      - **DIY destinations** that will require you to perform and schedule maintenance tasks on your own

      <table class="attribute-list">
      <tr>
      <td width="50%; fixed">
      <strong>Fully-managed destinations</strong>
      </td>
      <td>
      <strong>DIY destinations</strong>
      </td>
      </tr>
      <tr>
      <td>
      <ul>
      {% for destination in destinations %}
      {% if site.data.destinations[destination.type]destination-details.fully-managed == true %}
      <li>{{ destination.display_name }}</li>
      {% endif %}
      {% endfor %}
      <li>PostgreSQL (Heroku, Amazon RDS, Amazon Aurora)</li>
      </ul>
      </td>
      <td>
      <ul>
      {% for destination in destinations %}
      {% if site.data.destinations[destination.type]destination-details.fully-managed == false %}
      <li>{{ destination.display_name }}</li>
      {% endif %}
      {% endfor %}
      <li>PostgreSQL (self-hosted)</li>
      </ul>
      </td>
      </tr>
      </table>

  - title: "Destination pricing models"
    anchor: "pricing"
    summary: "Pricing for each destination type"
    content: |
      Every destination offered by Stitch has its own pricing structure. Some providers charge by overall usage, others by an hourly rate or the amount of stored data. Depending on your needs, some pricing structures may fit better into your budget.

      In the next section, you'll find each destination's pricing structure, including a link to detailed price info and whether a free option (trial or plan) is available. Here are a few things to keep in mind:

      {% assign attributes = "Destination|Version|Pricing model|Notes" | split:"|" %}

      <table class="attribute-list">
      <tr>
      {% for attribute in attributes %}
      {% if forloop.first == true %}
      <td width="30%; fixed" align="right">
      {% else %}
      <td>
      {% endif %}
      <strong>{{ attribute }}</strong>
      </td>
      {% endfor %}
      </tr>
      {% for destination in destinations %}
      {% assign version = destination.this-version | prepend: "v" %}
      <tr>
      <td class="attribute-name">
      <strong>{{ destination.display_name }}</strong>
      </td>
      <td>
      {{ version }}
      </td>
      <td>
      {{ site.data.destinations[destination.type]destination-details.pricing-model | flatify | markdownify }}
      </td>
      <td class="attribute-description">
      {{ site.data.destinations[destination.type]destination-details.pricing-details | flatify | markdownify }}
      {% if destination.type == "bigquery" %}
      To learn more about how Stitch may impact your BigQuery costs, <a href="{{ link.destinations.overviews.bigquery-pricing | prepend: site.baseurl }}">click here</a>.
      {% endif %}
      </td>
      </tr>
      {% endfor %}
      </table>

  - title: "Getting started, now"
    anchor: "getting-started-now"
    summary: "How to get started without any technical know-how"
    content: |
      If you simply want to try Stitch and Redshift, or if you don't have the ability to spin up a Redshift cluster of your own in AWS, we recommend trying [Panoply]({{ link.destinations.overviews.panoply | prepend: site.baseurl | append: "#setup" }}). With just a few clicks, you create your own fully-managed Redshift data warehouse and start replicating data in minutes.

      **Note**: If you decide to [switch destinations]({{ link.destinations.overviews.switch-destination | prepend: site.baseurl }}) later, you'll need to queue a full re-replication of your data to ensure historical data is present in the new destination.

  - title: "Additional resources and setup tutorials"
    anchor: "additional-resources"
    summary: "Some additional resources and setup tutorials"
    content: |
      Ready to pick a destination and get started? Use the links below to check out a more in-depth look at each destination or move on to the setup and connection process.

      {% include destinations/destination-tiles.html %}
---
{% include misc/data-files.html %}
{% assign destinations = site.destinations | where:"destination",true | sort: "display_name" %}