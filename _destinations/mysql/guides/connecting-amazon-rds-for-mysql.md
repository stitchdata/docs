---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/destination-templates/destination-setup/
## FOR INSTRUCTIONS & REFERENCE INFO


# -------------------------- #
# Page formatting & Controls #
# -------------------------- #

title: Connecting an Amazon RDS for MySQL Destination to Stitch
permalink: /destinations/mysql/connecting-an-amazon-rds-for-mysql-destination-to-stitch

keywords: amazon rds for mysql, amazon rds for mysql data warehouse, amazon rds for mysql data warehouse, amazon rds for mysql etl, etl to amazon rds for mysql, amazon rds for mysql destination
summary: "Connect an Amazon RDS for MySQL destination to your Stitch account."

content-type: "destination-setup"
key: "mysql-rds-destination-setup"
order: 2

toc: true
layout: tutorial
use-tutorial-sidebar: false


# -------------------------- #
#     Destination Details    #
# -------------------------- #

type: "mysql"
display_name: "Amazon RDS for MySQL"
name: "amazon-rds-mysql"

port: 3306

hosting-type: "amazon" # amazon, generic, microsoft, etc.

api-type: "mysql_destination"

this-version: "1"

ssh: true

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements:
  - item: |
      {% assign destination = page %}
      **An up-and-running {{ destination.display_name }} instance.** Instructions for creating a {{ destination.display_name }} destination are outside the scope of this tutorial; our instructions assume that you have an instance up and running. For help getting started with {{ destination.display_name }}, refer to [AWS's documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html){:target="new"}.
  - item: |
      **A database that uses the InnoDB storage engine.** This is the default storage engine for all supported {{ destination.display_name }} versions and the only one supported by Stitch's {{ destination.display_name }} destination.

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

steps:
## The Data pipeline region step is necessary ONLY
## if the user needs to whitelist Stitch's IP addresses
## for setup.

  - title: "Verify your Stitch account's data pipeline region"
    anchor: "verify-stitch-account-region"
    content: |
      {% include shared/whitelisting-ips/locate-region-ip-addresses.html first-step=true %}

## The database connection settings step is necessary ONLY
## if the user needs to whitelist Stitch's IP addresses
## for setup.
  - title: "Configure database connection settings"
    anchor: "connect-settings"
    content: |
      {% include integrations/templates/configure-connection-settings.html %}

  - title: "Create a Stitch {{ destination.display_name }} database user"
    anchor: "create-database-user"
    content: |
      {% include note.html type="single-line" content="**Note**: You must have superuser privileges or the ability to create a user and grant privileges to complete this step." %}

      In the following tabs are the instructions for creating a Stitch {{ destination.display_name }} database user and explanations for the permissions Stitch requires.

      {% include destinations/templates/destination-user-setup.html %}

  - title: "Enable local data loading"
    anchor: "enable-local-data-loading"
    content: |
      To allow Stitch to stream data from the cloud into your destination, you need to enable the `local_infile` parameter in MySQL.

      1. Check if the feature is already enabled. You can:
          - Look for the `local_infile` parameter in your `my.cnf` configuration file.
          - Run the following command from the command line:
              ```
              show global variables like 'local_infile';
              ```
      1. If the feature is disabled, enable it. To do so, you can:
          - Append the following line in `my.cnf`, after the `[mysqld]` tag. If this tag does not exist, create it. It should look like this:
              ```
              [mysqld]
              local_infile=true
              ```
          - Run the following command while logged in with your root user:
              ```
              set global local_infile=true
              ```
      1. If you are using a supported {{ destination.display_name }} version older than `8.0` (from `5.7.8` to `5.7.37`), you may run into errors stating that you are loading invalid UTF-8 characters. To avoid this issue, append the following lines in `my.cnf`:
            ```
            [mysql]
            default-character-set=utf8mb4

            [mysqld]
            character-set-server=utf8mb4
            collation-server=utf8mb4_general_ci
            ```

            If the `[mysql]` and `[mysqld]` tags already exist in the file, add the the values after each tag, otherwise add both the tags and values.
      
      1. Restart your database server to apply the changes.
          

      For more information, see the [MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/load-data-local-security.html).
      

  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      To complete the setup, you need to enter your {{ destination.display_name }} connection details into the {{ app.page-names.dw-settings }} page in Stitch.

    substeps:
      - title: "Enter connection details into Stitch"
        anchor: "enter-connection-details-into-stitch"
        content: |
          {% include shared/database-connection-settings.html type="general" %}

## The SSH step should remain ONLY if the destination
## supports SSH.
      - title: "Define SSH connection details"
        anchor: "define-ssh-connection-details"
        content: |
          {% include shared/database-connection-settings.html type="ssh" %}

## The SSL step should remain ONLY if the destination
## supports SSL.
      - title: "Define SSL connection details"
        anchor: "define-ssl-connection-details"
        content: |
          {% include shared/database-connection-settings.html type="ssl" ssl-fields=true %}

      - title: "Save the destination"
        anchor: "save-destination"
        content: |
          {% include shared/database-connection-settings.html type="finish-up" %}
---
{% include misc/data-files.html %}
{% assign destination = page %}