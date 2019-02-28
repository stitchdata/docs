---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Setting up an SSH Tunnel for a database connection
permalink: /common/databases/setting-up-ssh-tunnel-for-database-connection
summary: ""

input: false
layout: tutorial
use-tutorial-sidebar: false


# -------------------------- #
#       Introduction         #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}

  If your database isn't publicly accessible, you can use an SSH tunnel to connect to Stitch. The approach in this tutorial will use a publicly accessible instance to create the connection. The SSH server will act as an intermediary, forwarding the traffic from Stitch through an encrypted tunnel to the private database.

  The approach outlined in this guide is applicable to both [integrations]({{ site.baseurl }}/integrations) (where data is extracted) and [destinations]({{ site.baseurl }}/destinations) (where data is loaded).

  Additionally, note the following before you get started:

  - **Amazon Relational Database Services (RDS) and Redshift databases require different steps.** Refer to the [Setting up an SSH Tunnel for a database in Amazon Web Services]({{ link.connections.ssh-rds | prepend: site.baseurl }}) guide for these instructions.

  - **An SSH tunnel isn’t necessarily more secure than a direct connection**. An SSH tunnel is only as secure as the monitoring and hardening you perform on the SSH server hosting the tunnel.

  If you have questions or concerns about Stitch security, please refer to the [Security FAQ]({{ link.account.security-faq | prepend: site.baseurl }}).


# -------------------------- #
#        Requirements        #
# -------------------------- #

requirements:
  - item: |
      **An up and running, publicly accessible SSH server.** This tutorial will walk you through configuring the server to allow Stitch to access it, but creating the server is outside the scope of this guide. Loop in a member of your technical team for assistance.

         Additionally, the server should be accessible from the internet.

  - item: |
      **The public IP address of the SSH server.** This is the IP address that allowed traffic from the internet can use to access the server.


# -------------------------- #
#        Instructions        #
# -------------------------- #

steps:
  - title: "Configure the SSH server to allow Stitch access"
    anchor: "configure-ssh-server-stitch-access"
    content: |
      First, you'll configure the SSH server to allow traffic from Stitch to access the server. Whitelist the following IP addresses to allow access to the SSH server on the SSH port, which is typically `22`:

        {% for ip-address in ip-addresses %}
        - {{ ip-address.ip }}
        {% endfor %}

  - title: "Configure the database to allow SSH server traffic"
    anchor: "configure-database-allow-ssh-server-traffic"
    content: |
      Next, you'll configure the database to allow traffic from the SSH server.

      In your database's firewall, whitelist the SSH server's public IP address to allow it to access the database's port. For example: For PostgreSQL databases, the default port is `5432`.

  - title: "Retrieve your Public Key"
    anchor: "retrieve-your-public-key"
    content: |
      {% include shared/retrieve-public-key.html %}

  - title: "Create the Stitch SSH user"
    anchor: "create-stitch-ssh-user"
    content: |
      {% include shared/create-linux-user.html %}

  - title: "Complete the setup for Stitch"
    anchor: "complete-the-setup-for-stitch"
    content: |
      {% include shared/ssh-connection-guide-links.html ssh-type="generic" %}
---
{% include misc/data-files.html %}