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

title: Connecting a Google CloudSQL PostgreSQL Destination to Stitch
keywords: postgresql data warehouse, postgresql data warehouse, etl to postgres, postgres etl, postgresql etl, cloudsql postgres, cloudsql postgresql, cloudsql data warehouse

permalink: /destinations/postgresql/connecting-a-google-cloudsql-postgresql-data-warehouse
redirect_from: /destinations/postgresq/connecting-a-google-cloudsql-postgresql-data-warehouse

summary: "Connect a Google CloudSQL PostgreSQL database to your Stitch account as a destination."

content-type: "destination-setup"
key: "cloudsql-postgres-destination-setup"
order: 3

toc: true
layout: tutorial
use-tutorial-sidebar: false


# -------------------------- #
#     Destination Details    #
# -------------------------- #

display_name: "Google CloudSQL PostgreSQL"
name: "cloudsql-postgres"

type: "postgres"
setup-name: "PostgreSQL"

hosting-type: "google-cloudsql"

ssh: false
ssl: false
port: 5432

this-version: "1"

api-type: "postgres"

# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |
  In this tutorial, we’ll walk you through how to connect a Google CloudSQL PostgreSQL instance to Stitch as a destination.

  For more info on Google CloudSQL's features and limitations, [check out the official Google documentation](https://cloud.google.com/sql/docs/postgres/){:target="new"}.


# -------------------------- #
#        Requirements        #
# -------------------------- #

requirements:
  - item: |
      {% assign destination = page %}
      **An up-and-running, publicly accessible {{ destination.display_name }} instance.** Instructions for creating a {{ destination.display_name }} destination are outside the scope of this tutorial; our instructions assume that you have an instance up and running. For help getting started with {{ destination.display_name }}, refer to [Google's documentation](https://cloud.google.com/sql/docs/postgres/create-instance){:target="new"}.

      **Note**: The instance you want to connect must be both publicly accessible and running PostgreSQL version 9.3 or higher.
  - item: |
      **An existing, billing-enabled Cloud Platform project that houses the instance**. Even if you're using the Free option, [billing must be enabled](https://support.google.com/cloud/answer/6293499#enable-billing){:target="new"} for the project or Stitch will encounter connection issues.

      Selecting a project can be done in the [Projects page of the Google Console](https://console.cloud.google.com/project){:target="new"}.
  - item: |
      **Access to the CloudSQL Administration API for the Cloud Platform Project housing the instance**. Refer to [Google's documentation](https://console.cloud.google.com/flows/enableapi?apiid=sqladmin){:target="new"} for more info.
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

      Configuring the second part of the access control settings requires creating a database user for Stitch. This guide will use the psql method to create the user, which requires the use of a SQL client.

      {% assign clean-database-name = page.display_name | downcase | replace:" ","-" %}
      {% include destinations/templates/destination-user-setup.html database-type=clean-database-name %}

  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      To complete the setup, you need to enter your {{ destination.display_name }} connection details into the {{ app.page-names.dw-settings }} page in Stitch.
    substeps:
      - title: "Locate the connection details in the Google Console"
        anchor: "locate-database-connection-details"
        content: |
          {% include shared/connection-details/google-cloudsql.html %}

      - title: "Enter connection details into Stitch"
        anchor: "enter-connection-details-into-stitch"
        content: |
          {% include shared/database-connection-settings.html type="general" %}

      - title: "Save the destination"
        anchor: "save-destination"
        content: |
          {% include shared/database-connection-settings.html type="finish-up" %}
---
{% include misc/data-files.html %}
{% assign destination = page %}