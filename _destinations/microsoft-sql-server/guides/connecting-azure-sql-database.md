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

title: Connecting an Azure SQL Database Destination to Stitch
permalink: /destinations/microsoft-sql-server/connecting-azure-sql-database-destination-to-stitch

keywords: azure sql database, azure sql database data warehouse, azure sql database data warehouse, azure sql database etl, etl to azure sql database, azure sql database destination
summary: "Connect an Azure SQL Database destination to your Stitch account."

content-type: "destination-setup"
key: "azure-sql-database-destination-setup"
order: 2

toc: true
layout: tutorial
use-tutorial-sidebar: false


# -------------------------- #
#     Destination Details    #
# -------------------------- #

type: "microsoft-sql-server"
display_name: "Azure SQL Database"
name: "azure-sql-database"

ssh: true
ssl: true
port: 1433

hosting-type: "microsoft-azure" # amazon, generic, microsoft, etc.

api-type: "mssql_server"

this-version: "1"


# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements:
  - item: |
      {% assign destination = page %}
      **An up-and-running {{ destination.display_name }} instance.** Instructions for creating a {{ destination.display_name }} destination are outside the scope of this tutorial; our instructions assume that you have an instance up and running. For help getting started with {{ destination.display_name }}, refer to [Microsoft's documentation](https://learn.microsoft.com/en-us/azure/azure-sql/){:target="new"}.


# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

steps:
  - title: "Verify your Stitch account's data pipeline region"
    anchor: "verify-stitch-account-region"
    content: |
      {% include shared/whitelisting-ips/locate-region-ip-addresses.html first-step=true %}

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

  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      To complete the setup, you need to enter your {{ destination.display_name }} connection details into the {{ app.page-names.dw-settings }} page in Stitch.

    substeps:
      - title: "Enter connection details into Stitch"
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
          {% capture tsl-support-note %}
          SSL can only be used with versions of {{ destination.display_name }} that support TSL 1.2. Check which versions support it in [Microsoft's documentation]({{ site.data.destinations.microsoft-sql-server.resource-links.tls-support }}).
          {% endcapture %}
          {% include note.html type="single-line" content=tsl-support-note %}

          Check the **{{ defaults.field-names.ssl }}** checkbox. {{ defaults.field-copy.ssl }}


      - title: "Save the destination"
        anchor: "save-destination"
        content: |
          {% include shared/database-connection-settings.html type="finish-up" %}
---
{% include misc/data-files.html %}
{% assign destination = page %}