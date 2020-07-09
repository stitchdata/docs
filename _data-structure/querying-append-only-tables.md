---
# -------------------------- #
#          PAGE INFO         #
# -------------------------- #

title: Querying Append-Only Tables
permalink: /replication/loading/querying-append-only-tables
redirect_from: /data-structure/querying-append-only-tables
keywords: bigquery, google bigquery data warehouse, bigquery data warehouse, bigquery etl, etl to bigquery, append-only, append only, query append only
summary: "Learn how Append-only Loading works and how to account for it in your queries."

key: "append-only-querying"
type: ""

layout: general
toc: true
order: 1
content-type: "guide"

destination: "BigQuery"


# -------------------------- #
#           INTRO            #
# -------------------------- #

intro: |
  {% capture note %}
  - [Destinations configured to use Append-Only Loading]({{ link.destinations.storage.loading-behavior | prepend: site.baseurl | append:"#reference--destinations-loading-behavior" }}), or
  - Tables configured to use Append-Only Loading, such as [Google Ads' Report tables]({{ site.baseurl }}/integrations/saas/google-ads#data-loading-append-only)
  {% endcapture %}

  {% include note.html first-line="**This guide is applicable to:**" content=note %}

  When data is loaded using [Append-Only Loading]({{ link.destinations.storage.loading-behavior | prepend: site.baseurl | append:"#reference--destinations-loading-behavior" }}), existing records aren't updated, but instead appended to tables as new rows. This means that as time goes on, tables will contain different versions of the same record, reflecting how the record has changed over time.

  While data stored this way can provide insights and historical details, sometimes you may just want the latest version of a record. In this guide, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#          CONTENT           #
# -------------------------- #

sections:
  - title: "Before using this guide"
    anchor: "before-using-guide"
    summary: "Things to know before using this guide"
    content: |
      Before using this guide, note that:

      - You may need to modify the queries in this guide to use them yourself
      - Stitch Support's expertise lies in replicating data, and as such does not provide data analysis or querying assistance. We can, however, help with data discrepancies.

         If you'd like assistance with analysis or business intelligence solutions, we recommend reaching out to one of our [analytics partners]({{ site.partners }}){:target="new"}.

  - title: "Using system columns to identify record versions"
    anchor: "using-system-column"
    summary: "Columns you can use to identify record versions"
    content: |
      Every table created by Stitch contains columns prepended with `{{ system-column.prefix }}`. These are system columns created and used by Stitch to load data into your destination.

      For this guide, we'll focus on just two columns:

      <table>
      <tr>
      <td class="attribute-name">
      <strong>Column name</strong>
      </td>
      <td>
      <strong>Description</strong>
      </td>
      </tr>
      <tr>
      <td class="attribute-name">
      <strong>{{ system-column.sequence }}</strong>
      </td>
      <td>
      {{ system-column.sequence-description | flatify | markdownify }} 

      {{ "Stitch uses this column's values in a few places to correctly order rows for loading, but it can be also used to retrieve the latest version of a record from an Append-Only table." | markdownify }} 

      This is the primary column our strategy will use.
      </td>
      </tr>
      <tr>
      <td class="attribute-name">
      <strong>{{ system-column.batched-at }}</strong>
      </td>
      <td>
      {{ system-column.batched-at-description | flatify | markdownify }}

      Our strategy will use this column as a "tie breaker."
      </td>
      </tr>
      </table>

  - title: "Retrieving the latest version of every record"
    anchor: "latest-version-every-row"
    summary: "A querying strategy that retrieves the latest version of every record"
    content: |
      {% include note.html type="single-line" content="**Note**: The queries in this section are only intended to demonstrate one approach to querying. You may need to modify the queries to use them yourself." %}

      Let's take a look at an example. Assume we have an `orders` table that contains:

      - A Primary Key of `id`,
      - The system `{{ system-column.prefix }}` columns added by Stitch, and
      - Other order attribute columns

    subsections:
      - title: "Only using {{ system-column.sequence }}"
        anchor: "example--only-sdc-sequence"
        content: |
          If you wanted to create a snapshot of the latest version of this table, you could run a query like this using `{{ system-column.sequence }}`:

          {% capture code %}
              SELECT DISTINCT orders.*
                     FROM [stitch-analytics-bigquery-123:ecommerce.orders] orders
               INNER JOIN (
                            SELECT id,
                                   MAX({{ system-column.sequence }}) AS sequence
                              FROM [stitch-analytics-bigquery-123:ecommerce.orders]
                            GROUP BY id
                          ) latest_orders
                       ON orders.id = latest_orders.id
                      AND orders.{{ system-column.sequence }} = latest_orders.sequence
          {% endcapture %}

          {% assign description = "Example only using " | append: system-column.sequence %}

          {% include layout/code-snippet.html code=code code-description=description %}

          Here's what's happening in this query:

          1. The subquery retrieves a list of every record's Primary Key and maximum `{{ system-column.sequence }}` value.
          2. The outer query selects distinct versions of the latest version of every record.
          3. Lastly, the outer query joins the table to the list retrieved by the subquery, which makes all other columns available for querying.

      - title: "Using {{ system-column.batched-at }} as a tie breaker"
        anchor: "using--sdc-batched-at"
        content: |
          If only using `{{ system-column.sequence }}` doesn't yield the desired results, we recommend using `{{ system-column.batched-at }}` as a "tie breaker":

          {% capture code %}
              SELECT DISTINCT orders.*
                     FROM [stitch-analytics-bigquery-123:ecommerce.orders] orders
               INNER JOIN (
                            SELECT id,
                                   MAX({{ system-column.sequence }}) AS sequence,
                                   MAX({{ system-column.batched-at }}) as batched_at
                              FROM [stitch-analytics-bigquery-123:ecommerce.orders]
                            GROUP BY id
                          ) latest_orders
                       ON orders.id = latest_orders.id
                      AND orders.{{ system-column.sequence }} = latest_orders.sequence
                      AND orders.{{ system-column.batched-at }} = latest_orders.batched_at
          {% endcapture %}

          {% assign description = "Example using " | append: system-column.sequence | append: " and " | append: system-column.batched-at %}

          {% include layout/code-snippet.html code=code code-description=description %}

          The `{{ system-column.batched-at }}` value indicates the time that Stitch loaded the batch containing the record into the destination. Selecting a record's maximum `{{ system-column.batched-at }}` and `{{ system-column.sequence }}` values excludes versions of the record from older batches from the results.

  - title: "Create views in your destination"
    anchor: "create-destination-views"
    summary: "How to simplify querying by creating a view in your destination"
    content: |
      To make this easier, you can turn queries like the one above into a view. We recommend this approach because a view will encapsulate all the logic and simplify the process of querying against the latest version of your data.

      Refer to the documentation for your destination for more info on creating views:

      - [Amazon Redshift]({{ site.data.destinations.redshift.resource-links.create-views }}){:target="new"}
      - [Google BigQuery]({{ site.data.destinations.bigquery.resource-links.create-views }}){:target="new"}
      - [Microsoft Synapse SQL Analytics]({{ site.data.destinations.microsoft-azure.resource-links.create-views }}){:target="new"}
      - [PostgreSQL]({{ site.data.destinations.postgres.resource-links.create-views }}){:target="new"}
      - [Snowflake]({{ site.data.destinations.snowflake.resource-links.create-views }}){:target="new"}
---
{% include misc/data-files.html %}