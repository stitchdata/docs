---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Setting up an SSH Tunnel for a database connection
permalink: /common/ssh
summary: "If a database you want to connect to Stitch isn't publicly accessible, you can use an SSH tunnel. Use this guide to find the correct instructions for your database type."

input: false
layout: general
feedback: false

# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |
  If a database you want to connect to Stitch isn't publicly accessible, you can use an SSH tunnel.

  The steps for setting up an SSH connection vary depending on where your database is hosted. Refer to the sections below for more info.


# -------------------------- #
#           Content          #
# -------------------------- #

sections:
  - title: "Self-hosted databases"
    anchor: "self-hosted-databases"
    content: |
      If your database is hosted on your server and not in the cloud, it's considered a 'self-hosted' database. To set up SSH for a self-hosted database, use the [general SSH guide]({{ link.connections.ssh-generic | prepend: site.baseurl }}).

  - title: "Amazon-hosted databases"
    anchor: "amazon-hosted-databases"
    content: |
      Stitch currently supports connecting Amazon RDS and Amazon Redshift (destination only) databases.

      To set up SSH for these databases, use the [SSH for Amazon guide]({{ link.connections.ssh-amazon | prepend: site.baseurl }}).

  - title: "Microsoft Azure databases"
    anchor: "microsoft-azure-databases"
    content: |
      Stitch currently supports connecting Microsoft Azure SQL Server (as an integration) and Azure SQL Data Warehouse (as a destination). Other Microsoft Azure offerings aren't currently supported.

      To set up SSH for either of these databases, use the [SSH for Microsoft Azure guide]({{ link.connections.ssh-microsoft-azure | prepend: site.baseurl }}).
---