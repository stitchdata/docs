---
# -------------------------- #
#        Page Controls       #
# -------------------------- #

title: Understanding Stitch's Impact on BigQuery Costs
permalink: /destinations/bigquery/understanding-stitch-impact-on-bigquery-costs
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
  Unlike traditional relational databases and other cloud solutions like Amazon Redshift, Google BigQuery pricing is based on usage instead of fixed pricing. Because of this, it can be difficult to estimate how much a Stitch-enabled BigQuery data warehouse will cost to use over time.

  Stitch employs a number of different operations across both Google Cloud Storage and BigQuery as part of the replication process. In this article, we'll give you an overview of those operations and the impact they may have.


# -------------------------- #
#          Content           #
# -------------------------- #

sections:
  - title: "BigQuery pricing basics"
    anchor: "bigquery-pricing-basics"
    content: |
      BigQuery pricing includes two categories: Storage and usage costs.

      Before we get into the specifics, we strongly recommend that you familiarize yourself with the [BigQuery Pricing Model]({{ destination.pricing }}).

      We'll only cover the specific ways Stitch may potentially impact BigQuery costs in this doc, so reading Google's brief overview will help you make an informed decision.

  - title: "Google Cloud Storage costs"
    anchor: "google-cloud-storage-costs"
    content: |
      Before your data is loaded into BigQuery, Stitch's replication engine will replicate, process, and prepare data from your various integrations and temporarily move it into a Google Cloud Storage (GCS) bucket. This Cloud Storage bucket is automatically created by Stitch but owned by you.

      While there isn't a cost associated for moving data into a Cloud Storage bucket, there are some minimal costs for the standard operations that handle the data placed there: 

      - Stitch makes a number of Class A and B API calls on GCS during the replication process
      - Google charges for these calls, but in increments of 10,000 and at a very minimal rate

      Stitch files are deleted immediately after data is loaded into BigQuery, so the storage costs associated with a Cloud Storage bucket should be negligible. 

      **We expect the cost of using Google Cloud Storage with Stitch to be less than $5 a month.**

      [Click here]({{ destination.storage-pricing }}) for more info on Google's Cloud Storage pricing model.

  - title: "BigQuery usage costs"
    anchor: "bigquery-usage-costs"
    content: |
      BigQuery ultimately breaks down pricing into two categories: Storage pricing and query pricing. 

    subsections:
      - title: "Storage pricing"
        anchor: "storage-pricing"
        content: |
          The cost of storing your data in BigQuery is entirely dependent on how much data you replicate into the destination.

          However, when estimating how much data you expect to store in your destination, it's important to understand the append-only nature of how Stitch replicates most data into BigQuery.

          **To summarize: existing data isn't updated. Updates are added as new rows to existing tables. Due to this, the size of tables can grow substantially over time.**

          [Click here]({{ destination.pricing | append: "#storage" }}) for more info on Google's Storage pricing model.

      - title: "Query pricing"
        anchor: "query-pricing"
        content: |
          **The cost of loading data into BigQuery from Google Cloud Storage is free.**

          Queries currently run by Stitch to replicate your data do not currently count towards the $5/TB model currently charged by Google. 

          [Click here]({{ destination.pricing | append: "#queries" }}) for more info on Google's Query pricing model.
---
{% include misc/data-files.html %}
{% assign destination = site.destinations | where:"type","bigquery" | first %}