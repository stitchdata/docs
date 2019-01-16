---
title: Removing Columns from Redshift
permalink: /destinations/redshift/remove-columns-redshift
redirect_from: /destinations/redshift/remove-database-integration-columns-redshift
tags: [redshift_destination]
keywords: redshift, amazon redshift, redshift data warehouse, database integration, remove column, remove columns
summary: "Want to tidy up your Amazon Redshift data warehouse by removing columns you're no replicating? In this article, we'll walk you through using `pg_dump` to remove unwanted columns."
type: "redshift"

content-type: "destination-general"


sections:
  - content: |
      {% include important.html type="single-line" content="Columns can only be removed from integration tables where column selection is supported. If Stitch detects data for a removed column, the column will be recreated in the destination." %}

      When you rename or no longer want to replicate a column, what happens? For both Full Table and Incremental replication, the old column and all historical data will remain in the table even if there aren’t any new values being replicated.

      For some Stitch users, retaining these columns is perfectly fine. If you like to keep things tidy, however, you can easily remove the unwanted columns by recreating your realized tables without those columns.

      We recommend using `pg_dump` for this process, which is similar to altering the `SORT and DIST` keys on your tables.

  - title: "Step 1: Retrieve the table definition"
    anchor: "step-1-retrieve-table-definition"
    content: |
      In this example, we’ll show you how to remove the unwanted columns using `pg_dump` from the command line. We marked everything you’ll need to define yourself in square brackets `[like this]`.

      {% include note.html type="single-line" content="If any new data is detected for the deleted column, Stitch will recreate the column in your data warehouse." %}

      First, you’ll grab a full definition of your target table and then create the new table structure, removing the unwanted column(s):

      ```
      pg_dump --host [yourawshost.redshift.amazonaws.com] --port [your_port] --username [admin_username][database_name] -t '[schema_name.original_target_table_name]'
      ```

      The above command will return a response similar to the following:

      ```
      SET statement_timeout = 0;
      SET client_encoding = 'UTF8';
      SET standard_conforming_strings = off;
      SET check_function_bodies = false;
      SET client_min_messages = warning;
      SET escape_string_warning = off;

      SET search_path = schema_name, pg_catalog;

      SET default_tablespace = '';

      SET default_with_oids = true;

      --
      -- Name: original_target_table_name; Type: TABLE; Schema: schema_name; 
        Owner: admin_username; Tablespace: 
      --

      CREATE TABLE original_target_table_name (
           id bigint,
           value character varying(128),
           the_column_being_removed numeric(18,0), 
           {{ system-column.sequence }} numeric(18,0),
           {{ system-column.received-at }} timestamp without time zone,
           {{ system-column.batched-at }} timestamp without time zone,
           {{ system-column.table-version }} bigint,
           {{ system-column.replication-id }} character varying(128)
      );

      ALTER TABLE schema_name.original_target_table_name OWNER TO admin;

      --
      -- Data for Name: original_target_table_name; Type: TABLE DATA; Schema: 
        schema_name; Owner: admin
      --
      ...
      ```

  - title: "Step 2: Retrieve the table's Primary Key comment"
    anchor: "step-2-retrieve-primary-key-comment"
    content: |
      Next, you need to retrieve the table's Primary Key comment. This will be used in the next step to indicate which column(s) are the table's Primary Keys.

      Run the following query:

      ```sql
      SELECT description
        FROM pg_description
       WHERE objoid = '[original_target_table_name]'::regclass;
      ```

      This will retrieve the table's Primary Key comment:

      ```
      {"primary_keys":["column_name"]}
              /* format for Primary Key with one column */

      {"primary_keys":["column_name1", "column_name2"]}
              /* format for Primary Key with multiple columns */
      ```

      This will be used in the next step to indicate which column(s) are the table's Primary Keys.

      {% include important.html first-line="**Primary Key comments**" content="Redshift doesn’t enforce the use of Primary Keys, but Stitch requires them to replicate data. In the following example, you'll see `COMMENT` being used to note the table's Primary Key. **Make sure you include the Primary Key comment in the next step, as missing Primary Keys will cause issues with data replication.**" %}

  - title: "Step 3: Copy historical data into the new table"
    anchor: "step-3-copy-historical-data-new-table"
    content: |
      Next, you’ll `SELECT` all the historical data from the unwanted column into the new table. When you run this transaction yourself, you’ll need to change everything inside `[the square brackets]` as well as the following:

      - The column names in the table. Be sure to add `{{ system-column.rjm-prefix }}` or `{{ system-column.prefix }}` columns into the new table schema.
      - In the `ALTER TABLE OWNER` line, you’ll see `[stitch_redshift_user]`. This is the username of the Redshift user that Stitch uses to connect to your data warehouse. **Failing to enter the Stitch username here will prevent Stitch from replicating data for this table.**

      Here’s the transaction for our example table. Note where the undesired column is marked - when running the transaction yourself, you'll remove this:

      ```sql
      SET search_path to [schema_name];
      BEGIN;
       ALTER TABLE [table_name] RENAME TO [old_table_name];
       CREATE TABLE [new_table_name] (
          id bigint,
          value character varying(128),
          column_being_removed (18,0),                /* The undesired column - take it out */
          {{ system-column.sequence }} numeric(18,0),
          {{ system-column.received-at }} timestamp without time zone,
          {{ system-column.batched-at }} timestamp without time zone,
          {{ system-column.table-version }} bigint,
          {{ system-column.replication-id }} character varying(128)
       );
       INSERT INTO [new_table_name]
          (SELECT id,                                 /* Repeat the desired schema here */
                  value,
                  {{ system-column.sequence }},
                  {{ system-column.received-at }},
                  {{ system-column.batched-at }},
                  {{ system-column.table-version }},
                  {{ system-column.replication-id }}
           FROM [old_table_name]);

      COMMENT ON table [new_table_name]               /* Sets Primary Key comment */
      IS '{"primary_keys":["column_name"]}';          /* This is the most important part! */

      ALTER TABLE [new_table_name] RENAME TO [table_name];

      ALTER TABLE [table_name] OWNER TO [stitch_redshift_user];
                                          /* Grants table ownership to Stitch */

      DROP TABLE [old_table_name];
                                          /* Drops the "old" table with the undesired column */
      END;
      ```

  - title: "Step 4: Verify the table owner"
    anchor: "step-4-verify-table-owner"
    content: |
      When you perform this process yourself, **make sure that the Stitch Redshift user retains ownership of the table.**

      If Stitch isn't the owner of the table, issues with data replication will arise.

  - title: "Step 5: Verify the new schema"
    anchor: "step-5-verify-new-table-schema"
    content: |
      Verify your changes by using this command to retrieve the table’s schema:

      ```sql
      \d+ [schema_name].[table_name]
      ```

      The response would look something like this for the example table in this tutorial:

      ```markdown
      | column              | data type                   |
      |---------------------+-----------------------------|
      | id                  | BIGINT                      |
      | value               | VARCHAR(128)                |
      | {{ system-column.sequence }}       | NUMERIC                     |
      | {{ system-column.received-at }}    | TIMESTAMP WITHOUT TIMEZONE  |
      | {{ system-column.batched-at }}     | TIMESTAMP WITHOUT TIMEZONE  |
      | {{ system-column.table-version }}  | BIGINT                      |
      | {{ system-column.replication-id }} | VARCHAR(128)                |
      ```
---
{% include misc/data-files.html %}
{% assign destination = site.destinations | where:"type","redshift" | first %}