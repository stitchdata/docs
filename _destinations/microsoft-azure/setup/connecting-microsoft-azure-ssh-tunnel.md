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

title: Connecting a Microsoft Azure SQL Data Warehouse Destination to Stitch via SSH tunnel
permalink: /destinations/microsoft-azure-sql-data-warehouse/connecting-microsoft-azure-sql-data-warehouse-to-stitch-ssh-tunnel
keywords: microsoft azure sql data warehouse, microsoft azure data warehouse, microsoft azure data warehouse, microsoft azure etl, etl to microsoft azure, microsoft azure destination
summary: "Connect a Microsoft Azure SQL data warehouse to your Stitch account via an SSH tunnel."

content-type: "destination-setup"

toc: true
layout: tutorial
use-tutorial-sidebar: false

type: "microsoft-azure"
display_name: "Microsoft Azure"

ssh: true


# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |
  {% capture setup-notice %}
  Stitch's {{ destination.display_name }} destination only works with Microsoft's [Azure SQL Data Warehouse product](https://azure.microsoft.com/en-us/services/sql-data-warehouse/){:target="new"}.

  Stitch doesn't currently support using Azure SQL Server or Azure SQL Database as a destination. Attempting to connect these products to Stitch via the {{ destination.display_name }} destination in Stitch will result in errors.
  {% endcapture %}

  {% include note.html first-line="**Stitch only supports connecting to Azure SQL Data Warehouse instances**" content=setup-notice %}

  This guide describes how to connect a {{ destination.display_name }} destination to Stitch using an SSH tunnel.

  If your {{ destination.display_name }} instance is private, you can create a virtual machine to serve as an SSH bastion. This publicly accessible instance will act as an intermediary, forwarding the traffic from Stitch through an encrypted tunnel to your private {{ destination.display_name }} instance.


# -------------------------- #
#        Requirements        #
# -------------------------- #

requirements:
  - item: |
      **Some familiarity with Linux and the command line.** In this tutorial, you'll create a Linux user for Stitch to ensure access via SSH. While we've provided the commands you'll need to create the user, you should know how to access a server using the command line and feel comfortable running commands.
  - item: |
      **An up-and-running {{ destination.display_name }} instance.** Instructions for creating a {{ destination.display_name }} data warehouse are outside the scope of this tutorial; our instructions assume that you have an instance up and running. For help getting started with {{ destination.display_name }}, refer to [Microsoft's documentation](https://docs.microsoft.com/en-us/azure/sql-data-warehouse/create-data-warehouse-portal){:target="new"}.
  - item: |
      **An existing Azure Storage account.** Instructions for creating an Azure Storage account are outside the scope of this tutorial. For help getting started with an Azure Storage account, refer to [Microsoft's documentation](https://docs.microsoft.com/en-us/azure/storage/){:target="new"}.

# -------------------------- #
#         Instructions       #
# -------------------------- #

steps:
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

  - title: "Create and configure a virtual machine"
    anchor: "create-launch-virtual-machine"
    content: |
      Next, you'll create a virtual machine to serve as the SSH bastion. This publicly accessible instance will act as an intermediary, forwarding the traffic from Stitch through an encrypted tunnel to your private {{ destination.display_name }} instance.

    substeps:
      - title: "Launch the virtual machine"
        anchor: "launch-virtual-machine"
        content: |
          1. In the sidenav, click **Virtual machines**.
          2. On the **Virtual machines** page, click the **+ Add** button.
          3. Fill in the fields in the tabs. In the list below are the fields that require specific values for Stitch:
             - **Basics tab**:
                - **Public inbound ports**: Select **Allow selected ports**.
                - **Select inbound ports**: Select **SSH (22)**.
          4. After you've finished filling in the required fields, click **Review + create**.
          5. Click **Create** to create the virutal machine.

          After you click **Create**, Azure will launch the deployment process for the virtual machine. This may take a few minutes to complete.

      - title: "Configure the virtual machine's inbound access"
        anchor: "configure-virtual-machine-inbound-access"
        content: |
          {% capture ip-list %}
          {% for ip-address in ip-addresses %}{{ ip-address.ip }}{% unless forloop.last == true %},{% endunless %}{% endfor %}
          {% endcapture %}

          After Azure finishes deploying the virtual machine, you can move onto configuring the access rules for its security group. Inbound access rules will allow traffic from Stitch's IP addresses to access the virtual machine.

          1. In the sidenav, click **Virtual machines**.
          2. On the **Virtual machines** page, click virtual machine you created in the previous step.
          3. The details page for the virtual machine will display. In the middle menu, click **Networking**.
          4. In the **Inbound Port Rules** section, click the **Add inbound port rule** button.
          5. In the **Add inbound security rule** tab that displays, fill in the fields as follows. If a field isn't in this list, **use the default value**:
             - **Source**: Select **IP Addresses**.
             - **Source IP addresses/CIDR ranges**: Paste this comma-delimited list of Stitch's IP addresses:

                 ```markdown
                 {{ ip-list | strip_newlines }}
                 ```
             - **Protocol**: Select **TCP**.
             - **Action**: Select **Allow**.
             - **Name**: Enter `stitch`.
          6. When finished, click **Add** to create the inbound rule.

  - title: "Enable the virtual machine to access the {{ destination.display_name }} instance"
    anchor: "enable-virtual-machine-access-to-azure"
    content: |
      Next, you'll configure the {{ destination.display_name }} database to allow traffic forwarded from the virtual machine to access the server. This is accomplished by whitelisting the virtual machine's public IP address in the server's firewall settings.

    substeps:
      - title: "Retrieve the virtual server's public IP address"
        anchor: "retrieve-vm-public-ip-address"
        content: |
          You should still be on the **Networking** page for the virtual machine - if not, navigate there before proceeding.

          Locate the **Public IP** field, highlighted in the image below:

          ![Virtual machine public IP address field]({{ site.baseurl }}/images/destinations/azure-sql-dw-vm-public-ip-address.png)

          Keep this handy - you'll need it in the next step and to complete the setup in Stitch.

      - title: "Create a server firewall rule for the virtual machine"
        anchor: "create-server-firewall-rule-for-vm"
        content: |
          {% include destinations/microsoft-azure/azure-ip-whitelisting.html type="ssh" %}

  - title: "Create a Stitch Linux user on the virtual machine"
    anchor: "create-stitch-linux-user"
    content: |
      Next, you'll retrieve your Public Key and create a Linux user on the virtual machine for Stitch. This will create an authenticated user for Stitch, ensuring access to the virtual machine.
    substeps:
      - title: "Retrieve your Public Key"
        anchor: "retrieve-your-public-key"
        content: |
          {% include shared/retrieve-public-key.html %}

      - title: "Create the Stitch Linux user"
        anchor: "create-stitch-linux-user"
        content: |
          In this step, you'll create the Linux user for Stitch. You'll need to sign into the virtual machine as the root user before proceeding.

          {% include shared/create-linux-user.html no-notification=true %}

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
          {% include destinations/setup/destination-settings.html %}
---
{% include misc/data-files.html %}
{% assign destination = site.destinations | where:"type","microsoft-azure" | first %}