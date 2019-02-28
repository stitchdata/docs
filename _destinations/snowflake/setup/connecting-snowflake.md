---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/destination-templates/destination-setup/
## FOR INSTRUCTIONS & REFERENCE INFO


# -------------------------- #
#        Page Controls       #
# -------------------------- #

title: Connecting a Snowflake Destination to Stitch
permalink: /destinations/snowflake/connecting-a-snowflake-data-warehouse-to-stitch
tags: [snowflake_destination]
keywords: snowflake, snowflake data warehouse, snowflake data warehouse, snowflake etl, etl to snowflake, snowflake destination

summary: "Connect a Snowflake destination to your Stitch account."

content-type: "destination-setup"

toc: true
layout: tutorial
use-tutorial-sidebar: false


# -------------------------- #
#     Destination Details    #
# -------------------------- #

display_name: "Snowflake"
type: "snowflake"

ssh: false
ssl: true


# -------------------------- #
#        Requirements        #
# -------------------------- #

requirements:
  - item: "**A {{ destination.display_name }} account.**"
  - item: |
      **`ACCOUNTADMIN` role privileges in Snowflake, OR privileges equivalent to the `SECURITYADMIN` and `SYSADMIN` roles**. [More info on Snowflake's user roles can be found here](https://docs.snowflake.net/manuals/user-guide/security-access-control.html#system-defined-roles){:target="_blank"}.
  - item: |
      **Familiarity with {{ destination.display_name }}'s [SQL Worksheet feature](https://docs.snowflake.net/manuals/user-guide/snowflake-manager.html#worksheet-page){:target="_blank"} OR access to to a SQL client.**

      This tutorial will use the SQL Worksheet in the Snowflake web app to run SQL commands.


# -------------------------- #
#         Instructions       #
# -------------------------- #

steps:
  - title: "Create a Snowflake data warehouse"
    anchor: "create-data-warehouse"
    content: |
      {% capture auto-suspend-notice %}
      Make sure the `AUTO_SUSPEND` parameter is included in the warehouse creation command. This parameter determines how many seconds of inactivity must pass before a warehouse is automatically suspended.

      If this parameter isn't included, the default will be `NULL`, meaning that the warehouse will never automatically suspend. As a result, Snowflake credits will continue to be consumed even if the warehouse is inactive.
      {% endcapture %}

      {% capture pricing %}
      Before you create a warehouse, we recommend familiarizing yourself with [Snowflake's pricing and automated warehouse management features](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html){:target="_blank"}.
      {% endcapture %}

      {% include note.html type="single-line" content=pricing %}

      1. Log into your Snowflake account using a web browser or a SQL client.
      2. If you log in via a web browser, click the **Worksheet** icon at the top of the page.
      3. Create the warehouse by running this command, changing the`[square_brackets]` to the values you want:

         ```sql
         CREATE WAREHOUSE [stitch_warehouse]
         WITH
         AUTO_RESUME = TRUE|FALSE
         WAREHOUSE_SIZE = [size]
         AUTO_SUSPEND = [time_in_seconds];
         ```

         Check out [Snowflake's documentation](https://docs.snowflake.net/manuals/sql-reference/sql/create-warehouse.html){:target="new"} for more info on these parameters.

         The parameters in this command define the following:

          - **AUTO_RESUME**: If `TRUE`, the warehouse will be automatically resumed when accessed by a SQL statement. If `FALSE`, the warehouse will only start again when explicitly resumed through the Snowflake web interface or using `ALTER WAREHOUSE`.
          - **WAREHOUSE_SIZE**: Specifies the size of the warehouse to create. Accepted values are `XSMALL`, `SMALL`, `MEDIUM`, `LARGE`, `XLARGE`, `XXLARGE`, `XXXXLARGE`, and `XXXXLARGE`.

            The default is `XSMALL`.
          - **AUTO_SUSPEND**: Specifies the number of seconds of inactivity after which a warehouse is automatically suspended.
              {% include important.html first-line="**Make sure Auto-Suspend is enabled!**" content=auto-suspend-notice %}

  - title: "Create a Stitch database and database user"
    anchor: "create-database-and-user"
    content: |
      Next, you'll create a database and database user for Stitch.
    substeps:
      - title: "Create the database"
        anchor: "create-snowflake-database"
        content: |
          Create the database for Stitch, changing `[stitch_database]` to what you want the database to be called:

          ```sql
          CREATE DATABASE [stitch_database];
          ```

      - title: "Create the database user"
        anchor: "create-stitch-database-user"
        content: |
          {% include destinations/templates/destination-user-setup.html %}

  - title: "Configure network access settings"
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

  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      To complete the setup, you need to enter your {{ destination.display_name }} connection details into the {{ app.page-names.dw-settings }} page in Stitch.

      {% include destinations/setup/destination-settings.html %}
---
{% assign destination = site.destinations | where:"type",page.type | first %}
{% include misc/data-files.html %}
{% include misc/icons.html %}