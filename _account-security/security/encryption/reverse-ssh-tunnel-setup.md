---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Setting up a Reverse SSH Tunnel
permalink: /account-security/data-encryption/setting-up-reverse-ssh-tunnel
summary: "If a database is privately accessible, you can use a reverse SSH tunnel to connect Stitch. This tutorial will walk you through requesting and configuring a reverse SSH tunnel for use with Stitch."

input: false
layout: tutorial
use-tutorial-sidebar: false

enterprise: true
enterprise-cta:
  feature: "Reverse SSH tunnels "
  title: "{{ site.data.strings.enterprise.title.are-an | prepend: page.enterprise-cta.feature }}"


# -------------------------- #
#       Introduction         #
# -------------------------- #

intro: |
  {% include misc/data-files.html %}

  Unlike other connection methods, reverse SSH enables Stitch to establish a connection to a database in your private network without opening holes in your network's firewall. A reverse SSH tunnel is an outbound connection from a machine on your network that connects securely over the internet to Stitch.
  

# -------------------------- #
#        Requirements        #
# -------------------------- #

requirements:
  - item: |
      **A Stitch Enterprise plan.** Reverse SSH tunnels are available only on a Stitch Enterprise plan. Reach out to [Stitch Sales]({{ site.sales }}) for more info.
  - item: |
      **Some familiarity with Linux and the command line.** While we’ve provided the commands you’ll need to establish the reverse SSH tunnel, you should know how to access a server using the command line and feel comfortable running commands.

# -------------------------- #
#        Instructions        #
# -------------------------- #

steps:
  - title: "Contact Stitch with your SSH public key"
    anchor: "contact-stitch-ssh-public-key"
    content: |
      To set up a reverse SSH tunnel, you'll need to provide Stitch with the following:

      - The public key corresponding to the SSH keypair you plan to use to establish the tunnel
      - The IP address(es) that you'll connect to the Stitch SSH server from

      Once our team receives this information, we'll set up a secure SSH server for you to connect to. We'll provide you with the `SSH_HOST`, `SSH_USER`, and `TUNNEL_PORT` info needed to establish the SSH connection.

  - title: "Establish the reverse SSH tunnel"
    anchor: "establish-reverse-ssh-tunnel"
    content: |
      After you receive the SSH connection information from us, run the following command to establish the tunnel, replacing the items in brackets:

      {% capture code %}autossh -M 0 -f -N -R <TUNNEL_PORT>:<DATABASE_HOST_OR_IP>:<DATABASE_PORT> -i <SSH_PRIVATE_KEY> <SSH_USER>@<SSH_HOST> -o ServerAliveInterval=10 -o ServerAliveCountMax=1 -o ExitOnForwardFailure=yes 
      {% endcapture %}
      {% include layout/code-snippet.html language="shell" code=code %}

      The `<DATABASE_HOST_OR_IP>` and `<DATABASE_PORT>` values are the host/endpoint and port of the database you're connecting from, respectively. For `<TUNNEL_PORT>`, `<SSH_USER>`, and `<SSH_HOST>`, use the SSH connection values you received from our team.

      For example: Here's the same command, but with all the values inserted:

      {% capture code %}autossh -M 0 -f -N -R 10000:database.private.yourcompany.com:5432 -i id_rsa.pem yourcompany@33.44.55.66 -o ServerAliveInterval=10 -o ServerAliveCountMax=1 -o ExitOnForwardFailure=yes 
      {% endcapture %}
      {% include layout/code-snippet.html language="shell" code=code %}
---