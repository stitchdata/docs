---
title: Apply table partitioning and clustering in BigQuery
permalink: /destinations/bigquery/apply-table-partitioning-clustering
tags: [bigquery_destination]
keywords: bigquery, google bigquery, partition, partitioning, cluster, clustering, indexes
summary: "Want to improve your BigQuery performance and query costs? In this article, we’ll walk you through how to use table partitioning and clustering to streamline query processing in your BigQuery data warehouse."

content-type: "destination-general"

toc: true
type: "bigquery"

sections:
  - content: |
      {% include important.html type="single-line" content="The process we outline in this tutorial - which includes dropping tables - can lead to data corruption and other issues if done incorrectly. **Please proceed with caution or reach out to Stitch support if you have questions.**" %}

      Want to improve your BigQuery performance and query costs? In this article, we’ll walk you through how to use table partitioning and clustering to streamline query processing in your BigQuery data warehouse.
      

  - title: "Overview"
    anchor: "overview"
    content: |
       BigQuery's table partitioning and clustering features can improve query performance and cost by structuring data to match common query patterns. Learn more in BigQuery's [table partitioning documentation](https://cloud.google.com/bigquery/docs/partitioned-tables) and [clustering documentation](https://cloud.google.com/bigquery/docs/clustered-tables). Stitch creates BigQuery tables without partitioning or clustering, but Stitch can load into partitioned and clustered tables. This guide will walk you through how to add these features to a BigQuery table created by Stitch.
  - title: "Things to think about"
    anchor: "things-to-think-about"
    content: |
      Consider the following before diving in:

      1. **Optimizing for every single query isn’t possible.** Tables can only be partitioned by one field, which must be a timestamp or date column, and clustered by a single set of columns. The ideal choice of partitioning and clustering column(s) depends on the nature of your data and queries.
      2. **Tables using Full Table Replication aren’t good candidates for this process** Due to the nature of Full Table Replication, partitioning in these tables may be overwritten during the replication attempts that follow application.

  - title: "Add partitioning and clustering to an existing table"
    anchor: "add-partitioning-and-clustering"
    content: |

      We’ll use a table called `orders`, which is contained in the `rep_sales` dataset.

      Log into Stitch and the BigQuery Web UI to get started.

    subsections:
      - title: "Step 1: Pause Stitch Loading"
        anchor: "step-1-pause-stitch-loading"
        content: |
	  From Stitch, pause all source integrations that contain tables you plan to modify. We also need to ensure that Stitch doesn't load any data while we are modifying tables by monitoring the [Integration Details page](https://www.stitchdata.com/docs/getting-started#monitoring-replication-progress) for each paused integration until no Extractoins are in progress and 0 Rows are preparing.

      - title: "Step 2: Create a temporary table with partitioning and clustering"
        anchor: "step-2-create-temp-table"
        content: |
          In this step, you’ll create a temporary copy of the table with partioning and clustering added on the `created_at` column. Note that this is just an example - your choice of partitioning and clustering column will likely be different based on your data and the queries you hope to optimize, and you can even use different columns for partitioning and clustering. Run the following from the BigQuery Web UI Query Editor:

          ```sql
	  CREATE TABLE rep_sales.orders_tmp PARTITION BY DATE(created_at) CLUSTER BY created_at AS SELECT * from rep_sales.orders
          ```
	  
      - title: "Step 3: Drop the original table and rename the copy"
        anchor: "step-3-drop-original-and-rename"
        content: |
	  Since BigQuery doesn't support renaming tables, we'll have to drop our original table and then copy the temporary table back into its place.

	  To drop the original table, run the following from the BigQuery Web UI:

          ```sql
	  DROP TABLE rep_sales.orders
	  ```

	  Then, follow [the BigQuery documentation for copying a table via the Web UI](https://cloud.google.com/bigquery/docs/managing-tables#copying_a_single_source_table) using the original dataset and table name - in our example `rep_sales` and `orders` - as the destination.

	  Finally, drop the temporary table with this commany in the BigQuery Web UI:

	  ```sql
	  DROP TABLE rep_sales.orders_tmp
	  ```

      - title: "Step 4: Unpause Stitch"
        anchor: "step-4-unpause-stitch"
        content: |
          Return to Stitch and unpause any sources that you paused in Step 1.

---
{% include misc/data-files.html %}
{% assign destination = site.destinations | where:"type","bigquery" | first %}