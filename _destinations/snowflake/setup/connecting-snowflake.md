---
title: Connecting a Snowflake Data Warehouse to Stitch
permalink: /destinations/snowflake/connecting-a-snowflake-data-warehouse-to-stitch
tags: [snowflake_destination]
keywords: snowflake, snowflake data warehouse, snowflake data warehouse, snowflake etl, etl to snowflake, snowflake destination

summary: "Connect a Snowflake destination to your Stitch account."
toc: true
layout: destination-setup-guide
display_name: "Snowflake"
type: "snowflake"

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: "**A {{ destination.display_name }} account.**"
  - item: |
      **`ACCOUNTADMIN` role privileges in Snowflake, OR privileges equivalent to the `SECURITYADMIN` and `SYSADMIN` roles**. [More info on Snowflake's user roles can be found here](https://docs.snowflake.net/manuals/user-guide/security-access-control.html#system-defined-roles){:target="_blank"}.
  - item: |
      **Familiarity with {{ destination.display_name }}'s [SQL Worksheet feature](https://docs.snowflake.net/manuals/user-guide/snowflake-manager.html#worksheet-page){:target="_blank"} OR access to to a SQL client.**

      This tutorial will use the SQL Worksheet in the Snowflake web app to run SQL commands.

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "Create a Snowflake Data Warehouse"
    anchor: "create-data-warehouse"
    content: |
      {% capture pricing %}
      Before you create a warehouse, we recommend familiarizing yourself with [Snowflake's pricing and automated warehouse management features](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html){:target="_blank"}.
      {% endcapture %}

      {% include note.html content=pricing %}

      1. Log into your Snowflake account using a web browser or a SQL client.
      2. If you log in via a web browser, click the **Worksheet** icon at the top of the page.
      3. Create the warehouse:

         ```sql
         CREATE WAREHOUSE [stitch_warehouse]
          WITH
          WAREHOUSE_SIZE = '[size]' // xsmall, small, medium, large, xlarge, xxlarge, xxxlarge
         ```

      Additional warehouse parameters are available, including settings for Auto Suspend and Auto Resume. [Check out Snowflake's documentation for detailed explanations.](https://docs.snowflake.net/manuals/sql-reference/sql/create-warehouse.html)

  - title: "Create a Stitch Database & Database User"
    anchor: "create-database-and-user"
    content: |
      Next, you'll create a database and database user for Stitch.
    substeps:
      - title: "Create the Database"
        anchor: "create-snowflake-database"
        content: |
          Create the database for Stitch, changing `[stitch_database]` to what you want the database to be called:

          ```sql
          CREATE DATABASE [stitch_database];
          ```

      - title: "Create the Database User"
        anchor: "create-stitch-database-user"
        content: |
          1. Create a role for the Stitch user:

             ```sql
             CREATE ROLE [stitch_role] COMMENT = 'Role for Stitch access';
             ```

          2. **Optional**: If you've created a hierarchy that assigns all custom roles to the `SYSADMIN` role, grant the `stitch_role` [to the  `SYSADMIN` role](https://docs.snowflake.net/manuals/user-guide/security-access-control.html#role-hierarchy-and-privilege-inheritance){:target="_blank"}:

             ```sql
             GRANT ROLE [stitch_role] to role SYSADMIN;
             ```

          3. [Grant warehouse privileges to the Stitch role](https://docs.snowflake.net/manuals/user-guide/security-access-control.html#virtual-warehouse-privileges){:target="_blank"}, using the name of the warehouse you created for Stitch:

             ```sql
             GRANT ALL ON WAREHOUSE [warehouse] TO ROLE [stitch_role];

             // Grants all privileges except ownership
             ```

          4. [Grant database privileges to the Stitch role](https://docs.snowflake.net/manuals/user-guide/security-access-control.html#database-privileges){:target="_blank"}, using the name of the database you created for Stitch:

             ```sql
             GRANT ALL ON DATABASE [stitch_database] TO ROLE [stitch_role];
             ```

             Note that the privileges granted in steps 3 and 4 of this section will only apply to the warehouse and database you specify in the above queries. The Stitch user will not be granted privileges to any other warehouse or database unless you elect to do so.

          5. Create the Stitch user and grant the Stitch role to the user:

             ```sql
             CREATE USER [stitch_user]
                PASSWORD='[password]'
                COMMENT='User for Stitch database user'
                DEFAULT_ROLE='[stitch_role]'
                DEFAULT_WAREHOUSE='[warehouse]';

             GRANT ROLE [stitch_role] TO USER [stitch_user];
             ```

  - title: "Configure Network Access Settings"
    anchor: "whitelist-stitch-ips"
    content: |
      {% capture ip-addresses %}
      {% for ip-address in ip-addresses %}
      {{ ip-address.ip | prepend: "'"| append: "'," }}
      {% endfor %}
      {% endcapture %}

      In Snowflake, access is configured and managed through [Network Security Policies](https://docs.snowflake.net/manuals/user-guide/network-policies.html). 

      Stitch's IP addresses must be added to a network policy's **Allowed IP List** for the connection to be successful.

      1. Create the network policy and add Stitch's IP addresses to the list of allowed IP addresses.

         In the command below, change `[your-current-ip-address]` to the current IP address of the computer you're working on - this is required for the next step:

         ```sql
         CREATE NETWORK POLICY [stitch_policy]
         ALLOWED_IP_LIST = ({{ ip-addresses | strip_newlines | append:"'[your-current-ip-address]'" }});
         ```

      2. Apply the network policy to the account. Note that your current IP address must be included in the Allowed IP List to run this command successfully:

         ```sql
         ALTER ACCOUNT SET NETWORK_POLICY = [stitch_policy];
         ```

      If you encounter an error, ensure that your current IP address is in the Allowed IP List and try again. [Contact Snowflake support]({{ destination.contact-support }}) if errors persist.

  - title: "connect stitch"

---
{% assign destination = site.destinations | where:"type",page.type | first %}
{% include misc/data-files.html %}
{% include misc/more-info-icons.html %}

In this tutorial, we'll walk you through spinning up your own Snowflake data warehouse and connecting it to Stitch.