---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/destination-templates/destination-setup/
## FOR INSTRUCTIONS & REFERENCE INFO

title: Connecting a Microsoft Azure SQL Data Warehouse to Stitch
permalink: /destinations/microsoft-azure/connecting-a-microsoft-azure-sql-data-warehouse-to-stitch
tags: [microsoft-azure_destination]
keywords: microsoft azure sql data warehouse, microsoft azure data warehouse, microsoft azure data warehouse, microsoft azure etl, etl to microsoft azure, microsoft azure destination
summary: "Connect a Microsoft Azure SQL data warehouse to your Stitch account."

content-type: "destination-setup"

toc: true
layout: destination-setup-guide

type: "microsoft-azure"
display_name: "Microsoft Azure"

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: |
      **An up-and-running {{ destination.display_name }} instance.** Instructions for creating a {{ destination.display_name }} data warehouse are outside the scope of this tutorial; our instructions assume that you have an instance up and running. For help getting started with {{ destination.display_name }}, refer to [Microsoft's documentation](https://docs.microsoft.com/en-us/azure/sql-data-warehouse/create-data-warehouse-portal){:target="new"}.
  - item: |
      **An existing Azure Storage account.** Instructions for creating an Azure Storage account are outside the scope of this tutorial. For help getting started with an Azure Storage account, refer to [Microsoft's documentation](https://docs.microsoft.com/en-us/azure/storage/){:target="new"}.

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "Configure server firewall access"
    anchor: "configure-server-firewall-access"
    content: |
      {% include destinations/microsoft-azure/azure-ip-whitelisting.html %}

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

  - title: "connect stitch"
    content: |
      To complete the setup, you need to enter your {{ destination.display_name }} connection details into the {{ app.page-names.dw-settings }} page in Stitch.

    substeps:
      - title: "Locate {{ destination.display_name }} connection details"
        anchor: "locate-connection-details"
        content: |
          In this step, you'll retrieve the server address for the {{ destination.display_name }} you want to connect to Stitch. 
          
          This is the value you'll enter in the **Host** field in Stitch in the next step.

          {% include destinations/microsoft-azure/azure-connection-details.html %}

# {% capture setup-notice %}
# This guide describes how to connect Azure SQL Data Warehouse to Stitch via a **direct connection**.

# Refer to the [Connecting an Azure SQL Data Warehouse via SSH Tunnel]({{ link.destinations.setup.redshift-ssh | prepend: site.baseurl }}) guide to connect using an SSH tunnel.
# {% endcapture %}

# {% include note.html first-line="**This tutorial is for Azure SQL Data Warehouse direct connections**" content=setup-notice %}
---
{% include misc/data-files.html %}
{% assign destination = site.destinations | where:"type","microsoft-azure" | first %}