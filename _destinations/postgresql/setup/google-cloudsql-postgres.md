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

title: Connecting a Google CloudSQL PostgreSQL Destination to Stitch
tags: [postgresql_destination]
keywords: postgresql data warehouse, postgresql data warehouse, etl to postgres, postgres etl, postgresql etl, cloudsql postgres, cloudsql postgresql, cloudsql data warehouse

permalink: /destinations/postgresql/connecting-a-google-cloudsql-postgresql-data-warehouse
redirect_from: /destinations/postgresq/connecting-a-google-cloudsql-postgresql-data-warehouse

summary: "Ready to spin up a Google CloudSQL PostgreSQL destination and connect it to Stitch? This step-by-step tutorial will walk you through every part of the process."

content-type: "destination-setup"

toc: true
layout: tutorial
use-tutorial-sidebar: false

display_name: "CloudSQL PostgreSQL"
type: "postgres"


# -------------------------- #
#        Introduction        #
# -------------------------- #

intro: |
  In this tutorial, we’ll walk you through how to spin up a Google CloudSQL PostgreSQL instance and then connect it to Stitch as a destination.

  For more info on Google CloudSQL's features and limitations, [check out the official Google documentation](https://cloud.google.com/sql/docs/postgres/){:target="new"}.


# -------------------------- #
#        Requirements        #
# -------------------------- #

requirements:
  - item: |
      **Create or select a Cloud Platform project to house the instance**. [This can be done in the Projects page in the Google Console](https://console.cloud.google.com/project).
  - item: |
      **Enable billing for the Cloud Platform project**. Even if you're using the Free option, [billing must be enabled](https://support.google.com/cloud/answer/6293499#enable-billing) for the project or Stitch will encounter connection issues.
  - item: |
      **Enable the CloudSQL Administration API** for the [Cloud Platform project](https://console.cloud.google.com/flows/enableapi?apiid=sqladmin).

# -------------------------- #
#         Instructions       #
# -------------------------- #

steps:
  - title: "Create the CloudSQL instance"
    anchor: "create-cloudsql-instance"
    content: |
      1. In the Google Cloud Platform Console, navigate to the [CloudSQL Instances page](https://console.cloud.google.com/projectselector/sql/instances).
      2. Select the project you created and click **Continue**.
      3. Click **Create Instance**.
      4. Click **PostgreSQL**.
      5. In the **Instance ID** field, enter an ID for the instance. Note that this ID is permanent and must begin with a letter.
      6. Enter a password for the `postgres` (master) user.
      7. If you want specific values for other fields, enter them. Otherwise, you can use the defaults. [More info on the Instance Settings can be found here in Google's documentation](https://cloud.google.com/sql/docs/postgres/instance-settings).
      8. When finished, click **Create**.

      The instance may take a few minutes to finish initializing. After the process completes, click the instance to open it in the CloudSQL Instances page.

  - title: "Create a database in the CloudSQL instance"
    anchor: "create-database-in-cloudsql"
    content: |
      **This step is optional**. If you want to use the instance's default database (`postgres`), you can skip this step.

      <ul id="cloudsqlCreateDatabaseTabs" class="nav nav-tabs">
          <li class="active"><a href="#console" data-toggle="tab">Console</a></li>
          <li><a href="#psql" data-toggle="tab">psql Client</a></li>
      </ul>
      <div class="tab-content">
      <div role="tabpanel" class="tab-pane active" id="console" markdown="1">
      1. In the CloudSQL Instances page, click the **Databases** tab.
      2. In the Databases tab, click **New database**.
      3. In the window that displays, enter a name for the database in the **Name** field. Note that Google clone a template database to create the new database - we're going to use the template as-is, but you can change the settings afterwards if you like.
      4. Click **Create**.
      </div>

      <div role="tabpanel" class="tab-pane" id="psql" markdown="1">
      {% include destinations/postgres/create-database.html %}
      </div>
      </div>

  - title: "Configure security and access settings"
    anchor: "configure-security-access-settings"
    content: |
      Next, you'll configure the access settings for the instance. Google access control has two levels: at the instance and at the database.

      - At the **instance-level**, you'll whitelist Stitch's IP addresses. This will allow Stitch to connect to the instance.

      - At the **database-level**, you'll create a database user for Stitch. This will allow Stitch to load your data into the database. **We'll cover how to create the user and assign permissions in Step 4**.

      To whitelist Stitch's IP addresses:

      1. In the **CloudSQL Instances page**, locate and click the instance you created in Step 1. 
      2. Click **Access Control > Authorization**.
      3. In the **Authorized Networks** section, click **Add Network**.
      4. Enter one of Stitch's IP addresses in the **Network** field:

         {% for ip-address in ip-addresses %}
         - {{ ip-address.ip }}
         {% endfor %}

      5. Click **Done**.
      6. Repeat steps 3-5 for each of Stitch's IP addresses.
      7. Click **Save** to update the instance.

  - title: "Create a {{ destination.display_name }} Stitch user"
    anchor: "create-stitch-user"
    content: |
      {% include note.html type="single-line" content="**Note**: You must have the ability to create a user and grant privileges to complete this step." %}

      Configuring the second part of the access control settings requires creating a database user for Stitch. This guide will use the psql method to create the user, which requires the use of a SQL client.

      {% assign clean-database-name = page.display_name | downcase | replace:" ","-" %}
      {% include destinations/templates/destination-user-setup.html database-type=clean-database-name %}

  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      To complete the setup, you need to enter your {{ destination.display_name }} connection details into the {{ app.page-names.dw-settings }} page in Stitch.
    substeps:
      - title: "Locating the connection details in the Google Console"
        anchor: "locate-connection-details-in-google"
        content: |
          1. In the **CloudSQL Instances page**, locate and click the instance you created in Step 1.
          2. When the instance's **Overview** page displays, scroll down to the **Properties** section.
          3. Locate the **IPv4 address** field, which is highlighted in the image below:

             ![Google CloudSQL PostgreSQL IPv4 address field, which contains the hostname info.]({{ site.baseurl }}/images/destinations/gcp-instance-properties.png)

          4. Copy and paste the IPv4 address into a text file **or** leave this page open and open your Stitch account in another tab.

      - title: "Enter connection details into Stitch"
        anchor: "enter-connection-details-into-stitch"
        content: |
          {% include destinations/setup/destination-settings.html %}
---
{% include misc/data-files.html %}
{% assign destination = site.destinations | where:"type",page.type | first %}