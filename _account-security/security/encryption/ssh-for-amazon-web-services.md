---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Setting up an SSH Tunnel for a database in Amazon Web Services
permalink: /security/data-encryption/setting-up-ssh-tunnel-for-amazon-web-services
redirect_from: /account-security/data-encryption/setting-up-ssh-tunnel-for-amazon-web-services
summary: "If a database is in private subnet in your Amazon Web Services account, you can use an SSH tunnel to connect Stitch. This tutorial will walk you through setting up an SSH server and configuring access for an Amazon RDS or Amazon Redshift connection to Stitch."

key: "ssh-setup-amazon-web-services"
type: "security"
content-type: "encryption"

input: false
layout: tutorial
weight: 3

use-tutorial-sidebar: false

hosting-type: "amazon"


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

  For **SSH for self-hosted databases**, refer to the [SSH for self-hosted databases guide]({{ link.security.ssh-generic | prepend: site.baseurl }}).

  For **SSH for Microsoft Azure databases**, refer to the [SSH for Microsoft Azure guide]({{ link.security.ssh-microsoft-azure | prepend: site.baseurl }}).


# -------------------------- #
#        Requirements        #
# -------------------------- #

requirements:
  - item: |
      **Privileges in AWS that allow you to**:

        - **Create/manage EC2 instances.** This is required to create the SSH server.
        - **Create/manage Security Groups**. This is required to whitelist Stitch's IP addresses.
        - **View database details**. This is required to retrieve the database's connection details.
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

  - title: "Verify the database's VPC"
    anchor: "verify-database-vpc"
    content: |
      Next, you'll log into AWS and verify the Virtual Private Cloud (VPC) the database is in. The SSH server you'll create in Step 2 must reside in the same VPC as the database.

      First, log into your AWS account. Then use the instructions below for the type of database you're connecting to locate the VPC.

      {% capture rds-menu %}
      1. Navigate to the RDS Dashboard in AWS. If you use the **Services** menu (top left corner), click the **RDS** option under the **Database** section.
      2. From the RDS Dashboard, click **Databases** in the menu on the left side of the page.
      3. On the page that displays, click the database you're connecting to Stitch. This will open the Instance Details page.
      {% endcapture %}

      {% capture rds-instructions %}
      {{ rds-menu }}
      4. Click the **Connectivity & security** tab if it's not already open.
      5. Locate the **VPC** field in the **Networking** section:

         ![The VPC field in the Instance Details page in AWS]({{ site.baseurl }}/images/shared/ssh/amazon-locate-vpc.png)
      {% endcapture %}

      {% include layout/expandable-heading.html content=rds-instructions anchor="rds-vpc-instructions" title="I'm connecting an RDS database." %}

      {% capture redshift-menu %}
      1. Navigate to the Redshift Dashboard in AWS. If you use the **Services** menu (top left corner), click the **Amazon Redshift** option under the **Database** section.
      2. From the Redshift Dashboard, click **Clusters** in the menu on the left side of the page.
      3. On the page that displays, click the Redshift cluster you're connecting to Stitch. This will open the Cluster Details page.
      {% endcapture %}

      {% capture redshift-instructions %}
      {{ redshift-menu }}
      4. In the **Cluster Properties** section, locate the **VPC ID** field:

         ![The VPC ID field in the Cluster Details page in AWS]({{ site.baseurl }}/images/shared/ssh/amazon-redshift-vpc-field.png)
      {% endcapture %}

      {% include layout/expandable-heading.html content=redshift-instructions anchor="redshift-vpc-instructions" title="I'm connecting a Redshift database." %}

      Keep the name of the VPC handy - you'll need it to complete the next step.

  - title: "Create an SSH server in your VPC"
    anchor: "create-ssh-server-in-vpc"
    content: |
      In this step, you’ll launch an EC2 instance to serve as the SSH server. This publicly accessible instance will act as an intermediary, forwarding the traffic from Stitch through an encrypted tunnel to the database in the private subnet.

      **Note**: This instance must reside in the same VPC as the database. Refer to [Step 1](#verify-database-vpc) if you aren't sure which VPC to use.

      {% for substep in step.substeps %}
      - [Step 2.{{ forloop.index }}: {{ substep.title }}](#{{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Configure the SSH server"
        anchor: "configure-ssh-server"
        content: |
          The first part of creating an SSH server in your VPC is configuring the instance.
          1. Navigate to the EC2 Management Console in AWS. If you use the **Services** menu (top left corner), click the **EC2** option under the **Compute** section.
          2. On the EC2 Dashboard, click the **Launch Instance** button.
          3. Next, you’ll be asked to select the Amazon Machine Image, or AMI, that will be used to launch the instance. For this tutorial, we'll be using a Linux-based AMI.

             Click the **Select** button next to the AMI you want to use.
          4. On the next page, you'll select the instance type. Generally, a small instance will work just fine. For example: `t2.small`. You can find more info about instance types on [Amazon's website](https://aws.amazon.com/ec2/instance-types/){:target="new"}.

             After you select the instance type, click the **Configure Instance Details** button in the lower right corner of the page to continue.
          5. On the Configure Instance Details page, fill in the following fields:
             - **Network**: Select the same VPC that the database is in. Refer to [Step 1](#verify-database-vpc) if you aren't sure which VPC to use.
             - **Subnet**: Select the public subnet you want to associate with the EC2 instance. **Note**: This must be a public subnet - that is, a subnet with an Internet Gateway - as this will automatically assign a public IP address to machines in the subnet.
             - **Auto-assign public IP**: Select **Enable** from the drop-down. This is required to ensure the machine has a public IP address.

               Here's a look at our setup:

               ![Configuring the EC2 instance details]({{ site.baseurl }}/images/shared/ssh/amazon-ec2-instance-details.png)
          6. Click the **Next: Add Storage** button in the lower right corner of the page to continue.
          7. If you're only using the machine as a bastion (which is what we're doing in this tutorial), adding storage and tags are unnecessary. Skip over these pages until you reach the **Configure Security Group** page.

      - title: "Configure the SSH server's Security Group"
        anchor: "ssh-server-security-group"
        content: |
          The second part of creating an SSH server in your VPC is configuring the security group. During this step, you'll add Stitch's IP addresses to the security group, which will allow traffic from Stitch to access the SSH server.

          You can create a new Security Group or update an existing one. For this tutorial, we'll create a new group.

          1. In the **Assign a security group** field, select **Create a new security group**.
          2. In the **Security group name** field, enter a unique name for the Security Group. For example: `Stitch Bastion`
          3. In the table below the **Description** field, you'll add Stitch's IP addresses to the security group:
             - **Type**: If the default SSH port for your server is 22, set this to **SSH**.

                If it’s something else, set this to **Custom TCP Rule**.
             - **Protocol**: This will default to **TCP** - leave it as-is.
             - **Port Range**: This is the number of the SSH port associated with the server. **If you selected SSH as the Type**, this will default to `22`.

                **If you selected Custom TCP Rule**, enter the number of the SSH port in this field.
             - **Source**: This should default to **Custom**. In the field next to the Source drop-down menu, paste one of the [Stitch regional IP addresses you retrieved in Step 1](#verify-stitch-account-region).

          4. Click the **Add Rule** button to add another rule.
          5. Repeat steps 3 and 4 until all of the [Stitch IP addresses for your region](#verify-stitch-account-region) have been added to the Security Group.

             For example: This is the Security Group with Stitch's North America region IP addresses:

             ![Configuring the EC2 Instance Security Group using Stitch's North America region IP addresses]({{ site.baseurl }}/images/shared/ssh/amazon-ec2-security-group.png)
          6. When finished, click the **Review and Launch** button in the lower right corner of the page.

      - title: "Review and launch the SSH server"
        anchor: "review-launch-ssh-server"
        content: |
          The last step is to review the settings for the SSH server and launch it.

          Review the instance's settings, paying particular attention to the fields highlighted in the image below:

          ![Reviewing the EC2 Instance Details]({{ site.baseurl }}/images/shared/ssh/amazon-ec2-instance-review.png)

          - The **Security Groups** section should list either a new Security Group for Stitch OR an existing group that contains group rules for Stitch's IP addresses. If it doesn't, [refer to Step 2.2](#ec2-instance-security-group) for instructions.
          - In the **Instance Details** section:
             - **Network**: This field should contain the ID of the same VPC that the database is in.
             - **Subnet**: This field should contain the ID of a public subnet.
             - **Assign Public IP**: This field should have a value of `Yes`.
             - **Assign IPv6 IP**: This field should contain the value `Enable`. This indicates that the **Auto-assign public IP** setting from [Step 2.1](#configure-ssh-server) was defined correctly.

          After you're reviewed the instance's settings, click the **Launch** button in the lower right corner to launch the instance.

          **Note**: It may take a few minutes for the instance creation process to complete. The status in the EC2 Dashboard page will change to `Available` when the instance is ready.

  - title: "Enable the SSH server to access the database"
    anchor: "enable-ssh-server-access"
    content: |
      After the EC2 instance has finished initializing, you can move onto configuring the access rules for database. In this section, you'll create a VPC Security Group that will forward traffic from the SSH server (EC2 instance) to the database in the private subnet.

      {% for substep in step.substeps %}
      - [Step 3.{{ forloop.index }}: {{ substep.title }}](#{{ substep.anchor }})
      {% endfor %}
    
    substeps:
      - title: "Retrieve the SSH server's connection details"
        anchor: "retrieve-ssh-connection-details"
        content: |
          In this step, you'll retrieve the SSH server's public DNS (IPv4) and private IP address. This info will be used to set up the VPC security group in the next step, and eventually complete the setup in Stitch.

          1. Navigate to the EC2 Management Console in AWS. If you use the **Services** menu (top left corner), click the **EC2** option under the **Compute** section.
          2. On the EC2 Dashboard, click the **Instances** option under **Instances** in the menu on the left side of the page.
          3. In this list of instances that displays, locate the SSH server (EC2 instance) you created in Step 2.
          4. Click the instance. This will display the instance's details in the **Description** tab.
          5. Locate the **Public DNS (IPv4)** and **Private IPs** fields in this tab:

             ![EC2 Description tab with highlighted Public DNS (IPv4) and Private IPs fields highlighted]({{ site.baseurl }}/images/shared/ssh/amazon-ec2-instance-ip-address-fields.png)

          6. Copy these values somewhere handy - you'll need them to complete the setup. **Make sure you know which value is which** - confusing these values will prevent a successful connection.

      - title: "Create a database Security Group and whitelist the SSH server"
        anchor: "create-database-vpc-security-group-whitelist-ssh"
        content: |
          In this step, you'll whitelist the SSH server's private IP address in a Security Group. This will allow traffic from the SSH server to access the database.

          You can create a new Security Group or update an existing one. For this tutorial, we’ll create a new group.

          1. In the menu on the left side of the page, click the **Security Groups** option under **Security**.
          2. On the page that displays, click the **Create Security Group** button. A window will display.
          3. Fill in the fields as follows:
             - **Security group name**: Enter a unique name for the Security Group.
             - **Description**: Enter a brief description of what the group is.
             - **VPC**: Verify that the **VPC containing the database and SSH server** is selected in the drop-down.
          4. In the **Security group rules** section, click the **Inbound** tab.
          5. Click the **Add Rule** button.
          6. Fill in the fields as follows:
             - **Type:** Select **Custom TCP Rule**.
             - **Protocol**: This should default to **TCP**.
             - **Port Range**: Enter the port used by the database you're connecting to Stitch. For example: For a PostgreSQL database, the port might be `5432`.
             - **Source**: Paste the SSH server's **Private IP** and add `/32` at the end. In CIDR notation, `/32` indicates a specific IP address. In this case, you're creating a rule specifically for the SSH server's private IP address. For example: `172.31.10.171/32`
          7. Review the settings. Here's what our Security Group looks like:

             ![The Create Security Group window in AWS]({{ site.baseurl }}/images/shared/ssh/amazon-database-security-group.png)
          8. Click **Create** to create the Security Group.

      - title: "Associate the Security Group with the database"
        anchor: "associate-security-group-with-database"
        content: |
          In this step, you'll associate the Security Group from the previous step with the database. This will allow the traffic from the SSH server to access the database.

          Use the instructions below for the type of database you’re connecting to associate the Security Group with the database.

          {% capture rds-sg-instructions %}
          {{ rds-menu }} 
          4. Click the **Modify** button near the top right corner of the page. This will open the **Modify DB Instance** page.
          5. Locate the **Network & Security** section.
          6. In the **Security group** dropdown, select the Security Group from the previous step:
             ![The Security Group dropdown in the Modify DB page, highlighted]({{ site.baseurl }}/images/shared/ssh/amazon-rds-associate-security-group.png)
          7. Scroll to the bottom of the page and click **Continue**.
          8. On the next page, you'll review the changes and schedule their application. Select the schedule you want in the **Scheduling of modifications** section.
          9. Click **Modify DB Instance** to apply the changes.
          {% endcapture %}

          {% include layout/expandable-heading.html content=rds-sg-instructions anchor="rds-security-group-instructions" title="I'm connecting an Aurora or RDS database." %}

          {% capture redshift-sg-instructions %}
          {{ redshift-menu }}
          4. Click the **Cluster** button, then **Modify Cluster**. This will open the Modify Cluster window.
          5. In the **VPC security groups** field, select the Security Group from the previous step:

             ![The VPC security groups field in the Modify Cluster window, highlighted]({{ site.baseurl }}/images/shared/ssh/amazon-redshift-modify-cluster.png)
          6. Click **Modify**.
          {% endcapture %}

          {% include layout/expandable-heading.html content=redshift-sg-instructions anchor="redshift-security-group-instructions" title="I'm connecting a Redshift database." %}

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
      {% include shared/ssh/ssh-connection-guide-links.html hosting-type="amazon" %}
---
{% include misc/data-files.html %}