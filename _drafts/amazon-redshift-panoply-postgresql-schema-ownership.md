---
title: Amazon Redshift, Panoply, and PostgreSQL schema and table ownership
keywords: troubleshooting, destination, trouble, issue, help, error, errors, redshift, panoply, postgresql
permalink: /troubleshooting/destinations/amazon-redshift-panoply-postgresql-schema-ownership

layout: general

summary: ""
type: "redshift-destination, postgresql-destination error"
promote: "false"


walkthrough-data:
  pg-table:
    - schema: "salesforce"
      table: "contact"
      owner: "stitch"

    - schema: "google_adwords"
      table: "ads"
      owner: "database_admin"

    - schema: "google_adwords"
      table: "campaigns"
      owner: "database_admin"


sections:
  - content: |
      When an integration is initially connected to Stitch, a schema specific to that connection is created in your destination. Ownership permissions are required for all schemas and tables Stitch will load data into. Stitch occasionally needs to run `COMMENT` and `ALTER TABLE` commands to insert data, which require ownership privileges.

  - title: "Diagnose the issue"
    anchor: "diagnose-the-issue"
    content: |
      Receiving the following error in the **Notifications** tab of your Stitch account typically indicates a schema or table ownership issue:

      ```
      ERROR: must be owner of relation [table_or_schema_name]
      ```

      This error indicates that Stitch is unable to load data into the given schema or table because the Stitch user isn't the schema or table owner. Ownership of a database object provides privileges that Stitch requires to successfully load data.

      Performing the steps outlined in this guide can help you resolve the issue and get data flowing into your destination again.

  - title: "Step 1: Get table ownership info"
    anchor: "step-1--get-table-ownership-info"
    content: |
      {% include note.html type="single-line" content="**Note**: This step is only required if you aren't sure which schemas and tables may have possible ownership issues. Otherwise, skip to the next step." %}

      Query the catalog tables using this statement to list all tables and their owners:

      ```sql
      SELECT schemaname,
             tablename,
             tableowner
        FROM pg_catalog.pg_tables;
      ```

      Take note of any integration tables that aren’t owned by the Stitch user - those are the tables you’ll need to update. For example: In the table below, the `ads` and `campaigns` tables aren't owned by the `stitch_user`:

      <table class="attribute-list">
      <tr>
      <td>
      <strong>
      schemaname
      </strong>
      </td>
      <td>
      <strong>
      tablename
      </strong>
      </td>
      <td>
      <strong>
      tableowner
      </strong>
      </td>
      </tr>
      {% for record in page.walkthrough-data.pg-table %}
      <tr>
      <td>
      {{ record.schema }}
      </td>
      <td>
      {{ record.table }}
      </td>
      <td>
      {{ record.owner }}
      </td>
      </tr>
      {% endfor %}
      </table>

  - title: "Step 2: Transfer integration schema ownership to Stitch"
    anchor: "step-2--transfer-integration-schema-ownership"
    content: |
      Next, you'll transfer ownership of the integration to the Stitch user.

      {% capture heroku-user %}
      **Note**: For Heroku destinations, this will be the database user Stitch uses to connect to the destination. Refer to the [Heroku destination setup docs]({{ link.destinations.setup.heroku-postgres | prepend: site.baseurl | append: "#locate-connection-settings" }}) for more info.
      {% endcapture %}

      {{ heroku-user }}

      Transfer ownership of the integration schema to the Stitch user, replacing `<schema_name>` with the name of the schema and `<stitch_user>` with the name of the database user:

      ```sql
      ALTER SCHEMA <schema_name> OWNER TO <stitch_user>;
      ```

      For example: This command would transfer ownership of the `google_adwords` schema to the `stitch` user:

      ```sql
      ALTER SCHEMA google_adwords OWNER TO stitch;
      ```

      Repeat this step for every schema you need to transfer to Stitch.

  - title: "Step 3: Transfer integration table ownership to Stitch"
    anchor: "step-3--transfer-integration-table-ownership"
    content: |
      Next, you'll transfer ownership of all tables in the integration schema to the Stitch user. There are two ways to accomplish this:

      1. [Run a command for each table in the schema](#step-3--transfer-table-by-table), or
      2. [Run a psql script to automatically transfer ownership of tables](#step-3--transfer-script-method)

    subsections:
      - title: "Table-by-table method"
        anchor: "step-3--transfer-table-by-table"
        content: |
          {{ heroku-user }}

          For every table in the schema not owned by the Stitch user - as outlined in [Step 1](#step-1--get-table-ownership-info) - use the following command to transfer ownership.

          Transfer ownership of the integration's tables to the Stitch user, replacing `<schema_name>` with the name of the schema, `<table_name>` with the name of the table and `<stitch_user>` with the name of the database user:

          ```sql
          ALTER TABLE <schema_name>.<table_name> OWNER TO <stitch_user>;
          ```

          For example: This command would transfer ownership of the `ads` table in the `google_adwords` schema to the `stitch` user:

          ```sql
          ALTER TABLE google_adwords.ads OWNER TO stitch;
          ```

          Repeat this step for every table you need to transfer to Stitch.

      - title: "Script method"
        anchor: "step-3--transfer-script-method"
        content: |
          To transfer ownership of all tables in a schema automatically, run this script from the command line, replacing items enclosed in `< >`:

          ```psql
          for table in `psql -qAt --host <hostname> --port <port> --user <admin_user> -c "select tablename from pg_tables where schemaname = '<schema_name>';" {{ database_name }} ` ; do psql -qAt --host [your.{{ destination.type }}.amazonaws.com] --port <port> --user <admin_user> -c "alter table \"<schema_name>\".\"$table\" owner to <stitch_user>;" <database_name> ; done
          ```

          Repeat this for every schema that contains tablees you need to transfer to Stitch.

  - title: "Next steps"
    anchor: "next-steps"
    content: |
      If you need to transfer ownership of mulitple schemas, repeat [steps 2](#step-2--transfer-integration-schema-ownership) and [3](#step-3--transfer-integration-table-ownership) for each schema.

---
{% include misc/data-files.html %}