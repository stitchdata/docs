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

title: Connecting an Amazon Aurora PostgreSQL-RDS Destination to Stitch
permalink: /destinations/postgresql/connecting-an-amazon-aurora-postgresql-rds-data-warehouse-to-stitch
keywords: postgresql data warehouse, postgresql data warehouse, etl to postgres, postgres etl, postgresql etl, postgres rds, postgres-rds, relational database services
summary: "Connect an Amazon Aurora PostgreSQL RDS database to your Stitch account as a destination."

content-type: "destination-setup"
key: "aurora-postgres-destination-setup"
order: 2

toc: true
layout: tutorial
use-tutorial-sidebar: false


# -------------------------- #
#     Destination Details    #
# -------------------------- #

display_name: "Amazon Aurora PostgreSQL"
type: "postgres"
setup-name: "PostgreSQL"

hosting-type: "amazon"

ssh: true
ssl: true
port: 5432

api-type: "postgres"

this-version: "1"


# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |
  Amazon Relational Database Services (RDS) is a managed database service that runs on familiar database engines like PostgreSQL.

  In this tutorial, we’ll walk you through how to connect an Amazon Aurora PostgreSQL RDS database to Stitch as a destination.


# -------------------------- #
#        Requirements        #
# -------------------------- #

requirements:
  - item: |
      {% assign destination = page %}
      **An up-and-running {{ destination.display_name }} instance.** Instructions for creating a {{ destination.display_name }} destination are outside the scope of this tutorial; our instructions assume that you have an instance up and running. For help getting started with {{ destination.display_name }}, refer to [Amazon's documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreatePostgreSQLInstance.html){:target="new"}.

      **Note**: The database must be running version 9.3 or higher.
  - item: |
      **Permissions in Amazon Web Services (AWS) that allow you to**:

        - Create/manage Security Groups, which is required to whitelist Stitch's IP addresses.
        - View database details, which is required for retrieving the database's connection details.
  - item: "**Database privileges that allow you to create users and grant privileges.** This is required to create a database user for Stitch."


# -------------------------- #
#         Instructions       #
# -------------------------- #

steps:
  - title: "Configure database connection settings"
    anchor: "connect-settings"
    content: |
      {% include integrations/templates/configure-connection-settings.html %}

  - title: "Create a {{ destination.display_name }} Stitch user"
    anchor: "create-stitch-user"
    content: |
      {% include note.html type="single-line" content="**Note**: You must have the ability to create a user and grant privileges to complete this step." %}

      In the following tabs are the instructions for creating a Stitch {{ destination.display_name }} database user and explanations for the permissions Stitch requires.

      {% assign clean-database-name = page.display_name | downcase | replace:" ","-" %}
      {% include destinations/templates/destination-user-setup.html database-type=clean-database-name %}

  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      To complete the setup, you need to enter your {{ destination.display_name }} connection details into the {{ app.page-names.dw-settings }} page in Stitch.

    substeps:
      - title: "Locate the {{ destination.display_name }} connection details in AWS"
        anchor: "locate-connection-details-aws"
        content: |
          {% include shared/connection-details/amazon.html type="connection-details" %}

      - title: "Define the connection details in Stitch"
        anchor: "enter-connection-details-into-stitch"
        content: |
          {% include shared/database-connection-settings.html type="general" %}

      - title: "Define SSH connection details"
        anchor: "define-ssh-connection-details"
        content: |
          {% include shared/database-connection-settings.html type="ssh" %}

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