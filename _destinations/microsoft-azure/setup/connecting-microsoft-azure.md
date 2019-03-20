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

title: Connecting a Microsoft Azure SQL Data Warehouse Destination to Stitch
permalink: /destinations/microsoft-azure-sql-data-warehouse/connecting-a-microsoft-azure-sql-data-warehouse-to-stitch
redirect_from: /destinations/microsoft-azure-sql-data-warehouse/connecting-microsoft-azure-sql-data-warehouse-to-stitch-ssh-tunnel
keywords: microsoft azure sql data warehouse, microsoft azure data warehouse, microsoft azure data warehouse, microsoft azure etl, etl to microsoft azure, microsoft azure destination
summary: "Connect a Microsoft Azure SQL data warehouse to your Stitch account."

content-type: "destination-setup"

toc: true
layout: tutorial
use-tutorial-sidebar: false


# -------------------------- #
#     Destination Details    #
# -------------------------- #

type: "microsoft-azure"
display_name: "Microsoft Azure SQL Data Warehouse"

hosting-type: "microsoft-azure"

ssh: true
ssl: true
port: 1433


# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |
  {% capture setup-notice %}
  Stitch's {{ destination.display_name }} destination only works with Microsoft's [Azure SQL Data Warehouse product](https://azure.microsoft.com/en-us/services/sql-data-warehouse/){:target="new"}.

  Stitch doesn't currently support using Azure SQL Server or Azure SQL Database as a destination. Attempting to connect these products to Stitch via the {{ destination.display_name }} destination in Stitch will result in errors.
  {% endcapture %}

  {% include note.html first-line="**Stitch only supports connecting to Azure SQL Data Warehouse instances**" content=setup-notice %}
  

# -------------------------- #
#        Requirements        #
# -------------------------- #

requirements:
  - item: |
      **An up-and-running {{ destination.display_name }} instance.** Instructions for creating a {{ destination.display_name }} destination are outside the scope of this tutorial; our instructions assume that you have an instance up and running. For help getting started with {{ destination.display_name }}, refer to [Microsoft's documentation](https://docs.microsoft.com/en-us/azure/sql-data-warehouse/create-data-warehouse-portal){:target="new"}.
  - item: |
      **An existing Azure Storage account.** Instructions for creating an Azure Storage account are outside the scope of this tutorial. For help getting started with an Azure Storage account, refer to [Microsoft's documentation](https://docs.microsoft.com/en-us/azure/storage/){:target="new"}.

# -------------------------- #
#         Instructions       #
# -------------------------- #

steps:
  - title: "Configure database connection settings"
    anchor: "connect-settings"
    content: |
      {% include integrations/templates/configure-connection-settings.html %}

  - title: "Generate storage credentials"
    anchor: "generate-storage-credentials"
    content: |
      {% include destinations/microsoft-azure/azure-storage-credentials.html type="intro" %}

    substeps:
      - title: "Generate a shared access signature URL"
        anchor: "generate-shared-access-signature-url"
        content: |
          {% include destinations/microsoft-azure/azure-storage-credentials.html type="generate-sas-url" %}
          
      - title: "Retrieve your storage access key"
        anchor: "retrieve-storage-access-key"
        content: |
          {% include destinations/microsoft-azure/azure-storage-credentials.html type="retrieve-storage-access-key" %}
          
  - title: "Create a {{ destination.display_name }} Stitch user"
    anchor: "create-stitch-user"
    content: |
      In this step, you'll create a dedicated database user for Stitch. Creating a user for Stitch ensures that Stitch will be visible in any audits or logs, and that you can control the permissions granted to the user.

      {% include destinations/templates/destination-user-setup.html %}

  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      To complete the setup, you need to enter your {{ destination.display_name }} connection details into the {{ app.page-names.dw-settings }} page in Stitch.

    substeps:
      - title: "Locate {{ destination.display_name }} connection details"
        anchor: "locate-connection-details"
        content: |
          In this step, you'll retrieve the server address for the {{ destination.display_name }} you want to connect to Stitch. 
          
          This is the value you'll enter in the **Host** field in Stitch in the next step.

          {% include destinations/microsoft-azure/azure-connection-details.html %}

      - title: "Enter connection details into Stitch"
        anchor: "enter-connection-details-into-stitch"
        content: |
          {% include shared/database-connection-settings.html type="general" %}

      - title: "Define SSH connection details"
        anchor: "define-ssh-connection-details"
        content: |
          {% include shared/database-connection-settings.html type="ssh" %}

      - title: "Save the destination"
        anchor: "save-destination"
        content: |
          {% include shared/database-connection-settings.html type="finish-up" %}
---
{% include misc/data-files.html %}
{% assign destination = page %}