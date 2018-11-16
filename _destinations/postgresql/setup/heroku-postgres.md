---
title: Connecting a Heroku-Postgres Data Warehouse to Stitch
permalink: /destinations/postgresql/connecting-a-heroku-postgres-data-warehouse-to-stitch
tags: [postgresql_destination]
keywords: postgres data warehouse, postgresql data warehouse, etl to postgres, postgres etl, postgresql etl, heroku data warehouse, heroku etl, heroku
summary: "Create a Heroku-Postgres data warehouse and connect it to Stitch."

content-type: "destination-setup"

toc: true
layout: destination-setup-guide

display_name: "Heroku"
type: "postgres"

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: |
      **A Heroku account**. You can create an account by [clicking here](https://signup.heroku.com/) or entering `https://signup.heroku.com` in your browser.

requirements-info: |
  Heroku has a [variety of plans](https://www.heroku.com/pricing#databases) to choose from, including a Free option. Check out Heroku’s [Choosing the Right Heroku Postgres Plan article](https://devcenter.heroku.com/articles/heroku-postgres-plans) if you need some help selecting a plan.

  Contact Heroku if you have questions about their pricing, product features, or support.

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "Create a Heroku Database"
    anchor: "create-heroku-database"
    content: |
      In this first step, you’ll create and provision a Heroku database.

      1. Sign into your Heroku account.
      2. Navigate to the **Databases** page by clicking the **Options** menu (the grid icon next to your avatar in the upper right corner) then **Databases**.
      3. Click the **Create Database** button in this screen.
      4. In the Plan prompt, select the plan you want to use.
      5. Select the **Region** for the database by clicking the **Default Region** drop-down menu.
      6. Click **Add Database**.

      Heroku will begin the database provisioning process, which can take a few minutes. The status of your database will change to **Available** in the Database Dashboard page when things are complete:

      ![Heroku Database Dashboard]({{ site.baseurl }}/images/destinations/heroku-database-dashboard.png)

  - title: "Locate the Heroku Database Connection Settings"
    anchor: "locate-connection-settings"
    content: |
      Next, you’ll locate the database settings in Heroku. This info will be used in the last section to connect Stitch to your Heroku-Postgres destination.

      1. On the Heroku Database Dashboard page, **click the database you just created**.
      2. The database settings and credentials will display. Everything you need is in the **Connection Settings** section of this page:

         ![Heroku Connection Settings]({{ site.baseurl }}/images/destinations/heroku-connection-settings.png)
      3. Remember to click the **Show** link next to the **Password** field to retrieve the user's password.

      Leave this page open for now - you’ll need it to wrap things up.

  - title: "Grant the {{ page.display_name }} user CREATE permissions"
    anchor: "grant-create-permissions"
    content: |
      Stitch requires `CREATE` permissions to create integration schemas and tables in your destination and load data. [By default](https://devcenter.heroku.com/articles/heroku-postgresql-credentials#the-default-credential){:target="new"}, {{ page.display_name }} credentials don't include `CREATE` permissions, so you'll need to grant them to the database user before continuing.

      {% include destinations/setup/new-redshift-postgres-database-user.html %}

  - title: "connect stitch"
    content: |
      Lastly, you'll enter Heroku's connection details into Stitch. When you do this, you'll use the **PostgreSQL** destination option, as noted below.

---
{% include misc/data-files.html %}
{% assign destination = site.destinations | where:"type",page.type | first %}