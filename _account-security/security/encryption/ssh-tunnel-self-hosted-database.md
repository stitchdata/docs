---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Setting up an SSH Tunnel for a self-hosted database
permalink: /security/data-encryption/setting-up-ssh-tunnel-for-database-connection
redirect_from: /account-security/data-encryption/setting-up-ssh-tunnel-for-database-connection
summary: "If a database is privately accessible, you can use an SSH tunnel to connect Stitch. This tutorial will walk you through setting up an SSH server and configuring access for a self-hosted database connection to Stitch."

key: "ssh-setup-self-hosted"
type: "security"
content-type: "encryption"

input: false
layout: tutorial
use-tutorial-sidebar: false
weight: 3

hosting-type: "generic"


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

  For **SSH for Microsoft Azure databases**, refer to the [SSH for Microsoft Azure guide]({{ link.security.ssh-microsoft-azure | prepend: site.baseurl }}).


# -------------------------- #
#        Requirements        #
# -------------------------- #

requirements:
  - item: |
      **An up and running, publicly accessible SSH server.** This tutorial will walk you through configuring the server to allow Stitch to access it, but creating the server is outside the scope of this guide. Loop in a member of your technical team for assistance.

         Additionally, the server should be accessible from the internet.

  - item: |
      **The public IP address of the SSH server.** This is the IP address that allowed traffic from the internet can use to access the server.

  - item: |
      {% include shared/ssh/ssh-intro-requirements.html type="requirements" requirement-type="linux-familiarity" %}

  - item: |
      {% include shared/ssh/ssh-intro-requirements.html type="requirements" requirement-type="windows-ssh-client" %}


# -------------------------- #
#        Instructions        #
# -------------------------- #

steps:
  - title: "Configure the SSH server to allow Stitch access"
    anchor: "configure-ssh-server-stitch-access"
    content: |
      First, you'll configure the SSH server to allow traffic from Stitch to access the server. You'll need to whitelist Stitch's IP addresses on the SSH server's SSH port (typically `22`) to grant access.

      {% include shared/whitelisting-ips/locate-region-ip-addresses.html %}
      3. Whitelist the appropriate IP addresses.

  - title: "Configure the database to allow SSH server traffic"
    anchor: "configure-database-allow-ssh-server-traffic"
    content: |
      Next, you'll configure the database to allow traffic from the SSH server.

      In your database's firewall, whitelist the SSH server's private IP address to allow it to access the database's port. For example: For PostgreSQL databases, the default port is `5432`.

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
{% include misc/data-files.html %}