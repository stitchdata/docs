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

title: Connecting a Self-Hosted PostgreSQL Destination to Stitch
permalink: /destinations/postgresql/connecting-a-self-hosted-postgresql-data-warehouse-to-stitch
keywords: postgresql data warehouse, postgresql data warehouse, etl to postgres, postgres etl, postgresql etl
summary: "Ready to spin up a PostgreSQL data warehouse and connect it to Stitch? This step-by-step tutorial will walk you through every part of the process."

content-type: "destination-setup"

toc: true
layout: tutorial
use-tutorial-sidebar: false


# -------------------------- #
#     Destination Details    #
# -------------------------- #

type: "postgres"
display_name: "PostgreSQL"

hosting-type: "generic"

ssh: true
ssl: true
port: 5432


# -------------------------- #
#        Requirements        #
# -------------------------- #

requirements:
  - item: |
      **An up-and-running {{ destination.display_name }} instance.** Instructions for installing {{ destination.display_name }} and creating an initial database are outside the scope of this tutorial; our instructions assume that you have a {{ destination.display_name }} instance up and running. For help installing and getting started with {{ destination.display_name }}, refer to the [Postgres documentation](https://www.postgresql.org/docs/){:target="new"}.
  - item: |
      **A {{ destination.display_name }} instance running on {{ site.data.destinations.reference[destination.type]stitch-details-info.supported-versions }} or above.** While this isn't something that Stitch strictly enforces, we recommend keeping your [version current as a best practice](http://www.postgresql.org/support/versioning/).
  - item: |
      **`createdb` permissions in your {{ destination.display_name }} instance.** This is required to create a database for Stitch.


# -------------------------- #
#         Instructions       #
# -------------------------- #

steps:
  - title: "Configure database connection settings"
    anchor: "connect-settings"
    content: |
      {% include integrations/templates/configure-connection-settings.html %}

  - title: "Create a {{ destination.display_name }} Stitch user"
    anchor: "create-stitch-user"
    content: |
      {% assign clean-database-name = page.display_name | downcase %}

      {% include note.html type="single-line" content="**Note**: You must have superuser privileges or the ability to create a user and grant privileges to complete this step." %}

      In the following tabs are the instructions for creating a Stitch {{ destination.display_name }} database user and explanations for the permissions Stitch requires.

      {% include destinations/templates/destination-user-setup.html database-type=clean-database-name %}

  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      To complete the setup, you need to enter your {{ destination.display_name }} connection details into the {{ app.page-names.dw-settings }} page in Stitch.

    substeps:
      - title: "Enter connection details into Stitch"
        anchor: "enter-connection-details-into-stitch"
        content: |
          {% include shared/database-connection-settings.html type="general" %}

      - title: "Define SSH connection details"
        anchor: "define-ssh-connection-details"
        content: |
          {% include shared/database-connection-settings.html type="ssh" %}

      - title: "Define SSL connection details"
        anchor: "define-ssl-connection-details"
        content: |
          {% include shared/database-connection-settings.html type="ssl" ssl-fields=true %}

      - title: "Save the destination"
        anchor: "save-destination"
        content: |
          {% include shared/database-connection-settings.html type="finish-up" %}

---
{% include misc/data-files.html %}
{% assign destination = site.destinations | where:"type",page.type | first %}