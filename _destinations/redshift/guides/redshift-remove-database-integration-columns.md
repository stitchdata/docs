---
# -------------------------- #
#        Page Controls       #
# -------------------------- #

title: Removing Columns from Redshift
permalink: /destinations/redshift/remove-columns-redshift
redirect_from: /destinations/redshift/remove-database-integration-columns-redshift
keywords: redshift, amazon redshift, redshift data warehouse, database integration, remove column, remove columns
summary: "Want to tidy up your Amazon Redshift destination by removing columns you're no replicating? In this article, we'll walk you through using `pg_dump` to remove unwanted columns."
type: "redshift"

layout: tutorial
use-tutorial-sidebar: false

content-type: "destination-general"

# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |
  {% include important.html type="single-line" content="Columns can only be removed from integration tables where column selection is supported. If Stitch detects data for a removed column, the column will be recreated in the destination." %}

  When you rename or no longer want to replicate a column, what happens? By default, Stitch will not remove columns from destination tables, even if no new values are being loaded, meaning that all historical data for the column will remain in the table.

  For some Stitch users, retaining these columns is perfectly fine. If you like to keep things tidy, however, you can easily remove the unwanted columns by recreating your realized tables without those columns.

  We recommend using `pg_dump` for this process, which is similar to altering the SORT and DIST keys on tables.


# -------------------------- #
#         Instructions       #
# -------------------------- #

steps:
  - title: "Retrieve the table definition"
    anchor: "retrieve-table-definition"
    content: |
      In this example, we'll use a table named `orders` in the `rep_sales` schema and remove the `order_name` column.

      Using a SQL client or a command line tool, login to your Redshift database as an administrator.

      Retrieve the definition of the table using the following command, replacing the items in brackets (`< >`) with the required info about your Redshift instance and `rep_sales` and `orders` with the name of the schema and table, respectively:

      ```sql
      pg_dump --host <yourawshost.redshift.amazonaws.com> --port <port> --username <admin_username><database_name> -t 'rep_sales.orders'
      ```

      This will return a response similar to the following:

      ```sql
      SET statement_timeout = 0;
      SET client_encoding = 'UTF8';
      SET standard_conforming_strings = off;
      SET check_function_bodies = false;
      SET client_min_messages = warning;
      SET escape_string_warning = off;

      SET search_path = rep_sales, pg_catalog;

      SET default_tablespace = '';

      SET default_with_oids = true;

      --
      -- Name: orders; Type: TABLE; Schema: rep_sales; 
        Owner: <admin_username>; Tablespace: 
      --

      CREATE TABLE orders (
           id bigint,
           value character varying(128),
           order_name character varying(128), 
           {{ system-column.sequence }} numeric(18,0),
           {{ system-column.received-at }} timestamp without time zone,
           {{ system-column.batched-at }} timestamp without time zone,
           {{ system-column.table-version }} bigint,
           {{ system-column.replication-id }} character varying(128)
      );

      ALTER TABLE rep_sales.orders OWNER TO <admin_username>;

      --
      -- Data for Name: orders; Type: TABLE DATA; Schema: 
        rep_sales; Owner: <admin_username>
      --
      ...
      ```

  - title: "Retrieve the table's Primary Key comment"
    anchor: "retrieve-primary-key-comment"
    content: |
      Next, you need to retrieve the table's Primary Key comment. This will be used in the next step to indicate which column(s) are the table's Primary Keys.

      Run the following query:

      ```sql
      SELECT description
        FROM pg_catalog.pg_description
       WHERE objoid = 'orders'::regclass;
      ```

      The result will look like the following, where `primary_keys` is an array of strings referencing the columns used as the table's Primary Key:

      ```sql
      {"primary_keys":["id"]}
      ```

      This will be used in the next step to indicate which column(s) are the table's Primary Keys.

      {% include important.html first-line="**Primary Key comments**" content="Redshift doesn’t enforce the use of Primary Keys, but Stitch requires them to replicate data. In the following example, you'll see `COMMENT` being used to note the table's Primary Key. **Make sure you include the Primary Key comment in the next step, as missing or incorrectly defined Primary Key comments will cause issues with data replication.**" %}

  - title: "Copy historical data into the new table"
    anchor: "copy-historical-data-new-table"
    content: |
      In this step, you'll execute a transaction that will perform the following:

          1. Renames the table
          2. Creates a new table with a structure that includes the SORT and DIST keys
          3. Copies the data from the old table and inserts it into the new, redefined table
          4. Renames the new table
          5. Drops the old table

      When you run this transaction yourself, you’ll need to change everything inside the brackets (`< >`) as well as the following:

      - **The column names in the table**. Be sure to add `{{ system-column.rjm-prefix }}` or `{{ system-column.prefix }}` columns into the new table schema.
      - **The Stitch user's username.** In the `ALTER TABLE OWNER` line, you’ll see `<stitch_username>`. This is the username of the Redshift user that Stitch uses to connect to your data warehouse. Failing to enter the Stitch username here will prevent Stitch from loading data into this table.

      For the `rep_sales.orders` example table, this is the transaction that will perform the actions listed above:

      ```sql
      SET search_path to rep_sales;
      BEGIN;
       ALTER TABLE orders RENAME TO old_orders;
       CREATE TABLE new_orders (
          id bigint,                         /* Desired schema without the order_name column */
          value character varying(128),
          {{ system-column.sequence }} numeric(18,0),
          {{ system-column.received-at }} timestamp without time zone,
          {{ system-column.batched-at }} timestamp without time zone,
          {{ system-column.table-version }} bigint,
          {{ system-column.replication-id }} character varying(128)
       );
       INSERT INTO new_orders
          (SELECT id,                        /* Repeat the desired schema here */
                  value,
                  {{ system-column.sequence }},
                  {{ system-column.received-at }},
                  {{ system-column.batched-at }},
                  {{ system-column.table-version }},
                  {{ system-column.replication-id }}
           FROM old_orders);

       COMMENT ON table new_orders IS '{"primary_keys":["XXXXX"]}';
                                                              /* Sets Primary Key comment */

       ALTER TABLE new_orders RENAME TO orders;
       ALTER TABLE orders OWNER TO <stitch_user>;      /* Grants table ownership to Stitch */
       DROP TABLE old_orders;                        /* Drops the "old" table */
       END;
      ```

  - title: "Verify the table owner"
    anchor: "verify-table-owner"
    content: |
      Stitch requires ownership of all integration tables to successfully load data. If Stitch isn't the table owner, issues with data replication will occur.

      To verify the table's owner, run the following query and replace `rep_sales` and `orders` with the names of the schema and table, respectively:

      ```sql
      SELECT schemaname,
             tablename,
             tableowner
        FROM pg_catalog.pg_tables
       WHERE schemaname = 'rep_sales'
         AND tablename = 'order'
      ```

      If Stitch is not the owner of the table, run the following command:

      ```sql
      ALTER TABLE <schema_name>.<table_name> OWNER TO <stitch_user>;
      ```

  - title: "Verify the new schema"
    anchor: "verify-new-table-schema"
    content: |
      To verify that the changes were applied correctly, retrieve the table’s schema again using this command, replacing `rep_sales` and `orders` with the names of your schema and table, respectively: 

      ```sql
      \d+ rep_sales.orders
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

      Note that the `order_name` column no longer appears in the table's schema, indicating that the transaction used to remove it was successful.
---
{% include misc/data-files.html %}
{% assign destination = site.destinations | where:"type","redshift" | first %}