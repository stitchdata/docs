---
# -------------------------- #
#        Page Controls       #
# -------------------------- #

title: Understanding Stitch's Impact on Google BigQuery Costs
permalink: /destinations/google-bigquery/understanding-stitch-impact-on-bigquery-costs
redirect_from: /destinations/bigquery/understanding-stitch-impact-on-bigquery-costs

keywords: bigquery, google bigquery data warehouse, bigquery data warehouse, bigquery etl, etl to bigquery

summary: "Unlike traditional relational databases and other cloud solutions, Google BigQuery pricing isn't fixed-rate: it's based on usage. The goal of this article is to help you better understand how your data warehousing costs will be impacted by using Stitch's BigQuery destination so you can make an informed decision."

content-type: "destination-general"

toc: false
layout: general
type: "bigquery"


# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |
  Google BigQuery pricing is based on usage instead of fixed pricing, unlike traditional relational databases and other cloud solutions. Because of this, it can be difficult to estimate the cost of using a BigQuery destination with Stitch.

  Stitch employs a number of different operations across both Google Cloud Storage (GCS) and BigQuery as part of the replication process, which can impact your costs in several areas of Google Cloud Platform (GCP). In this article, we'll cover:

  {% for section in page.sections %}
  - [{{ section.summary }}](#{{ section.anchor }})
  {% endfor %}


# -------------------------- #
#          Content           #
# -------------------------- #

## Used for displaying the content in the `version` array
## in section/subsections.
version-table: |
  <table class="attribute-list">
  <tr>
  {% for version in LEVEL.versions %}
  <td width="50%; fixed">
  <strong>{{ version.display-name }}</strong>
  </td>
  {% endfor %}
  </tr>

  <tr>
  {% for version in LEVEL.versions %}
  <td width="50%; fixed">
  {{ version.copy | flatify | markdownify }}
  </td>
  {% endfor %}
  </tr>
  </table>

sections:
  - title: "Google Cloud Storage costs"
    anchor: "google-cloud-storage-costs"
    summary: "Stitch's impact on Google Cloud Storage costs"
    versions:
      - number: "1"
        display-name: "v1 (Append-Only)"
        copy: |
          **Minimal cost to you**

          The GCS bucket used to stage data for loading is automatically created by Stitch, but owned by you.

          As a result, there will be minimal costs for the [Class A and B API calls](https://cloud.google.com/storage/pricing){:target="new"} Stitch makes during the replication process.

          Files placed in GCS are deleted immediately after data is loaded into BigQuery, so storage costs for the GCS bucket should be minimal.
      - number: "2"
        display-name: "v2 (Upsert and Append-Only)"
        copy: |
          **No cost to you**

          Stitch owns and manages the GCS bucket used to stage data for loading to BigQuery.

          As a result, there are no GCS costs for using this version of Stitch's BigQuery destination.
    content: |
      Before your data is loaded into BigQuery, Stitch's replication engine will replicate, process, and prepare data from your various integrations and temporarily move it into a Google Cloud Storage (GCS) bucket. There isn't a cost for moving data into a GCS bucket, but there may be operational costs for handling data placed there.

      This is dependent on the version of Stitch's BigQuery destination you're using:

      {{ page.version-table | replace: "LEVEL","section" | flatify }}

      Refer to [Google's documentation]({{ site.data.destinations.bigquery.resource-links.storage-pricing }}){:target="new"} for more info on Google's Cloud Storage pricing model.

  - title: "BigQuery costs"
    anchor: "bigquery-costs"
    summary: "Stitch's impact on BigQuery costs"
    content: |
      BigQuery pricing has two categories:

      {% for subsection in section.subsections %}
      - [{{ subsection.title }}](#{{ subsection.anchor }}), which is {{ subsection.summary }}
      {% endfor %}

      Refer to [Google's BigQuery pricing documentation]({{ site.data.destinations.bigquery.resource-links.pricing }}){:target="new"} for more info.

      **Note**: The following sections only cover the specific ways Stitch can impact BigQuery costs.

    subsections:
      - title: "Storage pricing"
        anchor: "bigquery-storage-pricing"
        summary: "based on the amount of data stored in BigQuery"
        versions:
          - number: "1"
            display-name: "v1 (Append-Only)"
            copy: |
              Loading behavior is predefined; all data is loaded in an Append-Only manner. 

              Existing rows aren't updated. Multiple versions of a row can exist in a table, creating a log of how a row changed over time.

              Tables size will increase after every replication job, and increase storage costs as a result.
              
          - number: "2"
            display-name: "v2 (Upsert and Append-Only)"
            copy: |
              Loading behavior is defined by you during destination setup:

              - **Upsert**: Existing rows are updated in tables with defined Primary Keys. A single version of a row will exist in the table.

                 Table size and storage costs are dependent on the volume of new records added in the source.

              - **Append-Only**: Existing rows aren't updated. Multiple versions of a row can exist in a table, creating a log of how a row changed over time.

                Tables size will increase after every replication job, and increase storage costs as a result.
              
        content: |
          The cost of storing your data in BigQuery is dependent on how much data is replicated into the destination.

          BigQuery storage costs are impacted by the amount of data you replicated and the loading behavior used by the destination.

          {{ page.version-table | replace: "LEVEL","subsection" | flatify }}

          [todo- something about staging tables?]

      - title: "Query pricing"
        anchor: "bigquery-query-pricing"
        summary: "based on the amount of data processed by each executed query"
        versions:
          - number: "1"
            display-name: "v1 (Append-Only)"
            copy: |
              **No cost to you**

              The method Stitch uses to load data in an Append-Only manner is considered free under BigQuery's pricing model.

          - number: "2"
            display-name: "v2 (Upsert and Append-Only)"
            copy: |
              **The cost to you will vary**

              Query costs for loading data depend on the loading behavior you select during destination setup:

              - **Upsert**: **Costs associated with using the [BigQuery Data Manipulation Language (DML) function]({{ site.data.destinations.bigquery.resource-links.dml }}){:target="new"}**. Google charges for queries based on the number of bytes processed, or bytes read. Additionally, Google imposes [a minimum processing requirement]({{ site.data.destinations.bigquery.resource-links.on-demand-pricing }}){:target="new"} of 10MB per table referenced by the query, and with a minimum 10MB data processed per query.

                 **Note**: As of {{ page.date | date: '%B %d, %Y' }}, this information is correct. Refer to [Google's pricing documentation]({{ site.data.destinations.bigquery.resource-links.dml-pricing }}){:target="new"} for the most up-to-date information, and [let us know]({{ site.github_issues }}){:target="new"} if something is outdated.

              - **Append-Only**: **No cost to you**. The method Stitch uses to load data in an Append-Only manner is considered free under BigQuery's pricing model.
        content: |
          During loading, Stitch will run queries to move your data from the GCS bucket to BigQuery.

          BigQuery query costs are impacted by the loading behavior used by the destination.

          {{ page.version-table | replace: "LEVEL","subsection" | flatify }}

          Refer to [Google's documentation]({{ site.data.destinations.bigquery.resource-links.on-demand-pricing }}){:target="new"}  for more info on BigQuery query pricing.

  - title: "Cost considerations and management tools"
    anchor: "cost-considerations-management-tools"
    summary: "Some considerations and tools for managing your GCP costs"
    content: |
      When selecting the loading behavior for your BigQuery destination, we recommend keeping your BigQuery budget in mind. Understanding how Stitch can impact your costs will allow you to make an informed decision.

      The loading behavior you select is dependent on both your data needs and BigQuery budget. While we can't recommend one behavior type over another, we do recommend using **Append-Only** loading if BigQuery costs will be a concern. This recommendation is based on how [Google bills for the queries Stitch uses to load using **Upsert**](#bigquery-query-pricing).

      Additionally, Google provides tools in the GCP console that allow you to monitor and manage your costs:

      - [Billing Reports and Cost Trends]({{ site.data.destinations.bigquery.resource-links.billing-reports }}){:target="new"}
      - [Tutorial: BigQuery cost reporting dashboard in DataStudio](https://cloud.google.com/blog/products/data-analytics/taking-a-practical-approach-to-bigquery-cost-monitoring){:target="new"}
---
{% include misc/data-files.html %}