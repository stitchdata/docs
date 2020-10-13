---
# -------------------------- #
#        Page Controls       #
# -------------------------- #

title: Applying Encodings, SORT, & DIST Keys in Amazon Redshift

permalink: /destinations/amazon-redshift/apply-encodings-sort-dist-keys-redshift
redirect_from: /destinations/redshift/apply-encodings-sort-dist-keys-redshift

keywords: redshift, amazon redshift, redshift data warehouse, sort keys, dist keys, encodings, SORT, DIST, indexes
summary: "Want to improve your query performance? In this article, we’ll walk you through how to use encoding, Sort, and Distribution Keys to streamline query processing in your Amazon Redshift data warehouse."

content-type: "destination-general"
key: "redshift-encodings"
type: "redshift"

toc: true
layout: tutorial
use-tutorial-sidebar: false


# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |
  {% include important.html type="single-line" content="The process we outline in this tutorial - which includes dropping tables - can lead to data corruption and other issues if done incorrectly. **Proceed with caution or reach out to Stitch support if you have questions.**" %}

  Want to improve your query performance? In this guide, we’ll walk you through how to use encoding, SORT, and DIST (distribution) keys to streamline query processing.

  Before we dive into their application, here's a quick overview of each of these performance enhancing tools.

  - **Encodings**, or [compression types](http://docs.aws.amazon.com/redshift/latest/dg/t_Compressing_data_on_disk.html), are used to reduce the amount of required storage space and the size of data that’s read from storage. This in turn can lead to a reduction in processing time for queries.

  - **[SORT keys](http://docs.aws.amazon.com/redshift/latest/dg/t_Sorting_data.html)** determine the order in which rows in a table are stored. When properly applied, SORT Keys allow large chunks of data to be skipped during query processing. Less data to scan means a shorter processing time, thus improving the query’s performance.

  - **[Distribution, or DIST keys](http://docs.aws.amazon.com/redshift/latest/dg/t_Distributing_data.html)** determine where data is stored in Redshift. When data is replicated into your data warehouse, it’s stored across the compute nodes that make up the cluster. If data is heavily skewed - meaning a large amount is placed on a single node - query performance will suffer. Even distribution prevents these bottlenecks by ensuring that nodes equally share the processing load.

  ### Considerations

  1. **Optimizing for every single query isn’t possible.** We suggest selecting the most important queries and selecting SORT/DIST keys that will improve the performance of those queries.
  2. **Columns with few unique values aren’t good SORT keys**. Because SORT Keys store records together based on similar values, selecting a column with few unique values as the SORT key will heavily skew the data. This will lead to an increase in query processing time.
  3. **Tables using Full Table Replication aren’t good candidates for this process** Due to the nature of [Full Table Replication]({{ link.replication.full-table | prepend: site.baseurl }}), encodings, SORT, and DIST keys in these tables may be overwritten during the replication attempts that follow application.



# -------------------------- #
#         Instructions       #
# -------------------------- #

steps:
  - title: "Retrieve the table's schema"
    anchor: "retrieve-table-schema"
    content: |
      {% include note.html type="single-line" content="**Note**: The process outlined here can be used across the board to apply encodings **and** Keys." %}

      We’ll use a table called `orders`, which is contained in the `rep_sales` schema.

      To get started, log into your Redshift database using [psql](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-from-psql.html){:target="new"}.

      Use this command to retrieve the table schema, replacing `rep_sales` and `orders` with the names of your schema and table, respectively:

      {% capture code %}\d+ rep_sales.orders
      {% endcapture %}

      {% include layout/code-snippet.html code=code language="sql" %}

      For the `rep_sales.orders` table, the result looks like this:

      {% capture code %}| Column              | Data Type                  |
      | --------------------+----------------------------|
      | id [pk]             | BIGINT                     |
      | rep_name            | VARCHAR(128)               |
      | order_amount        | BIGINT                     |
      | order_confirmed     | BOOLEAN                    |
      | created_at          | TIMESTAMP                  |
      | _sdc_sequence       | NUMERIC                    |
      | _sdc_received_at    | TIMESTAMP WITHOUT TIMEZONE |
      | _sdc_batched_at     | TIMESTAMP WITHOUT TIMEZONE |
      | _sdc_table_version  | BIGINT                     |
      | _sdc_replication_id | VARCHAR(128)               |
      {% endcapture %}

      {% include layout/code-snippet.html code=code language="sql" %}

      In this example, we'll perform the following:

      - Apply SORT and DIST keys to the `id` column
      - Apply a `bytedict` encoding to the `rep_name` column


  - title: "Create a table copy and redefine the schema"
    anchor: "create-table-copy"
    content: |
      In this step, you’ll create a copy of the table, redefine its structure to include the DIST and SORT Keys, insert/rename the table, and then drop the "old" table.

    substeps:
      - title: "Retrieve the table's Primary Key comment"
        anchor: "retrieve-table-primary-key-comment"
        content: |
          In this step, you'll retrieve the table's Primary Key comment. This will be used in the next step to indicate which column(s) are the table's Primary Keys.

          Retrieve the table's Primary Key using the following query:

          {% capture code %}SELECT description
            FROM pg_catalog.pg_description
           WHERE objoid = 'old_orders'::regclass;
          {% endcapture %}

          {% include layout/code-snippet.html code=code language="sql" %}

          The result will look like the following, where `primary_keys` is an array of strings referencing the columns used as the table's Primary Key:

          {% capture code %}{"primary_keys":["id"]}
          {% endcapture %}

          {% include layout/code-snippet.html code=code language="sql" %}

          {% include important.html first-line="**Primary Key comments**" content="Redshift doesn’t enforce the use of Primary Keys, but Stitch requires them to replicate data. In the following example, you'll see `COMMENT` being used to note the table's Primary Key. **Make sure you include the Primary Key comment in the next step, as missing or incorrectly defined Primary Key comments will cause issues with data replication.**" %}

      - title: "Copy, redefine, insert, and drop the table"
        anchor: "run-table-transaction"
        content: |
          In this step, you'll execute a transaction that will perform the following:

          1. Renames the table
          2. Creates a new table with a structure that includes the SORT and DIST keys
          3. Copies the data from the old table and inserts it into the new, redefined table
          4. Renames the new table
          5. Drops the old table

          For the `rep_sales.orders` example table, this is the transaction that will perform the actions listed above:

          {% capture code %}SET search_path to rep_sales;
          BEGIN;
          ALTER TABLE orders RENAME TO old_orders;
          CREATE TABLE new_orders (
              id bigint,
              rep_name character varying(128) encode bytedict,     /* Sets the encoding */
              order_amount bigint,
              order_confirmed boolean,
              created_at timestamp without time zone,
              _sdc_sequence numeric(18,0),
              _sdc_received_at timestamp without time zone,
              _sdc_batched_at timestamp without time zone,
              _sdc_table_version bigint,
              _sdc_replication_id character varying(128)
          )  distkey (id)     // Sets the DIST Key
             sortkey (id);     // Sets the SORT Key
          INSERT INTO new_orders (SELECT * FROM old_orders);

          COMMENT ON table new_orders IS '{"primary_keys":["XXXXX"]}';
                                                                  /* Sets Primary Key comment */

          ALTER TABLE new_orders RENAME TO orders;
          ALTER TABLE orders OWNER TO <stitch_user>;      /* Grants table ownership to Stitch */
          DROP TABLE old_orders;                        /* Drops the "old" table */
          END;
          {% endcapture %}

          {% include layout/code-snippet.html code=code language="sql" %}

  - title: "Verify the table owner"
    anchor: "verify-table-owner"
    content: |
      Stitch requires ownership of all integration tables to successfully load data. If Stitch isn't the table owner, issues with data replication will occur.

      To verify the table's owner, run the following query and replace `rep_sales` and `orders` with the names of the schema and table, respectively:

      {% capture code %}SELECT schemaname,
             tablename,
             tableowner
        FROM pg_catalog.pg_tables
       WHERE schemaname = 'rep_sales'
         AND tablename = 'order'
      {% endcapture %}

      {% include layout/code-snippet.html code=code language="sql" %}

      If Stitch is not the owner of the table, run the following command:

      {% capture code %}ALTER TABLE <schema_name>.<table_name> OWNER TO <stitch_user>;
      {% endcapture %}

      {% include layout/code-snippet.html code=code language="sql" %}

  - title: "Verify the encoding and key application"
    anchor: "verify-application"
    content: |
      To verify that the changes were applied correctly, retrieve the table’s schema again using this command, replacing `rep_sales` and `orders` with the names of your schema and table, respectively:

      {% capture code %}\d+ rep_sales.orders
      {% endcapture %}

      {% include layout/code-snippet.html code=code language="sql" %}

      In this example, if the Keys and encodings were applied correctly, the response would look something like this:

      {% capture code %}| Column              | Data type                  | Encoding | Distkey | Sortkey |
      |---------------------+----------------------------+----------+---------+---------|
      | id                  | BIGINT                     | none     | true    | true    |  
      | rep_name            | VARCHAR(128)               | bytedict | false   | false   |  
      | order_amount        | BIGINT                     | none     | false   | false   |
      | order_confirmed     | BOOLEAN                    | none     | false   | false   |
      | created_at          | TIMESTAMP                  | none     | false   | false   |
      | _sdc_sequence       | NUMERIC                    | none     | false   | false   |
      | _sdc_received_at    | TIMESTAMP WITHOUT TIMEZONE | none     | false   | false   |
      | _sdc_batched_at     | TIMESTAMP WITHOUT TIMEZONE | none     | false   | false   |
      | _sdc_table_version  | BIGINT                     | none     | false   | false   |
      | _sdc_replication_id | VARCHAR(128)               | none     | false   | false   |
      {% endcapture %}

      {% include layout/code-snippet.html code=code language="sql" %}

      For the `id` column, the `Distkey` and `Sortkey` is set to `true`, meaning that the keys were properly applied.

      For `rep_name`, the `Encoding` is set to `bytedict`, indicating that the encoding was also properly applied.
---
{% include misc/data-files.html %}
{% assign destination = site.destinations | where:"type","redshift" | first %}