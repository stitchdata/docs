---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/destination-templates/destination-setup/
## FOR INSTRUCTIONS & REFERENCE INFO


# -------------------------- #
# Page formatting & Controls #
# -------------------------- #

title: Connecting a Microsoft SQL Server Destination to Stitch
permalink: /destinations/microsoft-sql-server/connecting-microsoft-sql-server-to-stitch

keywords: microsoft-sql-server, microsoft-sql-server data warehouse, microsoft-sql-server data warehouse, microsoft-sql-server etl, etl to microsoft-sql-server, microsoft-sql-server destination
summary: "Connect a Microsoft SQL Server destination to your Stitch account."

content-type: "destination-setup"
key: "microsoft-sql-server-destination-setup"
order: 1

toc: true
layout: tutorial
use-tutorial-sidebar: false


# -------------------------- #
#     Destination Details    #
# -------------------------- #

type: "microsoft-sql-server"
display_name: "Microsoft SQL Server"

ssh: true/false
ssl: true/false
# port: ## Remove if not needed

hosting-type: "" # amazon, generic, microsoft, etc.

api-type: ""

this-version: ""


# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements:
  - item: |
      {% assign destination = page %}
      **An up-and-running {{ destination.display_name }} instance.** Instructions for creating a {{ destination.display_name }} destination are outside the scope of this tutorial; our instructions assume that you have an instance up and running. For help getting started with {{ destination.display_name }}, refer to [<PROVIDER>'s documentation](){:target="new"}.
  - item: ""


# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

# steps:
#   - title: ""
#     anchor: ""
#     content: ""

# ## The Data pipeline region step is necessary ONLY
# ## if the user needs to whitelist Stitch's IP addresses
# ## for setup.

#   - title: "Verify your Stitch account's data pipeline region"
#     anchor: "verify-stitch-account-region"
#     content: |
#       {% include shared/whitelisting-ips/locate-region-ip-addresses.html first-step=true %}

# ## The database connection settings step is necessary ONLY
# ## if the user needs to whitelist Stitch's IP addresses
# ## for setup.
#   - title: "Configure database connection settings"
#     anchor: "connect-settings"
#     content: |
#       {% include integrations/templates/configure-connection-settings.html %}

#   - title: "Create a Stitch {{ destination.display_name }} database user"
#     anchor: "create-database-user"
#     content: |
#       {% include note.html type="single-line" content="**Note**: You must have superuser privileges or the ability to create a user and grant privileges to complete this step." %}

#       In the following tabs are the instructions for creating a Stitch {{ destination.display_name }} database user and explanations for the permissions Stitch requires.

#       {% include destinations/templates/destination-user-setup.html %}

#   - title: "Connect Stitch"
#     anchor: "connect-stitch"
#     content: |
#       To complete the setup, you need to enter your {{ destination.display_name }} connection details into the {{ app.page-names.dw-settings }} page in Stitch.

#     substeps:
#       - title: "Enter connection details into Stitch"
#         anchor: "enter-connection-details-into-stitch"
#         content: |
#           {% include shared/database-connection-settings.html type="general" %}

# ## The SSH step should remain ONLY if the destination
# ## supports SSH.
#       - title: "Define SSH connection details"
#         anchor: "define-ssh-connection-details"
#         content: |
#           {% include shared/database-connection-settings.html type="ssh" %}

# ## The SSL step should remain ONLY if the destination
# ## supports SSL.
#       - title: "Define SSL connection details"
#         anchor: "define-ssl-connection-details"
#         content: |
#           {% include shared/database-connection-settings.html type="ssl" ssl-fields=true %}

#       - title: "Save the destination"
#         anchor: "save-destination"
#         content: |
#           {% include shared/database-connection-settings.html type="finish-up" %}
---
{% include misc/data-files.html %}
{% assign destination = page %}