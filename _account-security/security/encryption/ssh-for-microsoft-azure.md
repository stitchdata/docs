---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Setting up an SSH Tunnel for a database in Microsoft Azure
permalink: /security/data-encryption/setting-up-ssh-tunnel-for-microsoft-azure
redirect_from: /account-security/data-encryption/setting-up-ssh-tunnel-for-microsoft-azure
summary: "If a database is in private subnet in your Microsoft Azure account, you can use an SSH tunnel to connect Stitch. This tutorial will walk you through setting up an SSH server and configuring access for a Microsoft Azure SQL Server or Microsoft Azure Synapse Analytics connection to Stitch."

key: "ssh-setup-microsoft-azure"
type: "security"
content-type: "encryption"

input: false
layout: tutorial
use-tutorial-sidebar: false
weight: 3

hosting-type: "microsoft-azure"


# -------------------------- #
#       Introduction         #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}

  {% include shared/ssh/ssh-intro-requirements.html type="intro" %}

  ---

  ## Databases this guide applies to {#applicable-databases}

  This guide is applicable to the following integrations and destinations:

  {% include shared/ssh/ssh-intro-requirements.html type="applicable-databases" %}

  For **SSH for Amazon-hosted databases**, refer to the [SSH for Amazon guide]({{ link.security.ssh-amazon | prepend: site.baseurl }}).

  For **SSH for self-hosted databases**, refer to the [SSH for self-hosted databases guide]({{ link.security.ssh-generic | prepend: site.baseurl }}).


# -------------------------- #
#        Requirements        #
# -------------------------- #

requirements:
  - item: |
      **Privileges in Microsoft Azure that allow you to**:

         - **Create/manage virtual machines.** This is required to create the SSH server.
         - **Create/manage security groups.** This is required to enable access between Stitch, the SSH server, and the database.
  - item: |
      {% include shared/ssh/ssh-intro-requirements.html type="requirements" requirement-type="linux-familiarity" %}

  - item: |
      {% include shared/ssh/ssh-intro-requirements.html type="requirements" requirement-type="windows-ssh-client" %}
      

# -------------------------- #
#        Instructions        #
# -------------------------- #

steps:
  - title: "Verify your Stitch account's data pipeline region"
    anchor: "verify-stitch-account-region"
    content: |
      {% include shared/whitelisting-ips/locate-region-ip-addresses.html first-step=true %}

  - title: "Create and configure a virtual machine"
    anchor: "create-launch-virtual-machine"
    content: |
      Next, you'll create a virtual machine to serve as the SSH server. This publicly accessible instance will act as an intermediary, forwarding the traffic from Stitch through an encrypted tunnel to your private {{ destination.display_name }} instance.

      {% for substep in step.substeps %}
      - [Step 2.{{ forloop.index }}: {{ substep.title }}](#{{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Configure the virtual machine's basic settings"
        anchor: "configure-vm-basic-settings"
        content: |
          1. Log into your Microsoft Azure account.
          2. In the search bar at the top of the page, type `virtual machines`.
          3. Click the **Virtual machines** result.
          4. On the **Virtual machines** page, click the **+ Add** button.
          5. Fill in the fields in the **Basics** tab as needed.
          6. When finished, click the **Networking** tab.

      - title: "Configure the virtual machine's networking settings"
        anchor: "configure-virtual-machine-inbound-access"
        content: |
          Next, you'll create a network security group that will allow inbound traffic from Stitch's IP addresses.

          1. In the **Virtual network** field, select the virtual network you want to associate with the virtual machine.
          2. In the **Subnet** field, select the public subnet you want to associate with the virtual machine.
          3. In the **Public IP** field, verify that a value other than **None** is selected. This is required to allow Stitch to successfully connect to the virtual machine.
          4. For **NIC network security group**, select **Advanced**. This will display the **Configure network security group** field.
          5. Click the **Create new** link under the **Configure network security group** field. This will open the **Create network security group** panel.
          6. In the panel, click the **+ Add an inbound rule** link in the **Inbound rules** section. This will open the **Add inbound security rule** panel.
          7. Fill in the fields as follows. If a field isn't in this list, **use the default value**:

             - **Source**: Select **IP Addresses**.
             - **Source IP addresses/CIDR ranges**: Paste a comma-delimited list of the Stitch IP addresses **for your Stitch data pipeline region** that you retrieved in [Step 1](#verify-stitch-account-region).

               **Note**: You may also want to add your own IP address(es) to this list. This ensures that you'll also be able to connect to the database via the virtual machine as needed.

             - **Source port ranges**: Enter `22`.
             - **Protocol**: Select **TCP**.
             - **Action**: Select **Allow**.
             - **Name**: Enter a name. For example: `stitch-inbound`.

             Here's a look at our setup using Stitch's North America IP address list:

             ![The Add inbound security rule panel in Azure, highlighted]({{ site.baseurl }}/images/shared/ssh/azure-inbound-security-rule.png)
          6. When finished, click **Add** to create the inbound rule.

      - title: "Launch the virtual machine"
        anchor: "launch-the-virtual-machine"
        content: |
          1. After you've finished configuring the virtual machine's networking settings, click the **Review + create** tab.
          2. Review the settings for the virtual machine, verifying that the **Public IP** field is not **None**.
          3. Click **Create** to launch the virtual machine.

          After you click **Create**, Azure will launch the deployment process for the virtual machine. This may take a few minutes to complete.

  - title: "Enable the SSH server to access the database"
    anchor: "enable-ssh-server-access"
    content: |
      Next, you'll configure the database to allow traffic forwarded from the virtual machine to access the database server. This is accomplished by whitelisting the virtual machine's private IP address in the server's firewall settings.

      {% for substep in step.substeps %}
      - [Step 3.{{ forloop.index }}: {{ substep.title }}](#{{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Retrieve the SSH server's connection details"
        anchor: "retrieve-vm-connection-details"
        content: |
          In this step, you'll retrieve the SSH server's public and private IP addresses. The private IP address will be used in the next step, whereas the public IP address will be used to complete the setup in Stitch.

          1. In the sidenav, click **Virtual machines**.
          2. In the search bar at the top of the page, type `virtual machines`.
          3. Click the **Virtual machines** result.
          4. In the list of available virtual machines, click the one you created in [Step 2](#create-launch-virtual-machine). This will open the instance's details page.
          5. Locate the **Public IP address** and **Private IP address** fields, which are highlighted in the image below:

             ![The virtual machine details page with the Public and Private IP address fields highlighted]({{ site.baseurl }}/images/shared/ssh/azure-ssh-connection-details.png)

          Copy the IP addresses somewhere handy, making sure to note which is public and which is private. Confusing these values will lead to an unsuccessful connection in Stitch.

      - title: "Create a server firewall rule for the virtual machine"
        anchor: "create-server-firewall-rule-for-vm"
        content: |
          <div class="panel-group" id="accordion">
            <div class="panel panel-default">
              <div class="panel-heading">
                  <h4 class="panel-title">
                      <a class="noCrossRef accordion-toggle" data-toggle="collapse" data-parent="#accordion" href="#collapse-integration-setup-vm">I'm connecting an integration.</a>
                  </h4>
              </div>
              <div id="collapse-integration-setup-vm" class="panel-collapse collapse noCrossRef">
                  <div class="panel-body">
                  {% capture integration-copy %}
                  {% include shared/whitelisting-ips/{{ page.hosting-type }}.html connection-type="integration" type="ssh" %}
                  {% endcapture %}

                  {{ integration-copy | markdownify }}
                  </div>
              </div>
            </div>
            <div class="panel panel-default">
              <div class="panel-heading">
                  <h4 class="panel-title">
                      <a class="noCrossRef accordion-toggle" data-toggle="collapse" data-parent="#accordion" href="#collapse-destination-setup-vm">I'm connecting a destination.</a>
                  </h4>
              </div>
              <div id="collapse-destination-setup-vm" class="panel-collapse collapse noCrossRef">
                  <div class="panel-body">
                  {% capture integration-copy %}
                  {% include shared/whitelisting-ips/{{ page.hosting-type }}.html connection-type="destination" type="ssh" %}
                  {% endcapture %}

                  {{ integration-copy | markdownify }}
                  </div>
              </div>
            </div>
          </div>

  - title: "Retrieve your Public Key"
    anchor: "retrieve-your-public-key"
    content: |
      {% include shared/ssh/ssh-retrieve-public-key.html %}

  - title: "Create the Stitch SSH user"
    anchor: "create-stitch-ssh-user"
    content: |
      {% include shared/ssh/ssh-create-linux-user.html %}

  - title: "Complete the setup for Stitch"
    anchor: "complete-the-setup-for-stitch"
    content: |
      {% include shared/ssh/ssh-connection-guide-links.html %}
---
{% include misc/data-files.html %}