---
title: Connecting a Google CloudSQL PostgreSQL Data Warehouse to Stitch
tags: [postgresql_destination]
keywords: postgresql data warehouse, postgresql data warehouse, etl to postgres, postgres etl, postgresql etl, cloudsql postgres, cloudsql postgresql, cloudsql data warehouse

permalink: /destinations/postgresql/connecting-a-google-cloudsql-postgresql-data-warehouse
redirect_from: /destinations/postgresq/connecting-a-google-cloudsql-postgresql-data-warehouse

summary: "Ready to spin up a Google CloudSQL PostgreSQL data warehouse and connect it to Stitch? This step-by-step tutorial will walk you through every part of the process."
toc: true
layout: destination-setup-guide
display_name: "CloudSQL PostgreSQL"
type: "postgres"

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: |
      **Create or select a Cloud Platform project to house the instance**. [This can be done in the Projects page in the Google Console](https://console.cloud.google.com/project).
  - item: |
      **Enable billing for the Cloud Platform project**. Even if you're using the Free option, [billing must be enabled](https://support.google.com/cloud/answer/6293499#enable-billing) for the project or Stitch will encounter connection issues.
  - item: |
      **Enable the CloudSQL Administration API** for the [Cloud Platform project](https://console.cloud.google.com/flows/enableapi?apiid=sqladmin).

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "Create the CloudSQL Instance"
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

      {% capture ssl%}
      If you want to use SSL to connect Stitch to {{ destination.display_name }}, you'll need to configure the instance to use SSL before continuing. You can find instructions for doing this in [Google's documentation](https://cloud.google.com/sql/docs/postgres/configure-ssl-instance).
      {% endcapture %}

      {% include important.html first-line="**Using an SSL connection?**" content=ssl %}

  - title: "Create a Database in the CloudSQL Instance"
    anchor: "create-database-in-cloudsql"
    content: |
      **This step is optional**. If you want to use the instance's default database (`postgres`), you can skip this step.

      {% include shared/google-cloud-platform/create-database.html %}

  - title: "Configure Security & Access Settings"
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

  - title: "create db user"
    content: |
      Configuring the second part of the access control settings requires creating a database user for Stitch. There are two methods of creating a user in Google Cloud Platform: via the console (or UI) or using a psql client.

      Before you choose a method, note that:

      - [Users created using the console](https://cloud.google.com/sql/docs/postgres/users) have the permissions associated with the `cloudsqlsuperuser` role. This will include the required permissions outlined below.
      - **If you want to grant Stitch's user specific permissions**, you need to use the psql client method. [Google currently only allows the assignment of permissions via this method](https://cloud.google.com/sql/docs/postgres/users#other_postgresql_users).

      {% include destinations/setup/redshift-postgres-permissions.html %}

      ### Create the Stitch Database User

      {% include shared/google-cloud-platform/create-user.html %}

  - title: "connect stitch"
    content: |
      The last step is to locate the instance's connection details and enter them into Stitch.
    substeps:
      - title: "Locating the Connection Details in the Google Console"
        anchor: "locate-connection-details-in-google"
        content: |
          1. In the **CloudSQL Instances page**, locate and click the instance you created in Step 1.
          2. When the instance's **Overview** page displays, scroll down to the **Properties** section.
          3. Locate the **IPv4 address** field, which is highlighted in the image below:

             ![Google CloudSQL PostgreSQL IPv4 address field, which contains the hostname info.]({{ site.baseurl }}/images/destinations/gcp-instance-properties.png)

          4. Copy and paste the IPv4 address into a text file **or** leave this page open and open your Stitch account in another tab.


---
{% include misc/data-files.html %}
{% assign destination = site.destinations | where:"type",page.type | first %}

In this tutorial, we’ll walk you through how to spin up a Google CloudSQL PostgreSQL instance and then connect it to Stitch as a destination, or data warehouse.

For more info on Google CloudSQL's features and limitations, [check out the official Google documentation](https://cloud.google.com/sql/docs/postgres/).

---