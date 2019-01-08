---
title: Connecting an Amazon PostgreSQL-RDS Data Warehouse to Stitch
permalink: /destinations/postgresql/connecting-an-amazon-postgresql-rds-data-warehouse-to-stitch
tags: [postgresql_destination]
keywords: postgresql data warehouse, postgresql data warehouse, etl to postgres, postgres etl, postgresql etl, postgres rds, postgres-rds, relational database services
summary: "Ready to spin up an Amazon PostgreSQL-RDS data warehouse and connect it to Stitch? This step-by-step tutorial will walk you through every part of the process."

content-type: "destination-setup"

toc: true
layout: destination-setup-guide
display_name: "Postgres-RDS"
type: "postgres"


# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: |
      **An Amazon Web Services (AWS) account.** Signing up is free - [click here](https://aws.amazon.com){:target="new"} or go to `https://aws.amazon.com` to create an account if you don't have one already.
  - item: "**Some technical know-how and familiarity with AWS.**"


# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "Define data warehouse settings"
    anchor: "define-data-warehouse-settings"
    content: |

      #In this step, you'll sign into your AWS account and configure the basic settings for the Postgres-RDS database.

      1. Sign into your AWS account.
      2. Once you’re signed into the AWS console, click the **Services** menu located in the top-left corner of the page.
      3. Locate the **RDS** option. This should be in the **Database** section of the page.{% include layout/inline_image.html type="right" file="/destinations/postgresql-rds-select-region.png" max-width="250px" alt="Selecting a Region in the RDS-AWS console." %}
      4. Select the **Region** you want to launch the instance in. You can do this by clicking the **Region drop-down menu** in the upper right corner of the console and selecting the appropriate region, as seen in the image to the right.
      5. In the **Create Instance** section of the page, click the **Launch a DB Instance** button.
      6. In the **Select Engine** page, click the **PostgreSQL icon** and then the **Select** button.
      7. In the **Production? page**, you have two options:
         - **Production:** The Production option uses [Multi-AZ Deployment](https://aws.amazon.com/rds/details/multi-az/) and [Provisioned IOPS Storage](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.ProvisionedIOPS.html), which are features that are intended to guard against downtime and disk I/O performance issues. This option is a good idea if you or your company can’t afford downtime or you anticipate heavy usage of the database.
         - **Dev/Test:** This option is suitable if this database will operate outside of production, can handle downtime, don’t anticipate heavy usage, or if you simply are giving RDS a try by using the [Free Usage Tier](http://aws.amazon.com/rds/free).
      8. Select the option you want and click the **Next Step** button.

  - title: "Configure the database: Basic Details"
    anchor: "configure--specify-basic-details"
    content: |
      There are two steps to configuring the database: specifying the basic details and configuring more advanced settings. In this step, you'll specify the basic details.

      In the **Specify DB Details** page, you’ll define the basic settings for your Postgres-RDS database. There are two sections on this page:

      - [Instance Specifications](#configure--specify--instance-specifications)
      - [Settings](#configure--specify--settings)
    substeps:

      - title: "Basic Details: Instance Specifications"
        anchor: "configure--specify--instance-specifications"
        content: |
          {% include misc/icons.html %}
          In the **Instance Specifications** section, you can select the licensing model, version, and more.

          {% capture required-configuration %}Some fields in this section must be configured a certain way to use Stitch. Required fields will be highlighted  and have a {{ notice-icon | replace:"TOOLTIP", "This field must be configured in the specified way to use Stitch." }} icon next to their name.
          {% endcapture %}

          {% include important.html type="single-line" content=required-configuration %}

          {% include destinations/postgres/postgresql-rds-instance-specifications.html %}

      - title: "Basic Details: Settings"
        anchor: "configure--specify--settings"
        content: |
          In the **Settings** section, you’ll define the name of the database and the master user credentials.

          - **DB Instance Identifier:** Enter a name for the database instance. This name must be unique for your account in the Region you selected.
          - **Master Username:** Enter a username for the master user. For info on the permissions this user is granted, [click here](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html#PostgreSQL.Concepts).
          - **Confirm Password:** Enter the master user’s password again to confirm.

          When finished, click the **Next Step** button.

  - title: "Configure the database: Advanced Settings"
    anchor: "configure--advanced-settings"
    content: |
      
      In the Configuring Advanced Settings page, you’ll define the last group of settings the instance needs to run. There are several sections on this page:

      - [Network & Security](#configure--advanced-settings--network-security-settings)
      - [Database Options](#configure--advanced-settings--database-options)
      - [Backup](#configure--advanced-settings--backup-settings)
      - [Maintenance](#configure--advanced-settings--maintenance-settings)

      {% include important.html type="single-line" content=required-configuration %}
    
    substeps:
      - title: "Advanced Settings: Network & Security"
        anchor: "configure--advanced-settings--network-security-settings"
        content: |
          In this section, you'll define the network security settings for the database.

          **Some fields in this section must be configured a certain way to use Stitch.**

          {% include destinations/postgres/postgresql-rds-network-security.html %}

      - title: "Advanced Settings: Database Options"
        anchor: "configure--advanced-settings--database-options"
        content: |
          In this section, you'll define the database's name and parameter settings.

          {% include destinations/postgres/postgresql-rds-database-options.html %}

      - title: "Advanced Settings: Backup"
        anchor: "configure--advanced-settings--backup-settings"
        content: |
          In this section, you'll define the backup settings for the database.

          {% include destinations/postgres/postgresql-rds-backup.html %}

      - title: "Advanced Settings: Maintenance"
        anchor: "configure--advanced-settings--maintenance-settings"
        content: |
          In this section, you'll define the maintenance settings for the database.

          {% include destinations/postgres/postgresql-rds-maintenance.html %}

  - title: "Launch the database"
    anchor: "launch-database"
    content: |
      When you’re finished defining the configuration settings, click **Launch DB Instance** to create and launch the instance.

      **Note that it may take a few minutes for the instance to complete the provisioning process**. The status in the RDS Dashboard page will change to Available when the process completes:

      ![Completed provisioning of the PostgreSQL-RDS database.]({{ site.baseurl }}/images/destinations/postgresql-rds-available.png)

      Once the status has changed to **Available**, you can move onto the next step.

  - title: "Configure the access settings"
    anchor: "configure-access-settings"
    content: |
      For Stitch to successfully connect with your Postgres-RDS instance, you'll need to add our IP addresses to the appropriate database Security Group.

      {% include layout/inline_image.html type="right" file="/destinations/postgresql-rds-instance-actions.png" max-width="450px" alt="Selecting the PostgreSQL-RDS instance, then opening the Instance Actions menu on the RDS Dashboard page" %}1. In the RDS Dashboard page, click the **grey selection box** (this is the first column in the table) next to the PostgreSQL instance you created. It will turn blue when selected.
      2. Click the **Instance Actions** menu.
      3. Select the **See Details** option. This will open the details page for the instance.
      4. Locate the **Security Groups** field in the **Security and Network** section.
      5. **If you created a new Security Group**, click the name of the group that's in this field.

         **If you associated an existing Security Group with the database**, click the name of group you selected when you created the database in [Step 3](#configure--advanced-settings--network-security-settings).
      {% include shared/aws-whitelisting.html %}

  - title: "create db user"
    content: |
      {% assign clean-database-name = page.display_name | downcase %}
      {% include destinations/templates/destination-user-setup.html database-type=clean-database-name %}

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

Amazon Relational Database Services (RDS) is a managed database service that runs on familiar database engines like PostgreSQL.

In this tutorial, we’ll walk you through how to spin up a Postgres-RDS instance and then connect it to Stitch as a destination, or data warehouse.

---