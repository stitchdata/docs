---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Setting up an SSH Tunnel for a database in Microsoft Azure
permalink: /common/ssh/setting-up-ssh-tunnel-for-microsoft-azure
summary: "If a database is in private subnet in your Microsoft Azure account, you can use an SSH tunnel to connect Stitch. This tutorial will walk you through setting up an SSH server and configuring access for a Microsoft Azure SQL Server or Microsoft Azure SQL Data Warehouse connection to Stitch."

input: false
layout: tutorial
use-tutorial-sidebar: false

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

  For **SSH for Amazon-hosted databases**, refer to the [SSH for Amazon guide]({{ link.connections.ssh-amazon | prepend: site.baseurl }}).

  For **SSH for self-hosted databases**, refer to the [SSH for self-hosted databases guide]({{ link.connections.ssh-generic | prepend: site.baseurl }}).


# -------------------------- #
#        Requirements        #
# -------------------------- #

requirements:
  - item: |
      {% include shared/ssh/ssh-intro-requirements.html type="requirements" requirement-type="linux-familiarity" %}

  - item: |
      {% include shared/ssh/ssh-intro-requirements.html type="requirements" requirement-type="windows-ssh-client" %}
      

# -------------------------- #
#        Instructions        #
# -------------------------- #

steps:
  - title: "Create and configure a virtual machine"
    anchor: "create-launch-virtual-machine"
    content: |
      Next, you'll create a virtual machine to serve as the SSH server. This publicly accessible instance will act as an intermediary, forwarding the traffic from Stitch through an encrypted tunnel to your private {{ destination.display_name }} instance.

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
               {{ ip-list | strip }}
               ```
             - **Protocol**: Select **TCP**.
             - **Action**: Select **Allow**.
             - **Name**: Enter `stitch`.
          6. When finished, click **Add** to create the inbound rule.

  - title: "Enable the SSH server to access the database"
    anchor: "enable-ssh-server-access"
    content: |
      Next, you'll configure the {{ destination.display_name }} database to allow traffic forwarded from the virtual machine to access the database server. This is accomplished by whitelisting the virtual machine's public IP address in the server's firewall settings.

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
          {% include shared/whitelisting-ips/{{ page.hosting-type }}.html type="ssh" %}

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
      {% include shared/ssh/ssh-connection-guide-links.html hosting-type="generic" %}
---