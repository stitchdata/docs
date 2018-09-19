---
title: Connecting an Amazon Redshift Data Warehouse to Stitch via SSH Tunnel
permalink: /destinations/redshift/connecting-redshift-data-warehouse-to-stitch-ssh-tunnel
tags: [redshift_destination]
keywords: redshift, amazon redshift, redshift data warehouse, etl to redshift, redshift etl, create redshift user, stitch redshift user, stitch user, redshift ssh, redshift ssh tunnel

summary: "If your Redshift cluster is in a private subnet, you can use an SSH tunnel to connect Stitch to your data warehouse."
toc: true
layout: destination-setup-guide

display_name: "Redshift"
type: "redshift"
ssh: true

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: |
      **An Amazon Web Services (AWS) account.** Signing up is free - [click here](https://aws.amazon.com){:target="new"} or go to `https://aws.amazon.com` to create an account if you don't have one already.
  - item: "**Some technical know-how and familiarity with AWS.**"
  - item: |
      **Optional: Create a non-default VPC**. {% include destinations/redshift/create-a-vpc.html %}

requirements-info: |
  Additionally, note the following before you get started:

  - This tutorial assumes you’ll be using a **Linux-based** server to launch your instance and create the SSH tunnel.

  - **An SSH tunnel isn’t necessarily more secure than a direct connection**. An SSH tunnel is only as secure as the monitoring and hardening you perform on the SSH server hosting the tunnel.

  If you have questions or concerns about Stitch security, please refer to the [Security FAQ]({{ link.account.security-faq | prepend: site.baseurl }}).

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "Create cluster login credentials"
    anchor: "create-cluster-login-credentials"
    content: |
      {% include destinations/redshift/create-cluster-login-credentials.html %}

  - title: "Select nodes and cluster types"
    anchor: "select-nodes--cluster-types"
    content: |
      {% include destinations/redshift/select-nodes-cluster-types.html %} 

  - title: "Configure and launch the {{ destination.display_name }} cluster"
    anchor: "configure-launch-cluster"
    content: |
      Next, you'll define the additional configuration settings for the Redshift cluster. For our purposes, we're going to leave most of the settings as-is and focus on the **Configure Networking Options** and **Security Groups** sections.
    substeps:
      - title: "Configure networking options"
        anchor: "configure-cluster-networking-options"
        content: |
          {% include destinations/redshift/configure-cluster--networking-options.html %}

      - title: "Define a Security Group"
        anchor: "define-cluster-security-group"
        content: |
          {% include destinations/redshift/configure-cluster--define-security-group.html %}

      - title: "Review and launch the Redshift cluster"
        anchor: "review-launch-cluster"
        content: |
          {% include destinations/redshift/configure-cluster--review-launch.html %}

  - title: "Create a bastion in your VPC"
    anchor: "create-bastion-in-vpc"
    content: |
      Next, you’ll launch an EC2 instance to serve as the SSH bastion. This publicly accessible instance will act as an intermediary, forwarding the traffic from Stitch through an encrypted tunnel to your private Redshift cluster.

      **Note**: This instance must reside in the same VPC as the Redshift cluster.
    substeps:

      - title: "Configure the EC2 instance"
        anchor: "configure-ec2-instance"
        content: |
          The first part of creating a bastion in your VPC is configuring the instance.

          1. Navigate to the VPC Management Console in AWS. If you use the **Services** menu (top left corner), click the **VPC** option under the **Networking & Content Delivery** section.
          2. On the VPC Dashboard, click the **Launch EC2 Instances** button.
          3. Next, you’ll be asked to select the Amazon Machine Image, or AMI, that will be used to launch the instance.

             We’ll be using a Linux-based AMI (like Ubuntu) for this tutorial:

             ![Ubuntu Amazon Machine Image option in AWS]({{ site.baseurl }}/images/destinations/redshift-ssh-ubuntu-ami.png)

             Click the **Select** button next to the AMI you want to use.
          4. On the next page, you'll select the instance type. Generally, a small instance will work just fine as a bastion. For example: `t2.medium`. You can find more info about instance types on [Amazon's website](https://aws.amazon.com/ec2/instance-types/).

             After you select the instance type, click the **Configure Instance Details** button in the lower right corner of the page to continue.
          5. On the Configure Instance Details page, fill in the following fields:
             - **Network** - Select the same VPC that you launched your Redshift cluster in. This was what you selected for the **Choose a VPC** field in [Step 3](#configure-cluster-networking-options).
             - **Subnet** - Select the subnet you want to associate with the EC2 instance. We recommend using a **public** subnet - that is, a subnet with an Internet Gateway - as this will automatically assign a public IP address to machines in the subnet.

               If you’re not sure what subnet to use, simply leave this as the default.
             - **Auto-assign public IP** - Select **Enable** from the drop-down. This should be enabled to ensure your machine has a public IP address.

             Here's a look at our setup:

             ![Configuring the EC2 Instance Details]({{ site.baseurl }}/images/destinations/redshift-ssh-instance-details.png)
          6. Click the **Next: Add Storage** button in the lower right corner of the page to continue.
          7. If you're only using the machine as a bastion (which is what we're doing in this tutorial), adding storage and tags are unnecessary. Skip over these pages until you reach the **Configure Security Group** page.

      - title: "Configure the EC2 instance's Security Group"
        anchor: "ec2-instance-security-group"
        content: |
          The second part of creating a bastion in your VPC is configuring the security group. During this step, you'll add the IP addresses that are allowed to access the bastion to the security group.

          You can create a **new** Security Group or update an existing one. For this tutorial, we'll create a new group.

          1. Select the **Create a new security group** option.
          2. In the **Security group name** field, enter `Stitch Bastion` or a unique name for the Security Group.
          3. In the table below the **Description** field, you'll add Stitch's IP addresses to the security group:
             - **Type**: If the default SSH port for your server is 22, set this to **SSH**.

                If it’s something else, set this to **Custom TCP Rule**.
             - **Protocol**: This will default to **TCP** - leave it as-is.
             - **Port Range**: This is the number of the SSH port associated with the bastion. **If you selected SSH as the Type**, this will default to `22`.

                **If you selected Custom TCP Rule**, enter the number of the SSH port in this field.
             - **Source**: This should default to **Custom**. In the field next to the Source drop-down menu, paste one of the following IP addresses:

                {% for ip-address in ip-addresses %}
                - {{ ip-address.ip }}
                {% endfor %}

          4. Click the **Add Rule** button to add another rule.
          5. Repeat steps 3 and 4 until all of Stitch's IP addresses have been added to the Security Group.

             Here's what the Security Group rules should look like:

             ![Configuring the EC2 Instance Security Group]({{ site.baseurl }}/images/destinations/redshift-ssh-ec2-security-group.png)
          6. When finished, click the **Review and Launch** button in the lower right corner of the page.

      - title: "Review and launch the EC2 instance"
        anchor: "review-launch-ec2-instance"
        content: |
          The last step is to review the settings for the EC2 instance and launch it.

          Review the instance's settings, paying particular attention to the fields highlighted in the image below:

          ![Reviewing the EC2 Instance Details]({{ site.baseurl }}/images/destinations/redshift-ssh-ec2-review.png)

          - The **Security Groups** section should list either a new Security Group for Stitch OR an existing group that contains group rules for Stitch's IP addresses. If it doesn't, [refer to the Configure the EC2 Instance's Security Group](#ec2-instance-security-group) for instructions.
          - In the **Instance Details** section:
             - **Network**: This field should contain the ID of the same VPC that you launched the Redshift cluster in [Step 3 of this tutorial](#step-3-configure--launch-the-cluster).
             - **Assign Public IP & Assign IPv6 IP:** We strongly recommend using a [public subnet with the instance](#configure-ec2-instance) and auto-assigning a public IP address. This will ensure that Stitch can access the instance.

          After you're reviewed the instance's settings, click the **Launch** button in the lower right corner to launch the instance.

          Note that it may take a few minutes for the instance creation process to complete. The status in the VPC Dashboard page will change to 'available' when the instance is ready.

  - title: "Enable the bastion to access the Redshift cluster"
    anchor: "enable-bastion-access"
    content: |
      After the EC2 instance has finished initializing, you can move onto configuring the access rules for Redshift cluster. In this section, you'll create a VPC Security Group that will forward traffic from the bastion (EC2 instance) to your private Redshift cluster.
    substeps:

      - title: "Retrieve the VPC's IPv4 CIDR"
        anchor: "retrieve-vpc-ip"
        content: |
          In this step, you'll retrieve the bastion's IP address, or IPv4 CIDR. This value will be followed by a slash and a number between 0 and 32. For example: `10.0.0.0/16`

          1. Navigate to the VPC Management Console in AWS. If you use the **Services** menu (top left corner), click the **VPC** option under the **Networking & Content Delivery** section.
          2. On the VPC Dashboard, click the **Your VPCs** option under **Virtual Private Cloud** in the menu on the left side of the page.
          3. A list of all the VPCs you have access to in your AWS account will display. Locate the one you launched your Redshift cluster and the bastion in.
          4. Locate the **IPv4 CIDR** column.

             If this column isn't in the table, simply **click on the VPC** to open its details in the bottom section of the page:

             ![VPC details & IPv4 CIDR]({{ site.baseurl }}/images/destinations/redshift-ssh-vpc-ipv4-cidr.png)
          5. Copy and paste the VPC's IPv4 CIDR value somewhere convenient - you'll need it in the next step.

      - title: "Create a VPC Security Group"
        anchor: "create-vpc-security-group"
        content: |
          Now that you've retrieved the bastion's IP address, you can create a security group that will allow traffic from the bastion to access the Redshift cluster.

          1. From the VPC page, click the **Security Groups** option under **Security** in the menu on the left side of the page.
          2. Click the **Create Security Group** button.
          3. In the Create Security Group window:
             - **Name tag**: Enter a name tag if you want; otherwise, leave blank.
             - **Group name**: Enter `Stitch`, or a unique name for the Security Group.
             - **Description**: Enter a brief description of what the group is.
             - **VPC**: Verify that the **VPC where you launched the Redshift cluster and bastion** is selected in the drop-down.
          4. Click **Yes, Create**.
          5. After the Security Group is created, locate it in the list of Security Groups.
          6. Click on the Security Group.
          7. In the bottom section of the page - where the Security Group's details are displayed - click the **Inbound Rules** tab.
          8. Click the **Edit** button to create an Inbound rule for the Security Group:
             - **Type:** Select **Custom TCP Rule**.
             - **Protocol**: This should default to **TCP** - leave it as-is.
             - **Port Range**: Enter the port used by the Redshift instance. Our instance is using the Redshift default ({{ destination.port }}).
             - **Source**: Enter the bastion's **VPC IPv4 CIDR**. Ex: `10.0.0.0/16`

             Here's what the Inbound rule should look like:

             ![VPC inbound Security Group rule]({{ site.baseurl }}/images/destinations/redshift-ssh-vpc-security-group-rule.png)
          9. When finished, click **Save** to create the rule.

  - title: "Create a Stitch Linux user"
    anchor: "create-stitch-linux-user"
    content: |
      Next, you'll retrieve your Public Key and create a Linux user on your server for Stitch.
    substeps:

      - title: "Retrieve your Public Key"
        anchor: "retrieve-your-public-key"
        content: |
          {% include shared/retrieve-public-key.html %}

      - title: "Create the Stitch Linux user"
        anchor: "create-stitch-linux-user"
        content: |
          {% include shared/create-linux-user.html %}

  - title: "create db user"
    content: |
      {% include destinations/setup/postgresql-create-user-intro.html %}

      {% include destinations/setup/redshift-postgres-permissions.html %}

      ### Create the database user {#create-the-user}

      {% include destinations/setup/redshift-postgres-database-users.html %}

  - title: "connect stitch"
    content: |
      To complete the setup, you need to enter your {{ destination.display_name }} connection details into the {{ app.page-names.dw-settings }} page in Stitch.

    substeps:
      - title: "Locate the {{ destination.display_name }} connection details"
        anchor: "locate-connection-details-aws"
        content: |
          {% include shared/aws-connection-details.html %}
---
{% include misc/data-files.html %}
{% assign destination = site.destinations | where:"type",page.type | first %}

{% capture setup-notice %}
This tutorial describes how to spin up a Redshift cluster and connect it to Stitch via an **SSH tunnel**.

Looking for help setting up a **direct connection?** Refer to the [Connecting a Redshift Data Warehouse]({{ link.destinations.setup.redshift | prepend: site.baseurl }}) guide.
{% endcapture %}

{% include note.html first-line="**This tutorial is for Redshift SSH tunnel setup**" content=setup-notice %}

[In this tutorial]({{ link.destinations.setup.redshift | prepend: site.baseurl }}), we covered how to spin up a Redshift cluster with a public IP address to use with Stitch. If your Redshift cluster is in a private subnet, however, you can use an SSH tunnel to connect Stitch to your data warehouse.

The method you’ll use to accomplish this involves launching an EC2 instance into the VPC associated with the cluster. This EC2 instance will have a public IP address and act as a bastion, allowing you to forward traffic through an encrypted tunnel to your private Redshift cluster.