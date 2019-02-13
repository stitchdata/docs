---
# -------------------------- #
#        Page Controls       #
# -------------------------- #

title: Apply table partitioning and clustering in BigQuery
permalink: /destinations/bigquery/apply-table-partitioning-clustering
keywords: bigquery, google bigquery, partition, partitioning, cluster, clustering, indexes

summary: "Want to improve your BigQuery performance and query costs? In this article, we’ll walk you through how to use table partitioning and clustering to streamline query processing in your BigQuery destination."

content-type: "destination-general"

toc: true
layout: tutorial
use-tutorial-sidebar: false
type: "bigquery"


# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |
  {% include important.html type="single-line" content="The process outlined in this tutorial - which includes dropping tables - can lead to data corruption and other issues if done incorrectly. **Please proceed with caution or reach out to Stitch support if you have questions.**" %}

  Want to improve your BigQuery performance and query costs? When Stitch loads data into BigQuery, tables are created without partitioning or clustering. However, you can apply these performance enhancement tools to your table to streamline query processing, which Stitch will respect on subsequent loads.

  In this guide, we'll walk you through how to add partitioning and clustering to a BigQuery table created by Stitch.

  ### Overview

  BigQuery's table partitioning and clustering features can improve query performance and cost by structuring data to match common query patterns.

  Learn more in BigQuery's [table partitioning documentation](https://cloud.google.com/bigquery/docs/partitioned-tables){:target="new"} and [clustering documentation](https://cloud.google.com/bigquery/docs/clustered-tables){:target="new"}.

  ### Considerations

  Before diving in, keep in mind that optimizing for every single query isn’t possible. Tables can only be partitioned by one field, which must be a timestamp or date column, and clustered by a single set of columns.

  The ideal choice of partitioning and clustering column(s) depends on the nature of your data and queries.


# -------------------------- #
#        Requirements        #
# -------------------------- #

requirements:
  - item: |
      **The required user permissions.** The user performing this process must have the [permissions outlined in BigQuery's documentation](https://cloud.google.com/bigquery/docs/creating-column-partitions#required_permissions){:target="new"}.


# -------------------------- #
#         Instructions       #
# -------------------------- #

steps:
  - title: "Sign into Stitch and the BigQuery Web UI"
    anchor: "sign-into-apps"
    content: |
      Sign into Stitch and the BigQuery Web UI to get started.

      As an example, we’ll use a table called `orders`, which is contained in the `rep_sales` dataset.

  - title: "Pause Stitch loading"
    anchor: "pause-stitch-loading"
    content: |
      From Stitch, pause all source integrations that contain tables you plan to modify.

      You will also need to ensure that Stitch doesn't load any data while you are modifying the tables. To do this, monitor the [{{ app.page-names.int-details }}]({{ link.replication.rep-progress | prepend: site.baseurl }}) page for each paused integration until:

      1. No **Extractions** are in progress, and
      2. There are zero rows in **Preparing**

      When the integrations meet these criteria, you can move onto the next step.

  - title: "Create a temporary table with partitioning and clustering"
    anchor: "create-temp-table"
    content: |
      Next, you'll create a temporary copy of the table with partitioning and clustering added on the `created_at` column.

      {% include note.html type="single-line" content="**Note**: Your choice of partitioning and clustering column should be based on your data and the queries you want to optimize. You can even use different columns for partitioning and clustering. This is just an example." %}

      Run the following from the BigQuery Web UI Query Editor:

      ```sql
      CREATE TABLE rep_sales.orders_tmp
      PARTITION BY DATE(created_at)
        CLUSTER BY created_at 
        AS 
          SELECT *
            FROM rep_sales.orders
      ```

  - title: "Drop the original table and rename the copy"
    anchor: "drop-original-and-rename"
    content: |
      As BigQuery doesn't support renaming tables, you'll have to drop the original table and then copy the temporary table into its place.

      1. To drop the original table, run the following from the BigQuery Web UI:

          ```sql
          DROP TABLE rep_sales.orders
          ```
      2. Copy the table via the Web UI. See [BigQuery's documentation](https://cloud.google.com/bigquery/docs/managing-tables#copying_a_single_source_table){:target="new"} for additional instructions.

         In the Copy Table dialog, define the fields as follows:

         - **Destination dataset**: Use the original dataset name. In this example, that's `rep_sales`.
         - **Destination table**: Use the original table name. In this example, that's `orders`.

         After you've copied the table, move onto the next step.
      3. To drop the temporary table, run the following from the BigQuery Web UI:

          ```sql
          DROP TABLE rep_sales.orders_tmp
          ```

  - title: "Unpause Stitch integrations"
    anchor: "unpause-stitch"
    content: |
      Return to Stitch and unpause any integrations that you paused in [Step 2](#pause-stitch-loading).
---
{% include misc/data-files.html %}
{% assign destination = site.destinations | where:"type","bigquery" | first %}