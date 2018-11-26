---
title: Applying Encodings, SORT, & DIST Keys in Redshift
permalink: /destinations/redshift/apply-encodings-sort-dist-keys-redshift
tags: [redshift_destination]
keywords: redshift, amazon redshift, redshift data warehouse, sort keys, dist keys, encodings, SORT, DIST, indexes
summary: "Want to improve your query performance? In this article, we’ll walk you through how to use encoding, Sort, and Distribution Keys to streamline query processing in your Amazon Redshift data warehouse."

content-type: "destination-general"

toc: true
type: "redshift"

sections:
  - content: |
      {% include important.html type="single-line" content="The process we outline in this tutorial - which includes dropping tables - can lead to data corruption and other issues if done incorrectly. **Please proceed with caution or reach out to Stitch support if you have questions.**" %}

      Want to improve your query performance? In this article, we’ll walk you through how to use encoding, Sort, and Distribution keys to streamline query processing.

  - title: "Overview"
    anchor: "overview"
    content: |
      What do each of these query performance enhancing tools do? Before we dive into their application, here's a quick overview:

    subsections:
      - title: "Encodings"
        anchor: "encodings"
        content: |
          **Encodings**, or [compression types](http://docs.aws.amazon.com/redshift/latest/dg/t_Compressing_data_on_disk.html), are used to reduce the amount of required storage space and the size of data that’s read from storage. This in turn can lead to a reduction in processing time for queries.

      - title: "SORT keys"
        anchor: "overview-sort-keys"
        content: |
          **[Sort keys](http://docs.aws.amazon.com/redshift/latest/dg/t_Sorting_data.html)** determine the order in which rows in a table are stored. When properly applied, Sort Keys allow large chunks of data to be skipped during query processing. Less data to scan means a shorter processing time, thus improving the query’s performance.

      - title: "Distribution keys"
        anchor: "overview-dist-keys"
        content: |
          **[Distribution, or DIST keys](http://docs.aws.amazon.com/redshift/latest/dg/t_Distributing_data.html)** determine where data is stored in Redshift. When data is replicated into your data warehouse, it’s stored across the compute nodes that make up the cluster. If data is heavily skewed - meaning a large amount is placed on a single node - query performance will suffer. Even distribution prevents these bottlenecks by ensuring that nodes equally share the processing load.

  - title: "Things to think about"
    anchor: "things-to-think-about"
    content: |
      Consider the following before diving in:

      1. **Optimizing for every single query isn’t possible.** We suggest selecting the most important queries and selecting Sort/Dist keys that will improve the performance of those queries.
      2. **Columns with few unique values aren’t good Sort keys**. Because Sort Keys store records together based on similar values, selecting a column with few unique values as the Sort key will heavily skew the data. This will lead to an increase in query processing time.
      3. **Tables using Full Table Replication aren’t good candidates for this process** Due to the nature of Full Table Replication, encodings, Sort, and DIST keys in these tables may be overwritten during the replication attempts that follow application.

  - title: "Apply encodings, DIST, and SORT keys"
    anchor: "apply-encodings-dist-sort-keys"
    content: |
      {% include note.html type="single-line" content="The process outlined here can be used across the board to apply encodings **and** Keys." %}

      We’ll use a table called `orders`, which is contained in the `rep_sales` schema.

      Log into your Redshift database using your SQL client to get started.

    subsections:
      - title: "Step 1: Retrieve the table schema"
        anchor: "step-1-retrieve-table-schema"
        content: |
          Use this command to retrieve the table schema for orders:

          ```sql
          \d+ [schema_name].[table_name]
          ```

          This command will produce the table schema. In our case, the result looks like this:

          ```
          Column              | Data Type                  
          --------------------+----------------------------+
          id                  | BIGINT               
          rep_name            | VARCHAR(128)              
          order_amount        | BIGINT                     
          order_confirmed     | BOOLEAN                    
          created_at          | TIMESTAMP                  
          _sdc_sequence       | NUMERIC                    
          _sdc_received_at    | TIMESTAMP WITHOUT TIMEZONE 
          _sdc_batched_at     | TIMESTAMP WITHOUT TIMEZONE 
          _sdc_table_version  | BIGINT                     
          _sdc_replication_id | VARCHAR(128)
          ```

      - title: "Step 2: Create a table copy and redefine the schema"
        anchor: "step-2-create-table-copy"
        content: |
          In this step, you’ll create a copy of the table, redefine its structure to include the `DIST` and `SORT` Keys, insert/rename the table, and then drop the "old" table.

          But first, retrieve the table's Primary Key using the following query:

          ```sql
          SELECT description FROM pg_description WHERE objoid = 'old_orders'::regclass;             
             /* This will retrieve the Primary Key comment: {"primary_keys":["XXXXX"]} */
          ```

          This will be used in the next step to indicate which column(s) are the table's Primary Keys.

          {% include important.html first-line="**Primary Key comments**" content="Redshift doesn’t enforce the use of Primary Keys, but Stitch requires them to replicate data. In the following example, you'll see `COMMENT` being used to note the table's Primary Key. **Make sure you include the Primary Key comment in the next step, as missing Primary Keys will cause issues with data replication.**" %}

          Here's the transaction we'd use on the `rep_sales.orders` table:

          ```sql
          SET search_path to rep_sales;
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
          ALTER TABLE orders OWNER TO stitch_user;      /* Grants table ownership to Stitch */
          DROP TABLE old_orders;                        /* Drops the "old" table */
          END;
          ```

      - title: "Step 3: Verify the table owner"
        anchor: "step-3-verify-table-owner"
        content: |
          When you perform this process yourself, **make sure that the Stitch Redshift user retains ownership of the table**.

          If Stitch isn't the owner of the table, issues with data replication will arise.

      - title: "Step 4: Verify the encoding and key application"
        anchor: "step-4-verify-application"
        content: |
          To verify that the changes were applied correctly, retrieve the table’s schema again using this command:

          ```sql
          \d+ [schema_name].[table_name]
          ```

          In this example, if the Keys and encodings were applied correctly, the response would look something like this:

          ```sql
          | Column              | Data type                  | Encoding | Distkey | Sortkey |
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
          ```

          For the `id` column, the `Distkey` and `Sortkey` is set to `true`, meaning that the keys were properly applied. For `rep_name`, the `Encoding` is set to `bytedict`, indicating that the encoding was also properly applied.

---
{% include misc/data-files.html %}
{% assign destination = site.destinations | where:"type","redshift" | first %}