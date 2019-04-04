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

title: Connecting a Heroku-Postgres Destination to Stitch
permalink: /destinations/postgresql/connecting-a-heroku-postgres-data-warehouse-to-stitch
keywords: postgres data warehouse, postgresql data warehouse, etl to postgres, postgres etl, postgresql etl, heroku data warehouse, heroku etl, heroku
summary: "Connect a Heroku-PostgreSQL destination to your Stitch account."

content-type: "destination-setup"

toc: true
layout: tutorial
use-tutorial-sidebar: false


# -------------------------- #
#     Destination Details    #
# -------------------------- #

display_name: "Heroku"
type: "postgres"
setup-name: "PostgreSQL"

ssh: false
ssl: true

# -------------------------- #
#        Requirements        #
# -------------------------- #

requirements:
  - item: |
      {% assign destination = page %}
      **A Heroku account**. You can create an account by [clicking here](https://signup.heroku.com/){:target="new"} or entering `https://signup.heroku.com` in your browser.

      Heroku has a [variety of plans](https://www.heroku.com/pricing#databases){:target="new"} to choose from, including a Free option. Check out Heroku’s [Choosing the Right Heroku Postgres Plan article](https://devcenter.heroku.com/articles/heroku-postgres-plans){:target="new"} if you need some help selecting a plan.

      Contact Heroku if you have questions about their pricing, product features, or support.
  - item: |
      **An up-and-running {{ destination.display_name }} database.** Instructions for creating a {{ destination.display_name }} database are outside the scope of this tutorial; our instructions assume that you have a database up and running. For help getting started with {{ destination.display_name }}, refer to [Heroku's documentation](https://devcenter.heroku.com/articles/heroku-postgresql){:target="new"}.


# -------------------------- #
#         Instructions       #
# -------------------------- #

steps:
  - title: "Locate the {{ destination.display_name }} connection details"
    anchor: "locate-connection-settings"
    content: |
      {% include shared/connection-details/heroku.html %}

  - title: "Grant the {{ page.display_name }} user CREATE permissions"
    anchor: "grant-create-permissions"
    content: |
      Stitch requires `CREATE` permissions to create integration schemas and tables in your destination and load data. [By default](https://devcenter.heroku.com/articles/heroku-postgresql-credentials#the-default-credential){:target="new"}, {{ page.display_name }} credentials don't include `CREATE` permissions, so you'll need to grant them to the database user before continuing.

      {% assign clean-database-name = page.display_name | downcase %}
      {% include destinations/templates/destination-user-setup.html database-type=clean-database-name %}

  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      Lastly, you'll enter Heroku's connection details into Stitch. When you do this, you'll use the **PostgreSQL** destination option, as noted below.

    substeps:
      - title: "Enter connection details into Stitch"
        anchor: "enter-connection-details-into-stitch"
        content: |
          {% include shared/database-connection-settings.html type="general" %}

      - title: "Save the destination"
        anchor: "save-destination"
        content: |
          {% include shared/database-connection-settings.html type="finish-up" %}
---
{% include misc/data-files.html %}
{% assign destination = page %}