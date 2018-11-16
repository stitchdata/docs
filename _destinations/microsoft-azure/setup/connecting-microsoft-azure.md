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
      **STORAGE ACCOUNT.** [ TODO- remains to be seen whether we want to use an existing one, or have them create a dedicated account for us]

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "Configure server firewall access"
    anchor: "configure-server-firewall-access"
    content: |
      For the connection from Stitch to be successful, you'll need to configure the firewall for your {{ destination.display_name }} instance to allow access from our IP addresses.

      1. Sign into your [{{ destination.display_name }}](https://azure.microsoft.com/en-us/account/){:target="new"} account.
      2. If you aren't automatically brought to your dashboard, navigate there.
      3. In the sidenav, click **SQL databases**.
      4. On the page that displays, click the name of the database you want to connect to Stitch.
      5. The details page for the database will display. Click the link in the **Server name** field.
      6. The details page for the server will display. Click the **Show firewall settings** link in the **Firewalls and virutal networks** field.
      7. For each of Stitch's IP addresses listed below, create a rule:
         - **Rule name**: Enter a name for the rule. For example: `Stitch 1`
         - **Start IP**: Paste one of Stitch's IP addresses.
         - **End IP**: Paste the same IP address.

         Stitch's IP addresses are:

         {% for ip-address in ip-addresses %}
          - {{ ip-address.ip | remove: "/32" }}
          {% endfor %}
      8. Click the three dots to the right of the **End IP** field to add the rule.
      9. Repeat steps 7 and 8 until there is a rule for each IP address. The screen should look similar to the following when you're finished:

         ![IP address rules for Stitch's IP addresses in Microsoft Azure firewall settings]({{ site.baseurl }}/images/destinations/microsoft-azure-ip-addresses.png)

      10. Click **Save**.

  - title: "Generate storage credentials"
    anchor: "generate-storage-credentials"
    content: |
      Next, you'll generate the storage credentials required to access Azure Storage.

    substeps:
      - title: "Generate a shared access signature URL"
        anchor: "generate-shared-access-signature-url"
        content: |
          1. In the sidenav, click **Storage accounts**.
          2. On the page that displays, click the name of the storage account you want to use.
          3. The middle panel contains the Storage account menu. In the **Settings** section, click **Shared access signature**.
          4. Leave the boxes for the **Allowed services**, **Allowed resource types**, and **Allowed permissions** checked. Because Microsoft doesn't currently allow users to individually grant permissions on services and resources, Stitch currently requires the default configuration, which includes all permissions. Refer to [Microsoft's documentation](https://docs.microsoft.com/en-us/rest/api/storageservices/Constructing-an-Account-SAS){:target="new"} for more info.

             **Note**: Despite the permissions granted here, Stitch will never delete data.
          5. Next, you'll define the access period using the **Start** and **End** fields in the **Start and expiry date/time** section:

             ![Start and end dates for Shared Access Signature generation in Microsoft Azure settings]({{ site.baseurl }}/images/destinations/microsoft-azure-sas-time-period.png)

             To reduce the likelihood of replication interruption, we recommend setting the expiration date well into the future.
          6. **IP ADDRESSES** - [TODO] - Right now this field only accepts a single IP address or a range.
          7. In the **Allowed protocols** section, select **HTTPS only**.
          8. For the **Signing key**, select the name of the key you want to use. **Note**: Stitch doesn't require the use of a specific key.
          9. When finished, click the **Generate SAS and connection string** button.

          10. A handful of fields will appear below the button. Locate the **Blob service SAS URL** field:

              ![The Blob Service SAS URL field, highlighted]({{ site.baseurl }}/images/destinations/microsoft-azure-blob-service-sas-url.png)

          11. Copy the URL to somewhere handy - you'll need it to complete the setup.

      - title: "Retrieve your storage access key"
        anchor: "retrieve-storage-access-key"
        content: |
          {% include note.html type="single-line" content="**Rotating keys**: If you rotate your storage access keys, you'll also need to update the Destination Settings in Stitch or you'll encounter connection issues." %}

          1. In the middle panel menu, click **Access keys** in the **Settings** section.
          2. On the page that displays, locate the section for the **Signing key** you selected in the previous section. For example: If you selected `key1` as the signing key, locate the section for **key 1**.
          3. Copy the value in the corresponding **Key** field to somewhere handy - you'll need it to complete the setup.

             The **Key** fields are highlighted for both keys in the image below. Remember that you'll only need the **Key** field value for the signing key you selected:

             ![Highlighted Key fields for the Storage Access Keys in Microsoft Azure]({{ site.baseurl }}/images/destinations/microsoft-azure-storage-keys.png)

  - title: "Create a {{ destination.display_name }} Stitch user"
    anchor: "create-stitch-user"
    content: |
      [ADD CONTENT HERE]

  - title: "connect stitch"
---
{% include misc/data-files.html %}
{% assign destination = site.destinations | where:"type","microsoft-azure" | first %}