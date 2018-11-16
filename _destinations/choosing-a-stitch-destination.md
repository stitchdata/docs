---
title: Choosing a Destination
permalink: /destinations/choosing-a-stitch-destination
tags: [destinations]
keywords: destination, destinations, data warehouse, data warehouses, warehouse, stitch etl, etl, compare destinations, choose destination, select destination
summary: "If you're new to data warehousing or want to see how Stitch's destination offerings compare to each other, look no further. This guide will help you choose the best Stitch destination for your data warehousing needs."

content-type: "destination-general"

toc: true
type: "all"
destination: false

sections:
  - content: |
      {% capture data-strategy%}
      **Not sure where to start?**<br>
      If you're feeling overwhelmed or you're unsure of what to look for, don't worry. For a primer on data warehouses and setting the data strategy for your organization, check out our [Data Strategy Guide]({{ site.data-strategy }}).
      {% endcapture %}

      {% include tip.html content=data-strategy %}

      When Stitch replicates your data, we'll load it into the destination - or data warehouse - of your choosing. A data warehouse is a central repository of integrated data from disparate sources.

      **As Stitch currently only allows you to connect one destination to your account**, we recommend asking yourself the questions below before making your selection. By fully assessing each choice first, you'll decrease the likelihood of needing to switch destinations or re-replicate all of your data at a later date.

       - [Does it support all (or most of) your data sources](#integration--destination-compatibility)?
       - [Will the structure of the data replicated by Stitch work with how you plan to use it](#data-structure)?
       - [Do you need a fully-managed solution, or can you perform maintenance tasks on your own](#setup--maintenance)?
       - [Is the destination's pricing structure suitable](#pricing)?

  - title: "Side-by-side comparison"
    anchor: "compare-destinations"
    content: |
      In the tabs below is a quick look at each of Stitch's destinations and how they compare to each other.

      The remaining sections of this guide expand on the information in these tabs.

      {% include destinations/destination-rollup.html %}

  - title: "Getting started, now"
    anchor: "getting-started-now"
    content: |
      If you simply want to try Stitch and Redshift, or if you don't have the ability to spin up a Redshift cluster of your own in AWS, we recommend trying [Panoply]({{ link.destinations.overviews.panoply | prepend: site.baseurl | append: "#setup" }}). With just a few clicks, you create your own fully-managed Redshift data warehouse and start replicating data in minutes.

      Keep in mind that switching to a different destination at any point will require a full re-replication of your data.

  - title: "Are your data sources compatible with your destination?"
    anchor: "integration--destination-compatibility"
    content: |
      Some integrations may be partially or fully incompatible with some of the destinations offered by Stitch. For example: Some destinations don't support storing multiple data types in the same column. If a SaaS integration sends over a column with mixed data types, some destinations may "reject" the data.

      For integrations that allow you to control how data is structured, you may be able to fix the problem at the source and successfully replicate the data. If this is not possible, however, Stitch may never be able to successfully replicate the incompatible data.

      [**Check Integration & Destination Compatibility**]({{ link.destinations.overviews.compatibility | prepend: site.baseurl }})

  - title: "Will the structure of the data suit your needs?"
    anchor: "data-structure"
    content: |
      While the majority of your data will look the same across our destinations, there are some key differences you should be aware of.
    subsections:
      - title: "Nested data structures"
        anchor: "nested-data-structures"
        content: |
          Some destinations don't natively support nested structures, meaning that before Stitch can load replicated data, these structures must be "de-nested". During this process, Stitch will flatten nested structures into relational tables and subtables. As a result of creating subtables, a higher number of rows will be used.

          If a destination does natively support nested structures, no de-nesting will occur and Stitch will store the records intact.

          Check out the [Handling of Nested Data & Row Count Impact]({{ link.destinations.storage.nested-structures | prepend: site.baseurl }}) for an in-depth look at what we mean by nested records, how Stitch handles nested data, and what those records will look like in your data warehouse.

          <table class="attribute-list">
              <tr>
                  <td>
                      <strong>
                          Supports Nested Structures
                      </strong>
                  </td>
                  <td>
                      <strong>
                          No Nested Structure Support
                      </strong>
                  </td>
              </tr>
              <tr>
                  <td>
                      <ul>
                          {% for destination in destinations %}
                              {% if destination.nested-structure-support == true %}
                                  <li>{{ destination.display_name }}{% if destination.type == "amazon-s3" %} (JSON){% endif %}</li>
                              {% endif %}
                          {% endfor %}
                      </ul>
                  </td>
                  <td>
                      <ul>
                              <li>Amazon S3 (CSV)</li>
                          {% for destination in destinations %}
                              {% if destination.nested-structure-support == false %}
                                  <li>{{ destination.display_name }}</li>
                              {% endif %}
                          {% endfor %}
                      </ul>
                  </td>
              </tr>
          </table>

      - title: "Updates to existing records"
        anchor: "incremental-and-append-only-replication"
        content: |
          While all destinations support loading incrementally replicated data, how that data is stored in your destination will vary by destination.

          Unlike other destinations, **BigQuery** and **Amazon S3** store data in an <a href="#" data-toggle="tooltip" data-original-title="{{site.data.tooltips.append-only-rep}}">Append-Only</a> manner. This means that existing rows are never updated in the destination, but appended to the end of the table. In the case of **Amazon S3**, [during each load a new file (CSV or JSON) will be created and added to the bucket]({{ link.destinations.overviews.amazon-s3 | prepend: site.baseurl | append: "#loading" }}). 

          This means that there can be many different rows in a table with the same Primary Key, each representing what the data was at that moment in time. These are not duplicate rows - they're "snapshots" of the record at different points.

          For more info, check out [this detailed explanation on Append-Only Replication]({{ link.replication.append-only | prepend: site.baseurl }}) or [our recommendations for querying append-only tables]({{ link.replication.append-only | prepend: site.baseurl }}).

          ### Redshift vs. PostgreSQL

          If you've worked with PostgreSQL in the past and are considering Redshift as your data warehouse, you should note that Redshift [implements some Postgres features differently](http://docs.aws.amazon.com/redshift/latest/dg/c_redshift-sql-implementated-differently.html){:target="_blank"}. In addition, some [features](http://docs.aws.amazon.com/redshift/latest/dg/c_unsupported-postgresql-features.html){:target="_blank"}, [data types](http://docs.aws.amazon.com/redshift/latest/dg/c_unsupported-postgresql-datatypes.html){:target="_blank"}, and [functions](http://docs.aws.amazon.com/redshift/latest/dg/c_unsupported-postgresql-functions.html){:target="_blank"} aren't supported at all.

  - title: "What type of maintenance do you need?"
    anchor: "setup--maintenance"
    content: |
      With the exception of a self-hosted PostgreSQL instance, all the destinations offered by Stitch are cloud-hosted databases, meaning you won't have to factor in server maintenance when making a decision.
    subsections:
      - title: "Fully-managed solutions"
        anchor: "fully-managed-solutions"
        content: |
          [**Azure SQL Data Warehouse**](https://docs.microsoft.com/en-us/azure/sql-data-warehouse/service-maintenance){:target="new"}, [**BigQuery**](https://cloud.google.com/solutions/bigquery-data-warehouse#maintenance){:target="new"}, [**Heroku**](https://devcenter.heroku.com/articles/platform-updates-maintenance-and-notifications){:target="new"}, **Panoply**, and **Snowflake** are fully-managed solutions that include routine maintenance and upgrades in their plans.

          **Note**: Setting up Snowflake requires more technical know-how than the other aforementioned destinations.
      - title: "DIY solutions"
        anchor: ""
        content: |
          **Redshift, Amazon Postgres-RDS**, and **self-hosted Postgres instances** will require you to perform and schedule maintenance tasks on your own. Spinning up a Redshift and Amazon Postgres-RDS instance will require technical knowledge and familiarity with the Amazon Web Services (AWS) console.

  - title: "What's the destination's pricing structure?"
    anchor: "pricing"
    content: |
      Every destination offered by Stitch has its own pricing structure. Some providers charge by overall usage, others by an hourly rate or the amount of stored data. Depending on your needs, some pricing structures may fit better into your budget.

      In the next section, you'll find each destination's pricing structure, including a link to detailed price info and whether a free option (trial or plan) is available. Here are a few things to keep in mind:

      <table class="attribute-list">
      {% for destination in destinations %}
      <tr>
      <td class="attribute-name">
      <strong>{{ destination.display_name }}</strong>
      </td>
      <td class="attribute-description">
      {{ destination.pricing_notes | flatify | markdownify }}
      {% if destination.type == "bigquery" %}
      To learn more about how Stitch may impact your BigQuery costs, <a href="{{ link.destinations.overviews.bigquery-pricing | prepend: site.baseurl }}">click here</a>.
      {% endif %}
      </td>
      </tr>
      {% endfor %}
      </table>

  - title: "Additional resources and setup tutorials"
    anchor: "additional-resources"
    content: |
      Ready to pick a destination and get started? Use the links below to check out a more in-depth look at each destination or move on to the setup and connection process.

      {% include destinations/destination-tiles.html %}
---
{% include misc/data-files.html %}
{% assign destinations = site.destinations | where:"destination",true | sort: "display_name" %}